import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
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
