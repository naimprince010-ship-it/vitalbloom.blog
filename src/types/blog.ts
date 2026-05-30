export type Category = {
  id: string;
  name: string;
  slug: string;
  description: string;
};

export type Tag = {
  id: string;
  name: string;
  slug: string;
};

export type Author = {
  id: string;
  name: string;
  bio: string;
  avatar: string;
  expertise?: string[];
};

export type PostStatus = "draft" | "published" | "scheduled";

export type PostSeo = {
  metaTitle: string;
  metaDescription: string;
  canonicalUrl?: string;
  ogImage?: string;
  focusKeyword?: string;
};

export type Post = {
  id: string;
  title: string;
  slug: string;
  excerpt: string;
  content: string;
  featuredImage: string;
  readingTime: number;
  status: PostStatus;
  publishedAt: string;
  updatedAt?: string;
  authorId: string;
  categoryId: string;
  tagIds: string[];
  seo: PostSeo;
};
