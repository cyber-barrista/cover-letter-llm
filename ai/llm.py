from langchain_openai import ChatOpenAI


def get_llm(temperature: float = 0.7):
    """
    Centralized LLM factory.
    """

    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=temperature
    )