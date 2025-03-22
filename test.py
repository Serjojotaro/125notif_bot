import asyncio
import csv
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = 
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Загружаем данные из CSV
users_by_direction = {}
with open("users.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        username, direction = row
        direction = direction.strip().lower()
        if direction not in users_by_direction:
            users_by_direction[direction] = []
        users_by_direction[direction].append(f"{username}")

@dp.message(Command("smm"))
@dp.message(Command("ph"))
@dp.message(Command("vd"))
@dp.message(Command("dsg"))
@dp.message(Command("it"))
async def tag_users(message: Message):
    direction = message.text[1:].lower()
    if direction in users_by_direction:
        tagged_users = " ".join(users_by_direction[direction])
        await message.reply(f"{direction.capitalize()} команда: {tagged_users}")
    else:
        await message.reply("Нет данных по этому направлению.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
