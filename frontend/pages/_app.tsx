import type { AppProps } from "next/app";
import Head from "next/head";

import { meridianDocumentTitle, MERIDIAN_COMPANY, MERIDIAN_SUPPORT_PRODUCT } from "../lib/branding";
import "../styles/globals.css";

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>{meridianDocumentTitle}</title>
        <meta
          name="description"
          content={`${MERIDIAN_SUPPORT_PRODUCT} for ${MERIDIAN_COMPANY} — order and product support.`}
        />
      </Head>
      <Component {...pageProps} />
    </>
  );
}
