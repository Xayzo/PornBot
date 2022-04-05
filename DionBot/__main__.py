from telethon import events, TelegramClient, Button
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice
from DionBot.events import register
from DionBot.porn import telethn as tbot, ubot2

import os
import logging
import random


logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN", None)

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


@register(pattern="^/asupan ?(.*)")

async def _(event):

    teks = await event.reply("**Mencari Video Asupan...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@DionAsupanCache", filter=InputMessagesFilterVideo

            )

        ]

        royzu = random.choice(asupannya)

        dion = await ubot2.download_media(royzu)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Asupan by Dion Bot", 

            file=dion

            )

        await teks.delete()

    except Exception:

        await teks.edit("Error karena dosamu besar.")


@register(pattern="^/desah ?(.*)")

async def _(event):

    bgst = await event.reply("**Mencari Desahan...🔍**") 

    try:

        desahannya = [

            desah

            async for desah in ubot2.iter_messages(

            "@desahancewesangesange", filter=InputMessagesFilterVoice

            )

        ]

        ewe = random.choice(desahannya)

        prik = await ubot2.download_media(ewe)

        await tbot.send_file(

            event.chat.id, 

            caption="🤤🤤🤤", 

            file=prik

            )

        await bgst.delete()

    except Exception:

        await bgst.edit("Error karena dosamu besar.")


print("Succesfully Started Bot!")
bot.run_until_disconnected()
