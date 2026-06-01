import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch1-expanded-v1d -->"

EXPANSIONS = {
    "why-you-wake-up-tired": """
<h2>Do Not Rely on One Fix</h2>
<p>Waking tired often improves through a combination of small changes. A cooler room, earlier caffeine cutoff, steadier wake time, and calmer evening may work together better than one perfect habit. Start with one change, then add another only after you know what helped.</p>
""",
    "morning-light-and-sleep": """
<h2>Make It Part of the Sleep Checklist</h2>
<p>Morning light belongs beside the evening habits most people already associate with sleep. Better sleep is not only a nighttime project. The first hour of the day can support the last hour of the day by giving your body a clearer rhythm.</p>
""",
    "caffeine-and-sleep-cutoff": """
<h2>Protect the Morning Too</h2>
<p>If you move caffeine earlier but still wake exhausted, do not simply add more coffee. Use morning light, hydration, food, and movement to support alertness. This gives your sleep experiment a fairer chance and may reduce the need for late-day caffeine.</p>
""",
    "bedtime-anxiety-racing-thoughts": """
<h2>Practice During the Day</h2>
<p>The skills that help bedtime anxiety are easier to use if you practice them before bedtime. Try a worry list, grounding cue, or slow exhale during the afternoon. Then the same tools feel more familiar when thoughts get loud at night.</p>
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
