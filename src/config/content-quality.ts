import { siteConfig } from "@/config/site";

export const canonicalSlugOverrides: Record<string, string> = {
  "better-sleep-routine": "better-sleep-routine-guide",
  "balanced-plate-method": "balanced-plate-guide"
};

export const noindexDuplicateSlugs = new Set(Object.keys(canonicalSlugOverrides));

export const getCanonicalUrlForSlug = (slug: string): string => {
  const canonicalSlug = canonicalSlugOverrides[slug] || slug;
  return `${siteConfig.url}/${canonicalSlug}`;
};

export const maxInlineInternalLinksPerArticle = 10;
