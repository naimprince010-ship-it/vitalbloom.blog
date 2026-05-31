import type { Metadata } from "next";
import { siteConfig } from "@/config/site";

export const metadata: Metadata = {
  title: "Editorial Policy",
  description:
    "Read VitalBloom's editorial policy for sourcing, fact-checking, updates, corrections, and health content standards."
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
          </section>

          <section>
            <h2 className="text-lg font-semibold text-zinc-900">Fact-Checking Approach</h2>
            <p className="mt-2">
              VitalBloom articles are reviewed for clarity, source alignment, and
              responsible wording. We avoid presenting general wellness guidance as
              personal medical advice, and we use cautious language when evidence is
              mixed, early, or not appropriate for every reader.
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
