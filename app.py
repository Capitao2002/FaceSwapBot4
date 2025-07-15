from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os
from swap_face import swap_face_faceswap
from bot_config import TELEGRAM_TOKEN

app = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def start(update, context):
    update.message.reply_text("Envie um vídeo e uma foto para trocar o rosto!")

def handle_video(update, context):
    video_file = update.message.video.get_file()
    video_path = os.path.join(UPLOAD_DIR, f"{update.message.message_id}_video.mp4")
    video_file.download(video_path)
    context.user_data['video_path'] = video_path
    update.message.reply_text("Vídeo recebido! Agora envie a foto do rosto para a troca.")

def handle_photo(update, context):
    photo_file = update.message.photo[-1].get_file()
    photo_path = os.path.join(UPLOAD_DIR, f"{update.message.message_id}_face.jpg")
    photo_file.download(photo_path)
    context.user_data['face_path'] = photo_path
    update.message.reply_text("Foto recebida! Processando a troca de rosto...")

    video_path = context.user_data.get('video_path')
    if not video_path:
        update.message.reply_text("Por favor, envie primeiro o vídeo.")
        return

    output_path = os.path.join(UPLOAD_DIR, f"{update.message.message_id}_output.mp4")
    swap_face_faceswap(video_path, photo_path, output_path)

    with open(output_path, 'rb') as f:
        update.message.reply_video(f, caption="Aqui está seu vídeo com o rosto trocado!")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.video, handle_video))
dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/")
def index():
    return "Bot de troca de rosto FaceFusion está rodando!"

if __name__ == "__main__":
    app.run(port=5000)
