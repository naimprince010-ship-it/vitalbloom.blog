import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")

DESCRIPTIONS = {
    "lifestyle": "Everyday routines, digital wellness, travel resets, remote work habits, and realistic lifestyle guidance.",
    "stress": "Stress relief tools, burnout prevention, work stress resets, student support, and calming routines.",
}


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def main() -> None:
    for slug, description in DESCRIPTIONS.items():
        term_id = run_wp("term", "list", "category", f"--slug={slug}", "--field=term_id").strip()
        if not term_id:
            raise RuntimeError(f"Category not found: {slug}")
        run_wp("term", "update", "category", term_id, f"--description={description}")
        print(f"updated: {slug} ({term_id})")


if __name__ == "__main__":
    main()
