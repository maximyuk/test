
import asyncio
from aiogram import Bot, Dispatcher
from handlers import questions, different_types


# Запуск бота
async def main():
    bot = Bot(token="5606002386:AAGd4L0woGYsgh4q2nCZP6z-0Be99YSsUjs")
    dp = Dispatcher()

    dp.include_routers(questions.router, different_types.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
