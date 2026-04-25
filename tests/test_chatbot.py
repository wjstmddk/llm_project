from unittest.mock import MagicMock, patch
import os
from src.chatbot import Chatbot
from src.config import Config


def make_mock_response(content: str):
    response = MagicMock()
    response.choices[0].message.content = content
    return response


def test_chatbot_chat():
    config = Config()
    config.OPENAI_API_KEY = "test-key"

    with patch("src.chatbot.OpenAI") as mock_openai_cls:
        mock_client = MagicMock()
        mock_openai_cls.return_value = mock_client
        mock_client.chat.completions.create.return_value = make_mock_response("Hello!")

        bot = Chatbot(config)
        reply = bot.chat("Hi")

        assert reply == "Hello!"
        assert len(bot.conversation_history) == 3  # system + user + assistant


def test_chatbot_reset():
    config = Config()
    config.OPENAI_API_KEY = "test-key"

    with patch("src.chatbot.OpenAI") as mock_openai_cls:
        mock_client = MagicMock()
        mock_openai_cls.return_value = mock_client
        mock_client.chat.completions.create.return_value = make_mock_response("Hi!")

        bot = Chatbot(config)
        bot.chat("Hello")
        bot.reset()

        assert len(bot.conversation_history) == 1  # only system message


def test_config_defaults():
    env_overrides = {k: v for k, v in os.environ.items()}
    env_overrides.pop("MODEL_NAME", None)
    env_overrides.pop("MAX_TOKENS", None)
    env_overrides.pop("TEMPERATURE", None)

    with patch.dict(os.environ, env_overrides, clear=True):
        config = Config()
        assert config.MODEL_NAME == "gpt-4o-mini"
        assert config.MAX_TOKENS == 1000
        assert config.TEMPERATURE == 0.7

