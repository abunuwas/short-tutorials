FROM python:3.10-slim

RUN mkdir -p /server

WORKDIR /server

RUN pip install -U pip && pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock README.md /server/

RUN poetry check

RUN poetry install

COPY server.py /server/

EXPOSE 8000

CMD ["uvicorn", "server:server", "--host", "0.0.0.0"]
