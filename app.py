import os
import random
import time
from asyncio import sleep

import pyrogram, dotenv
from pyrogram import Client
from pyrogram.types import Message

from ilymod import *

dotenv.load_dotenv()

app = pyrogram.Client(api_hash=os.environ["API_HASH"], api_id=os.environ["API_ID"], session_name="asd")


@app.on_message(pyrogram.filters.me)
def echo(client: Client, message: Message):
    if message.text:
        if message.text == "ily":
            ilyCMD(client, message)
        if message.text[0] == ".":
            dangerCMD(client, message)
        if message.text[:3] == "huy":
            huiCMD(client, message, message.text.split(" ")[1])


app.run()
