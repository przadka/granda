import openai
import os
import json
from llm_client import LLMClient
from typing import Dict, Any

class GPT4TurboLLMClient(LLMClient):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)

    def ask(self, system_message: str, user_message: str) -> Dict[str, Any]:
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=1.0,
            top_p=1,
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
