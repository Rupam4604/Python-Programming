from openai import OpenAI

# Connect to Ollama running on your computer
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# Send a request to the local Ollama model
response = client.chat.completions.create(
    model="deepseek-r1:8b",
    messages=[
        {
            "role": "user",
            "content": "Explain what a Python function is to a complete beginner."
        }
    ]
)

# Display the AI's response
print(response.choices[0].message.content)