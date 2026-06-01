import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-stress-reset-link-v1 -->"

LINK_SECTIONS: dict[str, str] = {
    "stress-management-guide": """
<section>
  <h2>Printable Stress Reset Checklist</h2>
  <p>If you want a shorter worksheet version of these steps, use the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a> to calm your body, reduce input, and choose one realistic next action.</p>
</section>
""",
    "simple-breathing-exercises": """
<section>
  <h2>Pair Breathing With a Reset Checklist</h2>
  <p>For a broader stress reset you can reuse during busy days, try the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a>.</p>
</section>
""",
    "practice-mindfulness-simply": """
<section>
  <h2>Use a Simple Stress Reset</h2>
  <p>If mindfulness feels hard when you are overwhelmed, the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a> can help you start with grounding and one small next step.</p>
</section>
""",
    "stress-affects-sleep": """
<section>
  <h2>Reset Stress Before Bed</h2>
  <p>When stress is making the evening feel scattered, use the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a> before moving into your sleep routine.</p>
</section>
""",
    "how-to-avoid-burnout": """
<section>
  <h2>Use a Stress Reset Before Burnout Builds</h2>
  <p>For a quick daily check-in, the <a href="/stress-reset-checklist-printable">Stress Reset Checklist Printable</a> can help you notice tension, reduce overload, and choose one next boundary.</p>
</section>
""",
}


def run_wp(*args: str) -> str:
    result = subprocess.run(
        ["wp", *args, "--allow-root"],
        cwd=WP_PATH,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID").strip()
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def main() -> None:
    for slug, section in LINK_SECTIONS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        if MARKER in content or 'href="/stress-reset-checklist-printable"' in content:
            print(f"already-linked: {slug}")
            continue

        updated = content.rstrip() + "\n\n" + MARKER + "\n" + section.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"linked: {pid} {slug}")


if __name__ == "__main__":
    main()
