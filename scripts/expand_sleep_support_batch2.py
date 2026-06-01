import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch2-expanded-v1 -->"

EXPANSIONS = {
    "nap-timing-guide": """
<h2>How to Wake Up From a Nap More Easily</h2>
<p>Waking up from a nap can feel rough if the nap is too long, too late, or taken in a very dark and cozy environment. Make waking easier by setting an alarm, keeping the room only moderately comfortable, and planning a simple wake-up cue.</p>
<ul>
  <li>Drink water after waking.</li>
  <li>Step into brighter light.</li>
  <li>Move gently for one or two minutes.</li>
  <li>Avoid making big decisions while groggy.</li>
  <li>Give yourself a few minutes before returning to demanding work.</li>
</ul>
<h2>Napping After a Bad Night</h2>
<p>If you slept poorly, a short nap may help you function. But use it as part of a recovery plan, not as the only fix. Protect the next night's sleep by keeping the nap earlier and returning to a steady evening routine.</p>
<h2>Napping and Stress</h2>
<p>Sometimes the body feels tired because stress is draining, not because sleepiness is the only issue. If you lie down and your mind races, try a stress reset first. Write the worry, relax your body, and choose one next step. Then decide whether a nap still feels useful.</p>
<h2>When to Skip a Nap</h2>
<p>Skip or shorten a nap if it repeatedly pushes bedtime later, leaves you groggy for hours, or becomes a way to avoid every stressful task. In those cases, a walk, food, hydration, or earlier bedtime may be more helpful.</p>
""",
    "bedroom-environment-checklist": """
<h2>Make One Change at a Time</h2>
<p>A bedroom reset can feel expensive or overwhelming if you try to fix everything at once. Start with the easiest friction point. If the room is too bright, address light first. If notifications wake you, change phone settings first. If the room feels stressful, clear the bedside area first.</p>
<h2>The 10-Minute Bedroom Reset</h2>
<ol>
  <li>Remove cups, wrappers, or clutter from the bedside area.</li>
  <li>Set tomorrow's essentials outside the bed area.</li>
  <li>Check the alarm and do-not-disturb settings.</li>
  <li>Adjust bedding for temperature.</li>
  <li>Dim the light and choose one wind-down cue.</li>
</ol>
<p>This small reset helps the room feel more like a place for rest and less like another unfinished task.</p>
<h2>When the Bedroom Is Shared</h2>
<p>If you share a bedroom, focus on changes that respect everyone: eye masks, earplugs, agreed phone settings, quieter alarms, or separate blankets. Shared sleep spaces need communication as much as optimization.</p>
<h2>Bedroom Work Boundaries</h2>
<p>If you must work or study in the bedroom, create a closing ritual. Put materials away, close the laptop, cover the desk area, or change lighting. A small boundary helps your brain separate work mode from sleep mode.</p>
""",
    "shift-work-sleep-basics": """
<h2>Create a Pre-Sleep Routine After Work</h2>
<p>After a shift, your body may still feel alert. Build a short routine that tells your system the work period is over. Eat something simple if needed, reduce bright light, silence notifications, and avoid starting stressful chores right before the sleep window.</p>
<h2>Communicate Your Sleep Window</h2>
<p>People who work daytime schedules may not understand that your sleep window is not free time. If possible, tell family, roommates, or friends when you need uninterrupted sleep. Use signs, calendar blocks, or phone settings to protect that time.</p>
<h2>Meals and Shift Work Sleep</h2>
<p>Heavy meals, skipped meals, or too much caffeine can make shift work harder. Try to keep meals predictable enough that hunger does not wake you and late caffeine does not interfere with sleep. Choose simple, repeatable options during demanding weeks.</p>
<h2>Safety Comes First</h2>
<p>If you are too sleepy to drive safely after a shift, treat that as serious. Use available transportation alternatives, rest before driving if possible, or speak with your workplace or healthcare professional about fatigue risks. Sleepiness is not just uncomfortable; it can be dangerous.</p>
<h2>Use Recovery Days Gently</h2>
<p>On days off, avoid expecting your body to immediately feel normal. Use light, food, movement, and rest to transition. If you switch between day and night schedules often, the body may need more support and consistency wherever possible.</p>
""",
    "sleep-routine-for-parents-caregivers": """
<h2>Let the Routine Be Imperfect</h2>
<p>A caregiver sleep routine must survive interruptions. If you miss the full routine, return to the minimum version: water, one reminder for tomorrow, dimmer light, and one slow breath. Returning to the routine matters more than completing it perfectly.</p>
<h2>Lower the Evening Decision Load</h2>
<p>Caregivers often make decisions all day. Reduce evening decisions by repeating a simple pattern: prepare one thing for tomorrow, choose one calming cue, and set one boundary around screens or tasks. Repetition makes the routine easier when you are tired.</p>
<h2>Use Micro-Recovery During the Day</h2>
<p>Nighttime sleep may be unpredictable, so daytime micro-recovery matters. Step outside for light, stretch while waiting, drink water, or sit quietly for two minutes. These moments do not replace sleep, but they can reduce the sense that you are running on nothing.</p>
<h2>Ask for Specific Help</h2>
<p>Specific requests are easier for others to answer. Try: "Can you take the first 20 minutes tomorrow morning?" or "Can you handle bedtime dishes tonight?" Practical support can protect the small routines that make sleep more possible.</p>
<h2>Notice Burnout Signals</h2>
<p>If exhaustion is paired with hopelessness, irritability, numbness, anxiety, or feeling unsafe, reach out for support. Caregiving can be meaningful and still overwhelming. You deserve help before you reach a breaking point.</p>
""",
    "weekend-sleep-schedule": """
<h2>Why Monday Feels So Hard</h2>
<p>Monday can feel harder when the weekend shifts sleep, meals, light, caffeine, and activity much later. Your body may be asked to switch back quickly, while your mind is also facing work or school demands. A gentler weekend rhythm can reduce that shock.</p>
<h2>Use a Sunday Reset</h2>
<p>On Sunday, choose one reset that supports Monday: get morning light, avoid a very late nap, prepare one thing for the morning, and write the first task. This does not remove Monday responsibilities, but it lowers the friction of starting.</p>
<h2>Social Plans and Sleep</h2>
<p>Weekend social plans matter too. You do not need to avoid late nights completely, but notice how often they happen and how long recovery takes. If a late night is planned, protect the next day with hydration, light, gentle movement, and a realistic bedtime.</p>
<h2>Catch-Up Sleep Without Chaos</h2>
<p>If you need extra sleep, add it thoughtfully. Sleeping a little later may help. Sleeping half the day may make the next night harder. Try to recover while keeping enough structure that your body still recognizes the rhythm of the week.</p>
<h2>Make the Weekend Restful in Other Ways</h2>
<p>Sleep is not the only recovery tool. Lowering stress, preparing meals, taking a walk, cleaning one small area, or spending time with supportive people can make the weekend restorative without relying only on extra sleep.</p>
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
