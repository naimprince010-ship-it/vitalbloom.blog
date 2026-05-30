import html
import re
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
DRAFT_DIR = Path("/tmp/vitalbloom-drafts")


def run_wp(*args: str) -> str:
    cmd = ["wp", *args, "--allow-root"]
    result = subprocess.run(
        cmd,
        cwd=WP_PATH,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)}\n{result.stderr.strip()}")
    return result.stdout.strip()


def parse_draft(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = lines[0].removeprefix("# ").strip()
    meta = {"Title": title}
    body_start = 1

    for index, line in enumerate(lines[1:], start=1):
        if line.startswith("## "):
            body_start = index
            break
        match = re.match(r"^([^:]+):\s*(.+)$", line)
        if match:
            meta[match.group(1).strip()] = match.group(2).strip().strip("`")

    return {
        "title": title,
        "slug": meta["Slug"],
        "category": meta["Category"],
        "keyword": meta["Primary keyword"],
        "meta_title": meta["Meta title"],
        "meta_description": meta["Meta description"],
        "excerpt": meta["Excerpt"],
        "content": markdown_to_html("\n".join(lines[body_start:])),
    }


def inline_markdown(text: str) -> str:
    text = html.escape(text.strip())
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def markdown_to_html(markdown: str) -> str:
    blocks = []
    paragraph = []
    list_items = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            blocks.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list():
        nonlocal list_items
        if list_items:
            items = "".join(f"<li>{inline_markdown(item)}</li>" for item in list_items)
            blocks.append(f"<ul>{items}</ul>")
            list_items = []

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        if not line:
            flush_paragraph()
            flush_list()
            continue

        if line.startswith("## "):
            flush_paragraph()
            flush_list()
            blocks.append(f"<h2>{inline_markdown(line[3:])}</h2>")
        elif line.startswith("### "):
            flush_paragraph()
            flush_list()
            blocks.append(f"<h3>{inline_markdown(line[4:])}</h3>")
        elif line.startswith("- "):
            flush_paragraph()
            list_items.append(line[2:])
        else:
            flush_list()
            paragraph.append(line)

    flush_paragraph()
    flush_list()
    return "\n".join(blocks)


def get_or_create_category(name: str) -> str:
    existing = run_wp("term", "list", "category", f"--name={name}", "--field=term_id")
    if existing:
        return existing.splitlines()[0]
    return run_wp("term", "create", "category", name, "--porcelain")


def find_post_by_slug(slug: str) -> str | None:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID")
    return found.splitlines()[0] if found else None


def publish_post(draft: dict) -> str:
    category_id = get_or_create_category(draft["category"])
    existing_id = find_post_by_slug(draft["slug"])
    common_args = [
        f"--post_title={draft['title']}",
        f"--post_name={draft['slug']}",
        f"--post_content={draft['content']}",
        f"--post_excerpt={draft['excerpt']}",
        "--post_status=publish",
        f"--post_category={category_id}",
    ]

    if existing_id:
        run_wp("post", "update", existing_id, *common_args)
        post_id = existing_id
        action = "updated"
    else:
        post_id = run_wp("post", "create", *common_args, "--porcelain")
        action = "created"

    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_title", draft["meta_title"])
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_metadesc", draft["meta_description"])
    run_wp("post", "meta", "update", post_id, "_yoast_wpseo_focuskw", draft["keyword"])
    return f"{action}: {post_id} {draft['slug']}"


def main() -> None:
    for path in sorted(DRAFT_DIR.glob("*.md")):
        print(publish_post(parse_draft(path)))


if __name__ == "__main__":
    main()
