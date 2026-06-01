import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch2-expanded-v1f -->"

EXPANSIONS = {
    "shift-work-sleep-basics": "<h2>One Small Win</h2><p>Choose one sleep protection habit for the next shift: darker room, earlier caffeine cutoff, or clearer communication. Small wins are easier to repeat.</p>",
    "sleep-routine-for-parents-caregivers": "<h2>One Small Win</h2><p>Choose one sleep support habit for tonight: prepare one thing, ask for one specific help, or use one calming cue. Small wins matter when rest is fragmented.</p>",
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
        updated = content.rstrip() + "\n\n" + MARKER + "\n" + expansion + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
