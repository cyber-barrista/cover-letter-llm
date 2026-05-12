from parsers.html_parser import extract_html_text


def extract_job_text(input_data: str) -> str:
    """
    Handles both URL and raw job text input.
    """

    # If it's a URL
    if input_data.startswith("http"):
        return extract_html_text(input_data)

    # Otherwise assume it's raw text
    return input_data