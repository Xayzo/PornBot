from telethon import TelegramClient
from telethon.sessions import MemorySession
from pyrogram import Client


    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)


telethn = TelegramClient(MemorySession(), API_ID, API_HASH)

ubot2 = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
try:
    ubot2.start()
except BaseException:
    print("Userbot Error! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)
