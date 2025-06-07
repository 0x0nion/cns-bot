import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from handlers import user_handlers


async def main():
    logging.basicConfig(level=logging.INFO)

    # Настройка бота
    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode="HTML",
                                           link_preview_is_disabled=True))

    await bot.delete_webhook(drop_pending_updates=True)

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        user_handlers.router,
    )

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
