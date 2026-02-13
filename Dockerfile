FROM python:3.12-slim

WORKDIR /app

# Copy requirements file first for better layer caching
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy package initialization file
COPY __init__.py .

# Copy configuration and main application
COPY config.py .
COPY main.py .

# Copy application directories
COPY ./src ./src
COPY ./schema ./schema
COPY ./utlis ./utlis
COPY ./env ./env

# Create models directory if it doesn't exist, or copy if it does
RUN mkdir -p ./models
COPY ./models ./models

EXPOSE 8000

# Use exec form to ensure proper signal handling
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]