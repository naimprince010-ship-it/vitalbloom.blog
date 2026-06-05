# Publish Cadence Mitigation

Generated: 2026-06-05

## Live Publish Date Distribution

- 2026-06-02: 36 published posts
- 2026-06-01: 24 published posts
- 2026-05-31: 10 published posts
- 2026-05-30: 30 published posts

## Risk

The site has a visible bulk-publishing pattern. This can look rushed to readers and may weaken trust signals for health and wellness content, especially when many posts share similar publication windows.

## Safe Mitigation

Do not fake historical publication dates. Instead:

1. Keep original `datePublished` available for transparency.
2. Emphasize `dateModified`/updated dates on listing cards after real content review.
3. Continue improving posts in batches and record real review dates.
4. Publish future new posts on a slower cadence, ideally 2-5 posts per week.
5. Avoid adding large new batches until existing priority content has been reviewed, strengthened, and indexed.

## Frontend Change

Homepage and category listing cards should show `Updated <date>` when a post has a modified date, falling back to `Published <date>` only when no update date exists. Individual article pages can still show original publication date plus updated/reviewed signals.
