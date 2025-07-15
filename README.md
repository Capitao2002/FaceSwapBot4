# FaceFusion Telegram Bot (Produção)

Este bot troca rostos em vídeos enviados via Telegram usando FaceFusion.

## Como usar

1. Envie um vídeo para o bot.
2. Envie uma foto do rosto a ser aplicado.
3. O bot retornará um vídeo com o rosto trocado.

## Rodando com Docker

```bash
docker build -t facefusion-bot .
docker run -p 5000:5000 facefusion-bot
