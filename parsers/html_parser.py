from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders import AsyncChromiumLoader


def extract_html_text(url: str) -> str:
    """
    Converts a webpage into clean readable text.
    """

    loader = AsyncChromiumLoader([url])
    docs = loader.load()

    transformer = Html2TextTransformer()
    cleaned_docs = transformer.transform_documents(docs)

    return cleaned_docs[0].page_content