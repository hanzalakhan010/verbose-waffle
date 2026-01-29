FROM python:3.11-slim


# 2. Install uv (The Magic Step)
# We copy the 'uv' binary from the official image. 
# This is the recommended, safest, and fastest way to install uv in Docker.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


ENV PYTHONUNBUFFERED=1\
    UV_COMPILE_BYTECODE=1 \
    PYTHONDONTWRITEBYTECODE=1


WORKDIR /app


COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


COPY ./app ./app

RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
