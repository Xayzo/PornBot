import os
from telethon import TelegramClient
from telethon.sessions import MemorySession, StringSession
from pyrogram import Client


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
