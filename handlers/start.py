from aiogram import types
from db import q
from keyboards import main_kb

def register(dp):
    @dp.message_handler(commands=["start"])
    async def start(msg: types.Message):
        user_id = msg.from_user.id
        args = msg.get_args()

        q("INSERT INTO users (user_id) VALUES (%s) ON CONFLICT DO NOTHING", (user_id,))

        if args:
            ref = int(args)
            if ref != user_id:
                q("UPDATE users SET referrer=%s WHERE user_id=%s AND referrer IS NULL", (ref, user_id))
                q("UPDATE users SET stars=stars+2, refs=refs+1 WHERE user_id=%s", (ref,))

        await msg.answer("🤖 FlyerAPI Bot", reply_markup=main_kb(user_id))
