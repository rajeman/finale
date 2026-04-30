"use client";

import Link from "next/link";

import { MERIDIAN_COMPANY, MERIDIAN_SUPPORT_PRODUCT, meridianHomeTagline } from "../lib/branding";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-12">
        <nav className="mb-12 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-800 dark:text-gray-200">{MERIDIAN_COMPANY}</h1>
            <p className="text-sm font-medium text-blue-700 dark:text-blue-300">{MERIDIAN_SUPPORT_PRODUCT}</p>
          </div>
          <Link
            href="/chat"
            className="rounded-lg bg-blue-600 px-6 py-2 font-medium text-white transition-colors hover:bg-blue-700"
          >
            Start support chat
          </Link>
        </nav>

        <div className="py-24 text-center">
          <p className="mb-3 text-sm font-semibold uppercase tracking-wide text-indigo-600 dark:text-indigo-400">
            {MERIDIAN_COMPANY}
          </p>
          <h2 className="mb-6 bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-4xl font-bold text-transparent md:text-6xl">
            {MERIDIAN_SUPPORT_PRODUCT}
          </h2>
          <p className="mx-auto mb-12 max-w-2xl text-xl text-gray-600 dark:text-gray-400">{meridianHomeTagline}</p>
          <Link href="/chat">
            <span className="inline-block rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 px-8 py-4 text-lg font-bold text-white transition-transform hover:scale-105 hover:from-blue-700 hover:to-indigo-700">
              Chat with support
            </span>
          </Link>
        </div>
      </div>
    </main>
  );
}
