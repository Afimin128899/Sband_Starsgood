from aiogram import types
from flyer_api import get_task, check_task
from db import q
from keyboards import main_kb
from config import TASK_REWARD

def register(dp):
    @dp.callback_query_handler(lambda c: c.data == "tasks")
    async def tasks(call):
        task = get_task(call.from_user.id)
        if task.get("status") != "ok":
            await call.message.edit_text("❌ Нет заданий", reply_markup=main_kb(call.from_user.id))
            return

        t = task["task"]
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("🔗 Перейти", url=t["url"]))
        kb.add(types.InlineKeyboardButton("✅ Проверить", callback_data=f"check_{t['id']}"))
        await call.message.edit_text("📋 Задание
💰 0.25 ⭐", reply_markup=kb)

    @dp.callback_query_handler(lambda c: c.data.startswith("check_"))
    async def check(call):
        task_id = call.data.split("_")[1]
        user_id = call.from_user.id

        if q("SELECT 1 FROM completed_tasks WHERE user_id=%s AND task_id=%s",
             (user_id, task_id), True):
            await call.answer("Уже засчитано", show_alert=True)
            return

        res = check_task(task_id, user_id)
        if res.get("status") != "completed":
            await call.answer("Не выполнено", show_alert=True)
            return

        q("INSERT INTO completed_tasks VALUES (%s,%s)", (user_id, task_id))
        q("UPDATE users SET stars=stars+%s WHERE user_id=%s", (TASK_REWARD, user_id))

        await call.message.edit_text("✅ Выполнено", reply_markup=main_kb(user_id))
