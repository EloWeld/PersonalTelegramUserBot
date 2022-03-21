import os
import random
import time
from asyncio import sleep

import pyrogram, dotenv
from pyrogram import Client
from pyrogram.types import Message


def ilyCMD(client: Client, message: Message) -> None:
    for i in ["Опа, здарова", "Так", "Так-с", "Ща пукну", "...", "...ща-ща..."]:
        message.edit(f"<b>{i}</b>")
        time.sleep(0.4)
    arr = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "💖"]
    h = "🤍"
    first_block = ""
    for i in "".join(
            [
                h * 9, "\n", h * 2, arr[0] * 2, h, arr[0] * 2, h * 2, "\n",
                h, arr[0] * 7, h, "\n",
                h, arr[0] * 7, h, "\n",
                h, arr[0] * 7, h, "\n",
                h * 2, arr[0] * 5, h * 2, "\n",
                h * 3, arr[0] * 3, h * 3, "\n",
                h * 4, arr[0], h * 4,
            ]
    ).split("\n"):
        first_block += i + "\n"
        message.edit(first_block)
        time.sleep(0.1)
    for i in arr:
        message.edit(
            "".join(
                [
                    h * 9, "\n",
                    h * 2, i * 2, h, i * 2, h * 2, "\n",
                    h, i * 7, h, "\n",
                    h, i * 7, h, "\n",
                    h, i * 7, h, "\n",
                    h * 2, i * 5, h * 2, "\n",
                    h * 3, i * 3, h * 3, "\n",
                    h * 4, i, h * 4, "\n",
                    h * 9,
                ]
            )
        )
        time.sleep(0.2)
    for _ in range(8):
        rand = random.choices(arr, k=34)
        message.edit(
            "".join(
                [
                    h * 9,
                    "\n",
                    h * 2,
                    rand[0],
                    rand[1],
                    h,
                    rand[2],
                    rand[3],
                    h * 2,
                    "\n",
                    h,
                    rand[4],
                    rand[5],
                    rand[6],
                    rand[7],
                    rand[8],
                    rand[9],
                    rand[10],
                    h,
                    "\n",
                    h,
                    rand[11],
                    rand[12],
                    rand[13],
                    rand[14],
                    rand[15],
                    rand[16],
                    rand[17],
                    h,
                    "\n",
                    h,
                    rand[18],
                    rand[19],
                    rand[20],
                    rand[21],
                    rand[22],
                    rand[23],
                    rand[24],
                    h,
                    "\n",
                    h * 2,
                    rand[25],
                    rand[26],
                    rand[27],
                    rand[28],
                    rand[29],
                    h * 2,
                    "\n",
                    h * 3,
                    rand[30],
                    rand[31],
                    rand[32],
                    h * 3,
                    "\n",
                    h * 4,
                    rand[33],
                    h * 4,
                    "\n",
                    h * 9,
                ]
            )
        )
        time.sleep(0.2)
    fourth = "".join(
        [
            h * 9,
            "\n",
            h * 2,
            arr[0] * 2,
            h,
            arr[0] * 2,
            h * 2,
            "\n",
            h,
            arr[0] * 7,
            h,
            "\n",
            h,
            arr[0] * 7,
            h,
            "\n",
            h,
            arr[0] * 7,
            h,
            "\n",
            h * 2,
            arr[0] * 5,
            h * 2,
            "\n",
            h * 3,
            arr[0] * 3,
            h * 3,
            "\n",
            h * 4,
            arr[0],
            h * 4,
            "\n",
            h * 9,
        ]
    )
    message.edit(fourth)
    while "🤍" in fourth:
        fourth = fourth.replace("🤍🤍🤍", "❤️❤️❤️", 1)
        fourth = fourth.replace("🤍🤍", "❤️❤️", 1)
        fourth = fourth.replace("🤍", "❤️", 1)
        message.edit(fourth)
        time.sleep(0.07)
    for i in range(8):
        message.edit((arr[0] * (8 - i) + "\n") * (8 - i))
        time.sleep(0.3)
    for i in ["Я", "<i>Я блять сука</i>", "Да ёбаный насрал, А-а-а!", "<i>Лю ❤️ Тя!</i>"]:
        message.edit(f"<b>{i}</b>")
        time.sleep(0.3)


def dangerCMD(client: Client, message: Message) -> None:
    orig_text = message.text.split('.',maxsplit=1)[1]
    for i in range(len(orig_text)):
        s = " ░" if i % 2 else " ▓"
        message.edit(orig_text[:i + 1] + s)
        time.sleep(0.05)
    message.edit(f"<b>{orig_text}</b>")
    time.sleep(0.2)
    message.edit(f"<i>{orig_text}</i>")
    time.sleep(0.2)
    message.edit(f"<code>{orig_text}</code>")
    time.sleep(0.2)
    message.edit(f"<b>{orig_text}</b>")

def huiCMD(client: Client, message: Message, emoji="🍆") -> None:
    message.edit("🍆🍆\n"
            "🍆🍆🍆\n"
            "  🍆🍆🍆\n"
            "    🍆🍆🍆\n"
            "     🍆🍆🍆\n"
            "       🍆🍆🍆\n"
            "        🍆🍆🍆\n"
            "         🍆🍆🍆\n"
            "          🍆🍆🍆\n"
            "          🍆🍆🍆\n"
            "      🍆🍆🍆🍆\n"
            " 🍆🍆🍆🍆🍆🍆\n"
            " 🍆🍆🍆  🍆🍆🍆\n"
            "    🍆🍆        🍆🍆".replace("🍆", emoji))