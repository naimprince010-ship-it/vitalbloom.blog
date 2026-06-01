import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch1-expanded-v1c -->"

EXPANSIONS = {
    "why-you-wake-up-tired": """
<h2>Build a Better Wake-Up Cue</h2>
<p>If mornings feel rough, add one cue that helps your body understand the day has started. Open curtains, drink water, step near daylight, or move gently for two minutes. This will not fix every cause of tiredness, but it can reduce the groggy drift that makes a poor night feel even worse.</p>
""",
    "morning-light-and-sleep": """
<h2>Keep Expectations Realistic</h2>
<p>Morning light is a helpful cue, not an instant cure. It may support rhythm over time, especially when combined with steady wake times and calmer evenings. Give the experiment several days before judging it, and keep the habit small enough that it fits normal mornings.</p>
""",
    "caffeine-and-sleep-cutoff": """
<h2>Review Your Cutoff Monthly</h2>
<p>Your ideal caffeine cutoff may change with stress, age, medication, schedule, pregnancy, health, or sleep debt. Review it when your sleep pattern changes. If the old routine stops working, adjust gently instead of assuming you have to quit caffeine completely.</p>
""",
    "bedtime-anxiety-racing-thoughts": """
<h2>Keep the Routine Short</h2>
<p>A bedtime anxiety routine should not become a long project. Choose three steps: write the worry, relax the body, and repeat a calming phrase. If you add too many steps, the routine can become another reason to feel behind at night.</p>
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
