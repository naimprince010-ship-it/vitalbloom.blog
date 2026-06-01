import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-stress-support-expanded-v1b -->"

EXPANSIONS: dict[str, str] = {
    "grounding-techniques-for-stress": """
<h2>Common Grounding Mistakes</h2>
<p>Grounding is meant to be supportive, but it can become frustrating if you treat it like a test. One common mistake is trying to feel calm immediately. Another is switching techniques every few seconds because the first one did not work fast enough. Give one cue a little time before changing.</p>
<p>It also helps to avoid comparing your response with someone else's. Some people feel calmer with breathwork, while others need movement, cold water, or a visual focus point. Your grounding menu should match your nervous system, not a generic ideal.</p>
<h2>A One-Week Grounding Practice Plan</h2>
<p>For one week, choose one grounding cue per day and practice it when stress is low. On Monday, try feet on the floor. On Tuesday, try object grounding. On Wednesday, try a slow exhale. On Thursday, try a short walk. On Friday, try the 5-4-3-2-1 technique. By the weekend, choose the two that felt most natural and keep them available for stressful moments.</p>
""",
    "work-stress-reset-routine": """
<h2>Red Flags That Your Work Stress Is Becoming Chronic</h2>
<p>Daily stress resets are useful, but they should not be used to normalize ongoing harm. Pay attention if you are regularly losing sleep because of work, feeling dread before every shift, skipping meals, snapping at people you care about, or feeling unable to recover even on days off.</p>
<p>These signs do not mean you are weak. They may mean the workload, role, environment, or expectations need a bigger change. Consider talking with a healthcare professional, trusted manager, HR contact, employee assistance resource, or another support person if work stress is affecting your health.</p>
<h2>Weekly Work Stress Review</h2>
<p>Once a week, ask what created the most avoidable stress. Was it unclear ownership, too many meetings, last-minute requests, interruptions, or lack of recovery time? Choose one small adjustment for the next week, such as blocking focus time, clarifying deadlines earlier, or protecting one lunch break.</p>
""",
    "student-stress-management-checklist": """
<h2>Make a Recovery List Before You Need It</h2>
<p>During a stressful week, it can be hard to remember what helps. Make a short recovery list in advance. Include three quick options, three medium options, and three people or campus resources you can contact if things get harder.</p>
<ul>
  <li>Quick options: water, breathing, stretching, stepping outside.</li>
  <li>Medium options: laundry, a meal, a study plan, a walk with a friend.</li>
  <li>Support options: advisor, professor, counseling, tutoring, trusted person.</li>
</ul>
<p>The list is not only for emergencies. It is a reminder that stress management includes practical support, not just willpower.</p>
<h2>After the Busy Week Ends</h2>
<p>When deadlines pass, do a short review. What helped? What made stress worse? Which class or obligation needs earlier planning next time? This reflection turns a hard week into useful information. Keep the review brief so it does not become another assignment.</p>
""",
    "daily-stress-relief-routine": """
<h2>Match the Routine to Your Stress Pattern</h2>
<p>Some people carry stress mostly in the body. Others feel it as racing thoughts, irritability, shutdown, or constant planning. Your routine should match the pattern you notice most often.</p>
<ul>
  <li>For body tension, prioritize stretching, walking, breathing, and posture breaks.</li>
  <li>For racing thoughts, prioritize writing, planning, and reducing input.</li>
  <li>For irritability, prioritize food, rest, space, and clearer boundaries.</li>
  <li>For shutdown, prioritize tiny starting steps and support.</li>
</ul>
<h2>Keep a Backup Routine</h2>
<p>Even the best routine will fail sometimes. A backup routine keeps you from abandoning the whole idea. Choose three tiny actions: drink water, take one slow breath, and write the next step. On difficult days, that counts. Consistency grows from returning, not from never missing a day.</p>
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
