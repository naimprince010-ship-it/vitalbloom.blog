import Link from "next/link";
import { footerNavigation, siteConfig } from "@/config/site";

export default function Footer() {
  return (
    <footer className="mt-16 border-t border-zinc-200 py-10">
      <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-5">
        <section aria-labelledby="footer-brand" className="space-y-3">
          <h2 id="footer-brand" className="text-base font-semibold text-zinc-900">
            {siteConfig.brandName}
          </h2>
          <p className="text-sm leading-6 text-zinc-600">{siteConfig.description}</p>
        </section>

        <nav aria-labelledby="footer-company" className="space-y-3">
          <h2 id="footer-company" className="text-sm font-semibold uppercase tracking-wide text-zinc-700">
            Company
          </h2>
          <ul className="space-y-2">
            {footerNavigation.company.map((item) => (
              <li key={item.href}>
                <Link href={item.href} className="text-sm text-zinc-600 hover:text-zinc-900">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>

        <nav aria-labelledby="footer-categories" className="space-y-3">
          <h2 id="footer-categories" className="text-sm font-semibold uppercase tracking-wide text-zinc-700">
            Categories
          </h2>
          <ul className="space-y-2">
            {footerNavigation.categories.map((item) => (
              <li key={item.href}>
                <Link href={item.href} className="text-sm text-zinc-600 hover:text-zinc-900">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>

        <nav aria-labelledby="footer-legal" className="space-y-3">
          <h2 id="footer-legal" className="text-sm font-semibold uppercase tracking-wide text-zinc-700">
            Legal
          </h2>
          <ul className="space-y-2">
            {footerNavigation.legal.map((item) => (
              <li key={item.href}>
                <Link href={item.href} className="text-sm text-zinc-600 hover:text-zinc-900">
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>

        <nav aria-labelledby="footer-profiles" className="space-y-3">
          <h2 id="footer-profiles" className="text-sm font-semibold uppercase tracking-wide text-zinc-700">
            Profiles
          </h2>
          <ul className="space-y-2">
            {siteConfig.socialProfiles.map((item) => (
              <li key={item.href}>
                <a
                  href={item.href}
                  className="text-sm text-zinc-600 hover:text-zinc-900"
                  rel="me noreferrer"
                  target="_blank"
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </div>

      <p className="mt-8 text-xs text-zinc-500">
        Copyright {new Date().getFullYear()} {siteConfig.brandName}. All rights reserved.
      </p>
    </footer>
  );
}
