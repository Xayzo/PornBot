from telethon import events, TelegramClient, Button
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice
from porn import telethn as tbot
from porn import ubot2 as dbot

import os
import random
import logging


logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)

bot = TelegramClient(
        "dion",
        api_id=16813597,
        api_hash="6ce811cff9c14820a3352aa5176066b6"
        ).start(
                bot_token=TOKEN
                )
db = {}

@bot.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            "**Halo para manusia sangean 👋🏻\nKetik /help untuk mendapatkan bantuan.**",
            buttons=[
                [Button.url("Updates", "https://t.me/DionProjects")]
                ]
            )


@bot.on(events.NewMessage(pattern="^[!?/]help$"))
async def helper(event):
    await event.reply(
            "**List command:\n\n• /bokep - Untuk mendapatkan video 4no\n•/asupan - Mendapatkan video asupan (bukan bokep 4no yah)\n• /desah - Mendapatkan desahan random\n• /hentai - Mendapatkan foto 4no**",
            buttons=[
                [Button.url("Updates", "https://t.me/DionProjects")]
                ]
            )


print("Succesfully Started Bot!")
bot.run_until_disconnected()
