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
from Userbot.helper.tools import _misc, ReplyCheck

# MODULE INI GUA BUAT SENDIRI KONTOL LU CARI AJA KALO EMANG ADA YA ANJING

__MODULES__ = "•Animasi•"

def help_string(org):
    return h_s(org, "help_anim")

@ky.ubot("dino")
async def _(client: nlx, message, _):
    typew = await message.edit_text("**DIN DINNN.....**")
    await asyncio.sleep(1.5)
    await typew.edit("**DINOOOOSAURUSSSSS!!**")
    await asyncio.sleep(1.5)
    await typew.edit("**🏃                        🦖**")
    await typew.edit("**🏃                       🦖**")
    await typew.edit("**🏃                      🦖**")
    await typew.edit("**🏃                     🦖**")
    await typew.edit("**🏃   **PUKII**          🦖**")
    await typew.edit("**🏃                   🦖**")
    await typew.edit("**🏃                  🦖**")
    await typew.edit("**🏃                 🦖**")
    await typew.edit("**🏃                🦖**")
    await typew.edit("**🏃               🦖**")
    await typew.edit("**🏃              🦖**")
    await typew.edit("**🏃             🦖**")
    await typew.edit("**🏃            🦖**")
    await typew.edit("**🏃           🦖**")
    await typew.edit("**🏃WOARGH!   🦖**")
    await typew.edit("**🏃           🦖**")
    await typew.edit("**🏃            🦖**")
    await typew.edit("**🏃             🦖**")
    await typew.edit("**🏃              🦖**")
    await typew.edit("**🏃               🦖**")
    await typew.edit("**🏃                🦖**")
    await typew.edit("**🏃                 🦖**")
    await typew.edit("**🏃                  🦖**")
    await typew.edit("**🏃                   🦖**")
    await typew.edit("**🏃                    🦖**")
    await typew.edit("**🏃                     🦖**")
    await typew.edit("**🏃  Huh-Huh           🦖**")
    await typew.edit("**🏃                   🦖**")
    await typew.edit("**🏃                  🦖**")
    await typew.edit("**🏃                 🦖**")
    await typew.edit("**🏃                🦖**")
    await typew.edit("**🏃               🦖**")
    await typew.edit("**🏃              🦖**")
    await typew.edit("**🏃             🦖**")
    await typew.edit("**🏃            🦖**")
    await typew.edit("**🏃           🦖**")
    await typew.edit("**🏃          🦖**")
    await typew.edit("**🏃         🦖**")
    await typew.edit("**DIA SEMAKIN MENDEKAT!!!**")
    await asyncio.sleep(1.5)
    await typew.edit("**🏃       🦖**")
    await typew.edit("**🏃      🦖**")
    await typew.edit("**🏃     🦖**")
    await typew.edit("**🏃    🦖**")
    await typew.edit("**Dahlah Pasrah Aja**")
    await asyncio.sleep(1.5)
    await typew.edit("**🧎🦖**")
    await asyncio.sleep(2)
    await typew.edit("**PAPAY SEMUANYA**")

@ky.ubot("kntl")
async def _(client: nlx, message, _):
    value = nlx.get_text(message)
    kontol = MEMES.GAMBAR_KONTOL
    if value:
        kontol = kontol.replace("⡀", emoji)
    await message.edit(kontol)

@ky.ubot("hmm")
async def _(client: nlx, message, _):
    await message.reply(
          "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱╱▔▔▔▔▔╲╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰▏▊▕▕▋▕▕╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
      )

@ky.ubot("heli")
async def _(client: nlx, message, _):
    await message.reply(
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )

@ky.ubot("titid")
async def titid(client: nlx, message, _):
    value = nlx.get_text(message)
    titid = MEMES.GAMBAR_TITID
    if value:
        titid = titid.replace("😋", emoji)
    await message.edit(titid)

@ky.ubot("babi")
async def _(client: nlx, message, _):
    await message.reply(
        "┈┈┏━╮╭━┓┈╭━━━━╮"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯"
        "┈╭━┻╮╲┗━━━━╮╭╮┈"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈"
    )

@ky.ubot("tank")
async def _(client: nlx, message, _):
    await message.reply(
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )

@ky.ubot("ange")
async def _(client: nlx, message, _):
    e = await message.edit_text("Ayanggg 😖")
    await asyncio.sleep(2)
    await e.edit("Aku Ange 😫")
    await asyncio.sleep(2)
    await e.edit("Ayuukk Picies Yang 🤤")

@ky.ubot("ajg")
async def _(client: nlx, message, _):
    await message.reply(
        "╥━━━━━━━━╭━━╮━━┳"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻"
    )

@ky.ubot("kocok")
async def _(client: nlx, message, _):
    e = await message.edit_text("KOCOKINNNN SAYANGG🥵")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT**")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT AAAHHH.....**")
    await asyncio.sleep(0.2)
    await e.edit("AHHH ENAKKKKK SAYANGGGG🥵🥵**")

@ky.ubot("syg")
async def _(client: nlx, message, _):
    e = await message.edit_text("I LOVEE YOUUU 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELALU YA 💕")
    await e.edit("💘💘💘💘")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU💞")

@ky.ubot("loveyou")
async def _(client: nlx, message, _):
    e = await message.edit_text("Hai Sayang💕")
    await e.edit("💝💘💓💗")
    await e.edit("Kamu cantik Bnaget Deh")
    await e.edit("💝💘💓💗")
    await e.edit("Kangen Nih aku")
    await e.edit("💘💞💗💕")
    await e.edit("Jangan Tinggalin Aku Ya")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELALU 💕")
    await e.edit("💘💘💘💘")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU💞")

@ky.ubot("bundir")
async def _(client: nlx, message, _):
    await message.edit_text(
        "Dadah Semuanya...          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )

@ky.ubot("gbt")
async def _(client: nlx, message, _):
    e = await message.reply("**PERNAAHHHHH KAHHH KAUUU MENGIRA**")
    await e.edit("**SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA**")
    await e.edit("**RAMBUUUT WARNAAA WARNII**")
    await e.edit("**BAGAI GULALI**")
    await e.edit("**IMUUUTTTTT LUCUUU**")
    await e.edit("**WALAAUUUU TAK TERLALU TINGGI**")
    await e.edit("**GW GABUUTTTT**")
    await e.edit("**EMMMM BACOTNYA**")
    await e.edit("**GABUTTTT WOI GABUT**")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("**CILUUUKKK BAAAAA**")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🚶                                 🐢")
    await e.edit("**AAHHH PUKIII**")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("😂")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await asyncio.sleep(1)
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("**PUKII**")

@ky.ubot("hack")
async def _(client: nlx, message, _):
    await message.edit_text("**ɪɴsᴇʀᴛɪɴɢ ᴜsᴇʀs ɪɴᴛᴏ ᴍᴀᴜʟ ᴅᴀᴛᴀʙᴀsᴇ...**")
    await asyncio.sleep(2)
    await message.edit_text(
        "❏ **ᴜsᴇʀ ᴏɴʟɪɴᴇ: True**\n├ **ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴇss: True**\n╰ **ᴍᴀᴜʟ sᴛᴏʀᴀɢᴇ: True**"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 0%**\n[░░░░░░░░░░░░░░░░░░░░]\n**ɪɴ ᴘʀᴏᴄᴇss...**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 20s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 11.07%**\n[██░░░░░░░░░░░░░░░░░░]\n**ᴇɴsᴜʀᴇ ᴛᴀʀɢᴇᴛ ɪs ᴅᴇᴛᴇᴄᴛᴇᴅ.**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 18s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 20.63%**\n[███░░░░░░░░░░░░░░░░░]\n**ᴛᴀʀɢᴇᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴛᴇᴄᴛᴇᴅ**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 16s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 34.42%**\n[█████░░░░░░░░░░░░░░░]\n**ᴇɴᴛᴇʀ ᴛᴀʀɢᴇᴛ ɪɴᴛᴏ ᴍᴀᴜʟ ᴅᴀᴛᴀʙᴀsᴇ**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 14s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 42.17%**\n[███████░░░░░░░░░░░░░]\n**ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍᴏʀᴇ sᴇᴄᴏɴᴅs.**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 12s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 55.30%**\n[█████████░░░░░░░░░░░]\n**ᴛᴀʀɢᴇᴛ ɪs ᴀɴ ɪᴅɪᴏᴛ**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 10s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 64.86%**\n[███████████░░░░░░░░░]\n**ᴛᴇʀᴅᴇᴛᴇᴋsɪ ʙᴀʜᴡᴀ ᴛᴀʀɢᴇᴛ sᴇᴏʀᴀɴɢ ʜᴛs ʏɢ ɢᴀᴍᴏɴ.**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 08s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 74.02%**\n[█████████████░░░░░░░]\n**ᴛᴇʀᴅᴇᴛᴇᴋsɪ ʙᴀʜᴡᴀ ᴛᴀʀɢᴇᴛ ᴛᴜᴋᴀɴɢ sᴇʟɪɴɢᴋᴜʜ.**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 06s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 86.21%**\n[███████████████░░░░░]\n**ᴛʀʏɪɴɢ ᴛᴏ ᴇɴᴛᴇʀ ᴍᴀᴜʟ ᴅᴀᴛᴀʙᴀsᴇ**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 04s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 93.50%**\n[█████████████████░░░]\n**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ᴍᴀᴜʟ ᴅᴀᴛᴀʙᴀsᴇ.**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 02s`"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "**ʜᴀᴄᴋɪɴɢ... 100%**\n[████████████████████]\n**ᴍᴏᴠᴇ ᴛᴀʀɢᴇᴛ ᴅᴀᴛᴀ ɪɴᴛᴏ ᴍᴀᴜʟ ᴅᴀᴛᴀʙᴀsᴇ.**\n**sᴘᴇᴇᴅ ᴏғ ᴛɪᴍᴇ:** `0m, 00s`"
    )
    await asyncio.sleep(2)
    await message.edit_text("❏ **ʜᴀᴄᴋɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇᴅ**\n╰ **ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    await asyncio.sleep(2)
    await message.edit_text(
        "❏ **ʜᴀᴄᴋɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇᴅ...!**\n├ **ʜᴀᴄᴋɪɴɢ ᴡᴇɴᴛ sᴍᴏᴏᴛʜʟʏ.**\n├ **ᴍᴀᴜʟ ᴅᴀᴛᴀʙᴀsᴇ**:\n╰ **ᴅᴀᴛᴀʙᴀsᴇ: gstorage.db.maul** ✅"
    )

@ky.ubot("love")
async def _(client: nlx, message, _):
    e = await message.reply("**PERNAAHHHHH KAHHH KAUUU MENGIRA**")
    await e.edit("❤️ I")
    await asyncio.sleep(0.5)
    await e.edit("❤️ I Love")
    await asyncio.sleep(0.5)
    await e.edit("❤️ I Love You")
    await asyncio.sleep(3)
    await e.edit("❤️ I Love You <3")

@ky.ubot("fuck")
async def _(client: nlx, message, _):
    e = await message.reply(".                       /¯ )")
    await e.edit(".                       /¯ )\n                      /¯  /")
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )

@ky.ubot("tembak")
async def _(client: nlx, message, _):
    await message.reply(
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\nMau Jadi Pacarku Gak?!",
    )

@ky.ubot("awk")
async def _(client: nlx, message, _):
    await message.reply(
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n**Awkwokwokwok...**",
    )

@ky.ubot("y")
async def _(client: nlx, message, _):
    await message.reply(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )

@ky.ubot("nahh")
async def _(client: nlx, message, _):
    typew = await message.reply(
        "`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 <b>Ini Buat Kamu</b>"
    )
    await asyncio.sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  <b>Tapi Bo'ong</b>")

@ky.ubot("santet")
async def _(client: nlx, message, _):
    typew = await message.edit_text("Mengaktifkan Perintah Santet Online....")
    await asyncio.sleep(2)
    await typew.edit("Mencari Nama Orang Ini...")
    await asyncio.sleep(1)
    await typew.edit("Santet Online Segera Dilakukan")
    await asyncio.sleep(1)
    await typew.edit("0%")
    await typew.edit("1% ▎")
    await asyncio.sleep(0.5)
    await typew.edit("2% ▍")
    await asyncio.sleep(0.5)
    await typew.edit("3% ▌")
    await asyncio.sleep(0.5)
    await typew.edit("4% ▊")
    await asyncio.sleep(0.5)
    await typew.edit("5% ▉")
    await asyncio.sleep(0.5)
    await typew.edit("6% █")
    await asyncio.sleep(0.5)
    await typew.edit("7% █▎")
    await asyncio.sleep(0.5)
    await typew.edit("8% █▍")
    await asyncio.sleep(0.5)
    await typew.edit("9% █▌")
    await asyncio.sleep(0.5)
    await typew.edit("10% █▊")
    await asyncio.sleep(0.5)
    await typew.edit("11% █▉")
    await asyncio.sleep(0.5)
    await typew.edit("12% ██")
    await asyncio.sleep(0.5)
    await typew.edit("13% ██▎")
    await asyncio.sleep(0.5)
    await typew.edit("14% ██▍")
    await asyncio.sleep(0.5)
    await typew.edit("15% ██▌")
    await asyncio.sleep(0.5)
    await typew.edit("16% ██▊")
    await asyncio.sleep(0.5)
    await typew.edit("17% ██▉")
    await asyncio.sleep(0.5)
    await typew.edit("18% ███")
    await asyncio.sleep(0.5)
    await typew.edit("19% ███▎")
    await asyncio.sleep(0.5)
    await typew.edit("20% ███▍")
    await asyncio.sleep(0.5)
    await typew.edit("21% ███▌")
    await asyncio.sleep(0.5)
    await typew.edit("22% ███▊")
    await asyncio.sleep(0.5)
    await typew.edit("23% ███▉")
    await asyncio.sleep(0.5)
    await typew.edit("24% ████")
    await asyncio.sleep(0.5)
    await typew.edit("25% ████▎")
    await asyncio.sleep(0.5)
    await typew.edit("26% ████▍")
    await asyncio.sleep(0.5)
    await typew.edit("27% ████▌")
    await asyncio.sleep(0.5)
    await typew.edit("28% ████▊")
    await asyncio.sleep(0.5)
    await typew.edit("29% ████▉")
    await asyncio.sleep(0.5)
    await typew.edit("30% █████")
    await asyncio.sleep(0.5)
    await typew.edit("31% █████▎")
    await asyncio.sleep(0.5)
    await typew.edit("32% █████▍")
    await asyncio.sleep(0.5)
    await typew.edit("33% █████▌")
    await asyncio.sleep(0.5)
    await typew.edit("34% █████▊")
    await asyncio.sleep(0.5)
    await typew.edit("35% █████▉")
    await asyncio.sleep(0.5)
    await typew.edit("36% ██████")
    await asyncio.sleep(0.5)
    await typew.edit("36% ██████▎")
    await asyncio.sleep(0.5)
    await typew.edit("36% ██████▍")
    await asyncio.sleep(0.5)
    await typew.edit("37% ██████▌")
    await asyncio.sleep(0.5)
    await typew.edit("38% ██████▊")
    await asyncio.sleep(0.5)
    await typew.edit("39% ██████▉")
    await asyncio.sleep(0.5)
    await typew.edit("40% ███████")
    await asyncio.sleep(0.5)
    await typew.edit("41% ███████▎")
    await asyncio.sleep(0.5)
    await typew.edit("42% ███████▍")
    await asyncio.sleep(0.5)
    await typew.edit("43% ███████▌")
    await asyncio.sleep(0.5)
    await typew.edit("44% ███████▊")
    await asyncio.sleep(0.5)
    await typew.edit("45% ███████▉")
    await asyncio.sleep(0.5)
    await typew.edit("46% ████████")
    await asyncio.sleep(0.5)
    await typew.edit("47% ████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("48% ████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("49% ████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("50% ████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("51% ████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("52% █████████")
    await asyncio.sleep(0.5)
    await typew.edit("53% █████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("54% █████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("55% █████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("56% █████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("57% █████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("58% ██████████")
    await asyncio.sleep(0.5)
    await typew.edit("59% ██████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("60% ██████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("61% ██████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("62% ██████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("63% ██████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("64% ███████████")
    await asyncio.sleep(0.5)
    await typew.edit("65% ███████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("66% ███████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("67% ███████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("68% ███████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("69% ███████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("70% ████████████")
    await asyncio.sleep(0.5)
    await typew.edit("71% ████████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("72% ████████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("73% ████████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("74% ████████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("75% ████████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("76% █████████████")
    await asyncio.sleep(0.5)
    await typew.edit("77% █████████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("78% █████████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("79% █████████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("80% █████████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("81% █████████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("82% ██████████████")
    await asyncio.sleep(0.5)
    await typew.edit("83% ██████████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("84% ██████████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("85% ██████████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("86% ██████████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("87% ██████████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("88% ███████████████")
    await asyncio.sleep(0.5)
    await typew.edit("89% ███████████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("90% ███████████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("91% ███████████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("92% ███████████████▊")
    await asyncio.sleep(0.5)
    await typew.edit("93% ███████████████▉")
    await asyncio.sleep(0.5)
    await typew.edit("94% ████████████████")
    await asyncio.sleep(0.5)
    await typew.edit("95% ████████████████▎")
    await asyncio.sleep(0.5)
    await typew.edit("96% ████████████████▍")
    await asyncio.sleep(0.5)
    await typew.edit("97% ████████████████▌")
    await asyncio.sleep(0.5)
    await typew.edit("98% ████████████████▌")
    await asyncio.sleep(1)
    await typew.edit("99% ██████████████████")
    await asyncio.sleep(1)
    await typew.edit("100% ██████████████████████")
    await asyncio.sleep(1)
    await typew.edit("**Target Berhasil Tersantet Online**")
