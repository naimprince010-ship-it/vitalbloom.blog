import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")
IMAGE_DIR = Path("/tmp/vitalbloom-drafts")

POST_IMAGES = {
    "healthy-snack-plate-ideas": "healthy-snack-plate-ideas.png",
    "fiber-rich-carbohydrates-guide": "fiber-rich-carbohydrates-guide.png",
    "add-protein-to-every-meal": "add-protein-to-every-meal.png",
    "hydration-tracker-printable": "hydration-tracker-printable.png",
    "beginner-meal-prep-checklist": "beginner-meal-prep-checklist.png",
    "weekend-sleep-schedule": "weekend-sleep-schedule.png",
    "sleep-routine-for-parents-caregivers": "sleep-routine-for-parents-caregivers.png",
    "shift-work-sleep-basics": "shift-work-sleep-basics.png",
    "bedroom-environment-checklist": "bedroom-environment-checklist.png",
    "nap-timing-guide": "nap-timing-guide.png",
    "bedtime-anxiety-racing-thoughts": "bedtime-anxiety-racing-thoughts.png",
    "caffeine-and-sleep-cutoff": "caffeine-and-sleep-cutoff.png",
    "morning-light-and-sleep": "morning-light-and-sleep.png",
    "why-you-wake-up-tired": "why-you-wake-up-tired.png",
    "sleep-debt-recovery-guide": "sleep-debt-recovery-guide.png",
    "recover-after-stressful-day": "recover-after-stressful-day.png",
    "stress-journaling-prompts": "stress-journaling-prompts.png",
    "stress-and-screen-time": "stress-and-screen-time.png",
    "evening-stress-reset": "evening-stress-reset.png",
    "morning-stress-reset": "morning-stress-reset.png",
    "daily-stress-relief-routine": "daily-stress-relief-routine.png",
    "student-stress-management-checklist": "student-stress-management-checklist.png",
    "work-stress-reset-routine": "work-stress-reset-routine.png",
    "grounding-techniques-for-stress": "grounding-techniques-for-stress.png",
    "calm-down-when-stress-feels-overwhelming": "calm-down-when-stress-feels-overwhelming.png",
    "stress-reset-checklist-printable": "stress-reset-checklist-printable.png",
    "remote-worker-wellness-checklist": "remote-worker-wellness-checklist.png",
    "balanced-plate-printable-guide": "balanced-plate-printable-guide.png",
    "sleep-hygiene-checklist-printable": "sleep-hygiene-checklist-printable.png",
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
    return result.stdout.strip()


def post_id(slug: str) -> str:
    found = run_wp("post", "list", f"--name={slug}", "--post_type=post", "--field=ID")
    if not found:
        raise RuntimeError(f"Post not found: {slug}")
    return found.splitlines()[0]


def existing_attachment_id(slug: str) -> str | None:
    title = slug.replace("-", " ").title()
    attachments_json = run_wp(
        "post",
        "list",
        "--post_type=attachment",
        "--post_mime_type=image",
        "--fields=ID,post_title,post_name",
        "--format=json",
    )
    attachments = json.loads(attachments_json or "[]")
    for attachment in attachments:
        post_name = str(attachment.get("post_name", ""))
        post_title = str(attachment.get("post_title", ""))
        if post_name == slug or post_name.startswith(f"{slug}-") or post_title == title:
            return str(attachment["ID"])
    return None


def main() -> None:
    for slug, filename in POST_IMAGES.items():
        image_path = IMAGE_DIR / filename
        if not image_path.exists():
            raise RuntimeError(f"Image file missing: {image_path}")

        attachment_id = existing_attachment_id(slug)
        if attachment_id:
            action = "reused"
        else:
            attachment_id = run_wp(
                "media",
                "import",
                str(image_path),
                f"--title={slug.replace('-', ' ').title()}",
                f"--alt={slug.replace('-', ' ')}",
                "--porcelain",
            )
            action = "uploaded"

        run_wp("post", "meta", "update", post_id(slug), "_thumbnail_id", attachment_id)
        print(f"featured-image-{action}: {slug} -> {attachment_id}")


if __name__ == "__main__":
    main()
