from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Ahoj! Som tvoj bot!\nNapíš /pomoc pre zoznam príkazov."
    )

async def pomoc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Dostupné príkazy:\n"
        "/start - Uvítacia správa\n"
        "/pomoc - Zoznam príkazov"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pomoc", pomoc))

print("Bot beží...")
app.run_polling()