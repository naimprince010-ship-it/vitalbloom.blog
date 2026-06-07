export const siteConfig = {
  name: "VitalBloom",
  brandName: "VitalBloom Blog",
  title: "VitalBloom Blog: Evidence-informed wellness and healthy living guides",
  description:
    "VitalBloom Blog is the wellness publication at VitalBloom.blog, publishing practical guides on nutrition, fitness, sleep, stress, mindfulness, and healthy living.",
  url: "https://www.vitalbloom.blog",
  locale: "en_US",
  contactEmail: "hello@vitalbloom.blog",
  defaultOgImage: "/og-default.png"
} as const;

export const seoDefaults = {
  defaultTitle: siteConfig.title,
  titleTemplate: `%s | ${siteConfig.name}`,
  defaultDescription: siteConfig.description,
  canonical: siteConfig.url,
  robots: {
    index: true,
    follow: true
  }
} as const;

export const mainNavigation = [
  { label: "Join", href: "/join" },
  { label: "Nutrition", href: "/category/nutrition" },
  { label: "Fitness", href: "/category/fitness" },
  { label: "Mindfulness", href: "/category/mindfulness" },
  { label: "Stress", href: "/category/stress" },
  { label: "Wellness", href: "/category/wellness" },
  { label: "Lifestyle", href: "/category/lifestyle" },
  { label: "Sleep", href: "/category/sleep" }
] as const;

export const footerNavigation = {
  company: [
    { label: "Home", href: "/" },
    { label: "Join", href: "/join" },
    { label: "7-Day Wellness Reset", href: "/7-day-wellness-reset" },
    { label: "VitalBloom Blog", href: "/vitalbloom-blog" },
    { label: "About", href: "/about" },
    { label: "Why Trust Us", href: "/why-trust-vitalbloom" },
    { label: "Contact", href: "/contact" },
    { label: "Privacy Policy", href: "/privacy-policy" },
    { label: "Terms", href: "/terms" }
  ],
  categories: [
    { label: "Nutrition", href: "/category/nutrition" },
    { label: "Fitness", href: "/category/fitness" },
    { label: "Mindfulness", href: "/category/mindfulness" },
    { label: "Stress", href: "/category/stress" },
    { label: "Wellness", href: "/category/wellness" },
    { label: "Lifestyle", href: "/category/lifestyle" },
    { label: "Sleep", href: "/category/sleep" }
  ],
  legal: [
    { label: "Disclaimer", href: "/disclaimer" },
    { label: "Editorial Policy", href: "/editorial-policy" },
    { label: "Cookie Policy", href: "/cookie-policy" }
  ]
} as const;
