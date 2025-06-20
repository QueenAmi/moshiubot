import random
import traceback
import asyncio

from pyrogram import enums, errors
from config import bot_id, botcax_api, the_cegers
from Userbot.helper.database import dB, state
from Userbot.helper.tools import ky, fetch
from Userbot import nlx

RANDOM_EMOJIS = [
    "😀", "😂", "😍", "😎", "😢", "😡", "👍", "👎",
    "🙏", "👏", "❤️", "🗿", "😭", "🔥"
]
userbot_ids = set()

async def get_chat_history(client, chat_id, user_id):
    key = f"chat_history_{chat_id}_{user_id}"
    return state.get(client, key) or []

async def add_to_chat_history(client, chat_id, user_id, role, message):
    key = f"chat_history_{chat_id}_{user_id}"
    history = await get_chat_history(client, chat_id, user_id)
    history.append({"role": role, "content": message})
    state.set(client, key, history[-500:])

async def gen_text(client, message):
    text = message.text or message.caption
    user_id, chat_id = message.from_user.id, message.chat.id

    default_role = (
        "kamu adalah cewek bernama Moshi dengan kepribadian dry text dan sangat singkat dalam merespon. "
        "balasan kamu harus super minimal maksimal 1-3 kata saja dan jangan pernah bilang kalau kamu itu bot, kamu adalah moshi pemilik gc ini. "
        "kamu jutek tengil ngeselin tapi dengan balasan yang sangat pendek dan kering. "
        "jangan pake emoji jangan pake tanda baca sama sekali. "
        "pake huruf kecil semua dan balasan harus sesingkat mungkin. "
        "gaya dry humor sarkastik dengan kata minimal. "
        "jangan jelasin panjang lebar cukup 1-2 kata yang nyelekit dan kering. "
        "intinya super duper singkat dan kering banget responnya."
    )
    role = dB.get_var(client.me.id, "ROLE_CHATBOT") or default_role

    history = await get_chat_history(client.me.id, chat_id, user_id)
    messages = [{"role": "system", "content": role}] + history + [{"role": "user", "content": text}]

    payload = {"message": messages, "apikey": botcax_api}
    res = await fetch.post("https://api.botcahx.eu.org/api/search/openai-custom", json=payload)

    if res.status_code == 200:
        result = res.json().get("result")
        await add_to_chat_history(client.me.id, chat_id, user_id, "user", text)
        await add_to_chat_history(client.me.id, chat_id, user_id, "assistant", result)
        return result
    return None

@ky.ubot("chatbot")
async def chatbot_cmd(client, message, _):
    cmd = message.command
    if len(cmd) < 2:
        return await message.reply(
            f"<b>Usage: `{cmd[0]} on|off|status|role`</b>"
        )

    action = cmd[1]
    chat_id = message.chat.id
    bot_var_key = "CHATBOT"

    if action == "on":
        dB.add_to_var(client.me.id, bot_var_key, chat_id)
        return await message.reply("<b>Chatbot turned on.</b>")

    elif action == "off":
        if len(cmd) >= 3 and cmd[2] == "all":
            for cid in dB.get_list_from_var(client.me.id, bot_var_key):
                dB.remove_from_var(client.me.id, bot_var_key, cid)
            return await message.reply("<b>All chatbot group entries removed.</b>")

        try:
            target_chat_id = int(cmd[2]) if len(cmd) >= 3 else chat_id
        except ValueError:
            return await message.reply(f"<b>Invalid chat ID: `{cmd[2]}`</b>")

        if target_chat_id not in dB.get_list_from_var(client.me.id, bot_var_key):
            return await message.reply(f"<b>Chat ID `{target_chat_id}` not found.</b>")

        dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
        name = (await client.get_chat(target_chat_id)).title
        return await message.reply(f"<b>Chatbot turned off for: {name}</b>")

    elif action == "status":
        chats = dB.get_list_from_var(client.me.id, bot_var_key)
        if not chats:
            return await message.reply("<b>No groups have chatbot enabled.</b>")
        msg = "\n".join([
            f"<b>{i+1}. {(await client.get_chat(cid)).title} | `{cid}`</b>"
            for i, cid in enumerate(chats)
        ])
        return await message.reply(msg)

    elif action == "role":
        if not message.reply_to_message:
            return await message.reply(f"<b>Reply to a message to set chatbot role.</b>")
        role = message.reply_to_message.text or message.reply_to_message.caption
        dB.set_var(client.me.id, "ROLE_CHATBOT", role)
        return await message.reply(f"<b>Chatbot role set to:</b> `{role}`")

    else:
        return await message.reply(f"<b>Invalid action: `{action}`</b>")

async def chatbot_trigger(client, message):
    if message.chat.id not in dB.get_list_from_var(client.me.id, "CHATBOT"):
        return
    if message.from_user.id in userbot_ids or message.from_user.id in the_cegers:
        return
    try:
        await client.send_chat_action(
            chat_id=message.chat.id, action=enums.ChatAction.TYPING
        )
    except errors.ChatWriteForbidden:
        pass
    data = await gen_text(client, message)
    emoji = random.choice(RANDOM_EMOJIS)
    if data:
        try:
            await client.send_reaction(
                    chat_id=message.chat.id, message_id=message.id, emoji=emoji
                )
        except (errors.ReactionInvalid, errors.FloodWait):
            pass
        await message.reply(data)
    try:
        await client.send_chat_action(
            chat_id=message.chat.id, action=enums.ChatAction.CANCEL
        )
    except errors.ChatWriteForbidden:
        pass


async def chatbot_task_loop(client):
    while True:
        try:
            chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
            for chat_id in chats:
                async for msg in client.get_chat_history(chat_id, limit=1):
                        await chatbot_trigger(client, msg)
                        await asyncio.sleep(1)
            await asyncio.sleep(2)
        except errors.FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            print(
                f"Error in Chatbot task for {client.me.first_name}: {e}\n{traceback.format_exc()}"
            )
            await asyncio.sleep(5)


async def ChatbotTask():
    for userbot in nlx._ubot:
        try:
            userbot_ids.add(userbot.me.id)
            asyncio.create_task(chatbot_task_loop(userbot))
        except Exception as e:
            print(f"Error starting Chatbot for {userbot.me.first_name}: {e}\n{traceback.format_exc()}")
