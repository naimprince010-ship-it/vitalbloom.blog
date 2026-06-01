import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-stress-support-expanded-v1 -->"

EXPANSIONS: dict[str, str] = {
    "calm-down-when-stress-feels-overwhelming": """
<h2>What to Do After the First Five Minutes</h2>
<p>Once the first wave of stress is lower, choose a slightly longer recovery step. This is where many people accidentally jump back into the same pressure that triggered the spike. Instead, use the calmer moment to make the situation easier to handle.</p>
<ul>
  <li>Send a short message asking for clarification.</li>
  <li>Move one task to tomorrow if it is not urgent.</li>
  <li>Eat something simple if you have skipped a meal.</li>
  <li>Take a five-minute walk before returning to the problem.</li>
  <li>Write down what you will do if the stress returns later.</li>
</ul>
<p>Follow-up matters because stress often returns in waves. A plan made during a calmer moment can help you avoid starting from zero again.</p>
<h2>Make a Personal Calm-Down Plan</h2>
<p>Build a small plan before you need it. Choose one body cue, one grounding cue, one support option, and one next-step question. Keep the plan somewhere easy to find.</p>
<ul>
  <li>Body cue: relax jaw and shoulders.</li>
  <li>Grounding cue: name five things in the room.</li>
  <li>Support option: text a trusted person or use a professional resource.</li>
  <li>Next-step question: what is the smallest useful action?</li>
</ul>
<p>The plan should be boring in a good way. During stress, simple is stronger than clever.</p>
""",
    "grounding-techniques-for-stress": """
<h2>How to Choose the Right Grounding Technique</h2>
<p>Different grounding techniques work for different kinds of stress. If your thoughts are racing, sensory grounding may help. If your body feels restless, movement grounding may work better. If you feel frozen, a simple physical cue like pressing your feet into the floor can be easier than a long exercise.</p>
<ul>
  <li>Use sensory grounding when your attention is stuck in worry.</li>
  <li>Use movement grounding when stress feels like agitation.</li>
  <li>Use breath grounding when you need a quiet reset.</li>
  <li>Use object grounding when you need something concrete to focus on.</li>
</ul>
<p>There is no perfect technique. The useful one is the one that helps you return to the present without adding pressure.</p>
<h2>Practice Grounding When You Are Already Calm</h2>
<p>Grounding is easier to use during stress if you have practiced it during ordinary moments. Try one technique while waiting for coffee, before opening email, after brushing your teeth, or before starting homework.</p>
<p>Short practice builds familiarity. Then, when stress rises, the technique feels less like a new assignment and more like a known path back to the present.</p>
""",
    "work-stress-reset-routine": """
<h2>Use a Stress Budget for the Day</h2>
<p>Not every workday has the same capacity. A stress budget helps you decide where your energy should go. On a heavy day, lower the number of optional decisions and protect recovery points. On a lighter day, you may be able to handle more collaboration, planning, or creative work.</p>
<ul>
  <li>High-stress day: focus on essentials, clear communication, and breaks.</li>
  <li>Medium-stress day: handle priorities and one improvement task.</li>
  <li>Low-stress day: plan ahead, clean up systems, or batch small tasks.</li>
</ul>
<p>This prevents you from expecting the same output from yourself every day regardless of workload, sleep, health, or life stress.</p>
<h2>Team-Level Reset Ideas</h2>
<p>Work stress is not only an individual issue. Teams can reduce stress by making small norms clearer. Meeting buffers, written priorities, fewer last-minute requests, and explicit response-time expectations can all lower daily pressure.</p>
<p>If you manage a team, consider asking: what creates the most avoidable stress here? The answer may point to a workflow issue, not a personal resilience problem.</p>
""",
    "student-stress-management-checklist": """
<h2>Exam Week Version</h2>
<p>Exam weeks need a smaller checklist. During high-pressure academic periods, the goal is to protect focus and recovery, not redesign your entire life.</p>
<ul>
  <li>List exams and deadlines in order.</li>
  <li>Choose the first subject to review today.</li>
  <li>Use active recall instead of only rereading notes.</li>
  <li>Plan sleep and meals as part of studying.</li>
  <li>Use campus support before you are completely stuck.</li>
</ul>
<p>Students often try to study everything at once. A better first move is to identify the next test, the weakest topic, and the first review block.</p>
<h2>How Friends Can Help</h2>
<p>Support does not always mean advice. A friend can sit nearby while you start a task, help you choose the next step, quiz you for ten minutes, or remind you to eat. If you are supporting a stressed student, ask what would help right now instead of assuming.</p>
<p>Specific support is easier to accept: "Can you help me make a study plan for tonight?" works better than "I am behind on everything."</p>
""",
    "daily-stress-relief-routine": """
<h2>Build Around Existing Habits</h2>
<p>A daily routine is easier when it attaches to habits you already do. This is called habit stacking. Instead of adding a completely separate wellness block, connect a stress relief cue to an existing moment.</p>
<ul>
  <li>After brushing teeth, take one slow breath.</li>
  <li>After opening your laptop, write the top priority.</li>
  <li>After lunch, walk for two minutes.</li>
  <li>After closing work, write tomorrow's first task.</li>
  <li>Before bed, move the phone away from the pillow.</li>
</ul>
<p>Small routines become powerful because they repeat. They also survive busy weeks better than routines that require ideal conditions.</p>
<h2>Review the Routine Monthly</h2>
<p>Your stress pattern changes with seasons, work, school, family needs, health, and sleep. Review your routine once per month. Keep what helps, remove what feels unrealistic, and add only one new habit at a time.</p>
<p>A stress relief routine should support your life. If it starts feeling like another performance, simplify it until it feels usable again.</p>
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
