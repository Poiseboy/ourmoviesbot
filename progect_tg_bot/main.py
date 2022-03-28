from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler, PollAnswerHandler, PollHandler
from credits import bot_token
from genre import comedy, cartoon, drama, horror, thriller, biography
import random, time

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

pict = ["https://st.depositphotos.com/1653909/1228/i/600/depositphotos_12283193-stock-photo-movie-clapper-and-film-reels.jpg", "https://img.lovepik.com//photo/40010/8993.jpg_860.jpg", "https://www.crushpixel.com/big-static12/preview4/film-movie-background-clapperboard-film-840191.jpg", "https://sharespro.ru/upload/iblock/a1f/home-movie.jpg", "https://cdnimg.rg.ru/img/content/201/78/65/92.jpg"]

def users_from_file(users):
    f = open(users, 'r')
    data = f.read()
    f.close
    return data

def add_users(update, context):
    result = ''
    for arg in context.args:
        result += arg + ' '

    wall = open('users.txt', 'a')
    with open('users.txt') as file:
        search_word = str(update.message.from_user.id)

        if search_word in open('users.txt').read():
            wall.close()
        else:
            wall.write(str(update.message.from_user.id) + '\n')
            wall.close()

def start(update, context):
    keyboard = [['Жанры 📖', 'Новости 📰', 'Отзывы 💬', 'Подобрать фильм 🤔']]
    
    update.message.reply_text("*Пройдите опрос для подбора фильма*", parse_mode = 'Markdown', reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    add_users(update, context)
    
    questions = "Что вы хотите увидеть в фильме"
    answer = ["Шутки, Веселье, Пошлые шутки, Отношения, Друзей, Приключения",
               "Доброту, Мультяшность, Хэппиэнд, Волшебство, Супергероев",
               "Драки, Криминал, Кровь, Страх, Слёзы, Острый сюжет, Оружие, Маньяки",
               "Слёзы, Любовь, Горе, Мотивацию, Поцелуи, Отношения, Грусть",
               "Биография, Вдохновение, Переживания, Деньги, Власть"] 
    
    # Отправляем опрос в чат
    message = context.bot.send_poll(
        update.effective_chat.id, questions, answer,
        is_anonymous=False, allows_multiple_answers=True,
    )
    # Сохраним информацию опроса в `bot_data` для последующего 
    # использования в функции `receive_poll_answer`
    payload = { # ключом словаря с данными будет `id` опроса
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    # сохранение промежуточных результатов в `bot_data`
    context.bot_data.update(payload)
    print(payload)

def answer(update, context):
    update.message.reply_text("*Пройдите опрос для подбора фильма*", parse_mode = 'Markdown', reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    add_users(update, context)
    
    questions = "Что вы хотите увидеть в фильме"
    answer = ["Шутки, Веселье, Пошлые шутки, Отношения, Друзей, Приключения",
               "Доброту, Мультяшность, Хэппиэнд, Волшебство, Супергероев",
               "Драки, Криминал, Кровь, Страх, Слёзы, Острый сюжет, Оружие, Маньяки",
               "Слёзы, Любовь, Горе, Мотивацию, Поцелуи, Отношения, Грусть",
               "Биография, Вдохновение, Переживания, Деньги, Власть"] 
    
    # Отправляем опрос в чат
    message = context.bot.send_poll(
        update.effective_chat.id, questions, answer,
        is_anonymous=False, allows_multiple_answers=True,
    )
    # Сохраним информацию опроса в `bot_data` для последующего 
    # использования в функции `receive_poll_answer`
    payload = { # ключом словаря с данными будет `id` опроса
        message.poll.id: {
            "questions": questions,
            "message_id": message.message_id,
            "chat_id": update.effective_chat.id,
            "answers": 0,
        }
    }
    # сохранение промежуточных результатов в `bot_data`
    context.bot_data.update(payload)
    print(payload)

def receive_poll_answer(update, context):
#    """Итоги опроса пользователей"""
    answer = update.poll_answer
    poll_id = answer.poll_id
    user = context.bot_data[poll_id]["chat_id"]
    results = update.poll_answer.option_ids
    print(poll_id, results)
    if 0 in results:
        context.bot.send_photo(user, random.choice(pict),caption = "Вам подойдёт фильм\n" + random.choice(comedy), parse_mode = 'Markdown')
        time.sleep(1)
    if 1 in results:
        context.bot.send_photo(user, random.choice(pict),caption = "Вам подойдёт фильм\n" + random.choice(cartoon), parse_mode = 'Markdown')
        time.sleep(1)
    if 2 in results:
        context.bot.send_photo(user, random.choice(pict),caption = "Вам подойдёт фильм\n" + random.choice(thriller), parse_mode = 'Markdown')
        time.sleep(1)
    if 3 in results:
        context.bot.send_photo(user, random.choice(pict),caption = "Вам подойдёт фильм\n" + random.choice(drama), parse_mode = 'Markdown')
        time.sleep(1)
    if 4 in results:
        context.bot.send_photo(user, random.choice(pict),caption = "*Вам подойдёт фильм*\n" + random.choice(biography), parse_mode = 'Markdown')
        time.sleep(1)
  

def genre(update, context):
    keyboard = [[InlineKeyboardButton('Ужасы 😨', callback_data='1'), InlineKeyboardButton('Триллер 🔪', callback_data='2')],
                [InlineKeyboardButton('Комедии 😀', callback_data='3'), InlineKeyboardButton('Мультфильмы 🧸', callback_data='4')],
                [InlineKeyboardButton('Гангстеры\n 🚬', callback_data='5'), InlineKeyboardButton('Драма 😭', callback_data='6')]]

    update.message.reply_text('Выберите интересующий вас жанр фильма', reply_markup = InlineKeyboardMarkup(keyboard))

def message(update, context):
    if update.message.text == "Жанры 📖":
        genre(update, context)
    if update.message.text == "Новости 📰":
        new(update, context)
    if update.message.text == "Отзывы 💬":
        lists(update, context)
    if update.message.text == "Подобрать фильм 🤔":
        answer(update, context)

def genre_from_file(genre):
    f = open(genre, 'r')
    data = f.read()
    f.close
    return data

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
            context.bot.send_message(update.effective_chat.id, genre_from_file('horror.txt'))
    elif query.data == '2':
            context.bot.send_message(update.effective_chat.id, genre_from_file('thriller.txt'))
    elif query.data == '3':
            context.bot.send_message(update.effective_chat.id, genre_from_file('comedy.txt'))
    elif query.data == '4':
            context.bot.send_message(update.effective_chat.id, genre_from_file('cartoon.txt'))
    elif query.data == '5':
            context.bot.send_message(update.effective_chat.id, genre_from_file('gangster_movie.txt'))
    elif query.data == '6':
            context.bot.send_message(update.effective_chat.id, genre_from_file('drama.txt'))
    else:
        context.bot.send_message(update.effective_chat.id, "Пока что нет такого жанра")

def new(update, context):
    context.bot.send_message(update.effective_chat.id, "*Охотники за привидениями: наследники* - 18 ноября 2021 года\
                                                                                                                                            *Небо* - 18 ноября 2021 года\
                                                                                                                                            *Энканто* - 25 ноября 2021 года\
                                                                                                                                            *Обитель Зла: Раккун Сити* - 2 декабря 2021 года\
                                                                                                                                            *Месть земли* - 2 декабря 2021 года\
                                                                                                                                            *День мёртвых* - 2 декабря 2021 года\
                                                                                                                                            *Бука. Моё любимое чудище* - 9 декабря 2021 года\
                                                                                                                                            *Мажор на мели* - 9 декабря 2021 года\
                                                                                                                                            *Календарь дьявола* - 9 декабря 2021года\
                                                                                                                                            *Зверопой 2* - 23 декабря 2021 года\
                                                                                                                                            *Десять дней с Сантой* - 30 декабря 2021 года", parse_mode = 'Markdown')
def wall_from_file(wall):
    f = open(wall, 'r')
    data = f.read()
    f.close
    return data

def add(update, context):
    result = ''
    for arg in context.args:
        result += arg + ' '

    wall = open('wall.txt', 'a')
    wall.write(str(update.message.from_user['username']) + ": " + result + '\n')
    wall.close()

def lists(update, context):
    context.bot.send_message(update.effective_chat.id, wall_from_file("wall.txt"))
    
def users(update, context):
    context.bot.send_message(update.effective_chat.id, wall_from_file("users.txt"))


start_handler = CommandHandler('start', start)
new_handler = CommandHandler('new', new)
genre_handler = CommandHandler('genre', genre)
button_handler = CallbackQueryHandler(button)
add_handler = CommandHandler('add', add)
list_handler = CommandHandler('list', lists)
users_handler = CommandHandler('users', users)
message_handler = MessageHandler(Filters.text, message)



dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
dispatcher.add_handler(start_handler)
dispatcher.add_handler(genre_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(new_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(list_handler)
dispatcher.add_handler(users_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()