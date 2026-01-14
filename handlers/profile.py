from aiogram import types
from db import q
from keyboards import main_kb

def register(dp):
    @dp.callback_query_handler(lambda c: c.data == "profile")
    async def profile(call):
        stars, refs = q(
            "SELECT stars, refs FROM users WHERE user_id=%s",
            (call.from_user.id,), True
        )[0]

        await call.message.edit_text(
            f"👤 Профиль\n⭐ {stars}\n👥 Рефералов: {refs}",
            reply_markup=main_kb(call.from_user.id)
        )
