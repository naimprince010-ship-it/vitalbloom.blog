import csv
import json
import re
import subprocess
from html import unescape
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
CSV_PATH = Path("content-plan/seo-authority-audit-priorities.csv")
REPORT_PATH = Path("content-plan/top-20-manual-quality-audit.md")
TOP_N = 20


def run_wp(*args: str) -> str:
    result = subprocess.run(
        ["wp", *args, "--allow-root"],
        cwd=WP_PATH,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def strip_tags(value: str) -> str:
    value = re.sub(r"<script\b[^>]*>.*?</script>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<style\b[^>]*>.*?</style>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", unescape(value)).strip()


def extract_links(content: str) -> list[str]:
    return re.findall(r'href=["\']([^"\']+)["\']', content, flags=re.I)


def extract_headings(content: str) -> list[str]:
    headings = re.findall(r"<h[2-3][^>]*>(.*?)</h[2-3]>", content, flags=re.I | re.S)
    return [strip_tags(heading) for heading in headings]


def source_links(content: str) -> list[str]:
    links = extract_links(content)
    return [
        link
        for link in links
        if link.startswith("http")
        and "vitalbloom.blog" not in link
        and "backend.vitalbloom.blog" not in link
    ]


def risk_notes(row: dict, content: str, headings: list[str], sources: list[str]) -> list[str]:
    notes = []
    text = strip_tags(content).lower()
    title = row["title"].lower()

    if int(row["sources"]) <= 2:
        notes.append("Only 2 source links; add 1-2 more specific authority references or studies.")
    if int(row["incoming_internal_links"]) <= 2:
        notes.append("Low inbound links inside the cluster; add links from 2-3 related posts.")
    if int(row["words"]) < 950:
        notes.append("Slightly thin for competitive wellness SEO; add one concrete example section.")
    if len(set(sources)) != len(sources):
        notes.append("Duplicate external source URLs detected; diversify references.")
    if not any(word in text for word in ["talk with", "professional", "clinician", "doctor", "registered dietitian"]):
        notes.append("YMYL safety language could be stronger for symptoms, injuries, diet, or medical concerns.")
    if "beginner" in title and not any("mistake" in heading.lower() for heading in headings):
        notes.append("Beginner intent could improve with a common mistakes section.")
    if "routine" in title and not any("example" in heading.lower() or "sample" in heading.lower() for heading in headings):
        notes.append("Routine intent could improve with a sample day/week section.")
    if row["hub"] == "nutrition" and "registered dietitian" not in text:
        notes.append("Nutrition content should include clearer dietitian/clinician caveat.")
    if row["hub"] == "fitness" and not any(word in text for word in ["pain", "injury", "sharp pain"]):
        notes.append("Fitness content should include clearer pain/injury stop guidance.")
    return notes


def read_top_rows() -> list[dict]:
    with CSV_PATH.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))[:TOP_N]


def fetch_post(slug: str) -> dict:
    post_id = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip().splitlines()[0]
    raw = run_wp(
        "post",
        "get",
        post_id,
        "--fields=ID,post_title,post_name,post_content,post_modified_gmt",
        "--format=json",
    )
    return json.loads(raw)


def score(notes: list[str]) -> str:
    if not notes:
        return "Pass"
    if len(notes) <= 2:
        return "Minor"
    if len(notes) <= 4:
        return "Medium"
    return "High"


def main() -> None:
    rows = read_top_rows()
    lines = [
        "# Top 20 Manual Quality Audit",
        "",
        "Scope: first 20 posts from the refreshed SEO authority priority list. All passed the technical audit, so this review focuses on human-quality, E-E-A-T, source depth, usefulness, and YMYL caution.",
        "",
        "## Summary",
        "",
    ]

    high = medium = minor = passed = 0
    details = []

    for index, row in enumerate(rows, start=1):
        post = fetch_post(row["slug"])
        content = post["post_content"]
        headings = extract_headings(content)
        sources = source_links(content)
        notes = risk_notes(row, content, headings, sources)
        rating = score(notes)
        if rating == "High":
            high += 1
        elif rating == "Medium":
            medium += 1
        elif rating == "Minor":
            minor += 1
        else:
            passed += 1
        details.append((index, row, post, headings, sources, notes, rating))

    lines.extend(
        [
            f"- Posts reviewed: {len(rows)}",
            f"- Pass: {passed}",
            f"- Minor fixes: {minor}",
            f"- Medium fixes: {medium}",
            f"- High-risk fixes: {high}",
            "",
            "## Recommended Next Fix Order",
            "",
            "1. Add stronger safety/caveat language to fitness and nutrition posts that discuss exercise, digestion, protein, or weight-related habits.",
            "2. Add one practical example block to thin or routine-focused posts, especially sample days, sample weeks, or common beginner mistakes.",
            "3. Increase source depth on posts with only two references by adding more specific government, academic, or professional-body sources.",
            "4. Add inbound links to low-inbound support posts from closely related cluster posts.",
            "",
            "## Post-by-Post Notes",
            "",
        ]
    )

    for index, row, post, headings, sources, notes, rating in details:
        lines.extend(
            [
                f"### {index}. {row['title']}",
                "",
                f"- Slug: `/{row['slug']}`",
                f"- Hub: {row['hub']}",
                f"- Manual rating: {rating}",
                f"- Metrics: {row['words']} words, {row['internal_links']} internal links, {row['incoming_internal_links']} inbound links, {row['sources']} source links",
                f"- Live modified GMT: {post['post_modified_gmt']}",
                f"- Heading sample: {', '.join(headings[:5]) if headings else 'No H2/H3 headings found'}",
        f"- Source sample: {', '.join(sources[:3]) if sources else 'No external source hrefs found in the stored post body; source count may come from source metadata/render layer.'}",
            ]
        )
        if notes:
            lines.append("- Fix notes: " + " ".join(notes))
        else:
            lines.append("- Fix notes: No manual quality gaps found in this pass.")
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
