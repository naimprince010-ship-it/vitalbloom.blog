export const WP_POSTS_QUERY = /* GraphQL */ `
  query GetPublishedPosts($first: Int = 24) {
    posts(first: $first, where: { status: PUBLISH, orderby: { field: DATE, order: DESC } }) {
      nodes {
        id
        title
        slug
        excerpt
        content
        date
        modified
        featuredImage {
          node {
            sourceUrl
          }
        }
        author {
          node {
            id
            name
            description
            avatar {
              url
            }
          }
        }
        categories {
          nodes {
            id
            name
            slug
            description
          }
        }
        tags {
          nodes {
            id
            name
            slug
          }
        }
        seo {
          title
          metaDesc
          canonical
          focuskw
          opengraphImage {
            sourceUrl
          }
        }
      }
    }
  }
`;

export const WP_POST_BY_SLUG_QUERY = /* GraphQL */ `
  query GetPostBySlug($slug: ID!) {
    post(id: $slug, idType: SLUG) {
      id
      title
      slug
      excerpt
      content
      date
      modified
      featuredImage {
        node {
          sourceUrl
        }
      }
      author {
        node {
          id
          name
          description
          avatar {
            url
          }
        }
      }
      categories {
        nodes {
          id
          name
          slug
          description
        }
      }
      tags {
        nodes {
          id
          name
          slug
        }
      }
      seo {
        title
        metaDesc
        canonical
        focuskw
        opengraphImage {
          sourceUrl
        }
      }
    }
  }
`;

export const WP_POSTS_BY_CATEGORY_QUERY = /* GraphQL */ `
  query GetPublishedPostsByCategory($categorySlug: String!, $first: Int = 24) {
    posts(
      first: $first
      where: {
        status: PUBLISH
        categoryName: $categorySlug
        orderby: { field: DATE, order: DESC }
      }
    ) {
      nodes {
        id
        title
        slug
        excerpt
        content
        date
        modified
        featuredImage {
          node {
            sourceUrl
          }
        }
        author {
          node {
            id
            name
            description
            avatar {
              url
            }
          }
        }
        categories {
          nodes {
            id
            name
            slug
            description
          }
        }
        tags {
          nodes {
            id
            name
            slug
          }
        }
        seo {
          title
          metaDesc
          canonical
          focuskw
          opengraphImage {
            sourceUrl
          }
        }
      }
    }
  }
`;

export const WP_CATEGORIES_QUERY = /* GraphQL */ `
  query GetCategories($first: Int = 100) {
    categories(first: $first) {
      nodes {
        id
        name
        slug
        description
      }
    }
  }
`;
