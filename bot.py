from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''Hi iam 👑QUEEN👑 from SCUK NETWORK
Add me to your group for welcome your group members
Made with Love ❤️ 
by @Tamil_Telugu_Kanada_Hindi_Movies

  ''')
def help(updater,context):
 updater.message.reply_text("Add me to your group ")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hello {member.full_name} , Welcome to SCUK NETWORK Thank you for Joining  ')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
