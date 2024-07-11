FROM python:3.12

WORKDIR /code

COPY pyproject.toml /code/

RUN pip install --root-user-action=ignore --no-cache-dir poetry==1.8.3 \
    && poetry install --no-root --only main

COPY . /code

ENTRYPOINT ["poetry", "run", "python3.12", "run.py"]
