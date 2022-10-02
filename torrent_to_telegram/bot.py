import logging


from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
import os
from main import torrent_downloader_as
import requests

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


# working
async def magnetlinks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    magnet = update.message.text

    # uniq = uuid.uuid4().hex
    # os.mkdir(f"downloads/{uniq}")
    #

    # for file in os.listdir(f"downloads/{uniq}"):
    #     await context.bot.send_document(chat_id=update.effective_chat.id,
    #                                     reply_to_message_id=update.message.id,
    #                                     document=open(f"downloads/{uniq}/{file}", 'rb'), caption="",
    #                                     read_timeout=100, write_timeout=100, connect_timeout=100)

    # Create buttons to slect language:

    if "magnet:?" in magnet:
        # edited_initial_msg = await context.bot.edit_message_text(chat_id=update.effective_chat.id,
        #                                                          text="Processing Torrent..", parse_mode='markdown',
        #                                                          message_id=update.message.message_id
        #                                                          )


        to_delete_id = await context.bot.send_message(chat_id=update.effective_chat.id,
                                                      text="Processing Torrent..", parse_mode='markdown',
                                                      )

        dic_of_dir_links = torrent_downloader_as(magnet)

        keyboard = []
        for k, v in dic_of_dir_links.items():
            button = InlineKeyboardButton(text=k, url=v)
            keyboard.append([button])

        kbd = InlineKeyboardMarkup(keyboard)
        await context.bot.deleteMessage(update.effective_chat.id, to_delete_id.message_id)
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Enjoy!", parse_mode='markdown',
                                       reply_to_message_id=update.message.id,
                                       reply_markup=kbd
                                       )

        await context.bot.send_message(chat_id='-1001631461762',
                                       text=f"{update}", parse_mode='markdown',
                                       reply_to_message_id=update.message.id,
                                       reply_markup=kbd
                                       )

        # time.sleep(1)
        # shutil.rmtree(f"downloads/{uniq}")


# working part
async def startcom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Send me a magnet url to start a torrent download!")


async def callback_30(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id='-1001631461762', text='A single message with 30s delay')


if __name__ == '__main__':
    token = ""
    application = ApplicationBuilder().token(token).build()

    # job_queue = application.job_queue
    #
    # job_queue.run_once(callback_30, 30)

    commands = CommandHandler('start', startcom)
    links = MessageHandler(filters.TEXT, magnetlinks)

    # on different commands - answer in Telegram
    application.add_handler(commands)
    application.add_handler(links)

    application.run_polling(drop_pending_updates=True)
