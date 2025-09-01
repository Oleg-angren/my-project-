import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен
BOT_TOKEN = "7788110191:AAHTtyz6uDcPq3eX0Xykqon4LJMTd7aPUjI"

# Бот и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("🚀 Бот работает на  pythonhere !")

# Эхо
@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты сказал: {message.text}")

# Запуск
async def main():
    logger.info("Бот запускается...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
   asyncio.run(main())

