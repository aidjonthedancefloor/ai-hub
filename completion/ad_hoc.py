from typing import Generator, List
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from llm.llm_factory import create_llm, create_chat_model

def ad_hoc_complete(system_prompts: List[str], user_prompts: List[str]) -> Generator[str, None, None]:
    """Single-shot completion with system and user prompts."""

    # llm = create_llm() # apparently this isn't supported by BaseLLM
    chat = create_chat_model()

    messages = [
        *(map(SystemMessage, system_prompts)),
        *(map(HumanMessage, user_prompts))
    ]

    response = chat.stream(messages)
    for chunk in response:
        print(chunk, flush=True) # debug
        yield chunk.content
