#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from telegram.ext import *
from telegram import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import math


API_KEY = "5572224359:AAHmJzYaCot3h-y2afNnMPIUSOvGk4VsB9U"

userOrderList = []
OrderSent = []
my_balance = 0
totalCost = 0

orderDict = { "Unagi": 5,      "Chicken katsu": 4,     "Pork katsu": 4.50,
            "1M": 2.50,        "1V": 2,                "1M1V": 3,          "2M1V": 3.50,            "2M2V":4,              "2V1M": 3.80,      "Fish": 1.50,
            "Nasi lemak": 3,   "Nasi goreng": 3,       "Ayam penyet": 3,   "Potato wedges" : 1,    "Popcorn chicken": 1,
            "100-Plus": 1.50,  "Coke": 1.50,           "Milo": 1.30,       "Iced tea": 1.20,       "Kopi": 1,              "Teh": 0.90}

def start_command(update, context):
    update.message.reply_text("Welcome to SaveTheEarth SG box, where our primary aim is to reduce food wastage and help our lovely food court vendors cut their cost! \n")
    update.message.reply_text("Here are the commands which you can use: \n\n /ordernow: select the dish you want to order \n\n /myorders:  order(s) which you have already placed \n\n /balance: to check your coin balance \n\n /vouchers: to check for any available vouchers to purchase \n\n If you're unsure of the command at any point in time, simply press /start and we will display this message again!")
 

def user_responses(text):
    global totalCost
    menu_items = ["Unagi", "Chicken katsu", "Pork katsu",
                  "1M", "1V","1M1V","2V1M","2M1V","2M2V", 
                    "Nasi lemak", "Nasi goreng", "Ayam penyet", "Potato wedges", "Popcorn chicken",
                    "100-Plus", "Coke", "Milo", "Kopi", "Ice tea", "Teh"]

    if text in menu_items:
        userOrderList.append(text)
        totalCost += orderDict[text]
        return f"The value of {text} is ${orderDict[text]}"

    
def handle_message(update, context):
    text = update.message.text #receive from user
    response = user_responses(text) #processes it
    if response:
        update.message.reply_text(response) #sends it back to user
        update.message.reply_text(f"This is your current order: {userOrderList}")
        update.message.reply_text(f"Your total cost: ${totalCost}")
        update.message.reply_text("You can click the boxes again if you intend to order more dishes!")
    
def canteens(update, context):
    
    keyboard = [
        [
            KeyboardButton("/Canteen_1", callback_data="1"),
            KeyboardButton("/Canteen_2", callback_data="2"),
            KeyboardButton("/Canteen_3", callback_data="3")],
    ]
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose a canteen!", reply_markup=ReplyKeyboardMarkup(keyboard))

def canteen1(update, context):
    keyboard = [[KeyboardButton("/Japanese", callback_data="jap"),
                KeyboardButton("/Cai_Fan", callback_data="mixedrice")],
                [KeyboardButton("/Muslim_Delights", callback_data="muslim"),
                KeyboardButton("/Beverage", callback_data="drinks") ]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose a stall!", reply_markup=ReplyKeyboardMarkup(keyboard))


def canteen2(update, context):
    keyboard = [[KeyboardButton("/Japanese", callback_data="jap"),
                KeyboardButton("/Cai_Fan", callback_data="mixedrice")],
                [KeyboardButton("/Muslim_Delights", callback_data="muslim"),
                KeyboardButton("/Beverage", callback_data="drinks") ]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose a stall!", reply_markup=ReplyKeyboardMarkup(keyboard))

def canteen3(update, context):
    keyboard = [[KeyboardButton("/Japanese", callback_data="jap"),
                KeyboardButton("/Cai_Fan", callback_data="mixedrice")],
                [KeyboardButton("/Muslim_Delights", callback_data="muslim"),
                KeyboardButton("/Beverage", callback_data="drinks") ]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose a stall!", reply_markup=ReplyKeyboardMarkup(keyboard))

def jap(update, context):
    keyboard = [[KeyboardButton("Unagi", callback_data="unagi")], 
                [KeyboardButton("Chicken katsu", callback_data="chickenK")],
                [KeyboardButton("Pork katsu", callback_data="porkK")]]

    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose an item!", reply_markup=ReplyKeyboardMarkup(keyboard)) 
    
def caifan(update, context):
    keyboard = [[KeyboardButton("1M", callback_data="1M")], 
                [KeyboardButton("1V", callback_data="1V")],
                [KeyboardButton("1M1V", callback_data="1M1V")],
                [KeyboardButton("2V1M", callback_data="2V1M")], 
                [KeyboardButton("2M1V", callback_data="2M1V")],
                [KeyboardButton("2M2V", callback_data="2M2V")]]

    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose an item!", reply_markup=ReplyKeyboardMarkup(keyboard)) 
    

def muslim(update, context):
    keyboard = [[KeyboardButton("Nasi lemak", callback_data="nasi_lemak")], 
                [KeyboardButton("Nasi goreng", callback_data="nasi_goreng")],
                [KeyboardButton("Ayam penyet", callback_data="ayam_penyet")],
                [KeyboardButton("Potato wedges", callback_data="fries")],
                [KeyboardButton("Popcorn chicken", callback_data="popcorn_chicken")]]

    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose an item!", reply_markup=ReplyKeyboardMarkup(keyboard)) 


def beverage(update, context):
    keyboard = [[KeyboardButton("100-Plus", callback_data="100plus")], 
                [KeyboardButton("Coke", callback_data="coke")],
                [KeyboardButton("Milo", callback_data="milo")],
                [KeyboardButton("Kopi", callback_data="kopi")],
                [KeyboardButton("Iced tea", callback_data="tea")],
                [KeyboardButton("Teh", callback_data="teh")]]

    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose an item!", reply_markup=ReplyKeyboardMarkup(keyboard)) 

def sendOrder(update, context):
    if userOrderList == []:
        update.message.reply_text("You have not submitted any order!")
        return
    
    if userOrderList in OrderSent:
        index = OrderSent.index(userOrderList)
        OrderSent.pop()
        
    OrderSent.append(userOrderList)
    update.message.reply_text(f"Order(s) made: {OrderSent}")


def balance(update, context):
    global my_balance
    my_balance = math.floor(totalCost * 5)
    update.message.reply_text(f"Your current coin balance is {my_balance}.")
    
def vouchers(update, context):
    update.message.reply_text(f"Your current coin balance is {my_balance}! \nExchange Rate: 1 coin = $0.05 discount \nEnter the number of coins you wish to exchange!")
    
    
def checkcoins(update, context):
    global my_balance 
    global totalCost
    if update.message.text.isdigit():
        deduct = int(update.message.text)
        if deduct > my_balance:
            update.message.reply_text("Please enter a whole number not more than your coin balance!")
                
        else:
            my_balance -= deduct
            voucherAmount = deduct / 20

            update.message.reply_text(f"Your new coin balance is {my_balance}.")

        if userOrderList:
            totalCost -=  voucherAmount
            update.message.reply_text((f"Your new total cost is ${totalCost}"))

    
    
updater = Updater(API_KEY, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start_command))
dp.add_handler(CommandHandler("ordernow", canteens))
dp.add_handler(CommandHandler("Canteen_1", canteen1))
dp.add_handler(CommandHandler("Canteen_2", canteen2))
dp.add_handler(CommandHandler("Canteen_3", canteen3))
dp.add_handler(CommandHandler("Japanese", jap))
dp.add_handler(CommandHandler("Cai_Fan", caifan))
dp.add_handler(CommandHandler("Muslim_Delights", muslim))
dp.add_handler(CommandHandler("Beverage", beverage))
dp.add_handler(CommandHandler("myorders", sendOrder))
dp.add_handler(CommandHandler("balance", balance))
dp.add_handler(CommandHandler("vouchers", vouchers))
dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_handler(MessageHandler(Filters.text, checkcoins), group=1)

updater.start_polling() 
updater.idle()


# In[ ]:




