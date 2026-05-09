from pydantic import ValidationError
from models.resume_schema import Resume
from models.job_schema import Job
import json

def parse_resume_output(llm_output: str):
    """
    Converts LLM output into validated Resume object.
    """

    try:
        data = json.loads(llm_output)
        return Resume(**data)

    except (json.JSONDecodeError, ValidationError):
        return None


def parse_job_output(llm_output: str):
    try:
        data = json.loads(llm_output)
        return Job(**data)

    except Exception:
        return None