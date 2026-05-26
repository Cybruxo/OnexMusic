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

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from OnexMusic import app
from OnexMusic.utils.database import get_playmode, get_playtype, is_nonadmin_chat
from OnexMusic.utils.decorators import language
from OnexMusic.utils.inline.settings import playmode_users_markup
from config import BANNED_USERS


@app.on_message(filters.command(["playmode", "mode"]) & filters.group & ~BANNED_USERS)
@language
async def playmode_(client, message: Message, _):
    playmode = await get_playmode(message.chat.id)
    if playmode == "Direct":
        Direct = True
    else:
        Direct = None
    is_non_admin = await is_nonadmin_chat(message.chat.id)
    if not is_non_admin:
        Group = True
    else:
        Group = None
    playty = await get_playtype(message.chat.id)
    if playty == "Everyone":
        Playtype = None
    else:
        Playtype = True
    buttons = playmode_users_markup(_, Direct, Group, Playtype)
    response = await message.reply_text(
        _["play_22"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
