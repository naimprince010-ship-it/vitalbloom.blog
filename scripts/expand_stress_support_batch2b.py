import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-stress-support-batch2-expanded-v1b -->"

EXPANSIONS: dict[str, str] = {
    "evening-stress-reset": """
<h2>Make Tomorrow Easier in One Step</h2>
<p>Before ending the evening reset, prepare one small thing for tomorrow. Put a notebook on the desk, fill a water bottle, choose clothes, set out medication, or write the first task on a sticky note. The action should take less than five minutes. Its purpose is not to optimize your life; it is to lower tomorrow's starting friction.</p>
<p>This is especially helpful after a stressful day because your future self may wake up with less patience and less decision-making energy.</p>
<h2>If You Share a Space</h2>
<p>Evening stress resets can be harder in shared homes, dorms, or busy households. Choose cues that do not require total quiet: headphones, a short walk, a notebook, a shower, or a small light change. If other people need you, try naming the reset: "I need ten minutes to close out the day, then I can talk."</p>
<p>Clear communication helps the reset feel less like disappearing and more like taking care of your capacity.</p>
""",
    "stress-and-screen-time": """
<h2>Make Your Phone Less Stressful by Default</h2>
<p>Small design changes can reduce digital stress without relying on constant self-control. Remove the most stressful apps from the first screen. Turn off badges that create urgency. Use grayscale during focus blocks if it helps. Keep calming tools, notes, music, or a timer easier to reach than the apps that pull you into loops.</p>
<h2>Use Screen Time to Support Recovery</h2>
<p>Not all screen use is harmful. A guided stretch, a video call with someone safe, a calming playlist, a recipe, or a therapy appointment reminder can support wellness. The key question is: does this screen use help me return to my life, or does it keep me stuck?</p>
<p>When screen time supports a clear purpose, it is less likely to become a stress spiral.</p>
<h2>Review Boundaries Weekly</h2>
<p>Digital stress changes with work, school, news cycles, and personal life. Review your boundaries once a week. Keep the ones that helped, remove rules that were unrealistic, and choose one screen moment to make calmer next week.</p>
""",
    "stress-journaling-prompts": """
<h2>Prompts for Work or School Stress</h2>
<ul>
  <li>What is the actual deadline?</li>
  <li>What part of this task is unclear?</li>
  <li>What is one question I can ask?</li>
  <li>What can be done in 10 minutes?</li>
  <li>What would be good enough for a first draft?</li>
</ul>
<p>These prompts are useful when stress turns a task into something vague and intimidating. The goal is to make the work visible enough to begin.</p>
<h2>Prompts for Boundary Stress</h2>
<ul>
  <li>Where am I overcommitted?</li>
  <li>What did I agree to without thinking?</li>
  <li>What needs a clearer timeline?</li>
  <li>What can I say no to kindly?</li>
  <li>What can I offer instead of a full yes?</li>
</ul>
<p>Stress journaling can reveal where your calendar or emotional energy is being stretched too thin.</p>
<h2>Keep a Prompt List Ready</h2>
<p>Save five prompts that work for you. When stress is high, do not search for a perfect question. Open the list, choose one prompt, write for five minutes, and end with one next step.</p>
""",
    "recover-after-stressful-day": """
<h2>Choose Rest Based on the Kind of Stress</h2>
<p>Different stressful days need different recovery. If the day was overstimulating, choose quiet. If it was lonely, choose connection. If it was sedentary, choose gentle movement. If it was physically demanding, choose comfort and rest. Matching recovery to the kind of stress makes the evening more effective.</p>
<h2>Use a Gentle Reflection Instead of Self-Criticism</h2>
<p>After a hard day, the mind may review every mistake. Try a gentler structure: what happened, what I needed, what helped, what I will try next time. This keeps reflection useful without turning it into punishment.</p>
<h2>Prepare for the Next Stressful Day</h2>
<p>If you know another demanding day is coming, prepare one support in advance. Plan a simple meal, block a short break, ask for help, write a reminder, or decide when you will stop working. Recovery is easier when tomorrow is not left completely unplanned.</p>
<p>Small preparation can protect you from repeating the same stress cycle.</p>
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
