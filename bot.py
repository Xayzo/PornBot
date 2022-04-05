from telethon import events, TelegramClient, Button
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice
from telethon.sessions import MemorySession
from pyrogram import Client

import os
import random
import logging


API_ID = "16813597"
API_HASH = "6ce811cff9c14820a3352aa5176066b6"
STRING_SESSION = "1BVtsOJ0Bu0kJpCVwakCO7FNuOb2YWubclYZxpXW_NGvkERlDtkYsFjYltqu5zfc_bQohskBxXS6gVIamVt3tFA3kgkDSVyeo90Ke9kwqquTNX_L66h-4pBKN9nY7QF5R_Kjc3yispcRJc6QIcOZLCkJODJ1kDeuRl762gOHaQFbcqPWA1HwVENIS6cBcA_6QhTqiZb8gZ12YLBya8M2Wzv0fsm1V0vyr5lTJN1-vZjPHy6uwI7_Q6SwIekVI5lfA-kHL0YaLHWV0IjdP27GNs4KBt_IdJNqvyMg0FrdEx-_dLLHe58POljsvxz8Ks7ZuTLGAvQfuQ4XoDLdHGwM-KBx9oRwvKaw="

telethn = TelegramClient(MemorySession(), API_ID, API_HASH)

ubot2 = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
try:
    ubot2.start()
except BaseException:
    print("Userbot Error! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)


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
                [Button.inline("Updates", "https://t.me/DionProjects")]
                ]
            )


@bot.on(events.NewMessage(pattern="^[!?/]help$"))
async def helper(event):
    await event.reply(
            "**List command:\n\n• /bokep - Untuk mendapatkan video 4no\n•/asupan - Mendapatkan video asupan (bukan bokep 4no yah)\nn• /desah - Mendapatkan desahan random\n• /hentai - Mendapatkan foto 4no**",
            buttons=[
                [Button.inline("Updates", "https://t.me/DionProjects")]
                ]
            )


@bot.on(events.NewMessage(pattern="^[!?/]asupan$"))
async def asup(event):

    teks = await event.reply("**Mencari Video Asupan...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in dbot.iter_messages(

            "@DionAsupanCache", filter=InputMessagesFilterVideo

            )

        ]

        royzu = random.choice(asupannya)

        dion = await dbot.download_media(royzu)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Asupan by Dion Bot", 

            file=dion

            )

        await teks.delete()

    except Exception:

        await teks.edit("Error karena dosamu besar.")


@bot.on(events.NewMessage(pattern="^[!?/]asupan$"))
async def desahh(event):

    bgst = await event.reply("**Mencari Desahan...🔍**") 

    try:

        desahannya = [

            desah

            async for desah in dbot.iter_messages(

            "@desahancewesangesange", filter=InputMessagesFilterVoice

            )

        ]

        ewe = random.choice(desahannya)

        prik = await dbot.download_media(ewe)

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
