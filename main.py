import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = "8782165712:AAHCXlt36OLeJDUDcCEOKZ1KombhwU4IHlQ"

# ← Сюда вставь свой URL после деплоя на Railway
WEBAPP_URL = "https://tgbot2-production-da1e.up.railway.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            "📅 Открыть квиз",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]])
    await update.message.reply_text(
        "👋 Привет! Нажми кнопку чтобы начать проверку знания исторических дат.",
        reply_markup=keyboard
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
