#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from .list import list
from database.gtrans_mdb import find_one

@Client.on_message(filters.command(["translate"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/translate")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
                try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"```{translation.text}```", reply_markup=hehek, reply_to_message_id=message.reply_to_message.message_id)
			except:
			   	await message.reply_text(f"```{translation.text}```", reply_markup=hehek, reply_to_message_id=message.reply_to_message.message_id)
			

		except :
			print("error")
	else:
			 ms = await message.reply_text("You can Use This Command by using reply to message")
			 await ms.delete()
