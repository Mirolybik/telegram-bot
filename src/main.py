import logging
import time

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

time = time.localtime() 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

#async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    await update.message.reply_text(update.message.text)

async def time(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(time)

def main():
    application = Application.builder().token("7871968201:AAGK0JWGwMM7iLvJyNQLILcR5qdR9DhbXQs").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("time", time))
#    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
