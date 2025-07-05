FROM python:3.13-slim

RUN pip install poetry==2.1.3

WORKDIR /app
COPY . /app

RUN poetry install
RUN poetry run playwright install --with-deps chromium

EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["poetry", "run", "streamlit", "run", "app.py", "--server.headless", "true"]
