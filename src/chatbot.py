from openai import OpenAI
from src.config import Config


class Chatbot:
    """A simple conversational chatbot backed by OpenAI's API."""

    def __init__(self, config: Config | None = None):
        self.config = config or Config()
        self.client = OpenAI(api_key=self.config.OPENAI_API_KEY)
        self.conversation_history: list[dict] = []
        self._reset_history()

    def _reset_history(self) -> None:
        self.conversation_history = [
            {"role": "system", "content": self.config.SYSTEM_PROMPT}
        ]

    def chat(self, user_message: str) -> str:
        """Send a message and return the assistant's reply."""
        self.conversation_history.append({"role": "user", "content": user_message})

        response = self.client.chat.completions.create(
            model=self.config.MODEL_NAME,
            messages=self.conversation_history,
            max_tokens=self.config.MAX_TOKENS,
            temperature=self.config.TEMPERATURE,
        )

        assistant_message = response.choices[0].message.content or ""
        self.conversation_history.append(
            {"role": "assistant", "content": assistant_message}
        )
        return assistant_message

    def reset(self) -> None:
        """Clear the conversation history."""
        self._reset_history()
