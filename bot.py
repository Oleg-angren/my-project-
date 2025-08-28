from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Замени на свой токен
API_TOKEN = '8082307822:AAFWJBO01AZhgLXyKC2s-bO9NK08PvNT7h0'

# Создаём бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я бот на aiogram 3!")

@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты сказал: {message.text}")

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

# Запускаем
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())