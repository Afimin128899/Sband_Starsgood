from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MIN_WITHDRAW
from db import q

def main_kb(user_id):
    stars = q("SELECT stars FROM users WHERE user_id=%s", (user_id,), True)[0][0]
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📋 Задания", callback_data="tasks"))
    kb.add(InlineKeyboardButton("👤 Профиль", callback_data="profile"))
    kb.add(InlineKeyboardButton("👥 Рефералы", callback_data="refs"))
    if stars >= MIN_WITHDRAW:
        kb.add(InlineKeyboardButton("💸 Вывод", callback_data="withdraw"))
    return kb
