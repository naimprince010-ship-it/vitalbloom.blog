import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-stress-support-batch2-expanded-v1c -->"

EXPANSIONS = {
    "stress-journaling-prompts": """
<h2>Stop With a Supportive Sentence</h2>
<p>End each journaling session with one sentence you can carry into the next hour. Try: "I can take one step," "This does not need to be solved tonight," or "I am allowed to ask for help." A supportive closing sentence helps the practice end with direction instead of more mental clutter.</p>
""",
    "recover-after-stressful-day": """
<h2>Let Recovery Be Ordinary</h2>
<p>Recovery does not need to look like a polished wellness routine. Sometimes it is dinner, a shower, clean clothes, a quiet room, and going to bed on time. Ordinary care is still care, especially after a day that asked too much from you.</p>
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
        updated = content.rstrip() + "\n\n" + MARKER + "\n" + expansion.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
