import os

import random

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice

from DionBot.events import register

from DionBot import telethn as tbot, ubot2                 

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
