import os
import random
import time
from asyncio import sleep

import pyrogram, dotenv
from pyrogram import Client
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import Message
import logging
_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

from ilymod import *

dotenv.load_dotenv()

app = pyrogram.Client(api_hash=os.environ["API_HASH"], api_id=os.environ["API_ID"], session_name="asd")


@app.on_message(pyrogram.filters.me)
def echo(client: Client, message: Message):
    if message.text:
        try:
            if message.text.lower() == "ily":
                logging.info("Love mode")
                ilyCMD(client, message)
            if message.text[0] == ".":
                logging.info("Typing mode")
                dangerCMD(client, message)
            if message.text[:3].lower() == "huy":
                logging.info("Huy mode")
                huiCMD(client, message)
        except MessageIdInvalid as e:
            logging.warning(e)


app.run()
