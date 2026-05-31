import { siteConfig } from "@/config/site";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Disclaimer",
  description: `${siteConfig.name} publishes educational wellness content and does not replace professional medical advice.`
};

export default function DisclaimerPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-xl border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <h1 className="text-3xl font-semibold tracking-tight text-zinc-900">Disclaimer</h1>
          <p className="mt-2 text-sm text-zinc-600">Last updated: May 29, 2026</p>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            Content published on {siteConfig.name} is for general educational purposes only and does not
            replace professional medical, legal, or financial advice.
          </p>
          <p>
            Always consult qualified professionals before making decisions related to health, nutrition,
            fitness, or mental wellness.
          </p>
          <p>
            Some pages may contain sponsored links or advertising placements. Any compensation will not
            influence editorial integrity.
          </p>
          <p>
            If you have questions about this disclaimer, contact {siteConfig.contactEmail}.
          </p>
        </section>
      </article>
    </main>
  );
}
