import Link from "next/link";
import { mainNavigation, siteConfig } from "@/config/site";

export default function Header() {
  return (
    <header className="sticky top-0 z-40 border-b border-zinc-200 bg-zinc-50/95 backdrop-blur">
      <div className="relative flex h-16 items-center justify-between gap-6">
        <Link
          href="/"
          className="text-lg font-semibold tracking-tight text-zinc-900 hover:text-zinc-700"
        >
          {siteConfig.brandName}
        </Link>

        <nav aria-label="Primary" className="hidden items-center gap-5 xl:flex">
          {mainNavigation.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="text-sm font-medium text-zinc-700 hover:text-zinc-900"
            >
              {item.label}
            </Link>
          ))}
        </nav>

        <details className="group xl:hidden">
          <summary
            aria-label="Open navigation menu"
            className="hamburger-summary flex h-10 w-10 cursor-pointer items-center justify-center rounded-md border border-zinc-200 bg-white text-zinc-900 transition hover:border-zinc-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
          >
            <span className="sr-only">Open navigation menu</span>
            <span aria-hidden="true" className="flex w-5 flex-col gap-1">
              <span className="h-0.5 rounded-full bg-zinc-900 transition group-open:translate-y-1.5 group-open:rotate-45" />
              <span className="h-0.5 rounded-full bg-zinc-900 transition group-open:opacity-0" />
              <span className="h-0.5 rounded-full bg-zinc-900 transition group-open:-translate-y-1.5 group-open:-rotate-45" />
            </span>
          </summary>
          <nav
            aria-label="Mobile primary"
            className="absolute right-0 top-14 w-64 rounded-lg border border-zinc-200 bg-white p-2 shadow-lg"
          >
            {mainNavigation.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block rounded-md px-3 py-2 text-sm font-medium text-zinc-700 hover:bg-zinc-50 hover:text-zinc-900 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
              >
                {item.label}
              </Link>
            ))}
          </nav>
        </details>
      </div>
    </header>
  );
}
