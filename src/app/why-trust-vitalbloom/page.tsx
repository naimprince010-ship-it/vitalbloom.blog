import type { Metadata } from "next";
import Link from "next/link";
import { siteConfig } from "@/config/site";

export const metadata: Metadata = {
  title: "Why Trust VitalBloom Blog",
  description:
    "Learn why readers can trust VitalBloom Blog: editorial standards, sources, disclaimers, corrections, and transparent wellness publishing practices.",
  alternates: {
    canonical: `${siteConfig.url}/why-trust-vitalbloom`
  },
  openGraph: {
    title: "Why Trust VitalBloom Blog",
    description:
      "Learn about VitalBloom Blog's editorial standards, source policy, corrections process, and responsible wellness publishing practices.",
    url: `${siteConfig.url}/why-trust-vitalbloom`
  },
  twitter: {
    title: "Why Trust VitalBloom Blog",
    description:
      "Learn about VitalBloom Blog's editorial standards, source policy, corrections process, and responsible wellness publishing practices."
  }
};

export default function WhyTrustVitalBloomPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            Reader Trust
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            Why Trust VitalBloom Blog
          </h1>
          <p className="mt-3 text-sm leading-6 text-zinc-600">
            We publish wellness guidance with transparency, source awareness, and
            careful health language.
          </p>
        </header>

        <div className="mt-6 space-y-7 text-sm leading-7 text-zinc-700">
          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              1. We Are an Educational Publication
            </h2>
            <p className="mt-2">
              VitalBloom Blog is built for free wellness education. We do not
              sell supplements, teas, skincare products, meal plans, training
              programs, or medical services through the articles we publish.
            </p>
            <p className="mt-2">
              That helps us keep articles focused on reader usefulness instead
              of pushing a product.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              2. We Use an Evidence-Informed Editorial Process
            </h2>
            <p className="mt-2">
              Health and wellness articles are checked for source alignment,
              practical context, cautious wording, and reader safety. We
              prioritize sources such as public health agencies, medical
              institutions, academic sources, and recognized professional
              organizations when health claims are involved.
            </p>
            <p className="mt-2">
              Sources are shown on individual articles where available, and we
              avoid presenting broad references as proof for every personal
              situation.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              3. We Do Not Overstate Medical Authority
            </h2>
            <p className="mt-2">
              VitalBloom Blog does not claim professional medical, nutrition,
              therapy, or fitness review unless a qualified reviewer is named on
              the page. Most articles are general educational content, not
              diagnosis, treatment, or personalized advice.
            </p>
            <p className="mt-2">
              Articles that mention urgent mental health or safety concerns point
              readers toward crisis or professional support.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              4. We Publish Practical Tools
            </h2>
            <p className="mt-2">
              Alongside longer guides, we publish checklists and printable-style
              resources for sleep hygiene, stress resets, balanced plates,
              hydration, and remote worker wellness. These tools are designed to
              help readers turn general guidance into realistic next steps.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              5. We Accept Corrections
            </h2>
            <p className="mt-2">
              Readers can report unclear wording, outdated references, broken
              links, or possible corrections by emailing{" "}
              <a
                href={`mailto:${siteConfig.contactEmail}`}
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                {siteConfig.contactEmail}
              </a>
              .
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              6. Our Standards Are Public
            </h2>
            <p className="mt-2">
              Read the full{" "}
              <Link
                href="/editorial-policy"
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                Editorial Policy
              </Link>
              ,{" "}
              <Link
                href="/disclaimer"
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                Disclaimer
              </Link>
              , and{" "}
              <Link
                href="/about"
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                About page
              </Link>{" "}
              for more detail about how VitalBloom Blog works.
            </p>
          </section>
        </div>
      </article>
    </main>
  );
}
