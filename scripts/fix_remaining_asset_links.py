import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-03"
MARKER = "<!-- vitalbloom-remaining-asset-link-v1 -->"


SECTIONS = {
    "beginner-home-workout-plan": """
<section>
  <h2>Support Home Workouts With Remote-Work Breaks</h2>
  <p>If you spend much of the day at a desk, pair this workout plan with the <a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a>. The checklist helps you add movement breaks, hydration, posture cues, and shutdown habits around the workout itself.</p>
  <p>This makes the plan easier to sustain because your daily environment supports movement instead of leaving all activity for one short workout window.</p>
</section>
""",
    "better-breaks-remote-work": """
<section>
  <h2>Use the Daily Checklist to Keep Breaks Visible</h2>
  <p>For a broader routine cue, add the <a href="/daily-wellness-checklist">Daily Wellness Checklist</a> to your week. It keeps break habits connected with hydration, meals, movement, sleep, and stress recovery.</p>
  <p>This helps breaks feel like part of a healthy day instead of an isolated productivity trick.</p>
</section>
""",
    "healthy-habits-remote-workers": """
<section>
  <h2>Connect Remote Habits to a Daily Wellness Checklist</h2>
  <p>Use the <a href="/daily-wellness-checklist">Daily Wellness Checklist</a> when you want a simple whole-day view of remote work habits. It keeps movement, hydration, food, light, breaks, and wind-down cues in one place.</p>
  <p>The checklist is useful when remote work makes healthy habits too easy to forget between meetings and tasks.</p>
</section>
""",
    "remote-worker-wellness-checklist": """
<section>
  <h2>Pair Remote Work Cues With Daily Wellness Basics</h2>
  <p>For a more general routine view, use the <a href="/daily-wellness-checklist">Daily Wellness Checklist</a>. It connects remote work cues with sleep, meals, movement, stress support, and end-of-day recovery.</p>
  <p>This pairing keeps the remote work checklist practical while still linking it to the wider wellness routine.</p>
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
    for slug, section in SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER not in content:
            run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{section.strip()}\n")
            action = "linked"
        else:
            action = "already-linked"

        run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_at", TODAY)
        run_wp("post", "meta", "update", pid, "_vitalbloom_reviewed_at", TODAY)
        print(f"{action}: {pid} {slug}")


if __name__ == "__main__":
    main()
