import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

_ = load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="gemini chatbot")
_ = parser.add_argument("user_prompt", type=str, help="user prompt")
_ = parser.add_argument("--verbose", action="store_true", help="enable verbose output")

args = parser.parse_args()
user_prompt = args.user_prompt

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

if response.usage_metadata is None:
    raise RuntimeError("response has no metadata")
else:
    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:  {response.usage_metadata.candidates_token_count}")
    print(f"Response: {response.text}")
