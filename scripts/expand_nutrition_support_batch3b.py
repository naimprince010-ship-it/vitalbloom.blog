import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch3-expanded-v1b -->"

EXPANSIONS = {
    "easy-balanced-dinner-formula": """
<h2>Save Three Dinner Combinations</h2>
<p>Write down three combinations that already work in your home. They might be eggs with potatoes and greens, beans with rice and salsa, or pasta with lentils and vegetables. Keeping a short list removes the pressure to invent dinner when you are tired.</p>
""",
    "simple-breakfast-meal-prep": """
<h2>Keep One Backup Breakfast</h2>
<p>A backup breakfast helps when prep does not happen. Keep one option that needs almost no work, such as oats with nut butter, yogurt with fruit, or toast with eggs. This keeps the routine flexible instead of fragile.</p>
""",
    "how-to-build-a-filling-salad": """
<h2>Use Enough Food for the Meal</h2>
<p>If the salad is lunch or dinner, it needs enough total food to match that role. Add a larger portion of protein, grains, beans, potatoes, or healthy fats when needed. A salad can be fresh and still be substantial.</p>
""",
    "healthy-snacks-for-work": """
<h2>Notice Which Snacks Actually Work</h2>
<p>After a few workdays, notice which snacks kept you satisfied and which ones did not. Keep the options that support focus and energy, then adjust the ones that leave you hungry or uncomfortable.</p>
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
