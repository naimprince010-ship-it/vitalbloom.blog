import type { Metadata } from "next";
import { siteConfig } from "@/config/site";

export const metadata: Metadata = {
  title: "About",
  description:
    "Learn about VitalBloom's evidence-informed wellness publishing mission, editorial process, and reader-first standards.",
  alternates: {
    canonical: `${siteConfig.url}/about`
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
            About {siteConfig.name}
          </h1>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            {siteConfig.name} publishes practical wellness, nutrition, fitness,
            sleep, and mindfulness guides for everyday readers.
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
            Articles are written for general education and are not a substitute
            for professional medical advice. Readers should speak with qualified
            professionals about personal health concerns.
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
        </section>
      </article>
    </main>
  );
}
