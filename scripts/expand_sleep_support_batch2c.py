import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch2-expanded-v1c -->"

EXPANSIONS = {
    "nap-timing-guide": """
<h2>Use Naps as a Signal</h2>
<p>If you suddenly need naps more often, treat that as information. It may point to sleep debt, stress, illness, medication changes, poor sleep quality, or a schedule that is asking too much. A nap can help the day, but the pattern still deserves attention.</p>
<h2>Keep Night Sleep the Priority</h2>
<p>For most people, naps work best when they support nighttime sleep rather than replace it. If your nap habit keeps moving bedtime later, shorten the nap, move it earlier, or focus on improving the main sleep window first.</p>
""",
    "bedroom-environment-checklist": """
<h2>Bedroom Checklist for Renters and Dorms</h2>
<p>If you cannot make permanent changes, use temporary ones. Try removable blackout curtains, a sleep mask, a fan, earplugs, a small bedside basket, or a consistent phone charging spot. The goal is to create repeatable cues even in a space you do not fully control.</p>
<h2>When Comfort Problems Persist</h2>
<p>If pain, breathing symptoms, allergies, or frequent waking continue despite improving the bedroom, consider professional guidance. Environment matters, but it is not the only factor in sleep quality.</p>
<h2>Make the Bed a Rest Cue</h2>
<p>When possible, keep work, stressful scrolling, and problem-solving out of bed. If your space is limited, create a clear closing ritual before using the bed for sleep: close the laptop, move papers away, dim lights, and start the wind-down.</p>
""",
    "shift-work-sleep-basics": """
<h2>Build a Wind-Down That Matches Your Clock</h2>
<p>Your wind-down may happen in the morning, afternoon, or late at night depending on your shift. The routine still matters. Use the same sequence: reduce light, lower noise, eat lightly if needed, silence alerts, and move toward the sleep space.</p>
<h2>Coordinate Caffeine With the Shift</h2>
<p>Instead of thinking about caffeine as morning or afternoon, think about it in relation to your sleep window. Stop early enough that it does not crowd your main sleep period. Track your response for several shifts because one day may not show the pattern.</p>
<h2>Respect Recovery as Health Maintenance</h2>
<p>Shift workers may feel pressure to use off-hours for everything except rest. Recovery is not wasted time. It protects mood, attention, safety, and long-term health.</p>
""",
    "sleep-routine-for-parents-caregivers": """
<h2>Create a Caregiver Sleep Checklist</h2>
<ul>
  <li>What can be prepared before the hardest part of the night?</li>
  <li>What can wait until tomorrow?</li>
  <li>Who can help with one specific task?</li>
  <li>What is the smallest wind-down cue I can repeat?</li>
  <li>What sign tells me I need more support?</li>
</ul>
<h2>Protect the First Recovery Opportunity</h2>
<p>When a recovery window appears, use it gently. Avoid filling every quiet moment with chores. Sometimes the most useful action is eating, resting, showering, or sitting in silence. Recovery windows are part of care, not a break from responsibility.</p>
<h2>Remember That Support Counts as Sleep Hygiene</h2>
<p>For caregivers, sleep hygiene is not only a bedroom checklist. It includes asking for help, reducing unnecessary load, and creating safer systems around rest.</p>
""",
    "weekend-sleep-schedule": """
<h2>Weekend Sleep for Students</h2>
<p>Students may use weekends to recover from late studying or social plans. Extra rest can help, but a huge Sunday shift can make classes harder. Keep one anchor: morning light, a reasonable wake time, or a Sunday planning reset.</p>
<h2>Weekend Sleep for Busy Workers</h2>
<p>If the weekend is your only recovery time, protect it from becoming only errands. Choose one rest cue before chores take over. A rested weekend may include both sleep and lower stress.</p>
<h2>A Simple Weekend Rule</h2>
<p>Give yourself flexibility, but do not let Sunday night become the price of Saturday. If the weekend schedule makes Monday repeatedly miserable, adjust the swing slightly rather than trying to fix everything at once.</p>
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
