import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch2-expanded-v1b -->"

EXPANSIONS = {
    "nap-timing-guide": """
<h2>Nap Timing for Students</h2>
<p>Students may use naps after late studying, early classes, or long commutes. A nap can help, but it should not become the only recovery plan. Pair naps with a realistic study schedule, food, hydration, and a bedtime routine. If you are staying up late every night and napping every afternoon, the bigger issue may be schedule design.</p>
<h2>Nap Timing for Remote Workers</h2>
<p>Remote workers may have more access to naps, but also more risk of blurring the workday. If you nap during a break, set a clear alarm and return with a defined next task. Avoid letting the nap become a way to avoid difficult work messages or decisions.</p>
<h2>How to Track Whether Naps Help</h2>
<p>Write down nap time, nap length, how you felt after waking, and how bedtime went. After a week, look for patterns. A helpful nap should support the day without making the night consistently harder.</p>
""",
    "bedroom-environment-checklist": """
<h2>Low-Cost Bedroom Changes</h2>
<p>You do not need to buy a full room makeover. Try low-cost changes first: move the phone charger, wash bedding, use a towel to block light under a door, rearrange clutter, use a fan, or set do-not-disturb. Small changes can remove major sleep friction.</p>
<h2>What to Do If You Cannot Control the Room</h2>
<p>Shared housing, dorms, apartments, caregiving, and noise outside your control can make the bedroom harder to manage. Focus on portable cues: eye mask, earplugs, headphones, consistent wind-down, and a small sleep kit. Control what you can without blaming yourself for the rest.</p>
<h2>Turn the Checklist Into a Habit</h2>
<p>Pick one day per week for a bedroom reset. Keep it short enough that you will repeat it. The goal is not a perfect room; it is fewer obstacles between you and rest.</p>
""",
    "shift-work-sleep-basics": """
<h2>Build a Sleep Kit</h2>
<p>A sleep kit can help when your schedule changes. Include an eye mask, earplugs, water, a do-not-disturb plan, comfortable sleep clothes, and anything that makes your room darker or quieter. Preparing the kit before a difficult shift reduces decisions when you are already tired.</p>
<h2>Protect Relationships While Protecting Sleep</h2>
<p>Shift work can affect family and social life. Explain your sleep window and recovery needs clearly. When possible, plan connection time outside your protected sleep block. This helps others understand that sleep is not avoidance; it is part of staying healthy and safe.</p>
<h2>Watch for Accumulated Sleep Debt</h2>
<p>One hard shift may be manageable. Many short sleep windows in a row can accumulate quickly. If you notice irritability, mistakes, microsleeps, or strong cravings for caffeine, treat those as signals that recovery needs more attention.</p>
""",
    "sleep-routine-for-parents-caregivers": """
<h2>Share the Mental Load When Possible</h2>
<p>Sleep routines are harder when one person carries every reminder, decision, and contingency plan. If you have a partner, family member, or support person, discuss one piece of the mental load that can be shared. Even small handoffs can reduce bedtime stress.</p>
<h2>Protect Rest After Night Wakings</h2>
<p>If you wake during the night for caregiving, keep the environment as sleep-friendly as possible afterward. Use dim light, avoid unnecessary phone checking, and return to a simple calming cue. The goal is to avoid turning a waking into a full mental restart.</p>
<h2>Use Compassionate Expectations</h2>
<p>Caregiver sleep may not look like standard sleep advice. Do not treat every interrupted night as a personal failure. Focus on support, recovery windows, and professional guidance when exhaustion becomes unsafe or unmanageable.</p>
""",
    "weekend-sleep-schedule": """
<h2>Plan Around Your Real Weekend</h2>
<p>Some weekends include social events, caregiving, work, religious gatherings, sports, or travel. A useful sleep schedule should fit your real life. Choose one anchor, such as wake time, morning light, or Sunday evening reset, instead of trying to control every hour.</p>
<h2>If You Stay Up Late</h2>
<p>If you know you will stay up late, support recovery the next day. Get light after waking, hydrate, eat normally, avoid a very late long nap, and return to a calmer evening. One late night does not have to become a full weekend rhythm shift.</p>
<h2>Use Monday as Feedback</h2>
<p>Notice how Monday feels. If you are groggy every Monday, the weekend may need a smaller schedule swing. Adjust gently: wake slightly earlier, avoid late Sunday caffeine, or prepare Monday's first step before Sunday night gets too late.</p>
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
