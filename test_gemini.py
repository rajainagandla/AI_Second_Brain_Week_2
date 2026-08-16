import os
import google.genai as genai

def main():
    # Load API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No GEMINI_API_KEY found in environment")

    # Initialize Gemini client
    client = genai.Client(api_key=api_key)

    # Create a chat session (new SDK style)
    chat = client.chats.create(model="gemini-1.5-flash")

    # Send a test message
    response = chat.send_message("Hello Gemini from VS Code!")
    print("Gemini says:", response.text)

if __name__ == "__main__":
    main()
