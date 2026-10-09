FROM python:3.14-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    tree \
    ffmpeg \
    curl \
    libopus-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

CMD ["python", "main.py"]