import { maxInlineInternalLinksPerArticle } from "@/config/content-quality";

const internalHrefPattern = /href=(["'])(\/(?!\/)[^"']*)\1/gi;

const normalizeInternalHref = (href: string): string => {
  const [path] = href.split("#");
  const [cleanPath] = path.split("?");
  return cleanPath.replace(/\/$/, "");
};

const stripHtml = (value: string): string => {
  return value.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
};

const escapeAttribute = (value: string): string => {
  return value
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
};

export type ArticleHeading = {
  id: string;
  level: 2 | 3;
  text: string;
};

const slugifyHeading = (value: string): string => {
  return value
    .toLowerCase()
    .replace(/&amp;/g, "and")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
};

export const addHeadingIds = (html: string): string => {
  const seen = new Map<string, number>();

  return html.replace(/<h([23])\b([^>]*)>([\s\S]*?)<\/h\1>/gi, (match, level, attributes, content) => {
    if (/\sid=/i.test(attributes)) {
      return match;
    }

    const text = stripHtml(content);
    const baseId = slugifyHeading(text) || `section-${level}`;
    const seenCount = seen.get(baseId) || 0;
    seen.set(baseId, seenCount + 1);
    const id = seenCount === 0 ? baseId : `${baseId}-${seenCount + 1}`;

    return `<h${level}${attributes} id="${escapeAttribute(id)}">${content}</h${level}>`;
  });
};

export const extractArticleHeadings = (html: string): ArticleHeading[] => {
  return [...html.matchAll(/<h([23])\b([^>]*)>([\s\S]*?)<\/h\1>/gi)]
    .map((match): ArticleHeading | null => {
      const idMatch = match[2].match(/\sid=(["'])(.*?)\1/i);
      const text = stripHtml(match[3]);

      if (!idMatch || !text) {
        return null;
      }

      return {
        id: idMatch[2],
        level: match[1] === "2" ? 2 : 3,
        text
      };
    })
    .filter((heading): heading is ArticleHeading => Boolean(heading));
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

export const addTableCellLabels = (html: string): string => {
  return html.replace(/<table\b[^>]*>[\s\S]*?<\/table>/gi, (table) => {
    const headers = [...table.matchAll(/<th\b[^>]*>([\s\S]*?)<\/th>/gi)]
      .map((match) => stripHtml(match[1]))
      .filter(Boolean);

    if (headers.length === 0) {
      return table;
    }

    return table.replace(/<tr\b[^>]*>[\s\S]*?<\/tr>/gi, (row) => {
      if (/<th\b/i.test(row)) {
        return row;
      }

      let cellIndex = 0;

      return row.replace(/<td\b([^>]*)>/gi, (cellOpen, attributes) => {
        const label = headers[cellIndex];
        cellIndex += 1;

        if (!label || /\sdata-label=/i.test(attributes)) {
          return cellOpen;
        }

        return `<td${attributes} data-label="${escapeAttribute(label)}">`;
      });
    });
  });
};

export const prepareArticleHtml = (
  html: string,
  currentSlug: string,
  duplicateCanonicalSlugs: Record<string, string>
): string => {
  return addHeadingIds(
    addTableCellLabels(
      reduceRepeatedInternalLinks(
        addInternalLinkNofollowForDuplicates(html, currentSlug, duplicateCanonicalSlugs)
      )
    )
  );
};
