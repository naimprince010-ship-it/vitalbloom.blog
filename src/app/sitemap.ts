import type { MetadataRoute } from "next";
import { noindexDuplicateSlugs } from "@/config/content-quality";
import { siteConfig } from "@/config/site";
import { getCategories, getPosts } from "@/lib/api";

export const revalidate = 60;
export const dynamic = "force-dynamic";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [posts, categories] = await Promise.all([getPosts(), getCategories()]);
  const now = new Date();

  const staticRoutes = [
    "",
    "/join",
    "/vitalbloom-blog",
    "/about",
    "/why-trust-vitalbloom",
    "/contact",
    "/privacy-policy",
    "/terms",
    "/disclaimer",
    "/editorial-policy",
    "/cookie-policy"
  ].map((path) => ({
    url: `${siteConfig.url}${path}`,
    lastModified: now,
    changeFrequency: "monthly" as const,
    priority: path === "" ? 1 : 0.6
  }));

  const categoryRoutes = categories.map((category) => ({
    url: `${siteConfig.url}/category/${category.slug}`,
    lastModified: now,
    changeFrequency: "weekly" as const,
    priority: 0.7
  }));

  const postRoutes = posts
    .filter((post) => !noindexDuplicateSlugs.has(post.slug))
    .map((post) => ({
      url: `${siteConfig.url}/${post.slug}`,
      lastModified: new Date(post.updatedAt || post.publishedAt),
      changeFrequency: "monthly" as const,
      priority: 0.8
    }));

  return [...staticRoutes, ...categoryRoutes, ...postRoutes];
}
