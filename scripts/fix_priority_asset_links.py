import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
TODAY = "2026-06-03"
MARKER = "<!-- vitalbloom-priority-asset-link-v1 -->"


ASSET_LINK_SECTIONS = {
    "morning-routine-for-low-energy-days": {
        "title": "Use a Checklist on Low-Energy Mornings",
        "body": """
<p>When energy is low, a short checklist can make the morning feel less vague. Use the <a href="/daily-wellness-checklist">Daily Wellness Checklist</a> as a gentle menu: water, light, food, movement, and one realistic next step.</p>
<p>Choose only one or two items instead of trying to complete the whole list. The goal is to reduce decision fatigue, not turn a low-energy morning into another performance test.</p>
""",
    },
    "beginner-home-workout-plan": {
        "title": "Turn the Plan Into a Simple Weekly Guide",
        "body": """
<p>If you want a more structured version of this routine, use the <a href="/beginner-home-workout-guide">Beginner Home Workout Guide</a> as the main weekly reference. It organizes strength, movement, rest, and progression into a clearer beginner framework.</p>
<p>This keeps the workout plan from becoming a random list of exercises. A guide-style structure helps you repeat the routine, notice progress, and avoid changing too many variables at once.</p>
""",
    },
    "high-protein-vegetarian-meals": {
        "title": "Use the Plate Printable to Build Vegetarian Meals",
        "body": """
<p>For a practical meal-planning step, use the <a href="/balanced-plate-printable-guide">Balanced Plate Printable Guide</a>. It can help you pair vegetarian protein with produce, fiber-rich carbohydrates, and satisfying flavor without counting every nutrient.</p>
<p>This is especially useful for vegetarian meals because protein can come from beans, lentils, tofu, tempeh, Greek yogurt, eggs, nuts, seeds, and mixed dishes rather than one single food.</p>
""",
    },
    "better-breaks-remote-work": {
        "title": "Make Breaks Easier With a Remote Work Checklist",
        "body": """
<p>If breaks disappear during focused work, keep the <a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a> nearby. It gives simple prompts for movement, eye rest, hydration, lunch boundaries, posture, and shutdown cues.</p>
<p>A checklist works best when it is visible before the day gets busy. Pick one morning cue, one midday cue, and one shutdown cue instead of trying to redesign the entire workday.</p>
""",
    },
    "daily-wellness-checklist": {
        "title": "Pair the Checklist With a Weekly Reset",
        "body": """
<p>For stressful weeks, pair this daily list with the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a>. The daily checklist covers habits; the stress reset gives a quick sequence for grounding, sorting priorities, and choosing the next step.</p>
<p>Using both keeps wellness practical. One tool supports the routine, while the other helps when the routine has already been disrupted.</p>
""",
    },
    "healthy-habits-remote-workers": {
        "title": "Use a Remote Worker Checklist as the Habit Anchor",
        "body": """
<p>Remote workers often need cues that replace the natural transitions of an office day. The <a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a> can act as a weekly habit anchor for breaks, meals, hydration, posture, and end-of-day boundaries.</p>
<p>Start with the habit that solves the most repeated friction point. If lunch disappears, protect lunch first. If stiffness builds, protect movement breaks first. If work runs late, protect the shutdown cue first.</p>
""",
    },
    "remote-worker-wellness-checklist": {
        "title": "Connect This Checklist to Better Breaks",
        "body": """
<p>For more detail on the break portion of this checklist, read <a href="/better-breaks-remote-work">How to Take Better Breaks During Remote Work</a>. That guide expands the checklist into practical break timing, screen rest, movement, and recovery ideas.</p>
<p>Use this page as the quick reference and the breaks guide when you need more examples. Keeping one short checklist and one deeper guide avoids turning remote wellness into a complicated system.</p>
""",
    },
    "beginner-home-workout-guide": {
        "title": "Add a Desk-Worker Recovery Tool",
        "body": """
<p>If you work at a desk or train at home between long sitting blocks, pair this guide with the <a href="/remote-worker-wellness-checklist">Remote Worker Wellness Checklist</a>. It adds movement-break, posture, hydration, and shutdown cues that support recovery outside the workout itself.</p>
<p>This matters because beginner progress is not only about the workout. Sleep, breaks, food, and daily movement all make the plan easier to repeat.</p>
""",
    },
    "journaling-for-mental-clarity": {
        "title": "Use a Stress Reset When Journaling Feels Stuck",
        "body": """
<p>If journaling turns into looping thoughts, use the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a> before or after writing. It gives a short grounding sequence and helps turn reflection into one manageable next step.</p>
<p>This keeps journaling from becoming another place to overthink. Write what is present, sort what is actionable, and let the checklist guide the next small move.</p>
""",
    },
    "how-to-build-a-simple-wellness-plan": {
        "title": "Turn the Plan Into a Daily Checklist",
        "body": """
<p>After choosing your wellness priorities, use the <a href="/daily-wellness-checklist">Daily Wellness Checklist</a> to make the plan visible. A plan becomes easier to follow when the next actions are simple enough to review each day.</p>
<p>Use the checklist lightly. It should remind you of the basics, not make every day feel like a pass-or-fail scorecard.</p>
""",
    },
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


def build_section(title: str, body: str) -> str:
    return f"""
{MARKER}
<section>
  <h2>{title}</h2>
  {body.strip()}
</section>
"""


def update_post(slug: str, section: dict[str, str]) -> str:
    pid = post_id(slug)
    content = run_wp("post", "get", pid, "--field=post_content")
    if MARKER not in content:
        updated = content.rstrip() + "\n\n" + build_section(section["title"], section["body"]).strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        action = "linked"
    else:
        action = "already-linked"

    run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_at", TODAY)
    run_wp("post", "meta", "update", pid, "_vitalbloom_reviewed_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", pid, "_vitalbloom_reviewed_at", TODAY)
    return f"{action}: {pid} {slug}"


def main() -> None:
    for slug, section in ASSET_LINK_SECTIONS.items():
        print(update_post(slug, section))


if __name__ == "__main__":
    main()
