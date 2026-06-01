import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-stress-support-expanded-v1c -->"

EXPANSIONS: dict[str, str] = {
    "student-stress-management-checklist": """
<h2>Keep the Checklist Visible</h2>
<p>A checklist only helps if you can find it when stress rises. Keep your version in a notebook, planner, phone note, or pinned document. During a busy week, read the checklist before starting the day and before studying at night. The repetition helps you return to basics when your mind wants to jump between every unfinished task.</p>
""",
    "daily-stress-relief-routine": """
<h2>Do Not Wait for the Perfect Day</h2>
<p>Stress relief routines are built during imperfect weeks. Start with the version that fits today, even if it is only one minute. A tiny routine repeated often is more useful than a complicated routine that depends on having extra time, perfect motivation, and a quiet schedule.</p>
""",
}


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
        updated = content.rstrip() + "\n\n" + MARKER + "\n" + expansion.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
