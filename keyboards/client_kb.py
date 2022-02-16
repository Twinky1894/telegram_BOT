from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup

kb_start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
buttons_start = ['📍Наши сервисные центры','🙋‍♂️Консультация инженера','❓Часто задаваемые вопросы','ℹ️Информация о платных ремонтах','⭐️Обратная связь']
kb_start.add(*buttons_start)

###########################################################################

kb_questions = InlineKeyboardMarkup()
b_question_1 = KeyboardButton('На какие случаи не распространяется гарантия?',callback_data="faq_warranty")
kb_questions.add(b_question_1)
b_question_2 = KeyboardButton('Потерян чек. Что делать?',callback_data="faq_lost")
kb_questions.add(b_question_2)
b_question_3 = KeyboardButton('Что делать если нет возможности привезти товар в сервисный центр?',callback_data="faq_delivery")
kb_questions.add(b_question_3)

###########################################################################

kb_location = InlineKeyboardMarkup()
b_location_1 = KeyboardButton('Как добраться до Вершины',callback_data="addres_1")
kb_location.add(b_location_1)
b_location_2 = KeyboardButton('Как добраться до Агоры',callback_data="addres_2")
kb_location.add(b_location_2)

###########################################################################

kb_url = InlineKeyboardMarkup()
burl = KeyboardButton('Прайс-лист', url="https://www.dns-shop.ru/service-center/paid-repair/")
kb_url.add(burl)