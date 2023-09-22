import pytest

from bot.constants.buttons import SUPPORT_BUTTON
from bot.constants.links import SUPPORT_FORM
from bot.constants.messages import GET_SUPPORT
from bot.keyboards.command_keyboards import support_keyboard_markup


@pytest.mark.asyncio
async def test_support_keyboard():
    """Проверяем, что support_keyboard, возвращает сообщение, ссылку и кнопку."""
    for inline_keyboard in support_keyboard_markup.inline_keyboard:
        assert inline_keyboard[0].text == SUPPORT_BUTTON
        assert inline_keyboard[0].callback_data == GET_SUPPORT
        assert inline_keyboard[0].url == SUPPORT_FORM
        assert len(inline_keyboard) == 1
