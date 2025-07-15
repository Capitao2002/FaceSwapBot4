import requests
from bot_config import TELEGRAM_TOKEN

WEBHOOK_URL = f"https://faceswapbot4.onrender.com/{TELEGRAM_TOKEN}"
response = requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook?url={WEBHOOK_URL}")
print("Webhook set:", response.json())
