# AI Prompt CLI

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-261230?style=for-the-badge)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge&logo=pre-commit)](https://pre-commit.com/)

A lightweight CLI tool for sending prompts to multiple Large Language Model (LLM) providers — OpenAI and Anthropic — directly from your terminal. Supports response output to files, JSON mode, and custom model selection.

---

## Features

- **Multi-Provider Support**: Switch between OpenAI (`gpt-4o-mini`) and Anthropic (`claude-3-haiku`) with a single flag
- **Custom Model Selection**: Override the default model for any provider
- **JSON Output**: Get structured JSON responses for programmatic use
- **File Output**: Save responses directly to a file
- **Minimal Dependencies**: Only requires the provider SDK you actually use

## Installation

```bash
# Clone the repository
git clone https://github.com/Raphasha27/ai-prompt-cli.git
cd ai-prompt-cli

# Install with pip
pip install -r requirements.txt
```

## Configuration

Copy the environment template and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and set at least one API key:

```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

## Usage

```bash
# Send a prompt using OpenAI (default)
python -m src.main --prompt "Explain quantum computing in one sentence"

# Use Anthropic Claude
python -m src.main --provider anthropic --prompt "What is the capital of France?"

# Specify a custom model
python -m src.main --provider openai --model gpt-4-turbo --prompt "Write a poem about Python"

# Save response to a file
python -m src.main --prompt "Hello" --output response.txt

# Get JSON output
python -m src.main --prompt "List 3 colors" --json
```

### CLI Options

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--prompt` | `-p` | The prompt to send (required) | — |
| `--provider` | — | LLM provider: `openai` or `anthropic` | `openai` |
| `--model` | — | Model override | Provider default |
| `--output` | `-o` | Save response to file | — |
| `--json` | — | Output as formatted JSON | `false` |

## Project Structure

```
ai-prompt-cli/
├── src/
│   ├── core/         # Core abstractions (extensible)
│   ├── providers/    # Provider implementations (extensible)
│   ├── templates/    # Prompt templates (extensible)
│   └── main.py       # CLI entry point and argument parsing
├── tests/            # Unit tests
├── .env.example      # Environment variable template
├── requirements.txt  # Python dependencies
└── pyproject.toml    # Project metadata and build config
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check src/
ruff format src/ --check
```

## Extending

Add new providers by creating modules in `src/providers/` and registering them in `src/main.py`. Each provider function should accept `(prompt: str, model: str) -> Optional[str]`.

## License

MIT License. See [LICENSE](LICENSE) for details.
---

## Product Ladder

```
GitHub (this repo)
    ↓
Portfolio → https://raphasha27.github.io/raphasha-dev-portfolio
    ↓
Case Study → (coming soon)
    ↓
Live Demo → (check the badges above)
    ↓
Contact → https://github.com/Raphasha27
```

Part of the [Kirov Dynamics Technology](https://github.com/Raphasha27) ecosystem.

**Built by Koketso Raphasha — Practical AI for Africa**