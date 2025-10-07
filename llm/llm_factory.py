from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.language_models import BaseLLM
from langchain_openai import ChatOpenAI, OpenAI

def create_chat_model() -> BaseChatModel:
    # use gpt-4o for now, but could sub out
    # this constructor reads `OPENAI_API_KEY` from env
    return ChatOpenAI(model="gpt-4o", temperature=0.7)

def create_llm() -> BaseLLM:
    return OpenAI(model="gpt-4o", temperature=0.7)