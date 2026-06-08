import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    formats: ["image/avif", "image/webp"],
    minimumCacheTTL: 2678400,
    remotePatterns: [
      {
        protocol: "https",
        hostname: "backend.vitalbloom.blog",
        pathname: "/wp-content/uploads/**"
      }
    ]
  }
};

export default nextConfig;
