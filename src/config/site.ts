export const siteConfig = {
  name: "VitalBloom",
  title: "Evidence-informed wellness, nutrition, and healthy living guides",
  description:
    "VitalBloom.blog publishes practical wellness, nutrition, fitness, and mindful living guidance for everyday readers.",
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
  { label: "Nutrition", href: "/category/nutrition" },
  { label: "Fitness", href: "/category/fitness" },
  { label: "Mindfulness", href: "/category/mindfulness" },
  { label: "Wellness", href: "/category/wellness" },
  { label: "Sleep", href: "/category/sleep" }
] as const;

export const footerNavigation = {
  company: [
    { label: "Home", href: "/" },
    { label: "About", href: "/about" },
    { label: "Contact", href: "/contact" },
    { label: "Privacy Policy", href: "/privacy-policy" },
    { label: "Terms", href: "/terms" }
  ],
  categories: [
    { label: "Nutrition", href: "/category/nutrition" },
    { label: "Fitness", href: "/category/fitness" },
    { label: "Mindfulness", href: "/category/mindfulness" },
    { label: "Wellness", href: "/category/wellness" },
    { label: "Sleep", href: "/category/sleep" }
  ],
  legal: [
    { label: "Disclaimer", href: "/disclaimer" },
    { label: "Editorial Policy", href: "/editorial-policy" },
    { label: "Cookie Policy", href: "/cookie-policy" }
  ]
} as const;
