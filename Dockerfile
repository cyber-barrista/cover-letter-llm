FROM mcr.microsoft.com/playwright/python:v1.54.0-jammy

RUN pip install poetry==2.1.3

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["poetry", "run", "streamlit", "run", "app.py", "--server.headless", "true", "--server.address=0.0.0.0"]