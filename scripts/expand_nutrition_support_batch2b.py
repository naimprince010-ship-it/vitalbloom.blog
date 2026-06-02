import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch2-expanded-v1b -->"

EXPANSIONS = {
    "how-to-eat-more-vegetables": """
<h2>Make the First Vegetable the Easiest One</h2>
<p>When you are building the habit, choose the easiest vegetable first. That might mean baby carrots, frozen broccoli, bagged salad, canned tomatoes, or prewashed greens. Easy counts because a vegetable you actually eat is more useful than a perfect option that stays unused.</p>
<p>After the habit feels normal, you can add more variety. Starting with convenience helps you build confidence and removes the pressure to cook from scratch every time.</p>
""",
    "budget-friendly-healthy-meals": """
<h2>Keep One Emergency Meal at Home</h2>
<p>An emergency meal can protect both your budget and your energy. Keep one simple meal available for nights when the plan falls apart. It might be canned beans, rice, frozen vegetables, and salsa, or eggs, potatoes, and frozen greens.</p>
<p>This backup does not need to be exciting. It needs to be fast, balanced enough, and cheaper than ordering food because there is nothing ready. A reliable emergency meal is one of the quietest budget tools in the kitchen.</p>
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
        updated = content.rstrip() + "\n\n" + MARKER + "\n" + expansion.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"expanded: {pid} {slug}")


if __name__ == "__main__":
    main()
