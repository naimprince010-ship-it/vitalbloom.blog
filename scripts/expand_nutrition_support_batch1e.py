import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch1-expanded-v1e -->"


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def main() -> None:
    slug = "fiber-rich-carbohydrates-guide"
    pid = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    content = run_wp("post", "get", pid, "--field=post_content")
    if MARKER in content:
        print(f"already-expanded: {slug}")
        return
    expansion = """
<h2>Start Where You Are</h2>
<p>If fiber-rich foods are new for you, begin with the option that already feels familiar. Familiar foods are easier to repeat, and repetition is what turns nutrition advice into a real habit.</p>
"""
    run_wp("post", "update", pid, f"--post_content={content.rstrip()}\n\n{MARKER}\n{expansion.strip()}\n")
    print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
