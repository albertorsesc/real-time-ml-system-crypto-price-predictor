FROM python:3.10.3-slim-buster

# Stream output to console
ENV PYTHONUNBUFFERED=1

# Install Poetry
RUN pip install poetry

WORKDIR /app

# Copy src code into Container
COPY . /app/

# Installs Python dependencies from `pyproject.toml` file.
RUN poetry install

CMD ["poetry", "run", "python", "src/main.py"]

