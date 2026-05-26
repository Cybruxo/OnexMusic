# * ● OnexMusic
# * ○ A high-performance engine for streaming music in Telegram voicechats.
# *
# * Copyright (C) 2026 Cybruxo
# *
# * This program is free software: you can redistribute it and/or modify it under the
# * terms of the GNU General Public License as published by the Free Software Foundation,
# * either version 3 of the License, or (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful, but WITHOUT ANY
# * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# * PARTICULAR PURPOSE. See the GNU General Public License for more details.
# *
# * Repository: https://github.com/Cybruxo/OnexMusic

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from OnexMusic import LOGGER, app, userbot
from OnexMusic.core.call import Cybruxo
from OnexMusic.misc import sudo
from OnexMusic.plugins import ALL_MODULES
from OnexMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("OnexMusic.plugins" + all_module)
    LOGGER("OnexMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Cybruxo.start()
    try:
        await Cybruxo.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("OnexMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await Cybruxo.decorators()
    await idle()
    await app.stop()
    LOGGER("OnexMusic").info("Stopping Onex Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
