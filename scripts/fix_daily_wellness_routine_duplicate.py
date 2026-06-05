import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
SLUG = "daily-wellness-routine-beginners"
TODAY = "2026-06-04"

SOURCES = [
    {
        "title": "Physical Wellness Toolkit",
        "url": "https://www.nih.gov/health-information/physical-wellness-toolkit",
        "publisher": "National Institutes of Health",
        "accessedAt": TODAY,
    },
    {
        "title": "Health Tips for Adults",
        "url": "https://www.niddk.nih.gov/health-information/weight-management/healthy-eating-physical-activity-for-life/health-tips-for-adults",
        "publisher": "National Institute of Diabetes and Digestive and Kidney Diseases",
        "accessedAt": TODAY,
    },
    {
        "title": "Adult Activity: An Overview",
        "url": "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
        "publisher": "Centers for Disease Control and Prevention",
        "accessedAt": TODAY,
    },
    {
        "title": "MyPlate Plan",
        "url": "https://www.myplate.gov/myplate-plan",
        "publisher": "U.S. Department of Agriculture",
        "accessedAt": TODAY,
    },
]

CONTENT = """
<p>Starting a wellness routine can feel overwhelming when every article suggests a long list of habits. Beginners usually do better with a simple routine that supports the basics: hydration, movement, balanced meals, stress awareness, and sleep.</p>
<p>This guide is built for real life. You can choose one habit from each part of the day, or start with only one small change and let the routine grow slowly.</p>

<h2>Start With the Five Wellness Basics</h2>
<p>A beginner wellness routine does not need to cover everything. Focus on five anchors that support most ordinary days: water, light, movement, meals, and rest. These anchors are flexible enough to fit workdays, school days, family days, and slower weekends.</p>
<ul>
  <li>Hydration: drink water when you wake up or with meals.</li>
  <li>Light: open curtains or step outside early in the day.</li>
  <li>Movement: walk, stretch, or use a short beginner workout.</li>
  <li>Meals: build simple plates with protein, produce, and fiber-rich carbohydrates.</li>
  <li>Rest: create an evening cue that helps your body slow down.</li>
</ul>

<h2>Morning Routine</h2>
<p>Morning habits work best when they are short and repeatable. Instead of building a long checklist, choose two or three signals that help your day start with less friction.</p>
<ul>
  <li><a href="/simple-hydration-guide">Drink water</a>.</li>
  <li>Open curtains or get morning light.</li>
  <li>Stretch for two minutes.</li>
  <li>Take three slow breaths.</li>
  <li>Choose one priority for the day.</li>
</ul>
<p>If mornings are rushed, use a minimum version: water, light, and one realistic next step.</p>

<h2>Midday Routine</h2>
<p>Midday habits support energy and focus. This is where many routines fall apart because the day becomes busy, so keep the choices practical.</p>
<ul>
  <li>Eat a balanced lunch using the <a href="/balanced-plate-guide">balanced plate guide</a>.</li>
  <li>Walk for 10 minutes or take a shorter movement break.</li>
  <li>Refill your water.</li>
  <li>Take a screen break.</li>
  <li>Check your posture and relax your shoulders.</li>
</ul>
<p>If you only do one thing, choose the habit that helps the rest of the afternoon feel easier.</p>

<h2>Evening Routine</h2>
<p>Evening habits help you transition into rest. They do not need to be perfect, quiet, or long. The goal is to give your body and mind a clear signal that the day is winding down.</p>
<ul>
  <li>Prepare tomorrow's first task.</li>
  <li>Dim lights when possible.</li>
  <li>Put your phone away for a short period.</li>
  <li>Stretch gently.</li>
  <li>Write down worries or tasks so they are not circling in your head.</li>
</ul>
<p>For more sleep support, use the <a href="/better-sleep-routine-guide">Better Sleep Routine Guide</a>.</p>

<h2>Weekly Wellness Habits</h2>
<p>Some habits work better weekly than daily. Weekly planning reduces decision fatigue and helps you recover when a day does not go as planned.</p>
<ul>
  <li>Plan a few meals or snacks.</li>
  <li>Schedule workouts or walking time.</li>
  <li>Clean one workspace or kitchen area.</li>
  <li>Review sleep patterns.</li>
  <li>Spend time outside if weather and safety allow.</li>
</ul>
<p>A weekly reset can be simple. See <a href="/how-to-build-a-weekly-reset-routine">How to Build a Weekly Reset Routine</a> for a broader version.</p>

<h2>Use Minimum Versions on Busy Days</h2>
<p>A beginner routine should feel possible on a normal day, not only an ideal day. Minimum versions keep momentum alive when time, energy, or stress gets in the way.</p>
<ul>
  <li>A 10-minute walk becomes two minutes.</li>
  <li>A full breakfast becomes yogurt and fruit.</li>
  <li>A long journal session becomes one sentence.</li>
  <li>A full workout becomes one set.</li>
  <li>A full evening routine becomes putting the phone away for 10 minutes.</li>
</ul>
<p>This is not lowering the standard. It is making the routine durable enough to survive real life.</p>

<h2>A Simple 7-Day Starter Plan</h2>
<p>If you are not sure where to begin, use the first week as a light experiment.</p>
<ul>
  <li>Day 1: Drink water with breakfast.</li>
  <li>Day 2: Add a short walk.</li>
  <li>Day 3: Build one balanced lunch.</li>
  <li>Day 4: Take a two-minute breathing break.</li>
  <li>Day 5: Add a screen-free wind-down cue.</li>
  <li>Day 6: Repeat the easiest habit.</li>
  <li>Day 7: Review what helped and what felt too hard.</li>
</ul>
<p>Keep the habits that fit your life and shrink the ones that felt too big. This makes the routine personal instead of copied from someone else's schedule.</p>

<h2>Avoid Common Beginner Mistakes</h2>
<p>Common mistakes include starting too many habits at once, expecting perfection, ignoring sleep, choosing habits you dislike, and quitting after one missed day.</p>
<p>Build slowly. A routine that feels almost too easy in week one is often the routine you can actually repeat in week four.</p>

<h2>How to Know Your Routine Is Working</h2>
<ul>
  <li>You can repeat it on normal busy days.</li>
  <li>It supports energy without creating guilt.</li>
  <li>You have a minimum version for stressful days.</li>
  <li>You are improving sleep, meals, movement, or stress awareness gradually.</li>
  <li>You recover quickly after missing a day.</li>
</ul>
<p>Progress should feel steady, not dramatic. The goal is a routine that quietly supports your life for months, not a perfect week that disappears.</p>

<h2>FAQ</h2>
<h3>What is the best wellness routine for beginners?</h3>
<p>The best routine is simple, repeatable, and focused on basics like sleep, hydration, movement, meals, and stress management.</p>
<h3>How many habits should I start with?</h3>
<p>Start with one or two. Add more when those feel natural.</p>
<h3>Do I need a strict schedule?</h3>
<p>No. A flexible routine is easier to maintain than a perfect schedule.</p>
<h3>What if I miss a day?</h3>
<p>Return the next day. Consistency is built by restarting, not by never missing.</p>

<h2>Related VitalBloom Guides</h2>
<ul>
  <li><a href="/daily-wellness-checklist">Daily Wellness Checklist</a></li>
  <li><a href="/how-to-build-a-simple-wellness-plan">How to Build a Simple Wellness Plan</a></li>
  <li><a href="/beginner-guide-to-balanced-living">Beginner Guide to Balanced Living</a></li>
  <li><a href="/healthy-habits-when-life-feels-busy">Healthy Habits When Life Feels Busy</a></li>
  <li><a href="/how-to-stay-consistent-with-healthy-habits">How to Stay Consistent With Healthy Habits</a></li>
  <li><a href="/simple-energy-boosting-habits">Simple Energy-Boosting Habits</a></li>
  <li><a href="/seasonal-wellness-tips">Seasonal Wellness Tips</a></li>
  <li><a href="/simple-self-care-checklist">Simple Self-Care Checklist</a></li>
  <li><a href="/digital-wellness-routine">Digital Wellness Routine</a></li>
</ul>

<h2>Conclusion</h2>
<p>A daily wellness routine for beginners should make life feel more supported, not more stressful. Start small, repeat the basics, and let the routine grow with you.</p>
""".strip()


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


def post_id() -> str:
    found = run_wp("post", "list", f"--name={SLUG}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {SLUG}")
    return found.splitlines()[0]


def main() -> None:
    pid = post_id()
    run_wp("post", "update", pid, f"--post_content={CONTENT}")
    run_wp("post", "meta", "update", pid, "_vitalbloom_sources", json.dumps(SOURCES, ensure_ascii=True))
    run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_by", "VitalBloom Editorial Team")
    run_wp("post", "meta", "update", pid, "_vitalbloom_fact_checked_at", TODAY)
    run_wp("post", "meta", "update", pid, "_vitalbloom_reviewed_at", TODAY)
    print(f"cleaned: {pid} {SLUG}")


if __name__ == "__main__":
    main()
