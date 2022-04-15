import telebot
from telebot import types

token = '5259312820:AAGWtAYi-_zoKbBUQ2F16m43S60_30fuMgQ'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    game_btn = types.InlineKeyboardButton(text="Поиграть в игры", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу что-нибудь покушать", callback_data='2')
    cinema_btn = types.InlineKeyboardButton(text="Посмотреть кино", callback_data='3')
    music_btn = types.InlineKeyboardButton(text="Послушать музыку ", callback_data='4')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='5')
    keyboard.add(game_btn)
    keyboard.add(eat_btn)
    keyboard.add(cinema_btn)
    keyboard.add(music_btn)
    keyboard.add(sleep_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        "Приветствуем тебя! Выбери, чем хочешь заняться? 😃",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == "1":
            img = open('game.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Перейди по ссылке, чтобы начать играть https://vseigru.net/",
                reply_markup=keyboard)
            img.close()
        elif call.data == "2":
            img = open('eda.png', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Закажи еду на https://eda.yandex.by/minsk?shippingType=delivery",
                reply_markup=keyboard)
            img.close()
        elif call.data == "3":
            img = open('cinema.png', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Смотри фильмы на https://rezka.ag/",
                reply_markup=keyboard)
            img.close()
        elif call.data == "4":
            img = open('music.png', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Музыка здесь https://music.yandex.by/home",
                reply_markup=keyboard)
            img.close()
        elif call.data == "5":
            bye = 'Спокойной ночи)'
            bot.send_message(
                chat_id=call.message.chat.id,
                text=bye
            )


if __name__ == "__main__":
    bot.polling(none_stop=True)
