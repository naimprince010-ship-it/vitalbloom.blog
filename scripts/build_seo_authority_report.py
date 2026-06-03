import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


DATA_PATH = Path("content-plan/seo-authority-audit-data.json")
REPORT_PATH = Path("content-plan/seo-authority-audit-report.md")
CSV_PATH = Path("content-plan/seo-authority-audit-priorities.csv")

HUBS = {
    "sleep": {
        "pillar": "better-sleep-routine-guide",
        "assets": {"sleep-hygiene-checklist-printable"},
        "keywords": {"sleep", "bedtime", "night", "nap", "caffeine", "wake", "evening", "rest"},
    },
    "stress_mindfulness": {
        "pillar": "stress-management-guide",
        "assets": {"stress-reset-checklist-printable"},
        "keywords": {"stress", "mindfulness", "breathing", "journaling", "burnout", "relaxation", "calm", "grounding", "recover", "stressful"},
    },
    "nutrition": {
        "pillar": "balanced-plate-guide",
        "assets": {"balanced-plate-printable-guide"},
        "keywords": {"meal", "protein", "fiber", "breakfast", "hydration", "snack", "grocery", "pantry", "nutrition", "plate", "vegetables", "eating"},
    },
    "fitness": {
        "pillar": "beginner-home-workout-guide",
        "assets": {"remote-worker-wellness-checklist"},
        "keywords": {"walking", "workout", "strength", "stretch", "fitness", "exercise", "mobility", "cardio", "rest-day"},
    },
    "wellness_lifestyle": {
        "pillar": "daily-wellness-routine-beginners",
        "assets": {"daily-wellness-checklist"},
        "keywords": {"wellness", "routine", "healthy", "habits", "digital", "self-care", "energy", "balanced", "travel", "weekly"},
    },
}


def slug_words(slug: str) -> set[str]:
    return set(re.split(r"[-_]+", slug.lower()))


def classify(post: dict) -> str:
    categories = {category.lower() for category in post.get("categories", [])}
    text_words = slug_words(post["slug"]) | set(re.findall(r"[a-z]+", post["title"].lower()))

    if "sleep" in categories:
        return "sleep"
    if "nutrition" in categories:
        return "nutrition"
    if "fitness" in categories:
        return "fitness"
    if "mindfulness" in categories:
        return "stress_mindfulness"

    scores = {}
    for hub, config in HUBS.items():
        scores[hub] = len(text_words & config["keywords"])
    best_hub, best_score = max(scores.items(), key=lambda item: item[1])
    return best_hub if best_score else "wellness_lifestyle"


def link_targets(post: dict) -> set[str]:
    targets = set()
    for link in post.get("internal_links", []):
        href = link.get("href", "").strip()
        path = href.split("#", 1)[0].strip("/")
        if path:
            targets.add(path)
    return targets


def short_issue_list(post: dict, hub: str, targets: set[str], incoming: int) -> list[str]:
    config = HUBS[hub]
    issues = []
    if post["word_count"] < 900:
        issues.append("expand_to_900_words")
    if len(targets) < 3:
        issues.append("add_internal_links")
    if config["pillar"] != post["slug"] and config["pillar"] not in targets:
        issues.append("link_to_hub_pillar")
    if config["assets"] and post["slug"] not in config["assets"] and not (targets & config["assets"]):
        issues.append("link_to_asset")
    if post["source_count"] < 2:
        issues.append("add_sources")
    if not post.get("yoast_title"):
        issues.append("add_meta_title")
    if not post.get("yoast_description"):
        issues.append("add_meta_description")
    if not post.get("focus_keyword"):
        issues.append("add_focus_keyword")
    if not post.get("fact_checked_by") or not post.get("fact_checked_at"):
        issues.append("add_fact_check_meta")
    if not post.get("has_featured_image"):
        issues.append("add_featured_image")
    if incoming < 2:
        issues.append("increase_inbound_internal_links")
    return issues


def score_priority(post: dict, issues: list[str], incoming: int) -> int:
    score = 0
    weights = {
        "add_internal_links": 18,
        "link_to_hub_pillar": 14,
        "link_to_asset": 10,
        "increase_inbound_internal_links": 14,
        "add_sources": 18,
        "add_meta_title": 8,
        "add_meta_description": 8,
        "add_focus_keyword": 5,
        "add_fact_check_meta": 12,
        "add_featured_image": 20,
        "expand_to_900_words": 10,
    }
    for issue in issues:
        score += weights.get(issue, 5)
    if post["word_count"] >= 900:
        score -= 4
    if post["source_count"] >= 3:
        score -= 3
    if incoming >= 4:
        score -= 4
    return max(score, 0)


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    posts = data["posts"]
    by_slug = {post["slug"]: post for post in posts}

    hubs = {post["slug"]: classify(post) for post in posts}
    outgoing = {post["slug"]: link_targets(post) for post in posts}
    incoming_map = defaultdict(set)
    for source_slug, targets in outgoing.items():
        for target in targets:
            if target in by_slug:
                incoming_map[target].add(source_slug)

    rows = []
    for post in posts:
        slug = post["slug"]
        hub = hubs[slug]
        incoming_count = len(incoming_map[slug])
        issues = short_issue_list(post, hub, outgoing[slug], incoming_count)
        rows.append({
            "slug": slug,
            "title": post["title"],
            "hub": hub,
            "words": post["word_count"],
            "internal_links": len(outgoing[slug]),
            "incoming_internal_links": incoming_count,
            "sources": post["source_count"],
            "has_meta_title": bool(post.get("yoast_title")),
            "has_meta_description": bool(post.get("yoast_description")),
            "has_focus_keyword": bool(post.get("focus_keyword")),
            "has_fact_check": bool(post.get("fact_checked_by") and post.get("fact_checked_at")),
            "has_featured_image": bool(post.get("has_featured_image")),
            "needs_pillar_link": HUBS[hub]["pillar"] != slug and HUBS[hub]["pillar"] not in outgoing[slug],
            "needs_asset_link": (
                bool(HUBS[hub]["assets"])
                and slug not in HUBS[hub]["assets"]
                and not bool(outgoing[slug] & HUBS[hub]["assets"])
            ),
            "issues": ";".join(issues),
            "priority_score": score_priority(post, issues, incoming_count),
        })

    rows.sort(key=lambda row: (-row["priority_score"], row["hub"], row["slug"]))

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    hub_counts = Counter(row["hub"] for row in rows)
    issue_counts = Counter()
    for row in rows:
        issue_counts.update(issue for issue in row["issues"].split(";") if issue)

    lines = [
        "# VitalBloom SEO Authority Audit",
        "",
        f"Generated from live WordPress data: {data['generated_at']}",
        f"Published posts audited: {data['post_count']}",
        "",
        "## Executive Summary",
        "",
        f"- Total published posts: {data['post_count']}",
        f"- Posts with featured images missing: {sum(1 for row in rows if not row['has_featured_image'])}",
        f"- Posts missing source metadata: {issue_counts['add_sources']}",
        f"- Posts needing more internal links: {issue_counts['add_internal_links']}",
        f"- Posts needing hub pillar link: {issue_counts['link_to_hub_pillar']}",
        f"- Posts needing printable/asset link: {issue_counts['link_to_asset']}",
        f"- Posts with weak inbound internal links: {issue_counts['increase_inbound_internal_links']}",
        "",
        "## Hub Distribution",
        "",
    ]

    for hub in HUBS:
        lines.append(f"- {hub}: {hub_counts[hub]} posts, pillar target: `/{HUBS[hub]['pillar']}`")

    lines.extend([
        "",
        "## Highest Priority Fixes",
        "",
        "| Priority | Hub | Slug | Main Issues |",
        "| ---: | --- | --- | --- |",
    ])
    for row in rows[:25]:
        issue_text = row["issues"].replace(";", ", ") or "none"
        lines.append(f"| {row['priority_score']} | {row['hub']} | `/{row['slug']}` | {issue_text} |")

    lines.extend([
        "",
        "## 30-Day Authority Plan",
        "",
        "### Week 1: Internal Authority",
        "- Add/repair hub pillar links from all relevant support posts.",
        "- Add links from pillar pages back to their strongest support pages.",
        "- Make sure every post has at least 3 relevant internal links and every link uses descriptive anchor text.",
        "",
        "### Week 2: Trust And E-E-A-T",
        "- Surface sources, fact-check date, author/editorial review, and disclaimer consistently on post pages.",
        "- Strengthen About, Editorial Policy, Contact, Privacy, and Disclaimer pages as trust signals.",
        "- Add or verify Organization, Article, and Breadcrumb structured data.",
        "",
        "### Week 3: Content Refresh",
        "- Improve the top 25 priority posts from this audit.",
        "- Add FAQ-style sections only where they answer real reader questions.",
        "- Remove repeated generic sections and make intros more specific to the search intent.",
        "",
        "### Week 4: Safe Authority Building",
        "- Use printable assets for outreach to real resource pages, bloggers, and community wellness sites.",
        "- Avoid paid links, link exchanges, and manipulative anchors.",
        "- Track Search Console impressions, indexed pages, and queries ranking positions 8-30.",
        "",
        "## CSV",
        "",
        f"Detailed row-by-row priorities: `{CSV_PATH.as_posix()}`",
        "",
    ])

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {REPORT_PATH}")
    print(f"wrote {CSV_PATH}")


if __name__ == "__main__":
    main()
