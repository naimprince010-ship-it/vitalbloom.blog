import type { Author, Category, Post } from "@/types/blog";
import { siteConfig } from "@/config/site";

const absoluteUrl = (pathOrUrl: string): string => {
  if (pathOrUrl.startsWith("http")) {
    return pathOrUrl;
  }

  return `${siteConfig.url}${pathOrUrl.startsWith("/") ? "" : "/"}${pathOrUrl}`;
};

export const organizationSchema = () => ({
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": `${siteConfig.url}/#organization`,
  name: siteConfig.name,
  url: siteConfig.url,
  contactPoint: {
    "@type": "ContactPoint",
    email: siteConfig.contactEmail,
    contactType: "customer support"
  }
});

export const websiteSchema = () => ({
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": `${siteConfig.url}/#website`,
  name: siteConfig.name,
  url: siteConfig.url,
  publisher: {
    "@id": `${siteConfig.url}/#organization`
  },
  inLanguage: "en"
});

export const breadcrumbSchema = (
  items: Array<{ name: string; url: string }>
) => ({
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  itemListElement: items.map((item, index) => ({
    "@type": "ListItem",
    position: index + 1,
    name: item.name,
    item: absoluteUrl(item.url)
  }))
});

export const articleSchema = (
  post: Post,
  author: Author | undefined,
  category: Category | undefined
) => ({
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": `${siteConfig.url}/${post.slug}#article`,
  headline: post.title,
  description: post.seo.metaDescription || post.excerpt,
  image: post.featuredImage ? [post.featuredImage] : undefined,
  datePublished: post.publishedAt,
  dateModified: post.updatedAt || post.publishedAt,
  author: {
    "@type": "Person",
    name: author?.name || "VitalBloom Editorial Team"
  },
  publisher: {
    "@id": `${siteConfig.url}/#organization`
  },
  mainEntityOfPage: {
    "@type": "WebPage",
    "@id": `${siteConfig.url}/${post.slug}`
  },
  articleSection: category?.name,
  citation: post.sources.map((source) => source.url),
  reviewedBy: post.editorialReview.reviewedBy
    ? {
        "@type": "Person",
        name: post.editorialReview.reviewedBy
      }
    : undefined,
  inLanguage: "en"
});

export const collectionPageSchema = (category: Category, posts: Post[]) => ({
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "@id": `${siteConfig.url}/category/${category.slug}#collection`,
  name: `${category.name} Articles`,
  description: category.description,
  url: `${siteConfig.url}/category/${category.slug}`,
  isPartOf: {
    "@id": `${siteConfig.url}/#website`
  },
  mainEntity: {
    "@type": "ItemList",
    itemListElement: posts.map((post, index) => ({
      "@type": "ListItem",
      position: index + 1,
      url: `${siteConfig.url}/${post.slug}`,
      name: post.title
    }))
  }
});
