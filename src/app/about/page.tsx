import type { Metadata } from "next";
import { siteConfig } from "@/config/site";

export const metadata: Metadata = {
  title: "About VitalBloom Blog",
  description:
    "Learn about VitalBloom Blog, the official wellness publication at VitalBloom.blog, including our publishing mission, editorial process, and reader-first standards.",
  alternates: {
    canonical: `${siteConfig.url}/about`
  },
  openGraph: {
    title: "About VitalBloom Blog",
    description:
      "Learn about VitalBloom Blog, the official wellness publication at VitalBloom.blog, including our publishing mission, editorial process, and reader-first standards.",
    url: `${siteConfig.url}/about`
  },
  twitter: {
    title: "About VitalBloom Blog",
    description:
      "Learn about VitalBloom Blog, the official wellness publication at VitalBloom.blog, including our publishing mission, editorial process, and reader-first standards."
  }
};

export default function AboutPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            About
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            About VitalBloom Blog
          </h1>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            VitalBloom Blog is the wellness publication at VitalBloom.blog. We
            publish practical wellness, nutrition, fitness, sleep, stress,
            lifestyle, and mindfulness guides for everyday readers.
          </p>
          <p>
            Our goal is to make healthy routines feel realistic. We focus on
            simple habits, balanced guidance, and careful language around health
            topics.
          </p>
          <p>
            We use an evidence-informed editorial process: articles are researched
            against credible public health, medical, academic, and expert sources
            when health claims are involved. Our editorial team prioritizes clear
            explanations, practical steps, and transparent references over hype or
            quick fixes.
          </p>
          <p>
            VitalBloom is an educational wellness publication. We do not provide
            diagnosis, treatment plans, or emergency support. We encourage readers
            to work with qualified professionals for personal medical, mental
            health, nutrition, or fitness concerns.
          </p>
          <p>
            Unless a page names a qualified reviewer, articles are editorially
            reviewed by VitalBloom for clarity, source alignment, and cautious
            health wording. We do not imply physician, dietitian, therapist, or
            trainer review where it has not happened.
          </p>
          <p>
            We label source-backed articles with references and editorial review
            details where available. We also maintain a correction path through
            our contact email so readers can flag unclear wording, broken
            sources, or outdated guidance.
          </p>
          <p>
            Our public contact address is {siteConfig.contactEmail}. The
            official website for this publication is {siteConfig.url}. We are
            building the publication in public-facing stages and currently use
            email as the primary contact channel rather than claiming social
            profiles that are not actively maintained.
          </p>
        </section>

        <section className="mt-8 grid gap-4 sm:grid-cols-2">
          <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-5">
            <h2 className="text-lg font-semibold text-zinc-900">What We Cover</h2>
            <p className="mt-2 text-sm leading-6 text-zinc-600">
              Sleep routines, beginner fitness, balanced eating, stress support,
              mindfulness, hydration, recovery, and sustainable daily habits.
            </p>
          </div>
          <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-5">
            <h2 className="text-lg font-semibold text-zinc-900">How We Work</h2>
            <p className="mt-2 text-sm leading-6 text-zinc-600">
              We build articles around reader intent, credible references, cautious
              health language, and updates when guidance or source quality changes.
            </p>
          </div>
          <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-5">
            <h2 className="text-lg font-semibold text-zinc-900">Review Standards</h2>
            <p className="mt-2 text-sm leading-6 text-zinc-600">
              Health-related articles are checked for source alignment, practical
              usefulness, and wording that avoids diagnosis, treatment claims, or
              one-size-fits-all promises.
            </p>
          </div>
          <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-5">
            <h2 className="text-lg font-semibold text-zinc-900">Reader Corrections</h2>
            <p className="mt-2 text-sm leading-6 text-zinc-600">
              Readers can request corrections, source reviews, or clarification by
              contacting us at {siteConfig.contactEmail}.
            </p>
          </div>
        </section>

        <section className="mt-8 border-t border-zinc-200 pt-6 text-sm leading-7 text-zinc-700">
          <h2 className="text-lg font-semibold text-zinc-900">
            Authorship and Accountability
          </h2>
          <p className="mt-2">
            Articles may be credited to the VitalBloom Editorial Team when they
            are produced through our shared editorial workflow. That byline means
            the content has been checked against our editorial standards, not that
            it has been personally reviewed by a licensed clinician.
          </p>
          <p className="mt-2">
            When we add named contributors or credentialed reviewers, their names,
            roles, and relevant qualifications will be shown on the article and in
            structured data.
          </p>
        </section>
      </article>
    </main>
  );
}
