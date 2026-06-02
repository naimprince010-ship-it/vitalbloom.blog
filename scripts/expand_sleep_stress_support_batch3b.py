import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-stress-support-batch3-expanded-v1b -->"

EXPANSIONS = {
    "sleep-friendly-evening-routine": """
<h2>Make the Routine Visible</h2>
<p>A visible routine is easier to follow when you are tired. Put a short checklist on your nightstand, bathroom mirror, or phone lock screen earlier in the evening. Keep it to three or four steps so it feels supportive rather than demanding.</p>
<p>For example: dim lights, prepare tomorrow, put phone away, read or breathe. A small visible cue can prevent the evening from drifting later without you noticing.</p>
""",
    "phone-free-bedtime-routine": """
<h2>Use a Gentle Morning Reward</h2>
<p>If bedtime phone use feels hard to change, pair the new boundary with something pleasant in the morning. You might enjoy coffee without scrolling, open curtains, play music, or read messages after breakfast instead of immediately from bed.</p>
<p>This helps the routine feel less like deprivation. You are not losing the phone forever; you are moving it to a time that is less likely to disrupt rest.</p>
""",
    "simple-relaxation-techniques": """
<h2>Keep Techniques Short Enough to Use</h2>
<p>A relaxation technique does not need to last 20 minutes to be worthwhile. A one-minute breathing pause, three muscle releases, or a short grounding check can interrupt stress before it builds further. Short tools are easier to use during real life.</p>
<p>If you have more time, extend the practice. If you do not, the smallest version still counts. Consistency matters more than length at the beginning.</p>
""",
    "how-to-reset-after-a-bad-night-sleep": """
<h2>Do Not Chase Perfect Productivity</h2>
<p>After poor sleep, chasing a perfectly productive day can create more stress. Pick the few tasks that matter most and give yourself permission to move slower. Use written lists because tired brains often forget steps or overestimate what can fit.</p>
<p>Protecting energy during the day can make the evening calmer. The reset is not about winning the day; it is about not making the next night harder.</p>
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
        run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{expansion.strip()}\n")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
