import { siteConfig } from "@/config/site";

export default function TermsPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-xl border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <h1 className="text-3xl font-semibold tracking-tight text-zinc-900">Terms and Conditions</h1>
          <p className="mt-2 text-sm text-zinc-600">Last updated: May 29, 2026</p>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            By accessing {siteConfig.name}, you agree to use this website lawfully and respectfully.
            Content is provided for informational and educational purposes only.
          </p>
          <p>
            You may share links to our content with attribution, but you may not republish or distribute
            full articles without written permission.
          </p>
          <p>
            We reserve the right to modify, suspend, or discontinue parts of the website at any time.
            Continued use after updates indicates acceptance of revised terms.
          </p>
          <p>
            Questions about these terms can be sent to {siteConfig.contactEmail}.
          </p>
        </section>
      </article>
    </main>
  );
}
