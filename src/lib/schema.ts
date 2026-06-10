import type { Author, Category, Post } from "@/types/blog";
import { siteConfig } from "@/config/site";

const absoluteUrl = (pathOrUrl: string): string => {
  if (pathOrUrl.startsWith("http")) {
    return pathOrUrl;
  }

  return `${siteConfig.url}${pathOrUrl.startsWith("/") ? "" : "/"}${pathOrUrl}`;
};

const isEditorialOrganizationName = (name: string | undefined): boolean => {
  return !name || /editorial|team|desk/i.test(name);
};

export const organizationSchema = () => ({
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": `${siteConfig.url}/#organization`,
  name: siteConfig.name,
  alternateName: [siteConfig.brandName, "VitalBloom.blog"],
  legalName: "VitalBloom Blog",
  url: siteConfig.url,
  sameAs: siteConfig.socialProfiles.map((profile) => profile.href),
  logo: absoluteUrl(siteConfig.defaultOgImage),
  description:
    "VitalBloom Blog is the official educational wellness publication at VitalBloom.blog covering nutrition, fitness, sleep, stress, mindfulness, lifestyle, and healthy living. VitalBloom Blog is not a supplement store, tea shop, skincare store, telemedicine service, or medical clinic.",
  keywords:
    "VitalBloom, VitalBloom Blog, VitalBloom.blog, wellness blog, healthy living guides",
  identifier: {
    "@type": "PropertyValue",
    propertyID: "officialWebsite",
    value: siteConfig.url
  },
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
  name: siteConfig.brandName,
  alternateName: [siteConfig.name, "VitalBloom.blog"],
  url: siteConfig.url,
  publisher: {
    "@id": `${siteConfig.url}/#organization`
  },
  about: [
    "Wellness",
    "Nutrition",
    "Fitness",
    "Sleep",
    "Stress management",
    "Mindfulness",
    "Healthy living"
  ],
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
  "@type": "BlogPosting",
  "@id": `${siteConfig.url}/${post.slug}#article`,
  headline: post.title,
  description: post.seo.metaDescription || post.excerpt,
  image: post.featuredImage
    ? [absoluteUrl(post.featuredImage)]
    : [absoluteUrl(siteConfig.defaultOgImage)],
  datePublished: post.publishedAt,
  dateModified: post.updatedAt || post.publishedAt,
  author: {
    "@type": isEditorialOrganizationName(author?.name) ? "Organization" : "Person",
    name: author?.name || "VitalBloom Editorial Team",
    url: siteConfig.url
  },
  publisher: {
    "@id": `${siteConfig.url}/#organization`
  },
  isPartOf: {
    "@id": `${siteConfig.url}/#website`
  },
  mainEntityOfPage: {
    "@type": "WebPage",
    "@id": `${siteConfig.url}/${post.slug}`
  },
  articleSection: category?.name,
  citation: post.sources.map((source) => ({
    "@type": "CreativeWork",
    name: source.title,
    url: source.url,
    publisher: source.publisher
      ? {
          "@type": "Organization",
          name: source.publisher
        }
      : undefined
  })),
  reviewedBy: post.editorialReview.reviewedBy || post.editorialReview.factCheckedBy
    ? {
        "@type": isEditorialOrganizationName(
          post.editorialReview.reviewedBy || post.editorialReview.factCheckedBy
        )
          ? "Organization"
          : "Person",
        name:
          post.editorialReview.reviewedBy ||
          post.editorialReview.factCheckedBy ||
          "VitalBloom Editorial Team"
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

export const faqPageSchema = (
  slug: string,
  faqs: Array<{ question: string; answer: string }>
) => ({
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": `${siteConfig.url}/${slug}#faq`,
  mainEntity: faqs.map((faq) => ({
    "@type": "Question",
    name: faq.question,
    acceptedAnswer: {
      "@type": "Answer",
      text: faq.answer
    }
  }))
});
