import type { Metadata } from "next";
import Link from "next/link";
import { siteConfig } from "@/config/site";

const resetDays = [
  {
    day: "Day 1",
    title: "Set a Baseline",
    action: "Write down your current sleep, stress, meals, movement, and energy level.",
    check: "Circle one habit that would make the biggest difference this week."
  },
  {
    day: "Day 2",
    title: "Build a Sleep Anchor",
    action: "Choose one realistic bedtime cue, such as dim lights or a 10-minute wind-down.",
    check: "Keep the cue small enough that you can repeat it on a busy night."
  },
  {
    day: "Day 3",
    title: "Reset Stress Quickly",
    action: "Try 2 to 5 minutes of slow breathing with a longer exhale.",
    check: "Notice whether your shoulders, jaw, or breathing changed afterward."
  },
  {
    day: "Day 4",
    title: "Make One Balanced Plate",
    action: "Build one meal with protein, fiber-rich carbohydrate, colorful produce, and fluid.",
    check: "Do not aim for perfect. Aim for repeatable."
  },
  {
    day: "Day 5",
    title: "Move Gently",
    action: "Walk, stretch, or do light mobility for 10 minutes.",
    check: "Pick a movement you would be willing to do again tomorrow."
  },
  {
    day: "Day 6",
    title: "Clear Mental Clutter",
    action: "Journal four lines: facts, thoughts, feelings, and next action.",
    check: "Keep the next action specific and small."
  },
  {
    day: "Day 7",
    title: "Choose Your Keepers",
    action: "Review the week and choose two habits to repeat for the next 14 days.",
    check: "Save only what helped. Drop what felt forced."
  }
];

const joinSubject = "Send me the 7-Day Wellness Reset";
const joinBody = [
  "Hi VitalBloom Blog,",
  "",
  "Please add me to the member updates list and send the 7-Day Wellness Reset updates.",
  "",
  "My main wellness goal right now is:",
  "",
  "Thanks"
].join("\n");

const joinMailto = `mailto:${siteConfig.contactEmail}?subject=${encodeURIComponent(
  joinSubject
)}&body=${encodeURIComponent(joinBody)}`;

export const metadata: Metadata = {
  title: "7-Day Wellness Reset",
  description:
    "Use the VitalBloom Blog 7-Day Wellness Reset to start simple sleep, stress, nutrition, movement, and mindfulness habits in one week.",
  alternates: {
    canonical: `${siteConfig.url}/7-day-wellness-reset`
  },
  openGraph: {
    title: "7-Day Wellness Reset | VitalBloom Blog",
    description:
      "A simple 7-day wellness reset from VitalBloom Blog for realistic sleep, stress, nutrition, movement, and mindfulness habits.",
    url: `${siteConfig.url}/7-day-wellness-reset`
  },
  twitter: {
    title: "7-Day Wellness Reset | VitalBloom Blog",
    description:
      "A simple 7-day wellness reset from VitalBloom Blog for realistic sleep, stress, nutrition, movement, and mindfulness habits."
  }
};

export default function SevenDayWellnessResetPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-4xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            Free Member Resource
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            7-Day Wellness Reset
          </h1>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-zinc-600">
            A simple one-week starter plan for sleep, stress, nutrition,
            movement, and mental clarity. It is educational and habit-focused,
            not medical advice.
          </p>
        </header>

        <section className="mt-6 rounded-lg border border-emerald-100 bg-emerald-50/70 p-5">
          <h2 className="text-lg font-semibold text-zinc-900">
            How to Use This Reset
          </h2>
          <p className="mt-2 text-sm leading-6 text-zinc-700">
            Spend 10 to 15 minutes per day. Keep each action small enough to
            repeat, then use Day 7 to choose the habits that are worth keeping.
          </p>
          <a
            href={joinMailto}
            className="mt-4 inline-flex rounded-md bg-emerald-700 px-4 py-2 text-sm font-semibold text-white transition hover:bg-emerald-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
          >
            Join for Reset Updates
          </a>
          <Link
            href="/7-day-wellness-reset-checklist"
            className="ml-0 mt-3 inline-flex rounded-md border border-emerald-200 bg-white px-4 py-2 text-sm font-semibold text-emerald-800 transition hover:bg-emerald-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500 sm:ml-3"
          >
            View the Checklist
          </Link>
        </section>

        <section className="mt-8 space-y-4">
          <h2 className="text-2xl font-semibold text-zinc-900">
            The 7-Day Plan
          </h2>
          <div className="grid gap-4 sm:grid-cols-2">
            {resetDays.map((item) => (
              <section
                key={item.day}
                className="rounded-lg border border-zinc-200 bg-zinc-50 p-5"
              >
                <p className="text-sm font-semibold text-emerald-700">
                  {item.day}
                </p>
                <h3 className="mt-1 text-lg font-semibold text-zinc-900">
                  {item.title}
                </h3>
                <p className="mt-2 text-sm leading-6 text-zinc-700">
                  {item.action}
                </p>
                <p className="mt-3 border-t border-zinc-200 pt-3 text-sm leading-6 text-zinc-600">
                  <span className="font-medium text-zinc-900">Check:</span>{" "}
                  {item.check}
                </p>
              </section>
            ))}
          </div>
        </section>

        <section className="mt-8 grid gap-4 sm:grid-cols-3">
          <Link
            href="/better-sleep-routine-guide"
            className="rounded-lg border border-zinc-200 p-4 text-sm font-medium text-zinc-900 hover:border-zinc-300"
          >
            Sleep Routine Guide
          </Link>
          <Link
            href="/stress-management-guide"
            className="rounded-lg border border-zinc-200 p-4 text-sm font-medium text-zinc-900 hover:border-zinc-300"
          >
            Stress Management Guide
          </Link>
          <Link
            href="/balanced-plate-guide"
            className="rounded-lg border border-zinc-200 p-4 text-sm font-medium text-zinc-900 hover:border-zinc-300"
          >
            Balanced Plate Guide
          </Link>
        </section>

        <section className="mt-8 border-t border-zinc-200 pt-5 text-sm leading-7 text-zinc-600">
          <h2 className="text-lg font-semibold text-zinc-900">
            Safety Note
          </h2>
          <p className="mt-2">
            This reset is for general wellness education. If you have symptoms,
            a diagnosed condition, injury, disordered eating concerns, or urgent
            mental health needs, speak with a qualified professional or local
            emergency service.
          </p>
        </section>
      </article>
    </main>
  );
}
