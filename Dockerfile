FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Instalar dependências do sistema (corrige o erro do OpenCV)
RUN apt-get update && apt-get install -y \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
