import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")

# Fill this map batch-wise after source verification. Keep only credible sources.
REFERENCES: dict[str, dict[str, object]] = {
    # "example-post-slug": {
    #     "fact_checked_by": "VitalBloom Editorial Team",
    #     "fact_checked_at": "2026-05-30",
    #     "sources": [
    #         {
    #             "title": "Example Source Title",
    #             "url": "https://example.gov/source",
    #             "publisher": "Example Publisher",
    #             "accessedAt": "2026-05-30",
    #         }
    #     ],
    # },
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
