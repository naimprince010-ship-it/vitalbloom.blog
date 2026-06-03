import type { Metadata } from "next";
import { siteConfig } from "@/config/site";

export const metadata: Metadata = {
  title: "Editorial Policy",
  description:
    "Read VitalBloom's editorial policy for sourcing, fact-checking, updates, corrections, and health content standards.",
  alternates: {
    canonical: `${siteConfig.url}/editorial-policy`
  },
  openGraph: {
    title: `${siteConfig.name} Editorial Policy`,
    description:
      "Read VitalBloom's editorial policy for sourcing, fact-checking, updates, corrections, and health content standards.",
    url: `${siteConfig.url}/editorial-policy`
  },
  twitter: {
    title: `${siteConfig.name} Editorial Policy`,
    description:
      "Read VitalBloom's editorial policy for sourcing, fact-checking, updates, corrections, and health content standards."
  }
};

export default function EditorialPolicyPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            Editorial Standards
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            Editorial Policy
          </h1>
          <p className="mt-3 text-sm leading-6 text-zinc-600">
            {siteConfig.name} publishes educational wellness content designed to be
            practical, transparent, and careful with health-related claims.
          </p>
        </header>

        <div className="mt-6 space-y-7 text-sm leading-7 text-zinc-700">
          <section>
            <h2 className="text-lg font-semibold text-zinc-900">Our Editorial Mission</h2>
            <p className="mt-2">
              We help readers build realistic routines around sleep, nutrition,
              movement, stress management, mindfulness, and everyday wellness. Our
              articles aim to explain what is generally known, what is practical to
              try, and when professional guidance may be needed.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">Sources and References</h2>
            <p className="mt-2">
              For health and wellness topics, we prioritize credible sources such
              as government health agencies, medical institutions, academic
              publications, peer-reviewed research databases, and recognized
              professional organizations. Sources are listed on articles when they
              support health claims or practical guidance.
            </p>
            <p className="mt-2">
              General references are not treated as proof for every sentence. When
              a post makes a specific health claim, our goal is to connect it to a
              relevant source and revise the page when the source support is too
              broad, outdated, or unclear.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">Fact-Checking Approach</h2>
            <p className="mt-2">
              VitalBloom articles are reviewed for clarity, source alignment, and
              responsible wording. We avoid presenting general wellness guidance as
              personal medical advice, and we use cautious language when evidence is
              mixed, early, or not appropriate for every reader.
            </p>
            <p className="mt-2">
              Our review checks include claim-source alignment, practical context,
              appropriate disclaimers, and whether a reader should be directed to a
              qualified professional for personal concerns.
            </p>
            <p className="mt-2">
              A VitalBloom editorial review is not the same as medical review. We
              only describe a page as medically, nutritionally, therapeutically, or
              professionally reviewed when a qualified reviewer is named.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              Authorship and Reviewer Labels
            </h2>
            <p className="mt-2">
              Some articles are credited to the VitalBloom Editorial Team because
              they are created and maintained through a shared editorial workflow.
              We avoid inventing individual author names or credentials. If a
              named contributor or credentialed reviewer is involved, the article
              should identify that person and their role.
            </p>
            <p className="mt-2">
              Articles also include a visible notice that they are general
              wellness information and not a substitute for professional care.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">
              Similar Topics and Canonical Pages
            </h2>
            <p className="mt-2">
              When two older articles cover nearly the same search intent, we keep
              the strongest page as the canonical version and may mark the shorter
              support page as non-indexable while preserving it for readers who
              already have the link. This reduces keyword cannibalization and
              makes the site easier to navigate.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">Updates and Corrections</h2>
            <p className="mt-2">
              We update content when we identify outdated wording, broken sources,
              better references, or new context that would help readers. If you see
              a possible error, outdated link, or unclear claim, contact us at{" "}
              <a
                href={`mailto:${siteConfig.contactEmail}`}
                className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
              >
                {siteConfig.contactEmail}
              </a>
              .
            </p>
            <p className="mt-2">
              High-impact health and wellness pages may be revisited when source
              quality changes, when reader feedback identifies unclear guidance, or
              when we expand an article with stronger examples, references, or
              internal links.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">Medical Disclaimer</h2>
            <p className="mt-2">
              VitalBloom content is for general education only. It is not a
              substitute for diagnosis, treatment, therapy, emergency care, or
              personalized advice from a qualified medical, mental health,
              nutrition, or fitness professional.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">Independence</h2>
            <p className="mt-2">
              Editorial choices are guided by reader usefulness, source quality, and
              responsible health communication. Advertising or monetization should
              not change the substance of our educational guidance.
            </p>
          </section>
        </div>
      </article>
    </main>
  );
}
