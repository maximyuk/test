from create_bot import bot, dp


async def on_startup() -> None:
    print("Bot Online")


async def start_bot():
    await on_startup()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
