import asyncio
from aiogram import Bot, Dispatcher
from handlers import *

# Запуск бота
async def main():
    bot = Bot(token="5579393510:AAFTu9JVaAd9IyujIkX3wN7NfkCHhJYAxdk")
    dp = Dispatcher()

    dp.include_routers(menu.router, nation.router)





    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())