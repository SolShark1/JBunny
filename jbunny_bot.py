from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

7252679351:AAEsiNJJ4zfskJIABiRIlomE2QBaq-cMXj0

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Make JBunny kiss Boosey", callback_data='kiss')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the Meme Coin Love Story! Tap the button below to make JBunny and Boosey kiss.', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="💖 JBunny and Boosey just kissed! 💖\nThe Meme Coin Love Story is coming true! 🌟")

def main() -> None:
    updater = Updater(telegram_token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()