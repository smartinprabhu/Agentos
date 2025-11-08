from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    base_url=settings.NVIDIA_API_BASE_URL,
    api_key=settings.NVIDIA_API_KEY,
)


def get_chat_completion(prompt: str, model: str = "deepseek-ai/deepseek-v3.1-terminus"):
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
