"""Record a weekly snapshot of every entry's GitHub activity.

Writes data/history/<ISO year>-W<week>.json and, with --report, a Markdown
report of entries that need a maintainer's attention (archived, stale,
renamed, or missing). With --apply-renames, entry URLs are updated to the
canonical repository URL when GitHub reports a rename or transfer.

Usage:
  GITHUB_TOKEN=... python3 scripts/snapshot.py [--apply-renames] [--report PATH]
"""
import argparse
import concurrent.futures
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.request

from listdata import DATA, github_repo, load_entries

API = "https://api.github.com"
STALE_DAYS = 183  # CONTRIBUTING.md: software needs a push in the last 6 months


def get(path):
    """GET an API path. Returns (status, json_or_None, headers)."""
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-selfhosted-ai-snapshot",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, json.load(resp), resp.headers
    except urllib.error.HTTPError as err:
        return err.code, None, err.headers


def contributor_count(owner, repo):
    """Count contributors from the last page number of a per_page=1 listing."""
    status, body, headers = get(f"/repos/{owner}/{repo}/contributors?per_page=1&anon=1")
    if status != 200:
        return None  # GitHub returns 403 for repos with very large histories
    m = re.search(r'[?&]page=(\d+)>; rel="last"', headers.get("Link", ""))
    return int(m.group(1)) if m else len(body or [])


def fetch(owner, repo):
    status, body, _ = get(f"/repos/{owner}/{repo}")
    if status != 200:
        return {"error": "not_found" if status == 404 else f"http_{status}"}
    owner, repo = body["owner"]["login"], body["name"]
    _, release, _ = get(f"/repos/{owner}/{repo}/releases/latest")
    return {
        "canonical_url": body["html_url"],
        "stars": body["stargazers_count"],
        "forks": body["forks_count"],
        "open_issues": body["open_issues_count"],
        "pushed_at": body["pushed_at"],
        "archived": body["archived"],
        "license": (body.get("license") or {}).get("spdx_id"),
        "latest_release": release.get("tag_name") if release else None,
        "latest_release_at": release.get("published_at") if release else None,
        "contributors": contributor_count(owner, repo),
    }


def find_issues(entries, results, now):
    issues = {"archived": [], "stale": [], "renamed": [], "missing": []}
    for entry in entries:
        gh = results.get(entry["slug"])
        if gh is None:
            continue
        if "error" in gh:
            issues["missing"].append((entry, gh["error"]))
            continue
        if gh["archived"]:
            issues["archived"].append((entry, ""))
        pushed = datetime.datetime.fromisoformat(gh["pushed_at"].replace("Z", "+00:00"))
        # Models, datasets, courses, and communities do not need regular pushes.
        if entry.get("kind", "software") == "software" and (now - pushed).days > STALE_DAYS:
            issues["stale"].append((entry, f"last push {pushed.date()}"))
        if gh["canonical_url"].rstrip("/") != entry["url"].rstrip("/"):
            issues["renamed"].append((entry, gh["canonical_url"]))
    return issues


def apply_renames(renamed):
    for entry, new_url in renamed:
        path = entry["_path"]
        text = path.read_text()
        old_line = f"url: {entry['url']}\n"
        if text.count(old_line) == 1:
            path.write_text(text.replace(old_line, f"url: {new_url}\n"))


def report(week, issues, applied):
    lines = [f"Weekly snapshot for {week}.", ""]
    labels = {
        "renamed": "Renamed or transferred" + (" (URLs updated in this PR)" if applied else ""),
        "archived": "Archived (consider removal under the removal policy)",
        "stale": f"Software with no push in {STALE_DAYS}+ days (consider removal under the removal policy)",
        "missing": "Repository not found (check and fix or remove)",
    }
    if not any(issues.values()):
        lines.append("No entries need attention this week.")
    for key, label in labels.items():
        if issues[key]:
            lines += [f"### {label}", ""]
            lines += [f"- {e['name']} (`{e['_path'].name}`) {note}".rstrip() for e, note in issues[key]]
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply-renames", action="store_true")
    parser.add_argument("--report")
    args = parser.parse_args()

    now = datetime.datetime.now(datetime.timezone.utc)
    year, week_no, _ = now.isocalendar()
    week = f"{year}-W{week_no:02d}"

    entries = load_entries()
    for entry in entries:
        entry["slug"] = entry["_path"].stem
    repos = {e["slug"]: github_repo(e["url"]) for e in entries}

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {slug: pool.submit(fetch, *repo) for slug, repo in repos.items() if repo}
        results = {slug: f.result() for slug, f in futures.items()}

    snapshot = {
        "week": week,
        "taken_at": now.isoformat(timespec="seconds"),
        "entries": {
            e["slug"]: {
                "name": e["name"],
                "url": e["url"],
                "category": e["category"],
                **({"github": results[e["slug"]]} if e["slug"] in results else {}),
            }
            for e in sorted(entries, key=lambda e: e["slug"])
        },
    }
    out = DATA / "history" / f"{week}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n")

    issues = find_issues(entries, results, now)
    if args.apply_renames:
        apply_renames(issues["renamed"])
    if args.report:
        with open(args.report, "w") as fh:
            fh.write(report(week, issues, args.apply_renames))

    counts = ", ".join(f"{len(v)} {k}" for k, v in issues.items())
    print(f"Wrote {out.relative_to(DATA.parent)}: {len(results)} GitHub repos; {counts}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
