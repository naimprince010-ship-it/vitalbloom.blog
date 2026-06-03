import { maxInlineInternalLinksPerArticle } from "@/config/content-quality";

const internalHrefPattern = /href=(["'])(\/(?!\/)[^"']*)\1/gi;

const normalizeInternalHref = (href: string): string => {
  const [path] = href.split("#");
  const [cleanPath] = path.split("?");
  return cleanPath.replace(/\/$/, "");
};

export const reduceRepeatedInternalLinks = (html: string): string => {
  const seenByHref = new Map<string, number>();
  let totalInternalLinks = 0;

  return html.replace(/<a\b[^>]*href=(["'])(\/(?!\/)[^"']*)\1[^>]*>([\s\S]*?)<\/a>/gi, (match, _quote, href, text) => {
    const normalizedHref = normalizeInternalHref(href);
    const seenCount = seenByHref.get(normalizedHref) || 0;
    seenByHref.set(normalizedHref, seenCount + 1);
    totalInternalLinks += 1;

    if (seenCount > 0 || totalInternalLinks > maxInlineInternalLinksPerArticle) {
      return text;
    }

    return match;
  });
};

export const addInternalLinkNofollowForDuplicates = (
  html: string,
  currentSlug: string,
  duplicateCanonicalSlugs: Record<string, string>
): string => {
  const canonicalSlug = duplicateCanonicalSlugs[currentSlug];

  if (!canonicalSlug) {
    return html;
  }

  return html.replace(internalHrefPattern, (match, quote, href) => {
    const normalizedHref = normalizeInternalHref(href);

    if (normalizedHref === `/${currentSlug}`) {
      return `href=${quote}/${canonicalSlug}${quote}`;
    }

    return match;
  });
};

export const prepareArticleHtml = (
  html: string,
  currentSlug: string,
  duplicateCanonicalSlugs: Record<string, string>
): string => {
  return reduceRepeatedInternalLinks(
    addInternalLinkNofollowForDuplicates(html, currentSlug, duplicateCanonicalSlugs)
  );
};
