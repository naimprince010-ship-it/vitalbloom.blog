import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")

LINKS = {
    "daily-wellness-checklist": [
        ("balanced meal", "/healthy-breakfast-ideas"),
        ("sleep routine", "/better-sleep-routine"),
    ],
    "sustainable-wellness-routine": [
        ("movement", "/walking-for-weight-management"),
        ("sleep plan", "/sleep-hygiene-checklist"),
    ],
    "healthy-breakfast-ideas": [
        ("protein", "/high-protein-vegetarian-meals"),
        ("balanced meal", "/daily-wellness-checklist"),
    ],
    "beginner-home-workout-plan": [
        ("walking", "/walking-for-weight-management"),
        ("recovery", "/better-sleep-routine"),
    ],
    "better-sleep-routine": [
        ("sleep hygiene", "/sleep-hygiene-checklist"),
        ("breathing exercise", "/simple-breathing-exercises"),
    ],
    "high-protein-vegetarian-meals": [
        ("balanced diet", "/daily-wellness-checklist"),
        ("breakfast", "/healthy-breakfast-ideas"),
    ],
    "walking-for-weight-management": [
        ("balanced eating", "/high-protein-vegetarian-meals"),
        ("sustainable routine", "/sustainable-wellness-routine"),
    ],
    "sleep-hygiene-checklist": [
        ("sleep routine", "/better-sleep-routine"),
        ("slow breathing", "/simple-breathing-exercises"),
    ],
    "simple-breathing-exercises": [
        ("sleep", "/sleep-hygiene-checklist"),
        ("remote work", "/healthy-habits-remote-workers"),
    ],
    "healthy-habits-remote-workers": [
        ("movement breaks", "/walking-for-weight-management"),
        ("breathing", "/simple-breathing-exercises"),
    ],
    "foods-support-better-digestion": [
        ("hydration", "/daily-wellness-checklist"),
        ("fiber-rich foods", "/high-protein-vegetarian-meals"),
    ],
    "stretching-routine-desk-workers": [
        ("walking", "/walking-for-weight-management"),
        ("home workout", "/beginner-home-workout-plan"),
    ],
    "evening-habits-better-rest": [
        ("Slow breathing", "/simple-breathing-exercises"),
        ("bedroom", "/sleep-hygiene-checklist"),
    ],
    "beginner-meditation-guide": [
        ("breath meditation", "/simple-breathing-exercises"),
        ("stress", "/how-to-avoid-burnout"),
    ],
    "how-to-avoid-burnout": [
        ("remote workers", "/healthy-habits-remote-workers"),
        ("sleep routine", "/better-sleep-routine"),
    ],
    "simple-hydration-guide": [
        ("Water-rich foods", "/foods-support-better-digestion"),
        ("movement", "/walking-for-weight-management"),
    ],
    "strength-training-basics": [
        ("home workouts", "/beginner-home-workout-plan"),
        ("recovery", "/better-sleep-routine"),
    ],
    "foods-drinks-affect-sleep": [
        ("Caffeine", "/sleep-hygiene-checklist"),
        ("evening meal", "/evening-habits-better-rest"),
    ],
    "journaling-mental-clarity": [
        ("Evening journaling", "/evening-habits-better-rest"),
        ("stress", "/how-to-avoid-burnout"),
    ],
    "seasonal-wellness-tips": [
        ("Hydration", "/simple-hydration-guide"),
        ("morning light", "/sleep-hygiene-checklist"),
    ],
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


def link_once(content: str, phrase: str, href: str) -> str:
    if f'href="{href}"' in content:
        return content

    linked_phrase = f'<a href="{href}">{phrase}</a>'
    lower_content = content.lower()
    lower_phrase = phrase.lower()
    index = lower_content.find(lower_phrase)
    if index == -1:
        return content

    return f"{content[:index]}{linked_phrase}{content[index + len(phrase):]}"


def main() -> None:
    for slug, links in LINKS.items():
        pid = post_id(slug)
        content = run_wp("post", "get", pid, "--field=post_content")
        updated = content
        for phrase, href in links:
            updated = link_once(updated, phrase, href)
        if updated != content:
            run_wp("post", "update", pid, f"--post_content={updated}")
            print(f"linked: {slug}")
        else:
            print(f"unchanged: {slug}")


if __name__ == "__main__":
    main()
