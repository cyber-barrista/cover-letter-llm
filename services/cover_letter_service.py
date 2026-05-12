from ai.llm import get_llm


def generate_cover_letter(resume_data, job_data, prompt_template):
    """
    Combines structured resume + job data → cover letter
    """

    llm = get_llm()

    prompt = prompt_template.format(
        resume=resume_data,
        job_listing=job_data
    )

    response = llm.invoke(prompt)

    return response.content