from langchain_core.prompts import PromptTemplate

prompt_classic = PromptTemplate.from_template(
"""
Write a concise professional cover letter.

Resume:
{resume}

Job:
{job_listing}

Focus on:
- skill overlap
- relevance
- concise business tone
- strong closing CTA
"""
)

prompt_modern = PromptTemplate.from_template(
"""
Write a modern "Tell us about yourself" message.

Start with:
"Hi, I'm <name>..."

Resume:
{resume}

Job:
{job_listing}

Be:
- concise
- confident
- aligned with role
"""
)
