import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-authority-expansion-v4c -->"

AUTHORITY_SECTIONS: dict[str, str] = {
    "walking-for-weight-management": """
<section>
  <h2>When Walking Feels Too Easy or Too Hard</h2>
  <p>If walking feels too easy, add a few minutes, a slightly faster pace, or a gentle hill. If it feels too hard, shorten the route and keep the pace comfortable. The right level should challenge you lightly while still feeling repeatable.</p>
</section>
""",
    "beginner-meditation-guide": """
<section>
  <h2>When to Try a Different Meditation Style</h2>
  <p>If breath focus feels frustrating, try sounds, walking, body scan, or a short phrase instead. Meditation is not one single method. Beginners often stay more consistent when they choose a focus that feels steady and approachable.</p>
</section>
""",
    "how-to-avoid-burnout": """
<section>
  <h2>Review Your Boundaries Weekly</h2>
  <p>Burnout prevention needs review because demands change. Once a week, ask what drained you most, what helped you recover, and what boundary needs to be clearer. Small weekly adjustments can prevent stress from quietly becoming the normal setting.</p>
</section>
""",
    "simple-hydration-guide": """
<section>
  <h2>Hydration During Travel or Busy Days</h2>
  <p>Travel, errands, and long meetings can interrupt hydration. Carry water when possible, drink with meals, and refill when you change locations. Small location-based cues make hydration easier when your normal routine is disrupted.</p>
</section>
""",
    "sleep-hygiene-checklist": """
<section>
  <h2>Track One Sleep Signal</h2>
  <p>To avoid overtracking, choose one sleep signal for a week: bedtime consistency, wake time, caffeine cutoff, or how rested you feel. One clear signal is easier to improve than trying to measure every detail at once.</p>
</section>
""",
    "evening-habits-better-rest": """
<section>
  <h2>Protect the Last Few Minutes</h2>
  <p>Even when the evening is messy, protect the final few minutes before bed. Lower stimulation, avoid reopening work, and use one calming cue. A short ending ritual can help the night feel more settled.</p>
</section>
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
    for slug, section in AUTHORITY_SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-expanded: {slug}")
            continue

        updated = content.rstrip() + "\n\n" + MARKER + "\n" + section.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
