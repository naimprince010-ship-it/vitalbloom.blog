import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-authority-expansion-v4b -->"

AUTHORITY_SECTIONS: dict[str, str] = {
    "walking-for-weight-management": """
<section>
  <h2>Quick Walking Checklist</h2>
  <ul>
    <li>Pick a realistic weekly walking target.</li>
    <li>Choose safe routes and comfortable shoes.</li>
    <li>Use short walks when time is limited.</li>
    <li>Pair walking with balanced meals, sleep, and stress support.</li>
    <li>Increase time or pace gradually, not all at once.</li>
  </ul>
  <p>Walking works because it is repeatable. Keep the plan simple enough that you can return to it after busy weeks.</p>
</section>
""",
    "beginner-meditation-guide": """
<section>
  <h2>Quick Meditation Checklist</h2>
  <ul>
    <li>Choose one daily cue for practice.</li>
    <li>Start with two to five minutes.</li>
    <li>Use one focus, such as breath, sound, or counting.</li>
    <li>Expect wandering and return gently.</li>
    <li>Stop or switch practices if meditation feels overwhelming.</li>
  </ul>
  <p>The habit is built by returning, not by having a perfectly quiet mind.</p>
</section>
""",
    "how-to-avoid-burnout": """
<section>
  <h2>Quick Burnout Boundary Checklist</h2>
  <ul>
    <li>Protect one real break during the day.</li>
    <li>Define a work shutdown cue.</li>
    <li>Keep meals, hydration, and sleep steady during busy seasons.</li>
    <li>Reduce late-night work messages when possible.</li>
    <li>Seek support if exhaustion or hopelessness persists.</li>
  </ul>
  <p>Burnout prevention works best when recovery is scheduled before you crash.</p>
</section>
""",
    "simple-hydration-guide": """
<section>
  <h2>Quick Hydration Checklist</h2>
  <ul>
    <li>Drink water with meals.</li>
    <li>Keep a bottle where you can see it.</li>
    <li>Add fluids around heat, sweating, or long walks.</li>
    <li>Include water-rich foods such as fruit, vegetables, and soups.</li>
    <li>Follow medical guidance if you have fluid restrictions.</li>
  </ul>
  <p>Hydration is easiest when it becomes part of your normal rhythm, not another complicated tracking task.</p>
</section>
""",
    "sleep-hygiene-checklist": """
<section>
  <h2>Quick Sleep Hygiene Priorities</h2>
  <ul>
    <li>Keep wake time reasonably consistent.</li>
    <li>Get light early in the day.</li>
    <li>Watch caffeine timing.</li>
    <li>Create a short wind-down routine.</li>
    <li>Keep the bedroom cool, dark, and calm when possible.</li>
  </ul>
  <p>Start with the habit that feels easiest. A small sleep routine repeated nightly is more useful than a perfect checklist used once.</p>
</section>
""",
    "evening-habits-better-rest": """
<section>
  <h2>Quick Evening Reset Checklist</h2>
  <ul>
    <li>Choose a time to begin winding down.</li>
    <li>Lower light and stimulation.</li>
    <li>Write tomorrow's first task.</li>
    <li>Use a gentle stretch or breathing cue.</li>
    <li>Keep the phone away from the bed when possible.</li>
  </ul>
  <p>The routine can be short. What matters is giving your body a familiar signal that the active part of the day is ending.</p>
</section>
""",
    "high-protein-vegetarian-meals": """
<section>
  <h2>Quick Vegetarian Protein Checklist</h2>
  <ul>
    <li>Choose a protein anchor for each main meal.</li>
    <li>Use beans, lentils, tofu, tempeh, eggs, or dairy if they fit your diet.</li>
    <li>Add fiber-rich carbohydrates for energy.</li>
    <li>Use sauces, herbs, and healthy fats for satisfaction.</li>
    <li>Prep one easy protein option for busy days.</li>
  </ul>
  <p>Vegetarian meals become easier when protein is planned first instead of added as an afterthought.</p>
</section>
""",
    "beginner-home-workout-plan": """
<section>
  <h2>Quick Home Workout Checklist</h2>
  <ul>
    <li>Warm up for a few minutes.</li>
    <li>Use controlled, pain-free movements.</li>
    <li>Start with two rounds if you are new.</li>
    <li>Rest enough to keep good form.</li>
    <li>Progress one small step at a time.</li>
  </ul>
  <p>A beginner plan should leave you feeling capable of returning, not so sore that you avoid the next session.</p>
</section>
""",
    "simple-breathing-exercises": """
<section>
  <h2>Quick Breathing Practice Checklist</h2>
  <ul>
    <li>Start when you are calm, not only during stress.</li>
    <li>Keep the breath comfortable and unforced.</li>
    <li>Use shorter counts if breath holds feel intense.</li>
    <li>Stop if you feel dizzy or panicky.</li>
    <li>Practice for one to three minutes at first.</li>
  </ul>
  <p>Breathing exercises are small tools. They work best when they stay gentle, repeatable, and easy to use in ordinary moments.</p>
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
