import { siteConfig } from "@/config/site";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Cookie Policy",
  description: `Learn how ${siteConfig.name} may use cookies for site functionality, analytics, and advertising measurement.`,
  alternates: {
    canonical: `${siteConfig.url}/cookie-policy`
  },
  openGraph: {
    title: `${siteConfig.name} Cookie Policy`,
    description: `Learn how ${siteConfig.name} may use cookies for site functionality, analytics, and advertising measurement.`,
    url: `${siteConfig.url}/cookie-policy`
  },
  twitter: {
    title: `${siteConfig.name} Cookie Policy`,
    description: `Learn how ${siteConfig.name} may use cookies for site functionality, analytics, and advertising measurement.`
  }
};

export default function CookiePolicyPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-xl border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <h1 className="text-3xl font-semibold tracking-tight text-zinc-900">Cookie Policy</h1>
          <p className="mt-2 text-sm text-zinc-600">Last updated: May 29, 2026</p>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            {siteConfig.name} uses cookies and similar technologies to improve website functionality,
            understand traffic patterns, and support advertising measurement.
          </p>
          <p>
            Essential cookies may be required for basic site operation. Optional analytics or advertising
            cookies may be introduced when those services are enabled and configured.
          </p>
          <p>
            Users can adjust cookie choices at any time through browser controls. Blocking some cookies may
            impact certain site features.
          </p>
          <p>
            For questions related to cookie usage, contact {siteConfig.contactEmail}.
          </p>
        </section>
      </article>
    </main>
  );
}
