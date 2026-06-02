import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-nutrition-support-batch1-expanded-v1c -->"

EXPANSIONS = {
    "hydration-tracker-printable": """
<h2>Hydration Tracker for Remote Workers</h2>
<p>Remote workers may sit for long blocks without natural breaks. Use hydration as a reason to move. Keep water visible for focus blocks, then refill away from the desk. This turns hydration into both a fluid cue and a movement cue.</p>
<h2>Hydration Tracker for Busy Mornings</h2>
<p>If mornings are rushed, pair water with a habit you already do: brushing teeth, making coffee, packing a bag, or opening the laptop. A small morning cue can prevent the pattern of forgetting fluids until late afternoon.</p>
""",
    "add-protein-to-every-meal": """
<h2>Protein and Snacks</h2>
<p>If meals are far apart, a protein-containing snack can help. Try yogurt with fruit, hummus with vegetables, nuts with fruit, cottage cheese with crackers, or edamame. Snacks do not need to be large; they need to solve the gap between meals.</p>
<h2>Build a Protein Rotation</h2>
<p>Choose three protein anchors for the week. For example: eggs for breakfast, beans for lunch, tofu or chicken for dinner. A small rotation reduces decision fatigue while still giving variety.</p>
<h2>Avoid All-or-Nothing Thinking</h2>
<p>Not every meal will be perfectly balanced. If one meal is low in protein, add a protein-rich snack or make the next meal more complete. Flexible correction is easier to sustain than strict rules.</p>
""",
    "fiber-rich-carbohydrates-guide": """
<h2>How Fiber Fits the Plate Method</h2>
<p>In the plate method, fiber-rich carbohydrates usually fill one quarter of the plate, while produce fills half and protein fills the remaining quarter. This visual structure helps you include carbohydrates without letting them crowd out protein or produce.</p>
<h2>Easy Swaps</h2>
<ul>
  <li>Add beans to a rice bowl.</li>
  <li>Choose oats instead of a low-fiber breakfast.</li>
  <li>Add fruit to yogurt.</li>
  <li>Use whole-grain bread for a sandwich.</li>
  <li>Choose potatoes with the skin when appropriate.</li>
</ul>
<h2>When Convenience Helps</h2>
<p>Microwave grains, canned beans, frozen vegetables, and pre-cut fruit can make fiber easier. Convenience foods can support health when they help you build a balanced meal more often.</p>
""",
    "healthy-snack-plate-ideas": """
<h2>Snack Plate Prep</h2>
<p>Prepare snack components once or twice per week. Wash fruit, portion nuts, boil eggs, cut vegetables, or keep hummus and crackers ready. Prep does not need to be elaborate; it just needs to make the better option easier to grab.</p>
<h2>Snack Plates and Hydration</h2>
<p>Pair snacks with water or another suitable drink. Sometimes afternoon fatigue is a mix of hunger, thirst, and screen overload. A snack plate plus water and a short break may work better than eating while still rushing.</p>
<h2>Build a Five-Minute Snack</h2>
<p>Choose one protein, one produce item, and one crunchy or fiber-rich item. For example: cheese, grapes, and crackers; hummus, carrots, and pita; or yogurt, berries, and oats. Keep the formula simple enough to use when you are tired.</p>
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
