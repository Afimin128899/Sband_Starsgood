from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers import start, tasks, profile, referrals, withdraw, admin

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register(dp)
tasks.register(dp)
profile.register(dp)
referrals.register(dp)
withdraw.register(dp)
admin.register(dp)

if __name__ == "__main__":
    executor.start_polling(dp)
