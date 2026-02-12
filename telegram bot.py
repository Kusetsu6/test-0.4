# Імпортуємо необхідні модулі для роботи з Telegram-ботом
import asyncio  # Це для роботи з асинхронними функціями (бот буде відповідати, не "зависаючи")
from aiogram import Bot, Dispatcher, types  # Головні інструменти для створення Telegram-бота
from aiogram.types import Message  # Тип даних для повідомлення від користувача

# Токен нашого бота, який ми отримали від @BotFather у Telegram
TYPE_API = "8589645001:AAElRXcd-wb-6omGsANKEDp5mTMmzEcANGo"

# Створюємо самого бота, передаючи токен
bot = Bot(token=TYPE_API)

# Створюємо диспетчер — він слідкує, які повідомлення приходять і що на них відповісти
dp = Dispatcher()

# Це обробник повідомлень — тобто бот буде відповідати на ВСІ повідомлення, які йому надсилають
@dp.message()
async def echo_handler(message: Message):
    # Бот надсилає відповідь: просто повторює те, що йому написали
    await message.answer(f"Ви написали: {message.text}")

# Головна функція для запуску бота
async def main():
    # Видаляємо старі вебхуки (щоб не було збоїв)
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускаємо бота — тепер він слухає повідомлення від користувачів
    await dp.start_polling(bot)

# Якщо ми запускаємо цей файл (а не імпортуємо як бібліотеку)
if __name__ == "__main__":
    # Запускаємо асинхронну головну функцію
    asyncio.run(main())