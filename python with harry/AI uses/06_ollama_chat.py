from openai import OpenAI


# --------------------------------
# 1. Connect to Ollama
# --------------------------------

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


# --------------------------------
# 2. Create conversation history
# --------------------------------

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI tutor. "
            "Explain programming concepts clearly "
            "and assume the student is a complete beginner."
        )
    }
]


# --------------------------------
# 3. Start the chatbot
# --------------------------------

print("===================================")
print("      Local Ollama AI Chatbot")
print("===================================")
print("Model: DeepSeek R1 8B")
print("Type 'exit' to quit.")
print()


while True:

    # Get user's question
    user_input = input("You: ")

    # Exit the program
    if user_input.lower() == "exit":
        print("AI: Goodbye! 👋")
        break

    # Add user's message to history
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Send conversation to Ollama
    response = client.chat.completions.create(
        model="deepseek-r1:8b",
        messages=messages
    )

    # Get AI response
    ai_response = response.choices[0].message.content

    # Add AI response to history
    messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )

    # Display AI response
    print("\nAI:", ai_response)
    print()