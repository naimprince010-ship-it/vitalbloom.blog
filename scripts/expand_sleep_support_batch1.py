import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch1-expanded-v1 -->"

EXPANSIONS = {
    "sleep-debt-recovery-guide": """
<h2>What Sleep Debt Recovery Is Not</h2>
<p>Sleep debt recovery is not punishment for staying up late, and it is not a challenge to sleep as many hours as possible in one day. It is a gradual return to steadier sleep opportunity, better timing cues, and lower evening pressure. Trying to force recovery can make sleep feel like another stressful task.</p>
<p>Instead of asking, "How do I erase this immediately?" ask, "What would help my body get enough sleep over the next several nights?" That question leads to better choices: earlier wind-down, less late caffeine, morning light, and a realistic bedtime.</p>
<h2>A Three-Night Reset Plan</h2>
<p>For night one, lower stimulation. Close work tabs, dim lights, and write tomorrow's first task. For night two, add a little more sleep opportunity by moving bedtime earlier or protecting wake time. For night three, keep the same routine and notice what is easier.</p>
<ul>
  <li>Night one: reduce input and prepare the bedroom.</li>
  <li>Night two: protect a realistic bedtime window.</li>
  <li>Night three: repeat the same order and avoid overcorrecting.</li>
</ul>
<h2>How Food, Movement, and Stress Fit In</h2>
<p>Recovery is easier when the day supports the night. A short walk, enough food, hydration, and a stress reset can all make evenings less chaotic. If you are exhausted, choose gentle movement instead of intense late workouts. If you are wired, use a body-based calming cue before bed.</p>
<h2>Track Recovery Without Obsessing</h2>
<p>Track only a few items: bedtime, wake time, caffeine cutoff, and morning energy. Avoid checking the clock repeatedly during the night. The purpose of tracking is to notice patterns, not to grade every sleep session.</p>
""",
    "why-you-wake-up-tired": """
<h2>Look at the Whole Week, Not One Night</h2>
<p>Morning tiredness can come from the pattern across several days. One night of decent sleep may not fully offset a week of late nights, stress, inconsistent wake times, or poor sleep quality. Review the week before blaming one bedtime.</p>
<ul>
  <li>How many nights were shorter than planned?</li>
  <li>Did your wake time swing by several hours?</li>
  <li>Did stress or screen time run late?</li>
  <li>Did caffeine shift later than usual?</li>
  <li>Did you wake during the night?</li>
</ul>
<h2>Check for Sleep Quality Clues</h2>
<p>You can spend enough time in bed and still wake tired if sleep quality is poor. Clues include waking often, waking with a dry mouth, morning headaches, restless legs, vivid stress dreams, or feeling unrefreshed despite enough hours. These clues do not diagnose a condition, but they are worth noticing.</p>
<h2>Make One Change at a Time</h2>
<p>When you wake tired, it is tempting to overhaul everything. A better approach is to test one change for a week. Move caffeine earlier, reduce late screens, keep wake time steadier, cool the room, or write worries down before bed. One clear experiment makes it easier to see what helps.</p>
<h2>Morning Recovery After Poor Sleep</h2>
<p>If you wake tired, avoid turning the whole day into a reaction. Get light, drink water, eat something simple, and choose the most important task first. If possible, avoid using too much caffeine late in the day to compensate, because that can keep the cycle going.</p>
""",
    "morning-light-and-sleep": """
<h2>Build a Light Routine That Fits Your Life</h2>
<p>The best light routine is the one you will repeat. If you have a calm morning, take a short walk. If you have a rushed morning, open curtains while getting ready. If you work early or commute before sunrise, use bright indoor light and seek outdoor light later when available.</p>
<p>Attach the cue to something you already do: brushing teeth, making coffee, feeding a pet, checking the calendar, or starting work. Habit stacking makes the light cue easier to remember.</p>
<h2>What to Track During the Experiment</h2>
<p>For one week, track wake time, light exposure, bedtime, and how sleepy you feel at night. You do not need a complex sleep score. Simple notes are enough. The goal is to see whether the morning cue helps your rhythm feel more stable.</p>
<h2>Morning Light and Mood</h2>
<p>Many people also notice that morning light supports alertness and mood. It is not a cure for depression, anxiety, or sleep disorders, but it can be one helpful daily cue. If low mood, severe fatigue, or sleep disruption persists, consider professional support.</p>
<h2>Evening Light Still Matters</h2>
<p>If mornings are bright but evenings are full of intense light, stressful screens, and late work, sleep may still be difficult. Pair morning light with an evening dim-down. This gives your body a clearer contrast between day and night.</p>
""",
    "caffeine-and-sleep-cutoff": """
<h2>Choose Your Cutoff Based on Symptoms</h2>
<p>If you fall asleep easily but wake at night, your caffeine experiment may look different from someone who cannot fall asleep. If you feel wired at bedtime, move caffeine earlier. If you wake tired despite enough hours, look at both caffeine and sleep quality. If anxiety rises with caffeine, consider a smaller dose or professional guidance.</p>
<h2>What to Drink Instead</h2>
<p>A caffeine cutoff works better when you have replacements ready. Try water, sparkling water, decaf coffee, herbal tea, warm milk, or a short walk. If caffeine is part of a work break, keep the break and change the drink. The ritual may matter as much as the caffeine.</p>
<h2>A Gentle Step-Down Plan</h2>
<p>If you drink a lot of caffeine, sudden changes can cause headaches or irritability. Consider stepping down gradually. Move the final drink earlier first, then reduce the size, then replace one serving if needed. People with medical conditions, pregnancy-related questions, or medication concerns should ask a healthcare professional.</p>
<h2>Track the Full Energy Cycle</h2>
<p>Do not only track bedtime. Notice afternoon energy, evening tiredness, nighttime waking, and next-morning mood. Caffeine can shape the whole cycle. A cutoff is useful if it improves the pattern without making the day miserable.</p>
""",
    "bedtime-anxiety-racing-thoughts": """
<h2>Why Thoughts Get Louder at Night</h2>
<p>During the day, tasks and noise can distract from worry. At night, the quiet can give thoughts more room. This does not mean the worries are more accurate at bedtime. It means your mind finally has space to process unresolved concerns.</p>
<p>Instead of arguing with every thought, create a routine that moves planning earlier and uses the bed for rest. A worry parking lot, body cue, and consistent wind-down can reduce the need to solve everything under the covers.</p>
<h2>Make a Bedtime Anxiety Script</h2>
<p>Use the same short phrase each time racing thoughts appear. Try: "This is a thought, not a task for tonight," or "I wrote it down and can return to it tomorrow." Repeating the same phrase prevents you from debating every worry individually.</p>
<h2>Use a Gentle Reset if You Are Awake</h2>
<p>If you are awake and getting frustrated, lower the pressure. Resting quietly still has value. If you need to get up briefly, keep lights dim and choose something calm. Avoid turning the wake-up into work, scrolling, or clock checking.</p>
<h2>When the Topic Is Too Heavy for a Checklist</h2>
<p>Some worries need real support, not just a bedtime routine. If thoughts are connected to trauma, panic, depression, unsafe situations, or self-harm, reach out to professional or crisis support. A sleep routine can help with ordinary worry, but you do not have to handle serious distress alone.</p>
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
