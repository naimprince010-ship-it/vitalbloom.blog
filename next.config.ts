import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    deviceSizes: [360, 414, 640, 750, 828, 1080, 1200],
    formats: ["image/avif", "image/webp"],
    imageSizes: [220, 320, 360],
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
