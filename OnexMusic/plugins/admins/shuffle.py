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

import random

from pyrogram import filters
from pyrogram.types import Message

from OnexMusic import app
from OnexMusic.misc import db
from OnexMusic.utils.decorators import AdminRightsCheck
from OnexMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["shuffle", "cshuffle"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_16"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
