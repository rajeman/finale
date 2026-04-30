import { publicApiBase } from "./publicApiBase";

export type ReasoningStepPayload = {
  id: string;
  label: string;
  detail?: string | null;
};

export type ChatSuccess = {
  message: string;
  reasoning_steps: ReasoningStepPayload[];
};

/**
 * POST /chat — backend expects `{ id, message }` and returns `{ response }`.
 * `id` is a stable session UUID so the server keeps one agent (and memory) per conversation.
 */
export async function postChat(sessionId: string, message: string): Promise<ChatSuccess> {
  const res = await fetch(`${publicApiBase()}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ id: sessionId, message }),
  });
  if (!res.ok) {
    const errBody = await res.text();
    throw new Error(errBody || `Chat request failed (${res.status})`);
  }
  const data = (await res.json()) as { response?: unknown };
  const raw = data.response;
  let messageText = "";
  if (typeof raw === "string") {
    messageText = raw;
  } else if (raw != null && typeof raw === "object") {
    messageText = JSON.stringify(raw);
  } else if (raw != null) {
    messageText = String(raw);
  }
  return {
    message: messageText,
    reasoning_steps: [],
  };
}
