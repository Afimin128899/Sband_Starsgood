from aiogram import types
from keyboards import main_kb

def register(dp):
    @dp.callback_query_handler(lambda c: c.data == "refs")
    async def refs(call):
        bot = await call.bot.get_me()
        link = f"https://t.me/{bot.username}?start={call.from_user.id}"

        await call.message.edit_text(
            f"👥 Рефералы\n\n🔗 {link}\n⭐ +2 за реферала",
            reply_markup=main_kb(call.from_user.id)
        )
