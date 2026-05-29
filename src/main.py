import argparse
import json
import os
from typing import Optional


def call_openai(prompt: str, model: str = "gpt-4o-mini") -> Optional[str]:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except ImportError:
        return None
    except Exception as e:
        return f"Error: {e}"


def call_anthropic(prompt: str, model: str = "claude-3-haiku-20240307") -> Optional[str]:
    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except ImportError:
        return None
    except Exception as e:
        return f"Error: {e}"


def main():
    parser = argparse.ArgumentParser(description="AI Prompt CLI — Send prompts to multiple LLM providers")
    parser.add_argument("--prompt", "-p", required=True, help="The prompt to send")
    parser.add_argument("--provider", choices=["openai", "anthropic"], default="openai", help="LLM provider")
    parser.add_argument("--model", default=None, help="Model override (default: provider-specific)")
    parser.add_argument("--output", "-o", help="Save response to file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    model = args.model or ("gpt-4o-mini" if args.provider == "openai" else "claude-3-haiku-20240307")

    if args.provider == "openai":
        result = call_openai(args.prompt, model)
    else:
        result = call_anthropic(args.prompt, model)

    if result is None:
        print(f"Provider '{args.provider}' not available. Install required package.")
        return

    if args.json:
        print(json.dumps({"provider": args.provider, "model": model, "response": result}, indent=2))
    else:
        print(result)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
        print(f"\nResponse saved to {args.output}")


if __name__ == "__main__":
    main()
