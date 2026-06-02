import json
import subprocess
from pathlib import Path


WP_PATH = Path("/var/www/backend.vitalbloom.blog")


def run_wp(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def run_wp_optional(*args: str) -> str:
    result = subprocess.run(["wp", *args, "--allow-root"], cwd=WP_PATH, text=True, capture_output=True, check=False)
    return result.stdout.strip()


def main() -> None:
    posts = json.loads(run_wp("post", "list", "--post_type=post", "--post_status=publish", "--fields=ID,post_name,post_title", "--format=json"))
    missing = []
    for post in posts:
        thumb = run_wp_optional("post", "meta", "get", str(post["ID"]), "_thumbnail_id")
        if not thumb:
            missing.append(post)
            print(f'{post["ID"]}|{post["post_name"]}|{post["post_title"]}')
    print(f"missing_count={len(missing)}")
    print(f"total_count={len(posts)}")


if __name__ == "__main__":
    main()
