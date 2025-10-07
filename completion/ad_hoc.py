from typing import List
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from llm.llm_factory import create_chat_model

def ad_hoc_complete(system_prompts: List[str], user_prompts: List[str]) -> str:
    """Single-shot completion with system and user prompts."""

    chat = create_chat_model()

    print({'sys': system_prompts, 'usr': user_prompts}) # debug
    messages = [
        *(map(SystemMessage, system_prompts)),
        *(map(HumanMessage, user_prompts))
    ]

    print(messages) # debug

    response = chat(messages)
    print(response.content) # debug
    return response.content
