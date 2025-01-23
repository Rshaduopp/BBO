from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

app = Flask(__name__)

# توكن البوت
TOKEN = "7930119641:AAE_sxzC_k-jvB8-Tm4PNHgu-NC8hbKO3LA"

# بوت تيليجرام
bot_app = ApplicationBuilder().token(TOKEN).build()

# وظيفة عند كتابة /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("مرحباً بك! أنا بوتك.")

# إضافة أوامر للبوت
bot_app.add_handler(CommandHandler("start", start))

# نقطة البداية لتشغيل التطبيق
@app.route("/")
def index():
    return "مرحباً! البوت يعمل الآن."

# تشغيل البوت في الخلفية
import threading
threading.Thread(target=lambda: bot_app.run_polling()).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
