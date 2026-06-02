import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
MARKER = "<!-- vitalbloom-fitness-support-batch1-expanded-v1b -->"

EXPANSIONS = {
    "low-impact-cardio-for-beginners": """
<h2>Plan for Weather and Energy Changes</h2>
<p>A low-impact cardio plan should have more than one option. If the weather is bad, use an indoor walk, stationary bike, marching routine, or gentle dance session. If your energy is low, shorten the session instead of skipping everything. A five-minute version keeps the habit alive.</p>
<p>This flexibility is important because beginners often stop when the original plan becomes inconvenient. Treat the backup plan as part of the routine, not a lesser version. The more ways you have to start safely, the easier it is to keep moving across different weeks.</p>
""",
    "daily-mobility-routine": """
<h2>Choose a Morning or Evening Version</h2>
<p>Your mobility routine can change depending on the time of day. In the morning, use gentle movements that help you wake up: shoulder circles, ankle rocks, hip shifts, and slow sit-to-stands. In the evening, choose slower movements and breathing that help the day feel finished.</p>
<p>Having two versions prevents the routine from feeling rigid. You can use the morning version when you want energy and the evening version when you want calm. Both count because both keep you moving through comfortable ranges.</p>
""",
    "rest-day-routine-for-beginners": """
<h2>Know the Difference Between Rest and Quitting</h2>
<p>Rest is planned recovery. Quitting usually comes from uncertainty, discouragement, or a routine that feels too hard to restart. A rest day becomes more useful when you know the next step: the next walk, strength session, mobility break, or low-impact cardio day.</p>
<p>Write the next workout before the rest day begins. This small detail can reduce anxiety and keep the routine connected. You can relax today because tomorrow already has a simple plan.</p>
<h2>Use Rest Days to Lower Friction</h2>
<p>Rest days are a good time to make the next active day easier. Set out shoes, charge headphones, refill a water bottle, wash workout clothes, or choose the short version of your next routine. These small actions protect momentum without adding another workout.</p>
<p>Recovery is not only physical. It also includes reducing the mental effort needed to continue. When the next step is easy to see, returning to movement feels less dramatic.</p>
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
