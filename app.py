import streamlit as st
import pyperclip
from dotenv import load_dotenv

from services.resume_service import process_resume
from services.job_service import process_job
from services.cover_letter_service import generate_cover_letter

from ai.prompts import prompt_classic, prompt_modern
from ai.llm import get_llm

load_dotenv()


def main():
    st.title("Cover Letter Generator")

    # Initialize session state
    if "cover_letter" not in st.session_state:
        st.session_state.cover_letter = None

    if "job_data" not in st.session_state:
        st.session_state.job_data = None

    if "resume_data" not in st.session_state:
        st.session_state.resume_data = None

    llm = get_llm()

    # -----------------------
    # 1. RESUME UPLOAD
    # -----------------------
    st.header("1. Upload Resume")

    resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    if resume_file is not None and st.session_state.resume_data is None:
        with st.spinner("Processing resume..."):
            st.session_state.resume_data = process_resume(resume_file)

    if st.session_state.resume_data:
        st.success("Resume processed successfully")

    # -----------------------
    # 2. JOB INPUT
    # -----------------------
    st.header("2. Job Listing")

    job_input_type = st.radio("Input type", ["URL", "Text"])

    job_input = None

    if job_input_type == "URL":
        job_input = st.text_input("Enter job URL")

    else:
        job_input = st.text_area("Paste job description")

    if st.button("Process Job"):
        if job_input:
            with st.spinner("Processing job..."):
                st.session_state.job_data = process_job(job_input)

    if st.session_state.job_data:
        st.success("Job processed successfully")

    # -----------------------
    # 3. STYLE SELECTION
    # -----------------------
    st.header("3. Cover Letter Style")

    style = st.radio("Select style", ["Classic", "Modern"])

    prompt_template = prompt_classic if style == "Classic" else prompt_modern

    # -----------------------
    # 4. GENERATE
    # -----------------------
    st.header("4. Generate Cover Letter")

    if st.button("Generate Cover Letter"):

        if not st.session_state.resume_data or not st.session_state.job_data:
            st.warning("Please upload resume and job first.")
        else:
            with st.spinner("Generating cover letter..."):

                cover_letter = generate_cover_letter(
                    resume_data=st.session_state.resume_data,
                    job_data=st.session_state.job_data,
                    prompt_template=prompt_template
                )

                st.session_state.cover_letter = cover_letter

    # -----------------------
    # OUTPUT
    # -----------------------
    if st.session_state.cover_letter:

        st.subheader("Generated Cover Letter")

        st.markdown(st.session_state.cover_letter)

        if st.button("Copy to Clipboard"):
            pyperclip.copy(st.session_state.cover_letter)
            st.success("Copied!")

        st.download_button(
            "Download Cover Letter",
            st.session_state.cover_letter,
            file_name="cover_letter.txt"
        )


if __name__ == "__main__":
    main()