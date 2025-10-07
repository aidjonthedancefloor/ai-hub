from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from typing import List
from llm_factory import create_chat_model

def complete(system_prompts: List[str], user_prompts: List[str]) -> str:
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
