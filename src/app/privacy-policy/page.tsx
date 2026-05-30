import { siteConfig } from "@/config/site";

export default function PrivacyPolicyPage() {
  return (
    <main className="flex flex-1 justify-center py-10 sm:py-12">
      <article className="w-full max-w-3xl rounded-xl border border-zinc-200 bg-white p-6 sm:p-8">
        <header className="border-b border-zinc-200 pb-5">
          <h1 className="text-3xl font-semibold tracking-tight text-zinc-900">Privacy Policy</h1>
          <p className="mt-2 text-sm text-zinc-600">Last updated: May 29, 2026</p>
        </header>

        <section className="mt-6 space-y-4 text-sm leading-7 text-zinc-700">
          <p>
            {siteConfig.name} respects your privacy. This policy explains what information we collect,
            how we use it, and how users in the USA and Canada can manage their choices.
          </p>
          <p>
            We may collect limited analytics, device information, and newsletter subscription data to
            improve content quality and site performance. We do not sell personal data.
          </p>
          <p>
            If advertising services are enabled, third-party vendors may use cookies to deliver relevant
            ads. Users can manage cookie preferences through browser settings and our consent controls.
          </p>
          <p>
            For data access, correction, or deletion requests, contact us at {siteConfig.contactEmail}.
          </p>
        </section>
      </article>
    </main>
  );
}
