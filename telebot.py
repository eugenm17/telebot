import telebot;

from telebot import types


bot = telebot.TeleBot('1780544485:AAE3cF3hYEe16dJLLJJ-uql8ukb9J7h3IMo');

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

   if message.text == "We have 12 sticks":

       bot.send_message(message.from_user.id, "I took 3 sticks")

   elif message.text == "I took 2 sticks":

       bot.send_message(message.from_user.id, "Ok,i took 2 sticks")
   elif message.text == "I took 1 sticks":

       bot.send_message(message.from_user.id, "I took 1 sticks")

   else:

       bot.send_message(message.from_user.id, "Bye-bye")


bot.polling(none_stop=True, interval=0)