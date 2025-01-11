FROM python:3.10.3-slim-buster

# Stream output to console
ENV PYTHONUNBUFFERED=1

# Install Poetry
RUN pip install poetry==2.0.0

WORKDIR /app

# copy the pyproject.toml and poetry.lock files into the container
COPY pyproject.toml poetry.lock /app/

# install Python dependencies from the pyproject.toml file
RUN poetry install --no-root

# copy all the source code into the container
# COPY src/*.py /app/src/
COPY . /app/

CMD ["poetry", "run", "python", "src/main.py"]

