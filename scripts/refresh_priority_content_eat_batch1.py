import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-content-refresh-eat-v1 -->"

EXPANSIONS = {
    "healthy-habits-remote-workers": """
<h2>Use the Remote Worker Wellness Checklist</h2>
<p>If remote work makes healthy habits easy to forget, use the <a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a> as a weekly reset. It keeps the basics visible: movement breaks, hydration, posture, screen boundaries, and a clear end-of-day cue.</p>
<p>This matters because remote work often removes natural transitions. A simple checklist can replace some of those missing cues without making the day feel over-managed.</p>
""",
    "remote-worker-wellness-checklist": """
<h2>Make the Checklist a Friday Review</h2>
<p>Use the <a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a> at the end of the week, not only when the day is already stressful. Ask which habit helped most, which one disappeared, and what small cue would make next week easier.</p>
<p>A Friday review can also protect weekends. Closing work intentionally, clearing one desk area, and writing Monday's first task can reduce the feeling that work is still following you around the house.</p>
""",
    "strength-training-basics": """
<h2>Start With a Form-First Mindset</h2>
<p>Strength training is easier to sustain when you learn the movement before chasing heavier resistance. Use a comfortable range, breathe steadily, and stop if a movement causes sharp pain or symptoms that feel concerning. A form-first mindset helps beginners build confidence without rushing.</p>
<p>For home routines, connect this guide with the <a href="/beginner-home-workout-guide">Beginner Home Workout Guide</a> and the <a href="/how-to-start-strength-training-at-home">How to Start Strength Training at Home</a> plan. Those guides turn the basics into a realistic weekly structure.</p>
""",
    "foods-drinks-affect-sleep": """
<h2>Notice Your Personal Sleep Pattern</h2>
<p>Food and drink timing affects people differently. For one week, notice caffeine timing, heavy evening meals, alcohol, hydration, and late snacks alongside how easily you fall asleep. Keep the notes simple so the pattern is easy to review.</p>
<p>If you spot a pattern, change one variable at a time. For example, move caffeine earlier before changing dinner, snacks, and bedtime all at once. A focused change makes it easier to know what actually helped.</p>
""",
    "journaling-mental-clarity": """
<h2>Use Journaling as a Stress Sorting Tool</h2>
<p>Journaling does not need to be polished writing. It can simply sort thoughts into categories: what happened, what I feel, what I can do, and what I need to let wait. This makes mental clutter easier to work with.</p>
<p>If stress is the main reason you journal, connect this practice with the <a href="/stress-management-guide">Stress Management Guide</a> and the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a>. Those resources give journaling a practical next step.</p>
""",
    "mindful-morning-routine": """
<h2>Keep the First Few Minutes Quiet</h2>
<p>A mindful morning routine can start before productivity. Give yourself a few quiet minutes for light, water, breathing, stretching, or a short intention before opening the busiest part of the day. This helps the routine feel like a transition instead of another task.</p>
<p>If mornings are often low-energy, pair this guide with the <a href="/morning-routine-for-low-energy-days">Morning Routine for Low-Energy Days</a>. A mindful routine should have a gentle version for slower mornings.</p>
""",
    "seasonal-wellness-tips": """
<h2>Review Seasonal Habits Once a Month</h2>
<p>Seasonal wellness works best when it changes before your routine starts to feel off. Once a month, review sleep timing, hydration, movement, meals, screen time, and outdoor light. Choose one adjustment for the season you are actually in.</p>
<p>This keeps the routine flexible. Warmer months may need more hydration cues, while darker months may need more morning light, indoor movement, and evening wind-down support.</p>
""",
    "small-healthy-habits": """
<h2>Choose One Keystone Habit</h2>
<p>A keystone habit is a small action that makes other healthy choices easier. For some people it is a morning walk. For others it is preparing breakfast, drinking water with meals, closing work on time, or charging the phone away from bed.</p>
<p>Start with one keystone habit instead of a long list. When that habit becomes easier, it can quietly support sleep, food, movement, and stress recovery.</p>
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
            print(f"already-refreshed: {slug}")
            continue
        run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{expansion.strip()}\n")
        print(f"refreshed: {pid} {slug}")


if __name__ == "__main__":
    main()
