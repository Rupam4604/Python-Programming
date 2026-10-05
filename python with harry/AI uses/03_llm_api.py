
import os

try:
    import config
except ModuleNotFoundError:
    config = None

from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key and config:
    api_key = getattr(config, "key", "")

if not api_key:
    raise RuntimeError(
        "Missing OpenAI API key. Set OPENAI_API_KEY or add your key to config.py."
    )

client = OpenAI(api_key=api_key)

stream = client.responses.create(
  model="gpt-5",
  input=[],
  text={
    "format": {
      "type": "text"
    },
    "verbosity": "medium"
  },
  reasoning={
    "effort": "medium",
    "mode": "standard",
    "summary": "auto"
  },
  tools=[],
  stream=True,
  store=True,
  include=[
    "reasoning.encrypted_content",
    "web_search_call.action.sources"
  ]
)

for event in stream:
    if event.type in ("response.output_text.delta", "response.refusal.delta"):
        print(event.delta, end="", flush=True)
    elif event.type == "error":
        raise RuntimeError(event.message)
    elif event.type == "response.failed":
        raise RuntimeError(event.response.error)