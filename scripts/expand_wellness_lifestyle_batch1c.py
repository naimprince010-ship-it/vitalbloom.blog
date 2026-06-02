import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-wellness-lifestyle-batch1-expanded-v1c -->"

EXPANSIONS = {
    "how-to-build-a-weekly-reset-routine": """
<h2>End With One Clear First Step</h2>
<p>Before the reset ends, choose the first step for the next day. This might be opening a document, taking a walk, making breakfast, or sending one message. A clear first step turns planning into action.</p>
""",
    "simple-self-care-checklist": """
<h2>Keep the Checklist Kind</h2>
<p>If the checklist starts to feel like another way to criticize yourself, simplify it. Self-care should make support easier to find, not create more pressure on an already difficult day.</p>
""",
    "digital-wellness-routine": """
<h2>Restart After Screen-Heavy Days</h2>
<p>Some days will be screen-heavy because of work, travel, or stress. Restart with one boundary the next day instead of trying to make up for it. Digital wellness works best as a repeatable reset.</p>
""",
}


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def main() -> None:
    for slug, expansion in EXPANSIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-expanded: {slug}")
            continue
        run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{expansion.strip()}\n")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
