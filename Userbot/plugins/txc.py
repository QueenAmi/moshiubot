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

# MODULE INI GUA BUAT SENDIRI KONTOL LU CARI AJA KALO EMANG ADA YA ANJING

__MODULES__ = "•Bacot 1•"

def help_string(org):
    return h_s(org, "help_txc")

@ky.ubot("jamet")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id not in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("WOII")
    await asyncio.sleep(1.5)
    await xx.edit("Lu yang rusuh sana sini?")
    await asyncio.sleep(1.5)
    await xx.edit("Ni gw bilang ya")
    await asyncio.sleep(1.5)
    await xx.edit("GAUSAH SO ASIK")
    await asyncio.sleep(1.5)
    await xx.edit("EMANG LU TERKENAL?")
    await asyncio.sleep(1.5)
    await xx.edit("Cuma kacung di real sok mau rusuh")
    await asyncio.sleep(1.5)
    await xx.edit("Orang yang kaya lu ni harus gw katain")
    await asyncio.sleep(1.5)
    await xx.edit("Jangan sok tinggi di telegram bgstt")
    await asyncio.sleep(1.5)
    await xx.edit("BOCAH KAMPUNG")
    await asyncio.sleep(1.5)
    await xx.edit("THOLOL KALAU LU MAU RUSUH JANGAN DISINI THOLOL")
    await asyncio.sleep(1.5)
    await xx.edit("Mending lu bantu mak lu sono, dari pada ga ada kerjaan")

@ky.ubot("bct")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id not in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("WOII")
    await asyncio.sleep(1.5)
    await xx.edit("Lu gausah kebanyakan bacot")
    await asyncio.sleep(1.5)
    await xx.edit("Ni gw bilang ya")
    await asyncio.sleep(1.5)
    await xx.edit("GAUSAH SO ASIK")
    await asyncio.sleep(1.5)
    await xx.edit("EMANG LU TERKENAL?")
    await asyncio.sleep(1.5)
    await xx.edit("Cuma kacung di real banyak bacot")
    await asyncio.sleep(1.5)
    await xx.edit("Orang yang kaya lu ni harus gw katain")
    await asyncio.sleep(1.5)
    await xx.edit("Jangan sok tinggi di telegram bgstt")
    await asyncio.sleep(1.5)
    await xx.edit("BOCAH KAMPUNG")
    await asyncio.sleep(1.5)
    await xx.edit("THOLOL KALAU LU MAU NGEBACOT JANGAN DISINI THOLOL")
    await asyncio.sleep(1.5)
    await xx.edit("Mending lu bantu mak lu sono, dari pada ga ada kerjaan")

@ky.ubot("vir")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id not in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI YANG VIRTUAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**APALAGI KEMALUAN NYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await xx.edit("**KASIAN BAHAHAHA GBLOK MKN TUH VIRTUAL**")

@ky.ubot("pto")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("OHH INII MANUSIANYA")
    await asyncio.sleep(1.5)
    await xx.edit("Yang ga pake pp tah")
    await asyncio.sleep(1.5)
    await xx.edit("Ni gw bilangin ya")
    await asyncio.sleep(1.5)
    await xx.edit("MENDING PAKE PP LU DAH")
    await asyncio.sleep(1.5)
    await xx.edit("GA PAKE PP BEGITU KELIATAN BANGET IDIOTNYA")
    await asyncio.sleep(1.5)
    await xx.edit("KEK BOCAH STRESS JUGA LAMA LAMA GUA LIATNYA")
    await asyncio.sleep(1.5)
    await xx.edit("KASIAN GUA AMA LU")
    await asyncio.sleep(1.5)
    await xx.edit("KEK BOCAH TOLOL")
    await asyncio.sleep(1.5)
    await xx.edit("MENDING KALO KATA GUA PAKE DAH TUH FITUR PP DI TELEGRAM.")

@ky.ubot("crht")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("NI GW KASIH TAU..")
    await asyncio.sleep(1.5)
    await xx.edit("LU KALAU MAU CURHAT")
    await asyncio.sleep(1.5)
    await xx.edit("JANGAN KE GW LAH GBLK")
    await asyncio.sleep(1.5)
    await xx.edit("MALAS DENGAR CERITA LU KNTL")
    await asyncio.sleep(1.5)
    await xx.edit("CERITA KAGAK JELAS GBLK")
    await asyncio.sleep(1.5)
    await xx.edit("CURHAT YANG HASILIN DUIT KEK")
    await asyncio.sleep(1.5)
    await xx.edit("INI MALAH CURHAT SOAL KEHIDUPAN LU YG KEK TAII ANYING ITU")
    await asyncio.sleep(1.5)
    await xx.edit("LU CUMA CERITA SOAL KEPALSUAN HIDUP LU DOANG THOLOL")
    await asyncio.sleep(1.5)
    await xx.edit("NAMA JUGA BOCAHH PUBER")
    await asyncio.sleep(1.5)
    await xx.edit("DI SAKITINN ORANG TUA SEDIKIT NGAMBEK GBLK")
    await asyncio.sleep(1.5)
    await xx.edit("BANTU NOH ORANG TUA LU KASIHAN NGASIH LU MAKAN")

@ky.ubot("sknl")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("**Jangan replay**")
    await asyncio.sleep(1.5)
    await xx.edit("kita ga kenal")
    await asyncio.sleep(1.5)
    await xx.edit("kalau mau replay, replay aja sendiri")
    await asyncio.sleep(1.5)
    await xx.edit("ke akun lu, jangan reply ke gw")
    await asyncio.sleep(1.5)
    await xx.edit("ga keren lu begitu sok kenal")
    await asyncio.sleep(1.5)
    await xx.edit("lu kalau mau kenalan dipc aja:v")
    await asyncio.sleep(1.5)
    await xx.edit("jangan direplay, yang direplay aja banyak")
    await asyncio.sleep(1.5)
    await xx.edit("BHAHAHAHA")
    await asyncio.sleep(1.5)
    await xx.edit("apa lagi yang dichat kwkwkw bercanda")

@ky.ubot("umm")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("umm boleh kenalan ga?")
    await asyncio.sleep(1.5)
    await xx.edit("anu kalau ga boleh gpp kok")
    await asyncio.sleep(1.5)
    await xx.edit("Tapi boong:v")
    await asyncio.sleep(1.5)
    await xx.edit("siapa juga yang mau kenal sama orang murahan")
    await asyncio.sleep(1.5)
    await xx.edit("sana sini mau, BAHAHAHA")
    await asyncio.sleep(1.5)
    await xx.edit("didekatin dikit langsung terima")
    await asyncio.sleep(1.5)
    await xx.edit("dibilang gatel si engga hehe")
    await asyncio.sleep(1.5)
    await xx.edit("TAPI DIBILANG MURAH IYA KWKWK")
    await asyncio.sleep(1.5)
    await xx.edit("UDAH MURAH MURAHAN LAGI GBLK BHAHA")

@ky.ubot("smlu")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("eh gw mau nanya nih")
    await asyncio.sleep(1.5)
    await xx.edit("kau punya malu kan?")
    await asyncio.sleep(1.5)
    await xx.edit("kalau punya malu kok sikap nya kaya...")
    await asyncio.sleep(1.5)
    await xx.edit("ga punya malu?")
    await asyncio.sleep(1.5)
    await xx.edit("apa jangan jangan....")
    await asyncio.sleep(1.5)
    await xx.edit("urat malu kau putus?")
    await asyncio.sleep(1.5)
    await xx.edit("BHAHAHAHAHA KAGAK PUNYA MALU")
    await asyncio.sleep(1.5)
    await xx.edit("upp bercanda eh")
    await asyncio.sleep(1.5)
    await xx.edit("tapi seriusan emg lu punya urat malu???")

@ky.ubot("shai")
async def _(client: nlx, message, _):
    user_id = message.from_user.id
    if user_id in DEVS:
        return await message.reply(
            "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await message.edit_text("**HAI ANAK LONTE**")
    await asyncio.sleep(1.5)
    await xx.edit("**KALO LU OPEN VCS GAUSAH DISINI ANJING**")
    await asyncio.sleep(1.5)
    await xx.edit("**PEPEK LU AJA ITEM GOBLOK**")
    await asyncio.sleep(1.5)
    await xx.edit("**HARGA DIRI LU AJA KEMURAHAN ANJING**")
    await asyncio.sleep(1.5)
    await xx.edit("**OPEN VCS 25K UDAH KYA BELI WARTEG**")
    await asyncio.sleep(1.5)
    await xx.edit("**WARTEG AJA LEBIH MAHAL DARI PADA HARGA DIRI LU KONTOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**DASAR LOMTE !.**")

@ky.ubot("solat")
async def _(client: nlx, message, _):
    e = await message.edit_text("Oh ini yg bocahnya yg katanya islam tapi jarang sholat")
    await asyncio.sleep(1.5)
    await e.edit("minimal sholat dongo")
    await asyncio.sleep(1)
    await e.edit("mau jadi apaan lu emangnya ga sholat?")
    await asyncio.sleep(1)
    await e.edit("maen tele bisa sholat kga")
    await asyncio.sleep(1)
    await e.edit("maen tele doang mah kga buat lu masuk surga dongo.")
    await asyncio.sleep(1)
    await e.edit("sholat ya anak monyet")
    await asyncio.sleep(1)
    await e.edit("biar di kata bandel juga")
    await asyncio.sleep(1)
    await e.edit("sholat mah tetep jalanin anjing.")
    await asyncio.sleep(1)
    await e.edit("jangan kek bocah onoh yg bisanya bikin skandal doang")
    await asyncio.sleep(1)
    await e.edit("biar di kata badung juga yg penting bisa ngaji.")

@ky.ubot("pe")
async def _(client: nlx, message, _):
    e = await message.edit_text("hai anak anjing minimal salam ya bangsat")
    await asyncio.sleep(1.5)
    await e.edit("lu kan di kibort lu ada huruf tu ya")
    await asyncio.sleep(1.5)
    await e.edit("minimal salam anjing kek ga punya agama aja lu")
    await asyncio.sleep(1.5)
    await e.edit("jangan kek bocah idiot cuma hi hi doang")
    await asyncio.sleep(1.5)
    await e.edit("apalagi cuma pa pe pa pe")
    await asyncio.sleep(1)
    await e.edit("kek bocah ateis anjing pa pe pa pe bangsat.")
