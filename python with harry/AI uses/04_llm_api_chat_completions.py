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
response = client.chat.completions.create(
    model="gpt-4o",

    messages=[
        {
            "role": "user",
            "content": (
                "Complete this chat:\n"
                "Jack: Hey\n"
                "Jill: How are you?\n"
                "Jack: Now what?\n"
                "Jill:"
            )
        }
    ],

    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


# Print response
print(response.choices[0].message.content)