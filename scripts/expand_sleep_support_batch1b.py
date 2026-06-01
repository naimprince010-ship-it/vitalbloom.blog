import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch1-expanded-v1b -->"

EXPANSIONS = {
    "sleep-debt-recovery-guide": """
<h2>Common Recovery Mistakes</h2>
<p>One common mistake is staying in bed for most of the day after a short night. Rest can help, but too much time in bed may make the next night less predictable. Another mistake is using late caffeine to power through the day, then feeling too alert at bedtime. A third mistake is trying to recover while keeping the same late-night work, screen, or stress pattern that created the debt.</p>
<p>Recovery works best when the day and night support each other. Use light in the morning, a realistic schedule during the day, and a calmer evening. Think of sleep debt recovery as a sequence, not a single heroic sleep.</p>
<h2>What If You Work Shifts?</h2>
<p>Shift work can make sleep debt harder because light, noise, family schedules, and work demands may conflict with your sleep window. Protect the sleep opportunity you do have: darken the room, reduce interruptions, use consistent cues, and communicate your sleep window when possible. If fatigue becomes unsafe or persistent, seek professional guidance.</p>
""",
    "why-you-wake-up-tired": """
<h2>Create a Morning Tiredness Log</h2>
<p>For seven days, write a simple note each morning. Include bedtime, wake time, caffeine timing, alcohol if relevant, late screens, stress level, and how rested you feel from 1 to 10. You may discover a pattern that is not obvious from memory.</p>
<p>Keep the log neutral. The goal is not to blame yourself. It is to gather clues. If tiredness continues despite improving obvious habits, bring the pattern to a healthcare professional.</p>
<h2>Do Not Ignore Safety</h2>
<p>Morning tiredness becomes more serious when it affects driving, operating equipment, caregiving, work, or school performance. If you are struggling to stay awake during important daily activities, treat that as a signal to get help rather than simply pushing harder.</p>
<h2>Small Fixes to Try First</h2>
<ul>
  <li>Keep the bedroom cooler.</li>
  <li>Move caffeine earlier.</li>
  <li>Reduce phone use in bed.</li>
  <li>Use morning light soon after waking.</li>
  <li>Write down worries before bedtime.</li>
</ul>
""",
    "morning-light-and-sleep": """
<h2>Morning Light for Different Schedules</h2>
<p>If you work a standard daytime schedule, aim for light soon after waking. If you are a student, pair light with breakfast, walking to class, or your first study block. If you are a caregiver, use the first outdoor moment of the day as your cue. If you work nights, light timing is more complicated, and professional guidance may be useful.</p>
<h2>Do You Need Direct Sun?</h2>
<p>You do not need to stare at the sun, and you should protect your eyes. The goal is safe brightness in your environment. Outdoor shade can still be brighter than many indoor rooms. If you have eye conditions or are considering a light therapy device, ask a professional for guidance.</p>
<h2>Pair Light With Movement</h2>
<p>A short walk adds another wake cue. It does not need to be a workout. Two to ten minutes outside can help mark the start of the day and may also support mood, alertness, and a calmer morning routine.</p>
<h2>If You Forget the Habit</h2>
<p>Put a reminder near something you already use: coffee, toothbrush, shoes, keys, or laptop. You can also set the curtain slightly open before bed if that is safe and practical. Make the cue easy to notice.</p>
""",
    "caffeine-and-sleep-cutoff": """
<h2>Afternoon Energy Without Late Caffeine</h2>
<p>If you depend on late caffeine, replace the energy cue with something else before removing it completely. Try daylight, a short walk, water, a protein-rich snack, a quick stretch, or a five-minute reset. Sometimes afternoon fatigue is not a caffeine problem; it is a food, hydration, sleep debt, or break problem.</p>
<h2>Watch the Caffeine-Stress Loop</h2>
<p>Caffeine can feel helpful during stress, but too much may make some people feel more tense or wired. Then poor sleep creates more fatigue, which leads to more caffeine the next day. Breaking the loop may require both a caffeine cutoff and a stress reset routine.</p>
<h2>Use a Cutoff That Is Realistic</h2>
<p>A cutoff you hate will not last. If you usually drink caffeine late in the afternoon, move it earlier gradually. Try a cutoff for one week, review sleep, then adjust. The goal is better sleep and steadier energy, not a perfect rule.</p>
<h2>When Caffeine Is Not the Main Issue</h2>
<p>If you move caffeine earlier and sleep still feels poor, look at other factors: stress, pain, medications, bedroom environment, late screens, inconsistent sleep timing, or possible sleep disorders. Caffeine is only one piece of the sleep puzzle.</p>
""",
    "bedtime-anxiety-racing-thoughts": """
<h2>Create a Pre-Bed Planning Window</h2>
<p>If racing thoughts show up every night, schedule a planning window earlier. Spend ten minutes writing tomorrow's first task, any reminders, and any worries that need follow-up. Close the notebook before the final wind-down. This trains your mind that planning has a place, and bed is not that place.</p>
<h2>Use Compassion Instead of Pressure</h2>
<p>Bedtime anxiety often gets worse when you add pressure: "I have to sleep now," or "Tomorrow will be ruined." Try a gentler phrase: "Resting is still useful," or "I can give my body a quiet place." This reduces the battle around sleep.</p>
<h2>Make the Room Feel Safer</h2>
<p>Small environmental cues can help: a comfortable temperature, less light, fewer alerts, familiar bedding, or a calming sound. If silence makes thoughts louder, a steady low sound may feel supportive. Choose cues that calm you without becoming another complicated routine.</p>
<h2>What to Avoid During Racing Thoughts</h2>
<ul>
  <li>Do not check the clock repeatedly if it increases pressure.</li>
  <li>Do not open stressful messages in bed.</li>
  <li>Do not try to solve every worry at midnight.</li>
  <li>Do not judge yourself for having thoughts.</li>
</ul>
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
