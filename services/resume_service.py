from parsers.resume_parser import extract_resume_text
from ai.llm import get_llm

def process_resume(file):
    """
    Converts uploaded PDF resume into structured representation
    """

    # Step 1: extract raw text
    raw_text = extract_resume_text(file)

    # Step 2: optional AI structuring (can improve later)
    llm = get_llm(temperature=0)

    prompt = f"""
Extract structured resume data in JSON format.

Resume:
{raw_text}

Return:
- name
- skills
- experience
- education
"""

    response = llm.invoke(prompt)

    return {
        "raw_text": raw_text,
        "structured": response.content
    }