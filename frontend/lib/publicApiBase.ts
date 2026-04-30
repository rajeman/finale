/**
 * Base URL for browser calls to the FastAPI app.
 *
 * - Production / Docker (static `out/` served by FastAPI): leave unset → "" so `/chat` is same-origin.
 * - `next dev`: backend is on another port, so default to local uvicorn unless overridden.
 * - Override anytime with `NEXT_PUBLIC_API_URL` (no trailing slash).
 */
export function publicApiBase(): string {
  const fromEnv = process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "");
  if (fromEnv) return fromEnv;
  if (process.env.NODE_ENV === "development") {
    return "http://127.0.0.1:8000";
  }
  return "";
}
