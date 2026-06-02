import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch3-expanded-v1c -->"

EXPANSIONS = {
    "simple-breakfast-meal-prep": """
<h2>Repeat Before You Add Variety</h2>
<p>Use the same breakfast for a few days before changing everything. Repetition teaches you whether the meal is filling, fast, and enjoyable enough. Once the routine works, add variety with different fruit, toppings, or flavors.</p>
""",
    "how-to-build-a-filling-salad": """
<h2>Prep Salad Parts Separately</h2>
<p>Keep greens, proteins, grains, dressing, and crunchy toppings separate until you are ready to eat. This keeps texture better and makes it easier to build different salads from the same prepared ingredients.</p>
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
