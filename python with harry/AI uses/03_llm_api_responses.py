import os

from openai import OpenAI

try:
    from config import OPENAI_API_KEY
except ModuleNotFoundError:
    OPENAI_API_KEY = None


# Get API key
api_key = os.getenv("OPENAI_API_KEY") or OPENAI_API_KEY

if not api_key:
    raise RuntimeError(
        "Missing OpenAI API key. "
        "Set OPENAI_API_KEY or add your key to config.py."
    )


# Create OpenAI client
client = OpenAI(api_key=api_key)


# Send request
stream = client.responses.create(
    model="gpt-5",

    input=(
        "Complete this chat:\n"
        "Jack: Hey\n"
        "Jill: How are you?\n"
        "Jack: Now what?\n"
        "Jill:"
    ),

    text={
        "format": {
            "type": "text"
        },
        "verbosity": "medium"
    },

    reasoning={
        "effort": "medium",
        "summary": "auto"
    },

    tools=[],

    stream=True
)


# Print response as it arrives
for event in stream:

    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)

    elif event.type == "response.refusal.delta":
        print(event.delta, end="", flush=True)

    elif event.type == "error":
        raise RuntimeError(event.message)

    elif event.type == "response.failed":
        raise RuntimeError(event.response.error)

print()