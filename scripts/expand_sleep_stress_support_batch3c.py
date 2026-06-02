import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-stress-support-batch3-expanded-v1c -->"

EXPANSIONS = {
    "phone-free-bedtime-routine": """
<h2>Start With Three Nights</h2>
<p>Try the routine for three nights before judging it. A short experiment feels less intimidating than a permanent rule, and it gives you enough experience to notice what needs adjusting.</p>
""",
    "simple-relaxation-techniques": """
<h2>End With One Next Step</h2>
<p>After relaxing, choose one next step: return to work, start dinner, go to bed, send one message, or write the worry down. Calm is easier to keep when it leads into a clear action.</p>
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
