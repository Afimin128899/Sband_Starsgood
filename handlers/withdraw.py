from aiogram import types
from db import q
from keyboards import main_kb
from config import ADMIN_ID

def register(dp):
    @dp.callback_query_handler(lambda c: c.data == "withdraw")
    async def withdraw(call):
        stars = q("SELECT stars FROM users WHERE user_id=%s",
                  (call.from_user.id,), True)[0][0]

        q("INSERT INTO withdrawals (user_id, amount) VALUES (%s,%s)",
          (call.from_user.id, stars))

        kb = types.InlineKeyboardMarkup()
        kb.add(
            types.InlineKeyboardButton("✅ Принять", callback_data=f"ok_{call.from_user.id}"),
            types.InlineKeyboardButton("❌ Отклонить", callback_data=f"no_{call.from_user.id}")
        )

        await call.bot.send_message(
            ADMIN_ID,
            f"💸 Вывод\nID: {call.from_user.id}\n⭐ {stars}",
            reply_markup=kb
        )

        await call.message.edit_text("⏳ Заявка отправлена админу", reply_markup=main_kb(call.from_user.id))
