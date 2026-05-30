import type { Metadata } from "next";
import { siteConfig } from "@/config/site";

export const metadata: Metadata = {
  title: "Contact",
  description: `Contact ${siteConfig.name} for editorial, privacy, or general website questions.`
};

export default function ContactPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            Contact
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            Contact {siteConfig.name}
          </h1>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            For editorial questions, privacy requests, corrections, or general
            website feedback, email us at{" "}
            <a
              href={`mailto:${siteConfig.contactEmail}`}
              className="font-semibold text-green-700 underline underline-offset-4 hover:text-green-800"
            >
              {siteConfig.contactEmail}
            </a>
            .
          </p>
          <p>
            Please do not send urgent medical questions. {siteConfig.name} does
            not provide personal medical advice, diagnosis, or treatment.
          </p>
        </section>
      </article>
    </main>
  );
}
