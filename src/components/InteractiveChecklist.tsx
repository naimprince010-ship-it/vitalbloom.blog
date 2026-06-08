"use client";

import { useEffect, useMemo, useState } from "react";

type ChecklistSection = {
  title: string;
  items: string[];
};

type InteractiveChecklistProps = {
  sections: ChecklistSection[];
  storageKey: string;
};

export default function InteractiveChecklist({
  sections,
  storageKey
}: InteractiveChecklistProps) {
  const allItems = useMemo(
    () =>
      sections.flatMap((section) =>
        section.items.map((item) => ({
          id: `${section.title}:${item}`,
          item,
          section: section.title
        }))
      ),
    [sections]
  );
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});

  useEffect(() => {
    const savedItems = window.localStorage.getItem(storageKey);

    if (!savedItems) {
      return;
    }

    try {
      setCheckedItems(JSON.parse(savedItems) as Record<string, boolean>);
    } catch {
      window.localStorage.removeItem(storageKey);
    }
  }, [storageKey]);

  useEffect(() => {
    window.localStorage.setItem(storageKey, JSON.stringify(checkedItems));
  }, [checkedItems, storageKey]);

  const completedCount = allItems.filter((item) => checkedItems[item.id]).length;

  const toggleItem = (id: string) => {
    setCheckedItems((currentItems) => ({
      ...currentItems,
      [id]: !currentItems[id]
    }));
  };

  const resetChecklist = () => {
    setCheckedItems({});
    window.localStorage.removeItem(storageKey);
  };

  return (
    <section className="mt-8 space-y-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <h2 className="text-2xl font-semibold text-zinc-900">
            Weekly Checklist
          </h2>
          <p className="mt-1 text-sm leading-6 text-zinc-600">
            {completedCount} of {allItems.length} items checked on this device.
          </p>
        </div>
        <button
          type="button"
          onClick={resetChecklist}
          className="self-start rounded-md border border-zinc-200 bg-white px-3 py-1.5 text-sm font-medium text-zinc-700 transition hover:border-zinc-300 hover:text-zinc-950 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-500"
        >
          Reset
        </button>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        {sections.map((section) => (
          <section
            key={section.title}
            className="rounded-lg border border-zinc-200 bg-zinc-50 p-5"
          >
            <h3 className="text-lg font-semibold text-zinc-900">
              {section.title}
            </h3>
            <ul className="mt-3 space-y-3 text-sm leading-6 text-zinc-700">
              {section.items.map((item) => {
                const id = `${section.title}:${item}`;
                const isChecked = Boolean(checkedItems[id]);

                return (
                  <li key={item}>
                    <label className="flex cursor-pointer gap-3 rounded-md p-1 transition hover:bg-white">
                      <input
                        type="checkbox"
                        checked={isChecked}
                        onChange={() => toggleItem(id)}
                        className="mt-1 h-4 w-4 shrink-0 rounded border-zinc-300 text-emerald-700 accent-emerald-700 focus:ring-emerald-500"
                      />
                      <span
                        className={
                          isChecked
                            ? "text-zinc-500 line-through decoration-zinc-400"
                            : "text-zinc-700"
                        }
                      >
                        {item}
                      </span>
                    </label>
                  </li>
                );
              })}
            </ul>
          </section>
        ))}
      </div>
    </section>
  );
}
