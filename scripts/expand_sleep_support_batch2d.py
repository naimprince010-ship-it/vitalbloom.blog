import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch2-expanded-v1d -->"

EXPANSIONS = {
    "bedroom-environment-checklist": """
<h2>Do a Morning Review</h2>
<p>When you wake, notice what helped and what interrupted sleep. Was the room too hot? Did a notification wake you? Did light enter too early? Morning review takes less than a minute and gives you one practical change for the next night.</p>
""",
    "shift-work-sleep-basics": """
<h2>Track Fatigue Honestly</h2>
<p>Shift workers can become used to feeling tired. Track fatigue honestly for a week: sleep window, caffeine timing, commute sleepiness, mood, and mistakes. If the pattern looks unsafe, treat it as a health and safety issue, not a personal weakness.</p>
""",
    "sleep-routine-for-parents-caregivers": """
<h2>Make the Routine Visible</h2>
<p>Keep the minimum routine somewhere visible: on the fridge, bedside table, phone note, or planner. When you are tired, you should not have to remember the whole plan. A visible checklist lowers the effort required to care for yourself.</p>
""",
    "weekend-sleep-schedule": """
<h2>Use a Flexible Wake Window</h2>
<p>Instead of an exact weekend wake time, use a wake window. For example, wake within a range that gives you rest without drifting too far from weekdays. A range feels more realistic and still protects Monday.</p>
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
