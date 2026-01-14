from aiogram import types
from db import q
from config import ADMIN_ID

def register(dp):
    @dp.callback_query_handler(lambda c: c.data.startswith(("ok_", "no_")))
    async def admin(call):
        if call.from_user.id != ADMIN_ID:
            return

        action, user_id = call.data.split("_")
        user_id = int(user_id)

        if action == "ok":
            q("UPDATE users SET stars=0 WHERE user_id=%s", (user_id,))
            q("UPDATE withdrawals SET status='approved' WHERE user_id=%s AND status='pending'", (user_id,))
            await call.bot.send_message(user_id, "✅ Выплата одобрена")
            await call.message.edit_text("✅ Выплата подтверждена")
        else:
            q("UPDATE withdrawals SET status='rejected' WHERE user_id=%s AND status='pending'", (user_id,))
            await call.bot.send_message(user_id, "❌ Выплата отклонена")
            await call.message.edit_text("❌ Выплата отклонена")
