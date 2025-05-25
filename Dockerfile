FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files to working directory
COPY . .

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.6.14 /uv /uvx /bin/

# Install dependencies
RUN uv sync --frozen --no-cache

# Run application
CMD ["/app/.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
