import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-stress-support-batch2-expanded-v1 -->"

EXPANSIONS: dict[str, str] = {
    "morning-stress-reset": """
<h2>Prepare the Night Before</h2>
<p>A calmer morning often starts the previous evening. You do not need a perfect night routine, but a few small decisions can reduce morning friction. Put keys, bags, medication, water, or breakfast items where you can see them. Write tomorrow's first task before bed. If mornings are rushed, decide what can be done at night instead of expecting your future self to manage everything while tired.</p>
<p>This matters because stress rises when the morning begins with avoidable decisions. A little preparation gives your brain fewer problems to solve before the day even starts.</p>
<h2>If You Wake Up Already Anxious</h2>
<p>Some mornings begin with a jolt of worry. If that happens, avoid treating the feeling as proof that the day will go badly. Start with the body: feet on floor, jaw relaxed, slow exhale, and one sentence about the next step. Then ask whether the worry needs action, support, or a later review.</p>
<p>If anxious mornings are frequent, intense, or affecting daily life, consider speaking with a healthcare professional or mental health provider. Morning routines can support you, but they are not meant to replace care when symptoms are persistent.</p>
<h2>Make the Reset Repeatable</h2>
<p>Choose a minimum version for busy days: water, light, one breath, one priority. That is enough to keep the habit alive. On better days, add movement, breakfast, journaling, or a longer planning block. A flexible reset is easier to maintain than a rigid routine that fails whenever life gets crowded.</p>
""",
    "evening-stress-reset": """
<h2>Create a Personal Shutdown Phrase</h2>
<p>A shutdown phrase can help your brain recognize that the day's work is finished. It might sound simple: "I have done what I can for today," or "Tomorrow has a first step." Repeat it after writing your closing list. The phrase is not denial; it is a boundary around problem-solving time.</p>
<h2>Handle Unfinished Tasks Kindly</h2>
<p>Many evenings feel stressful because something remains undone. Instead of carrying guilt into bed, sort unfinished tasks into three groups: must do tomorrow, can schedule later, and not important enough to carry. This makes the unfinished work visible without letting it take over the whole night.</p>
<p>If the same task keeps appearing on the list, it may need a smaller first step, clearer instructions, more support, or a decision to remove it.</p>
<h2>Use a Sensory Wind-Down</h2>
<p>Stress is not only mental. Try one sensory cue: warmer light, quieter sound, a comfortable blanket, a warm shower, calming scent, or a cool room. Sensory cues can help your body understand that the environment is changing from demand mode to recovery mode.</p>
""",
    "stress-and-screen-time": """
<h2>Build a Digital Stress Audit</h2>
<p>For three days, notice which digital habits raise stress and which actually help. You do not need to track every minute. Write down the apps, messages, or screen moments that leave you tense, rushed, numb, or more distracted. Then write down the screen uses that feel useful, connecting, or genuinely restful.</p>
<p>This audit prevents all-or-nothing thinking. The goal is not "screens are bad." The goal is to keep useful digital tools while reducing patterns that keep your nervous system on alert.</p>
<h2>Try a 20-Minute Buffer</h2>
<p>If a specific app or inbox makes stress spike, create a 20-minute buffer around vulnerable times. For example, avoid work email during the first 20 minutes after waking, or avoid news during the last 20 minutes before bed. Buffers are easier than full bans and still protect important transition moments.</p>
<h2>Replace One Scroll Loop</h2>
<p>Choose one scroll loop and replace it with a prepared option: a saved playlist, a short walk, a stretching video, a book, a puzzle, or a message to a real person. Replacement works better than simply telling yourself to stop, because stress often reaches for the easiest available behavior.</p>
""",
    "stress-journaling-prompts": """
<h2>Use Timed Journaling to Avoid Spiraling</h2>
<p>Journaling can help stress, but open-ended writing can sometimes turn into rumination. Use a timer when your thoughts are intense. Five minutes is enough for many stress check-ins. When the timer ends, write one next action and stop. This gives the practice a beginning and an ending.</p>
<h2>Prompts for After a Hard Conversation</h2>
<ul>
  <li>What was actually said?</li>
  <li>What am I adding or assuming?</li>
  <li>What feeling is strongest right now?</li>
  <li>Do I need to respond, wait, clarify, or let it pass?</li>
  <li>What would a calm next message sound like?</li>
</ul>
<p>These prompts help separate the conversation from the story your stress may build around it.</p>
<h2>Prompts for Bedtime Worry</h2>
<p>At night, use a shorter structure: worry, next step, when I will revisit it. For example: "I am worried about the appointment. I will write my questions tomorrow at 9 a.m." This reassures your mind that the issue is not forgotten, but it does not need to be solved in bed.</p>
""",
    "recover-after-stressful-day": """
<h2>Do Not Confuse Numbing With Recovery</h2>
<p>Numbing is understandable after a hard day, but it does not always restore you. Scrolling, overeating, drinking, shopping, or staying up too late may feel like relief in the moment and leave you more depleted later. Recovery should make tomorrow a little easier, not heavier.</p>
<p>This does not mean every relaxing activity must be productive. It means noticing whether a habit helps you feel more settled or keeps the stress cycle going.</p>
<h2>Use a 30-Minute Recovery Window</h2>
<p>If you have the time, create a 30-minute window after a stressful day. Spend the first 10 minutes decompressing, the next 10 supporting your body with food, water, shower, or movement, and the final 10 preparing one thing for tomorrow. This simple structure prevents the evening from disappearing into avoidance.</p>
<h2>Repair Connection Gently</h2>
<p>Stressful days can make people withdraw or snap. If stress affected a relationship, consider a small repair: "I had a hard day and was short earlier. I am sorry." Repair does not need a long explanation. It helps reduce the emotional residue of the day.</p>
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
