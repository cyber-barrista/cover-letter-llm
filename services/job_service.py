from parsers.job_parser import extract_job_text
from ai.llm import get_llm


def process_job(url_or_text):
    """
    Converts job input into structured job data
    """

    # Step 1: normalize input (URL or text handled inside parser)
    raw_text = extract_job_text(url_or_text)

    # Step 2: structure job with LLM
    llm = get_llm(temperature=0)

    prompt = f"""
Extract structured job data in JSON format:

Job Description:
{raw_text}

Return:
- title
- company
- responsibilities
- requirements
- skills
"""

    response = llm.invoke(prompt)

    return {
        "raw_text": raw_text,
        "structured": response.content
    }