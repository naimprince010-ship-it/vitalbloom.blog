import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-fitness-support-batch1-expanded-v1 -->"

EXPANSIONS = {
    "beginner-stretching-routine": """
<h2>Keep a Stretching Notes List</h2>
<p>After each session, write one short note: easy, tight, helpful, or uncomfortable. This is not formal tracking. It simply helps you notice patterns. You may learn that hips feel better after walking, shoulders feel tight after desk work, or evening stretching helps you slow down before bed.</p>
<p>Use those notes to adjust the routine. If one stretch always feels wrong, replace it. If one stretch consistently helps, keep it as an anchor. A beginner routine should become more personal over time.</p>
""",
    "low-impact-cardio-for-beginners": """
<h2>Use Music, Routes, and Cues</h2>
<p>Low-impact cardio becomes easier when it feels less like a chore. Use a playlist, podcast, walking route, indoor loop, or calendar cue that makes starting simpler. The cue matters because the hardest part for beginners is often beginning, not finishing.</p>
<p>If boredom is the issue, rotate between two activities. For example, walk on weekdays and use a low-impact home routine on rainy days. Variety can help while still keeping the habit familiar.</p>
""",
    "how-to-start-strength-training-at-home": """
<h2>Learn the Difference Between Effort and Pain</h2>
<p>Strength training should involve effort. Muscles may feel challenged, warm, or tired. Pain is different. Sharp pain, joint pain, dizziness, numbness, or symptoms that feel wrong are reasons to stop and reassess.</p>
<p>Beginners sometimes think every workout has to feel extremely hard. It does not. A good beginner session should leave you feeling like you could repeat the routine later in the week.</p>
""",
    "daily-mobility-routine": """
<h2>Use Mobility to Start Other Habits</h2>
<p>A daily mobility routine can become a bridge into other healthy habits. Five minutes of movement may make it easier to take a walk, start a strength session, drink water, or step away from work. This is useful because habits often build on each other.</p>
<p>If the full routine feels like too much, do one movement for one minute. Small starts keep the identity of the habit alive, even on busy days.</p>
""",
    "rest-day-routine-for-beginners": """
<h2>Make Rest Days Predictable</h2>
<p>Rest days feel easier when they are planned instead of accidental. Put them on the calendar the same way you schedule workouts. This helps you see rest as part of the routine rather than something that happens only when you are exhausted.</p>
<p>A predictable rest day can include a walk, mobility, meal prep, stretching, or simply more quiet time. The key is choosing recovery on purpose.</p>
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
