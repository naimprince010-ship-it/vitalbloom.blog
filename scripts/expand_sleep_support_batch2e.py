import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch2-expanded-v1e -->"

EXPANSIONS = {
    "bedroom-environment-checklist": """
<h2>Start With the Biggest Irritant</h2>
<p>If you only change one thing, choose the issue that bothers you most often. The best bedroom improvement is the one that removes repeated friction from your real nights.</p>
""",
    "shift-work-sleep-basics": """
<h2>Keep the Routine Portable</h2>
<p>If your shifts rotate, keep the routine portable: light control, caffeine timing, protected sleep window, and a short wind-down. These basics can move with the schedule even when the exact clock time changes.</p>
""",
    "sleep-routine-for-parents-caregivers": """
<h2>Use Rest as Prevention</h2>
<p>For caregivers, rest is not a reward after everything is done. It is prevention. Even small recovery cues can reduce mistakes, irritability, and the feeling of running on empty.</p>
""",
    "weekend-sleep-schedule": """
<h2>Keep It Kind</h2>
<p>A weekend sleep schedule should support your life, not punish you for needing rest or fun. Use the plan as a gentle anchor, then adjust based on how your body and Monday mornings respond.</p>
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
