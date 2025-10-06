from langchain_openai import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from typing import List
from util import assert_openapi_key_set

def do_complete(system_prompts: List[str], user_prompts: List[str]) -> str:
    assert_openapi_key_set()

    chat = ChatOpenAI(model="gpt-4o", temperature=0.7)

    print({'sys': system_prompts, 'usr': user_prompts}) # debug
    messages = [
        *(map(lambda p: SystemMessage(p), system_prompts)),
        *(map(lambda p: HumanMessage(p), user_prompts))
    ]

    print(messages) # debug

    response = chat(messages)
    print(response.content) # debug
    return response.content
