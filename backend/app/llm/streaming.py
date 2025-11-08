import json
from typing import AsyncGenerator


async def stream_handler(response: AsyncGenerator) -> AsyncGenerator[str, None]:
    async for chunk in response:
        if chunk.choices:
            choice = chunk.choices[0]
            # This is a hypothetical way to get reasoning content.
            # The actual implementation depends on the NVIDIA API response format.
            if hasattr(choice, "reasoning_content") and choice.reasoning_content:
                yield json.dumps({"type": "reasoning_token", "content": choice.reasoning_content})
            if choice.delta and choice.delta.content:
                yield json.dumps({"type": "content_token", "content": choice.delta.content})
