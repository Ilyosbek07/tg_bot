from telebot import types


def welcome():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(types.KeyboardButton('đ˛ Telefon nomerni yuborish', request_contact=True))
	return keyboard


def location():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(types.KeyboardButton('Manzilni yuborish yuborish', request_location=True))
	return keyboard


def menu_keyboard():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('đ Bo\'limlar va mahsulotlar')
	btn2 = types.KeyboardButton('đ Korzina')
	btn3 = types.KeyboardButton('đ¤ Mening ma\'lumotlarim')
	btn4 = types.KeyboardButton('đĻ Buyurtmalarim')
	btn5 = types.KeyboardButton('âšī¸ Biz haqimizda')
	keyboard.add(btn1)
	keyboard.add(btn2, btn3, btn4, btn5)
	return keyboard


def category(data):
	buttons = []
	keyboard = types.InlineKeyboardMarkup(row_width=2)
	for i in data:
		buttons.append(
			types.InlineKeyboardButton(f"{i['title']}", callback_data=f'product_{i["id"]}')
		)
	btn = types.InlineKeyboardButton('back', callback_data=f'back4')
	keyboard.add(*buttons)
	keyboard.add(btn, row_width=1)
	return keyboard


def get_back_keyboard():
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn = types.KeyboardButton('đ  Bosh menyu')
	keyboard.add(btn, row_width=1)
	return keyboard


def order(data):
	buttons = []
	keyboard = types.InlineKeyboardMarkup(row_width=4)
	x = 1
	for i in data:
		buttons.append(
			types.InlineKeyboardButton(x, callback_data=f'delproduct_{i["id"]}')
		)
		x += 1
	btn = types.InlineKeyboardButton('back', callback_data=f'back_456')
	keyboard.add(*buttons)
	keyboard.add(btn, row_width=1)
	return keyboard


def get_order(product):
	keyboard = types.InlineKeyboardMarkup(row_width=2)
	btn1 = types.InlineKeyboardButton('đ Buyurtma qilish', callback_data=f'toorder_{product["id"]}')
	btn2 = types.InlineKeyboardButton("đ Savatga qo'shish", callback_data=f'add_to_cart_{product["id"]}')
	keyboard.add(btn1, btn2, row_width=1)
	return keyboard


def saveorder(product):
	keyboard = types.InlineKeyboardMarkup(row_width=3)
	buttons = []
	for i in range(1, 10):
		buttons.append(
			types.InlineKeyboardButton(i, callback_data=f'count_{product}_{i}')
		)
	keyboard.add(*buttons)
	return keyboard


def back():
	keyboard = types.InlineKeyboardMarkup(row_width=3)
	keyboard.add(types.InlineKeyboardButton("Hammasi", callback_data=f'orderhistory'))
	return keyboard


def get_order_basket(product):
	keyboard = types.InlineKeyboardMarkup(row_width=2)
	btn1 = types.InlineKeyboardButton('đ Buyurtma qilish', callback_data=f'toorder_{product["id"]}')
	keyboard.add(btn1, row_width=1)
	return keyboard
