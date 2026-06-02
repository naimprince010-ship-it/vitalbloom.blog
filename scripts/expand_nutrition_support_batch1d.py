import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch1-expanded-v1d -->"

EXPANSIONS = {
    "fiber-rich-carbohydrates-guide": """
<h2>Make Fiber a Daily Cue</h2>
<p>Instead of counting every gram, choose one daily fiber cue. Add fruit to breakfast, beans to lunch, or vegetables to dinner. Repeating one cue is easier than trying to redesign every meal at once.</p>
<h2>Fiber and Satisfaction</h2>
<p>Fiber-rich carbohydrates often make meals feel more complete because they add texture and staying power. Pair them with protein and flavor so the meal is satisfying, not just technically nutritious.</p>
""",
    "healthy-snack-plate-ideas": """
<h2>Snack Plates for Travel or Errands</h2>
<p>When you are away from home, use portable options: nuts, fruit, whole-grain crackers, roasted chickpeas, shelf-stable hummus, or a simple sandwich. A small planned snack can prevent long gaps that leave you overly hungry.</p>
<h2>Keep Snacks Flexible</h2>
<p>Some days need a bigger snack; some need only fruit or water. Let the snack solve the real need instead of following a rigid rule. Flexibility makes the habit easier to keep.</p>
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
