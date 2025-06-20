import os
import asyncio 
import random

from Userbot import *
from Userbot import nlx
from Userbot.helper.tools import _anim, ky, h_s, capture_err, MEMES, _wrap_edit

from pyrogram import *
from pyrogram import filters 
from pyrogram.errors import FloodWait
from pyrogram.types import *
from config import (DEVS, api_hash, api_id, bot_id, bot_username, log_userbot,
                    owner_id)
from Userbot.helper.tools import _misc, ReplyCheck
from Userbot.plugins import tt_string as tod

# MODULE INI GUA BUAT SENDIRI KONTOL LU CARI AJA KALO EMANG ADA YA ANJING

__MODULES__ = "•Spillan•"

def help_string(org):
    return h_s(org, "help_ctt")

@ky.ubot("cektt")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    try:      
        await message.reply(f"{random.choice(tod.TT)}")
    except BaseException:
        pass

@ky.ubot("cekkntl")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    try:      
        await message.reply(f"{random.choice(tod.KNTL)}")
    except BaseException:
        pass

@ky.ubot("cekmmk")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    try:      
        await message.reply(f"{random.choice(tod.MMK)}")
    except BaseException:
        pass
