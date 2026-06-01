import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-authority-expansion-v4 -->"

AUTHORITY_SECTIONS: dict[str, str] = {
    "walking-for-weight-management": """
<section>
  <h2>How to Build a Walking Week</h2>
  <p>A walking routine works best when it has both structure and flexibility. Choose three anchor walks each week, then add optional shorter walks when your schedule allows. This keeps the habit steady without making every day feel like a test.</p>
  <p>For example, you might plan a 20-minute walk on Monday, Wednesday, and Saturday, plus a 10-minute walk after dinner on busy days. If you miss one walk, return to the next planned one instead of trying to make up everything at once.</p>
  <ul>
    <li>Begin with a pace that lets you talk comfortably.</li>
    <li>Add time before adding speed or hills.</li>
    <li>Use comfortable shoes and safe routes.</li>
    <li>Pair walks with meals, calls, or errands when possible.</li>
  </ul>
</section>
""",
    "beginner-meditation-guide": """
<section>
  <h2>A Simple 7-Day Meditation Start</h2>
  <p>Beginners often do better with a tiny plan than with a big goal. For the first week, meditate for only three minutes per day. Use the same cue each time, such as after brushing your teeth, before coffee, or before opening your laptop.</p>
  <p>Days one and two can be simple breath awareness. Days three and four can use counting. Days five and six can use a short body scan. On day seven, choose the version that felt easiest. This helps you learn what fits your mind and schedule.</p>
  <p>If you miss a day, keep the plan gentle. Restart with one minute instead of deciding the routine has failed.</p>
</section>
""",
    "how-to-avoid-burnout": """
<section>
  <h2>Make Burnout Prevention Visible</h2>
  <p>Burnout prevention is easier when your boundaries are visible. Put recovery cues where you will actually see them: a lunch reminder, a shutdown checklist, a water bottle on the desk, or a calendar block for a real break.</p>
  <p>It also helps to define what "done for today" means. Without a finish line, work can expand into every open space. A written shutdown routine gives your brain permission to stop rehearsing unfinished tasks.</p>
  <ul>
    <li>Choose one daily non-negotiable recovery habit.</li>
    <li>Write tomorrow's first task before ending work.</li>
    <li>Move one draining task earlier if it keeps following you into the evening.</li>
    <li>Ask for help before exhaustion becomes severe.</li>
  </ul>
</section>
""",
    "simple-hydration-guide": """
<section>
  <h2>How to Personalize Your Hydration Routine</h2>
  <p>A useful hydration routine should match your day. Someone who works indoors at a desk may need different cues than someone who exercises outside, travels often, or lives in a hot climate. Instead of chasing a perfect number, build a rhythm around meals, movement, and thirst.</p>
  <p>Try drinking water with breakfast, lunch, and dinner, then add extra fluids around walks, workouts, heat, or long periods of talking. If plain water feels boring, add citrus, mint, cucumber, or drink unsweetened tea.</p>
  <p>People with kidney, heart, or fluid-balance concerns should follow medical guidance, because hydration advice is not one-size-fits-all.</p>
</section>
""",
    "sleep-hygiene-checklist": """
<section>
  <h2>How to Use the Checklist Without Overwhelm</h2>
  <p>The best sleep hygiene checklist is the one you can actually repeat. Instead of trying all ten changes at once, choose one daytime habit and one evening habit. For example, get morning light and create a 20-minute wind-down period.</p>
  <p>Practice those for a week, then review what changed. If bedtime still feels difficult, adjust one more lever: caffeine timing, screen stimulation, bedroom temperature, or worry planning. Small experiments make it easier to see what helps.</p>
  <p>If sleep problems are persistent, severe, or paired with snoring, breathing pauses, restless legs, or daytime sleepiness, speak with a healthcare professional.</p>
</section>
""",
    "evening-habits-better-rest": """
<section>
  <h2>Build a Backup Evening Routine</h2>
  <p>Real evenings are not always calm. Work runs late, family needs attention, and plans change. A backup routine helps you protect rest even when the full routine is not possible.</p>
  <p>Create a five-minute version: dim one light, write tomorrow's first task, stretch your shoulders, take five slow breaths, and put your phone away from the bed. This small sequence still tells your body that the day is closing.</p>
  <p>On easier nights, use the longer routine. On difficult nights, use the backup. Flexibility keeps the habit from disappearing when life gets busy.</p>
</section>
""",
    "high-protein-vegetarian-meals": """
<section>
  <h2>How to Make Vegetarian Meals More Filling</h2>
  <p>A vegetarian meal can be high in protein but still feel incomplete if it lacks fiber, fat, or enough total food. Build meals with a protein anchor, a fiber-rich carbohydrate, colorful produce, and a flavorful fat or sauce.</p>
  <p>For example, tofu with vegetables is more satisfying when paired with rice and sesame dressing. Greek yogurt feels more complete with oats, berries, and seeds. Lentils become a stronger meal with vegetables, herbs, and olive oil or tahini.</p>
  <ul>
    <li>Use one main protein source per meal.</li>
    <li>Add beans, lentils, tofu, tempeh, eggs, or Greek yogurt regularly.</li>
    <li>Keep quick protein options ready for busy days.</li>
    <li>Pair protein with fiber for longer-lasting fullness.</li>
  </ul>
</section>
""",
    "beginner-home-workout-plan": """
<section>
  <h2>How to Keep the Plan Going After Week One</h2>
  <p>The first week is mostly about learning the routine. After that, focus on repeating the same basic workout long enough to build confidence. You do not need a new workout every day. Familiar movements help you notice progress and improve form.</p>
  <p>Use a simple progression rule: when you can finish all exercises with steady form and normal recovery, add one small challenge. That might mean one extra round, two more reps, a slightly slower tempo, or a resistance band.</p>
  <p>If soreness, fatigue, or joint discomfort builds, keep the next session easier. Consistency grows from good recovery.</p>
</section>
""",
    "simple-breathing-exercises": """
<section>
  <h2>Choose the Right Breathing Exercise for the Moment</h2>
  <p>Different breathing exercises fit different situations. If you feel rushed, a longer exhale may help you slow down. If you feel scattered, counting breaths can give your mind structure. If you feel tense before sleep, belly breathing may feel gentler than breath holds.</p>
  <p>Keep a small menu of options instead of forcing one technique every time. The goal is a comfortable reset, not perfect technique. If any exercise makes you dizzy, panicky, or uncomfortable, stop and breathe normally.</p>
  <ul>
    <li>For work stress: one-minute reset.</li>
    <li>For bedtime: slow belly breathing.</li>
    <li>For focus: counting breaths.</li>
    <li>For tension: longer exhale breathing.</li>
  </ul>
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
