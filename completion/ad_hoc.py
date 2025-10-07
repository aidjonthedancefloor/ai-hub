from typing import Generator, List
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from llm.llm_factory import create_llm, create_chat_model

def ad_hoc_complete(system_prompts: List[str], user_prompts: List[str]) -> str:
    """Single-shot completion with system and user prompts."""

    llm = create_llm()

    print({'sys': system_prompts, 'usr': user_prompts}) # debug
    messages = [
        *(map(SystemMessage, system_prompts)),
        *(map(HumanMessage, user_prompts))
    ]

    print(messages) # debug

    response = llm(messages)
    print(response.content) # debug
    return response.content

def streamed_ad_hoc_complete(system_prompts: List[str], user_prompts: List[str]) -> Generator[str, None, None]:
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
