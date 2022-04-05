import os
from telethon import TelegramClient
from telethon.sessions import MemorySession
from pyrogram import Client
from Dion.modules.bot import STRING_SESSION


API_ID = "16813597"
API_HASH = "6ce811cff9c14820a3352aa5176066b6"

telethn = TelegramClient(MemorySession(), API_ID, API_HASH)

ubot2 = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
try:
    ubot2.start()
except BaseException:
    print("Userbot Error! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)
