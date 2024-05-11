from aiogram.types import ReplyKeyboardMarkup,KeyboardButton






menyu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ish joyi kerak"),
        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text="Ustoz kerak"),
        ],
        [
            KeyboardButton(text="Shogird kerak"),
        ],
        [
            KeyboardButton(text="Samarqanddagi ob havo"),
            KeyboardButton(text="Toshkentdagi ob havo"),
        ],
        [
            KeyboardButton(text="Qadhqadaryodagi ob havo"),
            KeyboardButton(text="Qarshidagi ob havo"),
        ],
        [
            KeyboardButton(text="Navoiydagi ob havo"),
            KeyboardButton(text="Buxorodagi ob havo"),
        ],
        [
            KeyboardButton(text="Xorazimdagi ob havo"),
            KeyboardButton(text="Farg'onagagi ob havo"),
        ],
    ],
    resize_keyboard=True
)




javob_state=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q"),
        ],

    ],
    resize_keyboard=True
)






