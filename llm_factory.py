from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI

def create_chat_model() -> BaseChatModel:
    # use gpt-4o for now, but could sub out
    # this constructor reads `OPENAI_API_KEY` from env
    return ChatOpenAI(model="gpt-4o", temperature=0.7)