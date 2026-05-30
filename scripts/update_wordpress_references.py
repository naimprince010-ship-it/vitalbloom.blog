import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")

# Fill this map batch-wise after source verification. Keep only credible sources.
REFERENCES: dict[str, dict[str, object]] = {
    "daily-wellness-routine-beginners": {
        "fact_checked_by": "VitalBloom Editorial Team",
        "fact_checked_at": "2026-05-30",
        "sources": [
            {
                "title": "Physical Wellness Toolkit",
                "url": "https://www.nih.gov/health-information/physical-wellness-toolkit",
                "publisher": "National Institutes of Health",
                "accessedAt": "2026-05-30",
            },
            {
                "title": "Health Tips for Adults",
                "url": "https://www.niddk.nih.gov/health-information/weight-management/healthy-eating-physical-activity-for-life/health-tips-for-adults",
                "publisher": "National Institute of Diabetes and Digestive and Kidney Diseases",
                "accessedAt": "2026-05-30",
            },
        ],
    },
    "practice-mindfulness-simply": {
        "fact_checked_by": "VitalBloom Editorial Team",
        "fact_checked_at": "2026-05-30",
        "sources": [
            {
                "title": "Meditation and Mindfulness: Effectiveness and Safety",
                "url": "https://www.nccih.nih.gov/health/meditation/overview.htm",
                "publisher": "National Center for Complementary and Integrative Health",
                "accessedAt": "2026-05-30",
            },
            {
                "title": "Stress",
                "url": "https://www.nccih.nih.gov/health/stress",
                "publisher": "National Center for Complementary and Integrative Health",
                "accessedAt": "2026-05-30",
            },
        ],
    },
    "stress-affects-sleep": {
        "fact_checked_by": "VitalBloom Editorial Team",
        "fact_checked_at": "2026-05-30",
        "sources": [
            {
                "title": "About Sleep",
                "url": "https://www.cdc.gov/sleep/about/index.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": "2026-05-30",
            },
            {
                "title": "Stress",
                "url": "https://www.nccih.nih.gov/health/stress",
                "publisher": "National Center for Complementary and Integrative Health",
                "accessedAt": "2026-05-30",
            },
        ],
    },
    "exercise-sustainable-habit": {
        "fact_checked_by": "VitalBloom Editorial Team",
        "fact_checked_at": "2026-05-30",
        "sources": [
            {
                "title": "Adult Activity: An Overview",
                "url": "https://www.cdc.gov/physical-activity-basics/guidelines/adults.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": "2026-05-30",
            },
            {
                "title": "Physical Activity and Your Heart - Getting Started and Staying Active",
                "url": "https://www.nhlbi.nih.gov/health/heart/physical-activity/stay-active",
                "publisher": "National Heart, Lung, and Blood Institute",
                "accessedAt": "2026-05-30",
            },
        ],
    },
    "balanced-plate-method": {
        "fact_checked_by": "VitalBloom Editorial Team",
        "fact_checked_at": "2026-05-30",
        "sources": [
            {
                "title": "Healthy Eating Plate",
                "url": "https://www.health.harvard.edu/plate/healthy-eating-plate",
                "publisher": "Harvard Health Publishing",
                "accessedAt": "2026-05-30",
            },
            {
                "title": "Healthy Eating Tips",
                "url": "https://www.cdc.gov/nutrition/features/healthy-eating-tips.html",
                "publisher": "Centers for Disease Control and Prevention",
                "accessedAt": "2026-05-30",
            },
        ],
    },
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


def update_references() -> None:
    for slug, data in REFERENCES.items():
        pid = post_id(slug)
        sources = data.get("sources", [])
        run_wp(
            "post",
            "meta",
            "update",
            pid,
            "_vitalbloom_sources",
            json.dumps(sources, ensure_ascii=True),
        )
        for source_key, meta_key in [
            ("fact_checked_by", "_vitalbloom_fact_checked_by"),
            ("fact_checked_at", "_vitalbloom_fact_checked_at"),
            ("reviewed_by", "_vitalbloom_reviewed_by"),
            ("reviewed_at", "_vitalbloom_reviewed_at"),
        ]:
            value = str(data.get(source_key, "")).strip()
            if value:
                run_wp("post", "meta", "update", pid, meta_key, value)
        print(f"references-updated: {slug}")


if __name__ == "__main__":
    update_references()
