from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.constants.buttons import (
    ALL_RIGHT_BUTTON,
    CHANGE_NAME_BUTTON,
    CONTINUE_BUTTON,
    FILL_AGAIN_BUTTON,
    PROFESSION_ANALIST_BUTTON,
    PROFESSION_BACKEND_DEVELOPER_BUTTON,
    PROFESSION_FRONTEND_DEVELOPER_BUTTON,
    PROFESSION_TESTER_BUTTON,
    RECRUITER_ROLE_BUTTON,
    START_BUTTON,
    STUDENT_ROLE_BUTTON,
)

restart_keyboard_markup = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=START_BUTTON, callback_data="restart")]]
)

role_choice_keyboard_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text=STUDENT_ROLE_BUTTON, callback_data="student"
            )
        ],
        [
            InlineKeyboardButton(
                text=RECRUITER_ROLE_BUTTON, callback_data="recruiter"
            )
        ],
    ]
)

guess_name_keyboard_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text=CONTINUE_BUTTON, callback_data="continue_name"
            ),
            InlineKeyboardButton(
                text=CHANGE_NAME_BUTTON, callback_data="change_name"
            ),
        ],
    ]
)

profession_choice_keyboard_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text=PROFESSION_ANALIST_BUTTON, callback_data="analyst"
            )
        ],
        [
            InlineKeyboardButton(
                text=PROFESSION_BACKEND_DEVELOPER_BUTTON,
                callback_data="backend-developer",
            )
        ],
        [
            InlineKeyboardButton(
                text=PROFESSION_FRONTEND_DEVELOPER_BUTTON,
                callback_data="frontend-developer",
            )
        ],
        [
            InlineKeyboardButton(
                text=PROFESSION_TESTER_BUTTON, callback_data="tester"
            )
        ],
    ]
)

profile_keyboard_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text=ALL_RIGHT_BUTTON, callback_data="all_right"
            ),
            InlineKeyboardButton(
                text=FILL_AGAIN_BUTTON, callback_data="fill_again"
            ),
        ],
    ]
)
