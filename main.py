import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CREATOR_CHAT_ID = int(os.getenv("CREATOR_CHAT_ID"))

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if message.voice:
        await context.bot.forward_message(chat_id=CREATOR_CHAT_ID, from_chat_id=message.chat_id, message_id=message.message_id)
    elif message.photo:
        await context.bot.forward_message(chat_id=CREATOR_CHAT_ID, from_chat_id=message.chat_id, message_id=message.message_id)
    elif message.document:
        await context.bot.forward_message(chat_id=CREATOR_CHAT_ID, from_chat_id=message.chat_id, message_id=message.message_id)
    elif message.text:
        await context.bot.send_message(
            chat_id=CREATOR_CHAT_ID,
            text=f"Сообщение от @{message.from_user.username or message.from_user.id}:

{message.text}"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))

app.run_polling()
