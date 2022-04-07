from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler, PollAnswerHandler, PollHandler
from credits import bot_token
from genre import comedy, cartoon, drama, horror, thriller, biography
import random, time, codecs


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
            wall.write(str(update.message.from_user.id) + ' ' + str(update.message.from_user['username']) + '\n')
            wall.close()

def start(update, context):
    keyboard = [['Жанры 📖', 'Новинки 📰', 'Отзывы 💬'], ['Подобрать фильм 🤔', 'Оставить отзыв ✍'], ['Поддержать автора ⭐']]
    
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

#Функция для подбора фильма, когда юзер нажимает на кнопку "Подобрать фильм"
def answer(update, context):
    keyboard = [['Жанры 📖', 'Новинки 📰', 'Отзывы 💬'], ['Подобрать фильм 🤔', 'Оставить отзыв ✍'], ['Поддержать автора ⭐'],]
    
    update.message.reply_text("*Пройдите опрос для подбора фильма*", parse_mode = 'Markdown', reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
    
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

def kodland(update, context):
    context.bot.send_message(update.effective_chat.id, "Ого! У Вас неплохо получается искать пасхалки от школы программирования Kodland 🥳")
def kodland_egg(update, context):
    context.bot.send_message(update.effective_chat.id, "Ура! Вы нашли одну из пасхалок от школы программирования Kodland 🥳")
def kodlandgift(update, context):
    context.bot.send_message(update.effective_chat.id, "Cool! Ещё одну пасхалку от школы программирования Kodland в копилочку 🥳")
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
    else:
        True
  

def genre(update, context):
    keyboard = [[InlineKeyboardButton('Ужасы 😨', callback_data='1'), InlineKeyboardButton('Триллер 🔪', callback_data='2')],
                [InlineKeyboardButton('Комедии 😀', callback_data='3'), InlineKeyboardButton('Мультфильмы 🧸', callback_data='4')],
                [InlineKeyboardButton('Гангстеры\n 🚬', callback_data='5'), InlineKeyboardButton('Драма 😭', callback_data='6')],
                [InlineKeyboardButton('kodland', callback_data='7')]]

    update.message.reply_text('Выберите интересующий вас жанр фильма', reply_markup = InlineKeyboardMarkup(keyboard))

def message(update, context):
    if update.message.text == "Жанры 📖":
        genre(update, context)
    if update.message.text == "Новинки 📰":
        new(update, context)
    if update.message.text == "Отзывы 💬":
        lists(update, context)
    if update.message.text == "Подобрать фильм 🤔":
        answer(update, context)
    if update.message.text == "Оставить отзыв ✍":
        context.bot.send_message(update.effective_chat.id, "Напишите ваш отзыв в сообщении боту по образцу: /add + Ваш комменатрий")
        context.bot.send_message(update.effective_chat.id, "Или заполните анкету-отзыв ниже⬇")
        context.bot.send_message(update.effective_chat.id, "https://forms.gle/qt5LDSL6ogm2iFBJA")
#         add(update, context)
    if update.message.text == "Поддержать автора ⭐":
#         context.bot.send_message(update.effective_chat.id, "Ссылка на донатный кошелёк \n t.me/CryptoBot?start=IVIfoMuwIsVO")
        donate(update, context)

def donate(update, context):
    donate_keyboard = [[InlineKeyboardButton('QR код TON кошелька', callback_data='10',), InlineKeyboardButton('Адрес TON кошелька', callback_data='20')],
                [InlineKeyboardButton('Донат через Crypto Bot', callback_data='30'), InlineKeyboardButton('Сбербанк', callback_data='40')]]

    update.message.reply_text('Выберите интересующий вас способ доната', reply_markup = InlineKeyboardMarkup(donate_keyboard))

def genre_from_file(genre):
    fileObj = codecs.open( genre, "r", "utf_8_sig" )
    text = fileObj.read() 
    fileObj.close()
    return text

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
    elif query.data == '7':
        context.bot.send_message(update.effective_chat.id, "Ничего себе! Да вы специалист по пасхалкам от школы программирования Kodland 🥳")
    elif query.data == '10':
        context.bot.send_photo(update.effective_chat.id, photo = open("QR_TON.jpg", 'rb'))
    elif query.data == '20':
        context.bot.send_message(update.effective_chat.id, "EQDLCrfveKsrvFvgPzJA0rX1nw49hBrsFO-g5LtdFiEvapxU")
    elif query.data == '30':
        context.bot.send_message(update.effective_chat.id, "t.me/CryptoBot?start=IVIfoMuwIsVO")
    elif query.data == '40':
        context.bot.send_message(update.effective_chat.id, "5228 6005 4890 6629")

def new(update, context):
    context.bot.send_message(update.effective_chat.id, "*Доктор Стрэндж: В мультивселенной безумия* - 04.05.2022\
                                                                                                                                            *Аббатство Даунтон 2* - 05.05.2022\
                                                                                                                                            *Базз Лайтер* - 21.07.2022\
                                                                                                                                            *Белль и Себастьян: Новое поколение* - 05.05.2022\
                                                                                                                                            *Бодибилдер* - 07.04.2022\
                                                                                                                                            *kodland* - /kodlandgift\
                                                                                                                                            *Бордерлендс* - 25.08.2022\
                                                                                                                                            *Лето 1941 года * - 28.04.2022\
                                                                                                                                            *Варяг* - 21.04.22\
                                                                                                                                            *Мир Юрского периода: Господство* - 10.06.2022\
                                                                                                                                            *Тор: Любовь и гром* - 07.07.2022\
                                                                                                                                            *Нет* - 21.07.2022", parse_mode = 'Markdown')
def wall_from_file(wall):
    f = open(wall, 'r', encoding='utf-8')
    data = f.read()
    f.close
    return data

def add(update, context):
    result = ''
    for arg in context.args:
        result += arg + ' '
    if result != '':
        wall = open('wall.txt', 'a', encoding='utf-8')
        wall.write(str(update.message.from_user['username']) + ": " + result + '\n')
        wall.close()
        context.bot.send_message(update.effective_chat.id, "Благодарим Вас за комментарий, мы ценим ваше мнение ❤")


def lists(update, context):
    context.bot.send_message(update.effective_chat.id, wall_from_file("wall.txt"))
    
def users(update, context):
    context.bot.send_message(update.effective_chat.id, wall_from_file("users.txt"))


start_handler = CommandHandler('start', start)
new_handler = CommandHandler('new', new)
genre_handler = CommandHandler('genre', genre)
kodland_handler = CommandHandler('kodland', kodland)
kodland_egg_handler = CommandHandler('kodland_egg', kodland_egg)
kodlandgift_handler = CommandHandler('kodlandgift', kodlandgift)
button_handler = CallbackQueryHandler(button)
add_handler = CommandHandler('add', add)
list_handler = CommandHandler('list', lists)
users_handler = CommandHandler('users', users)
message_handler = MessageHandler(Filters.text, message)



dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
dispatcher.add_handler(start_handler)
dispatcher.add_handler(genre_handler)
dispatcher.add_handler(kodland_handler)
dispatcher.add_handler(kodland_egg_handler)
dispatcher.add_handler(kodlandgift_handler) 
dispatcher.add_handler(button_handler)
dispatcher.add_handler(new_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(list_handler)
dispatcher.add_handler(users_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()
