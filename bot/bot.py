import config
import telebot
from time import sleep, time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton #Only for creating Inline Buttons, not necessary for creating Invite Links

Group_ID = -1234567890 #Group ID for which invite link is to be created
bot = telebot.TeleBot(config.token, parse_mode="HTML")

#/start command message
@bot.message_handler(commands=['start'])
def startmsg(msg):
    bot.reply_to(msg, "Hey there, I'm a bot made by pyTelegramBotAPI!")

#Get notified of incoming members in group
@bot.message_handler(content_types=['new_chat_members'])
def newmember(msg):
    #Create an invite link class that contains info about the created invite link using create_chat_invite_link() with parameters
    invite = bot.create_chat_invite_link(Group_ID, member_limit=1, expire_date=int(time())+45) #Here, the link will auto-expire in 45 seconds
    InviteLink = invite.invite_link #Get the actual invite link from 'invite' class
    
    mrkplink = InlineKeyboardMarkup() #Created Inline Keyboard Markup
    mrkplink.add(InlineKeyboardButton("Join our group 🚀", url=InviteLink)) #Added Invite Link to Inline Keyboard
    
    bot.send_message(msg.chat.id, f"Hey there {msg.from_user.first_name}, Click the link below to join our Official Group.", reply_markup=mrkplink)
    
    #This will send a message with the newly-created invite link as markup button.
    #The member limit will be 1 and expiring time will be 45 sec.

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()