"""LLM Project - CLI Chatbot entry point."""

from src.chatbot import Chatbot
from src.config import Config


def main() -> None:
    config = Config()

    if not config.OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY is not set.")
        print("Copy .env.example to .env and add your API key.")
        return

    chatbot = Chatbot(config)
    print("LLM Chatbot (type 'quit' to exit, 'reset' to clear history)")
    print("-" * 50)

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() == "reset":
            chatbot.reset()
            print("Conversation history cleared.")
            continue

        response = chatbot.chat(user_input)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()
