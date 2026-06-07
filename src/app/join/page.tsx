import type { Metadata } from "next";
import Link from "next/link";
import { siteConfig } from "@/config/site";

const joinSubject = "Join VitalBloom Blog and send the 7-Day Wellness Reset";
const joinBody = [
  "Hi VitalBloom Blog,",
  "",
  "I would like to join the VitalBloom member updates list and receive the 7-Day Wellness Reset.",
  "",
  "My main interests are:",
  "- Sleep",
  "- Stress",
  "- Nutrition",
  "- Fitness",
  "- Mindfulness",
  "- Wellness habits",
  "",
  "Thanks"
].join("\n");

const joinMailto = `mailto:${siteConfig.contactEmail}?subject=${encodeURIComponent(
  joinSubject
)}&body=${encodeURIComponent(joinBody)}`;

export const metadata: Metadata = {
  title: "Join VitalBloom Blog",
  description:
    "Join VitalBloom Blog for the 7-Day Wellness Reset, member updates, practical wellness guides, printable checklists, and future saved-guide features.",
  alternates: {
    canonical: `${siteConfig.url}/join`
  },
  openGraph: {
    title: "Join VitalBloom Blog",
    description:
      "Join VitalBloom Blog for the 7-Day Wellness Reset, member updates, practical wellness guides, printable checklists, and future saved-guide features.",
    url: `${siteConfig.url}/join`
  },
  twitter: {
    title: "Join VitalBloom Blog",
    description:
      "Join VitalBloom Blog for the 7-Day Wellness Reset, member updates, practical wellness guides, printable checklists, and future saved-guide features."
  }
};

export default function JoinPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            Member Updates
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            Join VitalBloom Blog
          </h1>
          <p className="mt-3 text-sm leading-6 text-zinc-600">
            Get the 7-Day Wellness Reset, practical wellness guides,
            checklists, and future member updates from the official VitalBloom
            Blog.
          </p>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            VitalBloom is being built as a useful wellness destination, not just
            a place people visit once. The member updates list is the first step
            toward saved guides, printable downloads, weekly routines, and
            personalized topic preferences.
          </p>
          <p>
            We do not provide personal medical advice, and joining does not
            replace care from a qualified professional. Updates are educational,
            practical, and focused on realistic habits.
          </p>
        </section>

        <section className="mt-8 rounded-lg border border-emerald-100 bg-emerald-50/70 p-5">
          <h2 className="text-lg font-semibold text-zinc-900">
            Get the 7-Day Wellness Reset
          </h2>
          <p className="mt-2 text-sm leading-6 text-zinc-700">
            Start with one week of realistic sleep, stress, nutrition,
            movement, and mindfulness actions. Send a quick email to join the
            waitlist and get reset updates while the full member account system
            is being built.
          </p>
          <div className="mt-4 flex flex-wrap gap-3">
            <a
              href={joinMailto}
              className="inline-flex rounded-md bg-emerald-700 px-4 py-2 text-sm font-semibold text-white transition hover:bg-emerald-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
            >
              Join by Email
            </a>
            <Link
              href="/7-day-wellness-reset"
              className="inline-flex rounded-md border border-emerald-200 bg-white px-4 py-2 text-sm font-semibold text-emerald-800 transition hover:bg-emerald-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
            >
              View the Reset
            </Link>
          </div>
        </section>

        <section className="mt-8 grid gap-4 sm:grid-cols-2">
          <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-5">
            <h2 className="text-lg font-semibold text-zinc-900">
              What Members Will Get
            </h2>
            <ul className="mt-2 list-disc space-y-2 pl-5 text-sm leading-6 text-zinc-600">
              <li>Weekly wellness guide updates</li>
              <li>7-Day Wellness Reset updates</li>
              <li>Printable checklists and trackers</li>
              <li>Sleep, stress, nutrition, and fitness routines</li>
              <li>Early access to future member tools</li>
            </ul>
          </div>
          <div className="rounded-lg border border-zinc-200 bg-zinc-50 p-5">
            <h2 className="text-lg font-semibold text-zinc-900">
              Start With These Guides
            </h2>
            <ul className="mt-2 space-y-2 text-sm leading-6">
              <li>
                <Link
                  href="/stress-management-guide"
                  className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
                >
                  Stress Management Guide
                </Link>
              </li>
              <li>
                <Link
                  href="/better-sleep-routine-guide"
                  className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
                >
                  Better Sleep Routine Guide
                </Link>
              </li>
              <li>
                <Link
                  href="/balanced-plate-guide"
                  className="font-medium text-green-700 underline underline-offset-4 hover:text-green-800"
                >
                  Balanced Plate Guide
                </Link>
              </li>
            </ul>
          </div>
        </section>
      </article>
    </main>
  );
}
