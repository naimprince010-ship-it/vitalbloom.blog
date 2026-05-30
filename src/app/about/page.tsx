import type { Metadata } from "next";
import { siteConfig } from "@/config/site";

export const metadata: Metadata = {
  title: "About",
  description:
    "Learn about VitalBloom's practical, evidence-informed wellness publishing mission."
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
            Articles are written for general education and are not a substitute
            for professional medical advice. Readers should speak with qualified
            professionals about personal health concerns.
          </p>
        </section>
      </article>
    </main>
  );
}
