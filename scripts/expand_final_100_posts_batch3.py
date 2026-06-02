import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-final-100-posts-expanded-v3 -->"

EXPANSIONS = {
    "how-to-stay-consistent-with-healthy-habits": """
<h2>Make the Next Step Obvious</h2>
<p>Consistency often fails when the next step is hidden. Leave the walking shoes visible, keep breakfast ingredients together, write the first line of tomorrow's task, or put the water bottle on the desk. The easier the next step is to see, the less energy it takes to begin.</p>
""",
    "weekend-reset-for-better-sleep": """
<h2>Use a Weekend Cutoff Cue</h2>
<p>Choose one cue that tells the weekend evening to slow down: closing the kitchen, dimming lights, putting the phone on charge, or writing Monday's first task. A cutoff cue helps the weekend feel restful without letting the night drift endlessly.</p>
""",
    "simple-energy-boosting-habits": """
<h2>End the Day in a Way That Helps Tomorrow</h2>
<p>Energy habits continue into the evening. Set out clothes, prepare breakfast, write one priority, or lower lights before bed. A calmer ending can make tomorrow's energy feel less dependent on willpower.</p>
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
