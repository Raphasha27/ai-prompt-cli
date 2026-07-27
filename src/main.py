import argparse
import json
import os
from pathlib import Path

def load_env():
    env_path = Path(".env")
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip())

def prompt_openai(prompt: str, model: str = "gpt-4o-mini") -> str:
    try:
        from openai import OpenAI
    except ImportError:
        return "Error: openai package not installed. Run: pip install openai"

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    if not client.api_key:
        return "Error: OPENAI_API_KEY not set in environment or .env file"

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def prompt_anthropic(prompt: str, model: str = "claude-3-haiku-20240307") -> str:
    try:
        from anthropic import Anthropic
    except ImportError:
        return "Error: anthropic package not installed. Run: pip install anthropic"

    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    if not client.api_key:
        return "Error: ANTHROPIC_API_KEY not set in environment or .env file"

    try:
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        return f"Error: {e}"

def main():
    load_env()
    parser = argparse.ArgumentParser(description="AI Prompt CLI - Send prompts to LLM providers")
    parser.add_argument("--prompt", "-p", required=True, help="The prompt to send")
    parser.add_argument("--provider", "-P", default="openai", choices=["openai", "anthropic"], help="AI provider")
    parser.add_argument("--model", "-m", help="Model name (defaults to provider default)")
    parser.add_argument("--output", "-o", help="Output file path (optional)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.provider == "openai":
        model = args.model or "gpt-4o-mini"
        result = prompt_openai(args.prompt, model)
    elif args.provider == "anthropic":
        model = args.model or "claude-3-haiku-20240307"
        result = prompt_anthropic(args.prompt, model)

    if args.json:
        output = json.dumps({"provider": args.provider, "model": model, "response": result}, indent=2)
    else:
        output = result

    if args.output:
        Path(args.output).write_text(output)
        print(f"Output written to {args.output}")
    else:
        print(output)

if __name__ == "__main__":
    main()
