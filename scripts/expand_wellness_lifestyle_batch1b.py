import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-wellness-lifestyle-batch1-expanded-v1b -->"

EXPANSIONS = {
    "healthy-habits-when-life-feels-busy": """
<h2>Choose a Busy-Day Version and a Better-Day Version</h2>
<p>Every habit can have two versions. The busy-day version is the smallest useful action: five minutes of walking, one balanced snack, one glass of water, or a 10-minute wind-down. The better-day version can be longer or more complete.</p>
<p>This removes the pressure to do the same routine every day. Your life changes, so your habit size can change too. What matters is keeping the thread of care intact instead of waiting for a perfect week.</p>
""",
    "how-to-build-a-weekly-reset-routine": """
<h2>Prepare for the Most Difficult Day</h2>
<p>During the reset, identify the hardest day of the upcoming week. Then choose one support for that day: an easy dinner, a shorter workout, a packed snack, a bedtime reminder, or fewer optional tasks.</p>
<p>This is where a weekly reset becomes practical. You are not only organizing the week; you are protecting the day most likely to drain you. One support placed in advance can prevent a hard day from turning into a hard week.</p>
""",
    "simple-self-care-checklist": """
<h2>Make a Stress-Level Version</h2>
<p>Create three versions of self-care: low stress, medium stress, and high stress. Low stress might include a walk or meal prep. Medium stress might include a breathing break, a boundary, and a simple dinner. High stress might mean contacting support, cancelling something nonessential, and resting.</p>
<p>This helps because self-care needs change with intensity. When stress is high, the checklist should become simpler and more supportive, not longer and more demanding.</p>
""",
    "digital-wellness-routine": """
<h2>Protect One Human Moment</h2>
<p>Choose one daily moment where screens stay away so another part of life can be more present. It might be breakfast, a walk, the first few minutes after work, a conversation, or the final part of bedtime.</p>
<p>This works because digital wellness is not only about reducing screen time. It is about making room for attention, rest, connection, and body cues that can get drowned out by constant input.</p>
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
