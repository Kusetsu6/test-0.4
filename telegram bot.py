# Файл: main.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import TOKEN # Імпорт токена

# Ініціалізація
dp = Dispatcher()
bot = Bot(8589645001:AAElRXcd-wb-6omGsANKEDp5mTMmzEcANGo)

# Обробник команди /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Обробляє команду /start."""
    await message.answer(f"Привіт, <b>{message.from_user.full_name}</b>!")

async def main() -> None:
    """Запускає процес Long Polling."""
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот зупинено вручну.")