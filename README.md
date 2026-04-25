# LLM Project

A simple command-line chatbot powered by OpenAI's API.

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and set your OPENAI_API_KEY
   ```

3. **Run the chatbot**
   ```bash
   python main.py
   ```

## Usage

```
LLM Chatbot (type 'quit' to exit, 'reset' to clear history)
--------------------------------------------------
You: Hello!
Assistant: Hi! How can I help you today?

You: reset
Conversation history cleared.

You: quit
Goodbye!
```

## Configuration

| Variable        | Default       | Description              |
|-----------------|---------------|--------------------------|
| `OPENAI_API_KEY`| *(required)*  | Your OpenAI API key      |
| `MODEL_NAME`    | `gpt-4o-mini` | OpenAI model to use      |
| `MAX_TOKENS`    | `1000`        | Max tokens per response  |
| `TEMPERATURE`   | `0.7`         | Response creativity (0-1)|

## Project Structure

```
llm_project/
├── main.py          # CLI entry point
├── src/
│   ├── chatbot.py   # Core chatbot logic
│   └── config.py    # Configuration management
├── tests/
│   └── test_chatbot.py
├── requirements.txt
└── .env.example
```

## Running Tests

```bash
pip install pytest
pytest tests/
```