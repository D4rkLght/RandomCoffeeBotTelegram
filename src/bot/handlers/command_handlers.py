from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from bot.constants.messages import HELP_MESSAGE, START_MESSAGE
from bot.keyboards.command_keyboards import (
    help_keyboard,
    start_keyboard_markup,
)


async def start(update: Update, context: CallbackContext) -> None:
    """Функция-обработчик команды start."""
    await update.message.reply_text(
        text=START_MESSAGE, reply_markup=start_keyboard_markup
    )


async def help(update: Update, context: CallbackContext) -> None:
    """Функция-обработчик для команды /help."""
    await update.message.reply_html(
        text=(HELP_MESSAGE), reply_markup=help_keyboard
    )


start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
