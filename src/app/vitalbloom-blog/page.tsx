import type { Metadata } from "next";
import JsonLd from "@/components/JsonLd";
import Link from "next/link";
import { siteConfig } from "@/config/site";
import { breadcrumbSchema } from "@/lib/schema";

const pageUrl = `${siteConfig.url}/vitalbloom-blog`;

export const metadata: Metadata = {
  title: "VitalBloom Blog Official Website",
  description:
    "VitalBloom Blog is the official wellness publication at VitalBloom.blog, offering free evidence-informed guides rather than selling supplements, teas, skincare, or medical services.",
  alternates: {
    canonical: pageUrl
  },
  openGraph: {
    title: "VitalBloom Blog Official Website",
    description:
      "Learn what VitalBloom Blog is, what we publish, and how to find the official VitalBloom.blog wellness publication.",
    url: pageUrl
  },
  twitter: {
    title: "VitalBloom Blog Official Website",
    description:
      "Learn what VitalBloom Blog is, what we publish, and how to find the official VitalBloom.blog wellness publication."
  }
};

const brandPageSchema = {
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": `${pageUrl}#aboutpage`,
  name: "VitalBloom Blog Official Website",
  description:
    "VitalBloom Blog is the official wellness publication at VitalBloom.blog. It publishes free educational wellness guides and does not sell supplements, teas, skincare, or medical services.",
  url: pageUrl,
  isPartOf: {
    "@id": `${siteConfig.url}/#website`
  },
  about: {
    "@id": `${siteConfig.url}/#organization`
  },
  mainEntity: {
    "@id": `${siteConfig.url}/#organization`
  },
  inLanguage: "en"
};

const brandBreadcrumbSchema = breadcrumbSchema([
  { name: "Home", url: "/" },
  { name: "VitalBloom Blog Official Website", url: pageUrl }
]);

export default function VitalBloomBlogPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <JsonLd data={[brandPageSchema, brandBreadcrumbSchema]} />
      <article className="w-full max-w-3xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            Official Site
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            VitalBloom Blog Official Website
          </h1>
          <p className="mt-3 text-sm leading-6 text-zinc-600">
            VitalBloom Blog is the official wellness publication at
            VitalBloom.blog.
          </p>
        </header>

        <div className="mt-6 space-y-7 text-sm leading-7 text-zinc-700">
          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              What VitalBloom Blog Is
            </h2>
            <p className="mt-2">
              VitalBloom Blog publishes free educational wellness guides for
              everyday readers. We cover nutrition, fitness, sleep, stress,
              mindfulness, lifestyle routines, and balanced healthy living.
            </p>
            <p className="mt-2">
              If you searched for VitalBloom, this is the official
              VitalBloom.blog website and brand page for the VitalBloom Blog
              wellness publication.
            </p>
            <p className="mt-2">
              The official web address for this publication is{" "}
              <a
                href={siteConfig.url}
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                {siteConfig.url}
              </a>
              .
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              What VitalBloom Blog Is Not
            </h2>
            <p className="mt-2">
              VitalBloom Blog is not a supplement store, tea shop, skincare
              store, telemedicine service, or medical clinic. We do not sell
              products, diagnose conditions, or provide personalized health care.
            </p>
            <p className="mt-2">
              Our purpose is educational publishing: practical guides, checklists,
              source-backed explanations, and safer wellness language for readers
              who want realistic habits.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              Where to Start
            </h2>
            <div className="mt-3 grid gap-3 sm:grid-cols-2">
              <Link
                href="/stress-management-guide"
                className="rounded-md border border-zinc-200 p-4 font-medium text-zinc-900 hover:border-zinc-300"
              >
                Stress Management Guide
              </Link>
              <Link
                href="/balanced-plate-guide"
                className="rounded-md border border-zinc-200 p-4 font-medium text-zinc-900 hover:border-zinc-300"
              >
                Balanced Plate Guide
              </Link>
              <Link
                href="/better-sleep-routine-guide"
                className="rounded-md border border-zinc-200 p-4 font-medium text-zinc-900 hover:border-zinc-300"
              >
                Better Sleep Routine Guide
              </Link>
              <Link
                href="/beginner-home-workout-guide"
                className="rounded-md border border-zinc-200 p-4 font-medium text-zinc-900 hover:border-zinc-300"
              >
                Beginner Home Workout Guide
              </Link>
            </div>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              How We Build Trust
            </h2>
            <p className="mt-2">
              Our articles use an evidence-informed editorial process, visible
              references where health claims are involved, clear disclaimers,
              correction pathways, and cautious wording around medical and mental
              health topics.
            </p>
            <p className="mt-2">
              Read more in our{" "}
              <Link
                href="/why-trust-vitalbloom"
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                trust guide
              </Link>{" "}
              and{" "}
              <Link
                href="/editorial-policy"
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                editorial policy
              </Link>
              .
            </p>
          </section>
        </div>
      </article>
    </main>
  );
}
