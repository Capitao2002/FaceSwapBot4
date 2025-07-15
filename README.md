# FaceFusion Telegram Bot

Este projeto é um bot do Telegram que realiza a troca de rostos em vídeos usando FaceFusion.

## Como usar

1. Envie um vídeo para o bot.
2. Envie uma foto do rosto a ser inserido.
3. O bot responderá com o vídeo com o rosto trocado.

## Rodando com Docker

```bash
docker build -t facefusion-bot .
docker run -p 5000:5000 facefusion-bot
```

## Estrutura

- `app.py` – Flask + Telegram bot
- `swap_face.py` – Troca de rostos (simulação com OpenCV)
- `bot_config.py` – Token do Telegram
- `requirements.txt` – Dependências
- `Dockerfile` – Para build e deploy
- `uploads/` – Pasta temporária para arquivos enviados
