from pypdf import PdfReader


def extract_resume_text(file) -> str:
    """
    Extract raw text from uploaded PDF resume.
    """

    reader = PdfReader(file)

    text_parts = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_parts.append(page_text)

    return "\n".join(text_parts)