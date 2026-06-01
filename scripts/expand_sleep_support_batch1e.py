import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-support-batch1-expanded-v1e -->"


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def main() -> None:
    slug = "caffeine-and-sleep-cutoff"
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    pid = found.splitlines()[0]
    content = run_wp("post", "get", pid, "--field=post_content")
    if MARKER in content:
        print(f"already-expanded: {slug}")
        return
    expansion = """
<h2>Keep the Experiment Simple</h2>
<p>Do not change bedtime, caffeine, workouts, screens, and meals all at once if your goal is to understand caffeine. Keep the experiment simple enough that you can see the pattern. A clear cutoff test is more useful than a complicated reset that is impossible to interpret.</p>
"""
    updated = content.rstrip() + "\n\n" + MARKER + "\n" + expansion.strip() + "\n"
    run_wp("post", "update", pid, f"--post_content={updated}")
    print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
