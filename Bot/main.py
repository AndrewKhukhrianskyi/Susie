import telebot
import config
import rot
import base_encoding

from random import randint
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

''' Hello! '''
@bot.message_handler(commands = ['start'])
def welcome(message):
    sticker = open('stickers/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    item1 = types.KeyboardButton('ROT?')
    item2 = types.KeyboardButton('Инструкция')
    item3 = types. KeyboardButton('Base-кодирование?')

    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, "Приветствую, {0.first_name}!\n Меня зовут <b>{1.first_name}</b>. Я бот, занимающийся шифрованием и дешифрованием простых текстов при помощи криптографии.".format(message.from_user, bot.get_me()),
                     parse_mode = 'html', reply_markup = markup)

''' Main work '''

@bot.message_handler(content_types = ['text'])
def text_enc_message(message):
    if message.chat.type == 'private':
        if message.text == 'ROT?':
            bot.send_message(message.chat.id, 'ROT (англ. rotate; «сдвинуть на n позиций», иногда используется написание через дефис — ROT-n)\
            представляет собой шифр подстановки простой заменой для алфавита английского языка (стандартной латиницы).')

        elif message.text == 'Инструкция':
            bot.send_message(message.chat.id, 'Работаю по такому принципу - введите что-нибудь и я сразу зашифрую и расшифрую сообщение. Закодирую аналогичным образом.')

        elif message.text == 'Base-кодирование?':
            bot.send_message(message.chat.id, 'Base64 — стандарт кодирования двоичных данных при помощи только 64 символов ASCII. \
            Алфавит кодирования содержит текстово-цифровые латинские символы A-Z, a-z и 0-9 (62 знака) и 2 дополнительных символа, зависящих от системы реализации')
        else:

            ''' ROT '''
            enc_message = rot.rot_enc(message.text, rot.rot_mover)
            bot.send_message(message.chat.id, 'Шифр:')
            bot.send_message(message.chat.id, enc_message)
            bot.send_message(message.chat.id, 'ROT:')
            bot.send_message(message.chat.id, rot.rot_mover)
            

            dec_message = rot.rot_dec(enc_message, rot.rot_mover)
            bot.send_message(message.chat.id, 'Текст:')
            bot.send_message(message.chat.id, dec_message)

            
            

bot.polling(none_stop = True)
    









