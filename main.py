import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

import config
from datetime import datetime

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Я на месте")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(
        "Саша, привет! Твои любимые друзья подготовили сюрприз в честь твоего дня рождения, но он надежно спрятан. Выполни все задания и тогда ты его найдешь. Встречаемся в эту субботу <b>25 ноября в 17:00 по адресу "
        "Привокзальная площадь 3к4, Лен. область, Мурино.</b> Мы будем ждать тебя во дворе дома. "
        "Не забудь взять с собой хорошее настроение!", reply_markup=keyboard, parse_mode=ParseMode.HTML)


@dp.message(F.text.lower() == "я на месте")
async def iam_here(message: types.Message):
    birthday = datetime(2023, 11, 26, 17, 0, 0)
    if datetime.now() < birthday:
        await message.reply("Я же сказал, встречаемся 26 ноября в 17:00!!!")
    else:
        await message.reply("Твоя игра начинается прямо сейчас! Ты будешь получать задания, ответы которых нужно "
                            "прислать в чат, и если они окажутся верными, я пришлю тебе следующую локацию. "
                            "И первое задание звучит так: \n\n"
                            "<em>Родитель щучьего хвоста</em>\n\n"
                            "А угадать это слово тебе помогут кубики на площадке, собери из них правильный ответ",
                            reply_markup=types.ReplyKeyboardRemove(), parse_mode=ParseMode.HTML)


@dp.message(F.text.lower() == "быба")
async def byba(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Я у Быбы")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Ииии это правильный ответ! \n"
                         "Неожиданно, но следующая локация это <b>Быба</b>\n"
                         "Скорее беги к ней, там тебя ждет следующее задание.",
                         reply_markup=keyboard, parse_mode=ParseMode.HTML)


@dp.message(F.text.lower() == "я у быбы")
async def byba_place(message: types.Message):
    image = FSInputFile("podsolnuh.jpg")
    result = await message.answer_photo(
        image
    )
    await message.answer("Теперь тебе нужно разгадать ребус. Присылай правильный ответ и получишь следующую локацию.",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == "подсолнух")
async def podsolnuh(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Нашла!")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("А ты догадливая! Но все не так просто! Теперь тебе нужно найти подсолнухи в квартире.",
                         reply_markup=keyboard)


@dp.message(F.text.lower() == "нашла!")
async def podsolnuh_place(message: types.Message):
    await message.answer("Отлично! Теперь тебе нужно угадать откуда этот отрывок:\n\n"
                         "Одиноким можно быть где угодно, но у одиночества городской жизни, в окружении миллионов "
                         "людей, есть особый привкус. Казалось бы, подобное состояние противоположно жизни в городе, "
                         "громадному присутствию других человеков, - и все же, чтобы развеять чувство внутренней "
                         "отделенности, одной лишь физической близости недостаточно. Живя бок о бок с другими,"
                         " удается - очень запросто - ощущать себя оставленным и отделенным...",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == "одинокий город")
async def lonely_city(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Она у меня в руках")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Правильно! Найди эту книгу в квартире!", reply_markup=keyboard)


@dp.message(F.text.lower() == "она у меня в руках")
async def book_place(message: types.Message):
    await message.answer("Здорово! А вот теперь по-настоящему сложное задание!!\n"
                         "Реши пример и его ответ это номер страницы из этой книги с подсказкой "
                         "следующей локации. \n\n"
                         "<em>(242 + 406) / (97 - 25)</em>\n\n"
                         "Но только одно условие: калькулятором пользоваться нельзя!",
                         reply_markup=types.ReplyKeyboardRemove(), parse_mode=ParseMode.HTML)


@dp.message(F.text.lower() == "9")
async def math_place(message: types.Message):
    await message.answer("Отлично! Открывай 9 страницу и читай открывок в первом абзаце. Это и "
                         "есть подсказка к твоей следующей локации.")


@dp.message(F.text.lower() == "балкон")
async def balcony(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Нажми сюда, как докуришь...")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Это было сложно, но ты справилась! \n"
                         "Время перекура! Иди на балкон и там тебя ждет последнее задание.\n"
                         "Ах, да... там тоже кое-что спрятано!", reply_markup=keyboard)


@dp.message(F.text.lower() == "нажми сюда, как докуришь...")
async def balcony_place(message: types.Message):
    await message.answer("Ну что ж, ты почти нашла свой подарок! Осталось последнее задание...\n"
                         "Угадай локацию:\n\n"
                         "В доме он стоит, но не гуляет,\n"
                         "Пищу хранит, но не ест,\n"
                         "Холод создает, но не мерзнет.\n"
                         "Кто это?", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == "холодильник")
async def freeze(message: types.Message):
    await message.answer("Ураа! Поздравляем, ты прошла это испытание! Скорее беги к холодильнику, там тебя ждет "
                         "сладкий подарок!")


@dp.message()
async def error(message: types.Message):
    # TODO: fix image
    image = FSInputFile("sticker.png")
    result = await message.answer_photo(
        image
    )
    await message.answer("Упс... это неправильный ответ. Попробуй еще раз.")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
