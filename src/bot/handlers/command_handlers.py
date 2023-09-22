from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from bot.constants.messages import START_MESSAGE
from bot.constants.states import States
from bot.keyboards.command_keyboards import start_keyboard_markup


async def start(update: Update, context: CallbackContext):
    """Функция-обработчик команды start."""
    if update.message:
        await update.message.reply_text(
            START_MESSAGE, reply_markup=start_keyboard_markup
        )
    else:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(START_MESSAGE)
        await query.edit_message_reply_markup(
            reply_markup=start_keyboard_markup
        )

    return States.START


start_handler = CommandHandler("start", start)
