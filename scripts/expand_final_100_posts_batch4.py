import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-final-100-posts-expanded-v4 -->"


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def main() -> None:
    slug = "simple-energy-boosting-habits"
    pid = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    content = run_wp("post", "get", pid, "--field=post_content")
    if MARKER in content:
        print(f"already-expanded: {slug}")
        return
    expansion = """
<h2>Keep It Repeatable</h2>
<p>Choose energy habits you can repeat during ordinary weeks, not only ideal weeks. Repeatable basics create steadier results.</p>
"""
    run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{expansion.strip()}\n")
    print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
