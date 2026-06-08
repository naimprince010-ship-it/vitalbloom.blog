import type { Metadata } from "next";
import InteractiveChecklist from "@/components/InteractiveChecklist";
import JsonLd from "@/components/JsonLd";
import Link from "next/link";
import { siteConfig } from "@/config/site";
import { breadcrumbSchema } from "@/lib/schema";

const checklistSections = [
  {
    title: "Sleep",
    items: [
      "Choose one consistent wind-down cue.",
      "Dim bright lights or reduce screen intensity before bed.",
      "Write tomorrow's first task before getting into bed."
    ]
  },
  {
    title: "Stress",
    items: [
      "Take 2 to 5 minutes for slow breathing.",
      "Name one stressor you can act on and one you cannot control.",
      "Set one small boundary around time, messages, or availability."
    ]
  },
  {
    title: "Nutrition",
    items: [
      "Build one balanced plate with protein, fiber, produce, and fluid.",
      "Prepare one simple snack before you are already hungry.",
      "Keep one water cue tied to a daily routine."
    ]
  },
  {
    title: "Movement",
    items: [
      "Walk, stretch, or move gently for 10 minutes.",
      "Pick movement that feels repeatable, not impressive.",
      "Notice one place your body feels less tense afterward."
    ]
  },
  {
    title: "Mindful Reset",
    items: [
      "Journal facts, thoughts, feelings, and next action.",
      "Do one phone-free pause during the day.",
      "Choose two habits to keep for the next two weeks."
    ]
  }
];

const joinSubject = "Send me the 7-Day Wellness Reset Checklist";
const joinBody = [
  "Hi VitalBloom Blog,",
  "",
  "Please add me to the member updates list and send the 7-Day Wellness Reset Checklist updates.",
  "",
  "My main wellness focus is:",
  "",
  "Thanks"
].join("\n");

const joinMailto = `mailto:${siteConfig.contactEmail}?subject=${encodeURIComponent(
  joinSubject
)}&body=${encodeURIComponent(joinBody)}`;

const pageUrl = `${siteConfig.url}/7-day-wellness-reset-checklist`;

const checklistPageSchema = {
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": `${pageUrl}#webpage`,
  name: "7-Day Wellness Reset Checklist",
  description:
    "A practical one-week wellness checklist for sleep, stress, nutrition, movement, and mindfulness habits.",
  url: pageUrl,
  isPartOf: {
    "@id": `${siteConfig.url}/#website`
  },
  publisher: {
    "@id": `${siteConfig.url}/#organization`
  },
  inLanguage: "en"
};

const checklistHowToSchema = {
  "@context": "https://schema.org",
  "@type": "HowTo",
  "@id": `${pageUrl}#howto`,
  name: "How to Use the 7-Day Wellness Reset Checklist",
  description:
    "Use the checklist to track small sleep, stress, nutrition, movement, and mindful reset habits for one week.",
  totalTime: "P7D",
  supply: [
    {
      "@type": "HowToSupply",
      name: "7-Day Wellness Reset Checklist"
    }
  ],
  step: checklistSections.map((section, index) => ({
    "@type": "HowToStep",
    position: index + 1,
    name: section.title,
    text: section.items.join(" ")
  }))
};

const checklistBreadcrumbSchema = breadcrumbSchema([
  { name: "Home", url: "/" },
  { name: "7-Day Wellness Reset Checklist", url: pageUrl }
]);

export const metadata: Metadata = {
  title: "7-Day Wellness Reset Checklist",
  description:
    "Use the VitalBloom Blog 7-Day Wellness Reset Checklist to track simple sleep, stress, nutrition, movement, and mindfulness habits for one week.",
  alternates: {
    canonical: pageUrl
  },
  openGraph: {
    title: "7-Day Wellness Reset Checklist | VitalBloom Blog",
    description:
      "A practical one-week wellness checklist for sleep, stress, nutrition, movement, and mindful reset habits.",
    url: pageUrl
  },
  twitter: {
    title: "7-Day Wellness Reset Checklist | VitalBloom Blog",
    description:
      "A practical one-week wellness checklist for sleep, stress, nutrition, movement, and mindful reset habits."
  }
};

export default function SevenDayWellnessResetChecklistPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <JsonLd
        data={[
          checklistPageSchema,
          checklistHowToSchema,
          checklistBreadcrumbSchema
        ]}
      />
      <article className="w-full max-w-4xl rounded-lg border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <p className="text-sm font-medium uppercase tracking-[0.12em] text-zinc-500">
            Printable-Style Resource
          </p>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-900">
            7-Day Wellness Reset Checklist
          </h1>
          <p className="mt-3 max-w-2xl text-sm leading-6 text-zinc-600">
            A practical checklist for one week of small sleep, stress,
            nutrition, movement, and mindful reset habits. Use it as a simple
            tracker, not as medical advice.
          </p>
        </header>

        <section className="mt-6 rounded-lg border border-emerald-100 bg-emerald-50/70 p-5">
          <h2 className="text-lg font-semibold text-zinc-900">
            How to Use the Checklist
          </h2>
          <p className="mt-2 text-sm leading-6 text-zinc-700">
            Pick one action from each section during the week. Check off what
            you actually complete, then choose two habits to repeat after the
            reset.
          </p>
          <div className="mt-4 flex flex-wrap gap-3">
            <a
              href={joinMailto}
              className="inline-flex rounded-md bg-emerald-700 px-4 py-2 text-sm font-semibold text-white transition hover:bg-emerald-800 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
            >
              Join for Checklist Updates
            </a>
            <Link
              href="/7-day-wellness-reset"
              className="inline-flex rounded-md border border-emerald-200 bg-white px-4 py-2 text-sm font-semibold text-emerald-800 transition hover:bg-emerald-50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
            >
              View the 7-Day Plan
            </Link>
          </div>
        </section>

        <InteractiveChecklist
          sections={checklistSections}
          storageKey="vitalbloom-7-day-wellness-reset-checklist"
        />

        <section className="mt-8 rounded-lg border border-zinc-200 bg-white p-5">
          <h2 className="text-lg font-semibold text-zinc-900">
            End-of-Week Review
          </h2>
          <div className="mt-3 grid gap-3 text-sm leading-6 text-zinc-700 sm:grid-cols-3">
            <p className="rounded-md border border-zinc-200 p-3">
              One habit that helped:
            </p>
            <p className="rounded-md border border-zinc-200 p-3">
              One habit to drop:
            </p>
            <p className="rounded-md border border-zinc-200 p-3">
              Two habits to repeat:
            </p>
          </div>
        </section>

        <section className="mt-8 grid gap-4 sm:grid-cols-3">
          <Link
            href="/stress-management-guide"
            className="rounded-lg border border-zinc-200 p-4 text-sm font-medium text-zinc-900 hover:border-zinc-300"
          >
            Stress Management Guide
          </Link>
          <Link
            href="/better-sleep-routine-guide"
            className="rounded-lg border border-zinc-200 p-4 text-sm font-medium text-zinc-900 hover:border-zinc-300"
          >
            Better Sleep Routine Guide
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
            This checklist is for general wellness education. If you have
            symptoms, a diagnosed condition, injury, disordered eating concerns,
            or urgent mental health needs, speak with a qualified professional
            or local emergency service.
          </p>
        </section>
      </article>
    </main>
  );
}
