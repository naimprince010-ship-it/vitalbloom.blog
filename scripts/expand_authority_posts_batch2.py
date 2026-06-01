import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-authority-expansion-v2 -->"

AUTHORITY_SECTIONS: dict[str, str] = {
    "screen-time-and-sleep-quality": """
<section>
  <h2>A Practical Digital Wind-Down Plan</h2>
  <p>A good digital wind-down plan should be specific enough to follow on tired nights. Choose a time when your phone changes roles: it stops being a source of work, news, and entertainment, and becomes only a quiet alarm, music player, or emergency contact device.</p>
  <p>Start by moving the most stimulating apps away from your home screen in the evening. Then silence non-urgent notifications, lower brightness, and decide what you will do instead of scrolling. The replacement matters because most people use screens at night to decompress, not because they truly want more information.</p>
  <p>If your schedule makes a long cutoff unrealistic, use a smaller boundary. Even the final ten minutes before bed can become screen-free. Over time, that small pause can make bedtime feel less rushed.</p>
</section>
<section>
  <h2>Screen Habits to Test This Week</h2>
  <ul>
    <li>Charge your phone across the room instead of beside the pillow.</li>
    <li>Turn off autoplay on video apps.</li>
    <li>Move work email off your evening home screen.</li>
    <li>Use one calm replacement habit, such as reading or stretching.</li>
    <li>Write tomorrow's first task before opening entertainment apps.</li>
  </ul>
  <p>Track sleep quality for a few nights after each change. The goal is to discover which screen habits affect you most.</p>
</section>
""",
    "small-healthy-habits": """
<section>
  <h2>How to Stack Small Habits</h2>
  <p>Small habits become more powerful when they connect to routines you already have. This is called habit stacking. Instead of waiting for motivation, attach a healthy action to something that already happens every day.</p>
  <p>For example, drink water after brushing your teeth, stretch after closing your laptop, or prepare a snack after putting dinner away. The existing habit acts as a reminder, so the new habit requires less mental effort.</p>
  <p>Keep each habit small enough that you can do it even on a busy day. Once it feels automatic, you can add another layer.</p>
</section>
<section>
  <h2>Small Habit Pairings That Work Well</h2>
  <ul>
    <li>After morning coffee, take a two-minute walk outside.</li>
    <li>After lunch, refill your water bottle.</li>
    <li>After a meeting, stand up and stretch your shoulders.</li>
    <li>After dinner, prepare one easy breakfast option.</li>
    <li>After brushing your teeth at night, write tomorrow's first task.</li>
  </ul>
  <p>These pairings are intentionally simple. Consistency grows faster when the habit feels easy to start.</p>
</section>
""",
    "seasonal-wellness-tips": """
<section>
  <h2>Use Each Season as a Routine Checkpoint</h2>
  <p>Seasonal wellness becomes easier when you treat each new season as a planning cue. Instead of waiting until routines fall apart, review the basics: sleep, hydration, movement, meals, stress, and social connection.</p>
  <p>Ask what will predictably change over the next few months. Summer may bring heat, travel, and later evenings. Winter may bring less daylight, colder weather, and more indoor time. Busy holiday or school seasons may require shorter workouts and simpler meals.</p>
  <p>The best seasonal routine is not completely new. It is your normal routine adjusted for the conditions you are actually living in.</p>
</section>
<section>
  <h2>Season-by-Season Habit Ideas</h2>
  <ul>
    <li>Spring: refresh walking routes, add seasonal produce, and reset sleep after schedule changes.</li>
    <li>Summer: plan hydration, protect outdoor exercise from heat, and keep easy meals ready.</li>
    <li>Autumn: rebuild structure after travel, school changes, or relaxed summer routines.</li>
    <li>Winter: get daylight early, prepare indoor movement options, and protect sleep during holidays.</li>
  </ul>
  <p>Choose one seasonal adjustment at a time. A small plan made early is more useful than a dramatic reset made after burnout.</p>
</section>
""",
    "healthy-habits-remote-workers": """
<section>
  <h2>Design a Remote Work Day With Better Transitions</h2>
  <p>Remote work often feels tiring because the day lacks natural transitions. There may be no commute, hallway walk, lunch break, or clear shutdown. Adding small transitions can help your brain separate work, meals, movement, and rest.</p>
  <p>Try creating a start ritual and an end ritual. A start ritual might be water, light, and a short priority list. An end ritual might be closing tabs, writing tomorrow's first task, and taking a short walk or stretch before switching into home time.</p>
  <p>These rituals do not need to be long. Their value comes from repetition. They tell your body and attention what part of the day you are entering.</p>
</section>
<section>
  <h2>Remote Work Health Checklist</h2>
  <ul>
    <li>Keep water visible near your desk.</li>
    <li>Schedule lunch away from your keyboard when possible.</li>
    <li>Use a recurring reminder for posture and movement breaks.</li>
    <li>Keep work apps out of the bedroom.</li>
    <li>Protect one real recovery break that is not just more scrolling.</li>
  </ul>
  <p>If your home is also your office, boundaries need to be visible and repeatable. Small cues make those boundaries easier to maintain.</p>
</section>
""",
    "mindful-morning-routine": """
<section>
  <h2>Build a Morning Routine Around Attention</h2>
  <p>A mindful morning routine is less about doing many wellness habits and more about choosing where your attention goes first. If the first input of the day is urgent messages, stressful news, or a crowded task list, the morning can quickly feel reactive.</p>
  <p>Use the first few minutes to create a slower entry point. Water, light, movement, and breathing are useful because they are physical, simple, and repeatable. They bring attention back to the present before the day becomes noisy.</p>
  <p>If you live with family, share a small space, or have an early work schedule, keep the routine tiny. A mindful routine that takes three minutes and actually happens is better than a beautiful routine that only fits perfect mornings.</p>
</section>
<section>
  <h2>Three Versions of a Mindful Morning</h2>
  <ul>
    <li>Three-minute version: drink water, take three breaths, and choose one priority.</li>
    <li>Ten-minute version: add light, gentle stretching, and a short note about the day.</li>
    <li>Thirty-minute version: include a walk, breakfast, journaling, or meditation if it fits naturally.</li>
  </ul>
  <p>Use the version that matches the day. Flexibility helps the routine survive busy mornings.</p>
</section>
""",
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


def main() -> None:
    for slug, section in AUTHORITY_SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content:
            print(f"already-expanded: {slug}")
            continue

        updated = content.rstrip() + "\n\n" + MARKER + "\n" + section.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
