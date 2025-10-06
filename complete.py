from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from typing import List
from util import assert_openapi_key_set
from llm_factory import create_chat_model

def do_complete(system_prompts: List[str], user_prompts: List[str]) -> str:
    assert_openapi_key_set()

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
