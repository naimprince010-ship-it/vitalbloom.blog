import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-sleep-printable-link-v1 -->"

LINK_SECTIONS: dict[str, str] = {
    "sleep-hygiene-checklist": """
<section>
  <h2>Printable Sleep Hygiene Checklist</h2>
  <p>If you want a simpler weekly version of these habits, use our <a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a> as a quick evening reset and bedroom audit.</p>
</section>
""",
    "evening-habits-better-rest": """
<section>
  <h2>Use a Printable Evening Reset</h2>
  <p>For a shorter checklist you can reuse each week, see the <a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a>.</p>
</section>
""",
    "screen-time-and-sleep-quality": """
<section>
  <h2>Pair Screen Boundaries With a Checklist</h2>
  <p>To turn screen changes into a repeatable bedtime routine, try the <a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a>.</p>
</section>
""",
    "stress-affects-sleep": """
<section>
  <h2>Use a Simple Sleep Reset</h2>
  <p>If stress makes bedtime feel scattered, the <a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a> can help you choose one calming next step.</p>
</section>
""",
    "beginner-evening-routine-better-sleep": """
<section>
  <h2>Printable Checklist for Your Evening Routine</h2>
  <p>For a weekly tracker version of these steps, use the <a href="/sleep-hygiene-checklist-printable">Sleep Hygiene Checklist Printable</a>.</p>
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
        if MARKER in content or 'href="/sleep-hygiene-checklist-printable"' in content:
            print(f"already-linked: {slug}")
            continue

        updated = content.rstrip() + "\n\n" + MARKER + "\n" + section.strip() + "\n"
        run_wp("post", "update", pid, f"--post_content={updated}")
        print(f"linked: {pid} {slug}")


if __name__ == "__main__":
    main()
