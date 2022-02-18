
from start_bot import dp, bot
from aiogram import types, Dispatcher,executor
from aiogram.dispatcher.filters import Text
from keyboards import kb_start, kb_questions, kb_location, kb_url, kb_consult

async def command_start(message : types.Message):
    #await message.delete()
    print('Пользователь ' + str(message.from_user.id) + ' подключился')
    await bot.send_message(message.from_user.id, '✋Этот бот предназначен для ответов на вопросы и для помощи в диагностике и выявлении неисправности устройств.\n\n Давайте попробуем! Выберите интересующий вас пункт', reply_markup=kb_start)

async def addresses(message : types.Message):
    #await message.delete()
    await bot.send_message(message.from_user.id, 'В городе Сургут находятся 2 пункта приема техники в ремонт : \n\n1)​Генерала Иванова 1, ТЦ Вершина, второй этаж \nВремя работы 10:00-22:00 без выходных \n\n2)​Профсоюзов 11, ТЦ Агора, второй этаж \nВремя работы 10:00-22:00 без выходных \n\nНо вы всегда можете сдать товар в любом магазине!',reply_markup=kb_location)

async def addres_1(call: types.CallbackQuery):
    await bot.send_location(call.from_user.id,61.2566, 73.4313)
    await call.answer()

async def addres_2(call: types.CallbackQuery):
    await bot.send_location(call.from_user.id,61.2694, 73.3821)
    await call.answer()

async def faq(message : types.Message):
    #await message.delete()
    await bot.send_message(message.from_user.id,'Выберите интересующий вас вопрос:\n',reply_markup=kb_questions)

async def faq_warranty(call: types.CallbackQuery):
    await call.message.answer('Гарантия не распростаняется если :\n\n⚙️Неисправность устройства вызвана нарушением правил его эксплуатации, транспортировки и хранения, изложенных в «Руководстве пользователя».\n⚙️На устройстве отсутствует, нарушен или не читается оригинальный серийный номер.На устройстве отсутствуют или нарушены заводские, или гарантийные пломбы и наклейки.\n⚙️Ремонт, техническое обслуживание или модернизация устройства производились лицами, не уполномоченными на то компанией-производителем.\n⚙️Дефекты устройства вызваны использованием устройства с программным обеспечением, не входящим в комплект поставки устройства, или не одобренным для совместного использования производителем устройства.')
    await call.answer()

async def faq_lost(call: types.CallbackQuery):    
    await call.message.answer('Если чек был утерян или испорчен, то:\n\n⚙️постарайтесь заранее вспомнить, когда и где вы приобретали товар (точная или приблизительная дата покупки, магазин), приобретали ли вы вместе с товаром какие-либо аксессуары, другие устройства;\n⚙️обратитесь в сервисный центр или магазин, имея при себе товар и всю информацию о его покупке.Специалист найдет вашу покупку в базе и предложит вариант решения в сложившейся ситуации.\n!')
    await call.answer()

async def faq_delivery(call: types.CallbackQuery):    
    await call.message.answer('Если это крупногабаритная техника*, тогда вы можете обратиться в сервисный центр по телефону и заказать услугу вывоза крупногабаритной техники или вызов мастера на дом (если услуга доступна в вашем регионе).\n\nЕсли ваш товар средних размеров и меньше, то вы также можете обратиться в сервисный центр по телефону и вас проконсультируют удаленно по вопросам неисправной работы товара.\n\n*КБТ- Требует для перевозки грузовой автомобиль и несколько человек для переноски.\nРазмеры в упаковке:\n1. Объемом от 0,25 до 1 куб. метра.\n2. От 180 до 350 см в сумме трёх измерений: ширина + глубина + высота.\n3. Вес более 5 кг.')
    await call.answer()

async def consult(message : types.Message):
    #await message.delete()
    await bot.send_message(message.from_user.id,'Выберите необходимый  пункт', reply_markup=kb_consult)

async def consult_spec(message : types.Message):
    await bot.send_message(message.from_user.id,'Выберите необходимый  пункт', reply_markup=kb_consult)
    
async def consult_engineer(message : types.Message):
    await bot.send_message(message.from_user.id,'Выберите необходимый  пункт', reply_markup=kb_consult)

async def paid_repair(message : types.Message):
    #await message.delete()
    await message.answer('Просто решаем сложные проблемы.\nРемонтируем цифровую и бытовую технику.\nПочему вы должны пойти именно к нам?\nБесплатная диагностика и консультация\nКвалифицированные специалисты\nГарантия 3 месяца на замененные компоненты и работу.\nШирокий ассортимент запчастей\n35 мировых бренда доверили нам право ремонтировать их устройства.Компании: Apple, Epson, Brother, Canon, Xiaomi, Indesit и другие')
    await bot.send_message(message.from_user.id,'С прайс-листом вы можете ознакомиться по ссылке', reply_markup=kb_url)

async def feed_back(message : types.Message):
    #await message.delete()
    await bot.send_message(message.from_user.id,'Этот раздел пока дорабатывается.')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])

    dp.register_message_handler(consult, text="🙋‍♂️Консультация")
    dp.register_message_handler(paid_repair, text="ℹ️Информация о платных ремонтах")
    dp.register_message_handler(feed_back, text="⭐️Обратная связь")

    dp.register_message_handler(addresses, text="🚩Наши сервисные центры")
    dp.register_callback_query_handler(addres_1, text="addres_1")
    dp.register_callback_query_handler(addres_2, text="addres_2")

    dp.register_message_handler(faq, text="❓Часто задаваемые вопросы")
    dp.register_callback_query_handler(faq_warranty, text="faq_warranty")
    dp.register_callback_query_handler(faq_lost, text="faq_lost")
    dp.register_callback_query_handler(faq_delivery, text="faq_delivery")
