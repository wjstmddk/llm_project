from unittest.mock import MagicMock, patch
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
    import os
    os.environ.pop("MODEL_NAME", None)
    os.environ.pop("MAX_TOKENS", None)
    os.environ.pop("TEMPERATURE", None)

    config = Config()
    assert config.MODEL_NAME == "gpt-4o-mini"
    assert config.MAX_TOKENS == 1000
    assert config.TEMPERATURE == 0.7
