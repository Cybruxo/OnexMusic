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
from pyrogram.types import Message

from OnexMusic import app
from OnexMusic.core.call import Cybruxo

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Cybruxo.stop_stream_force(message.chat.id)
