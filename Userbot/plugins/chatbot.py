import random
import traceback
import asyncio

from pyrogram import enums, errors, filters
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
    
    try:
        res = await fetch.post("https://api.botcahx.eu.org/api/search/openai-custom", json=payload)
        if res.status_code == 200:
            result = res.json().get("result")
            await add_to_chat_history(client.me.id, chat_id, user_id, "user", text)
            await add_to_chat_history(client.me.id, chat_id, user_id, "assistant", result)
            return result
    except Exception as e:
        print(f"Error generating text: {e}")
    
    return None

@ky.ubot("chatbot")
async def chatbot_cmd(client, message, _):
    cmd = message.command
    if len(cmd) < 2:
        return await message.reply(
            f"<b>Usage: `{cmd[0]} on|off|status|role`</b>"
        )

    action = cmd[1].lower()
    chat_id = message.chat.id
    bot_var_key = "CHATBOT"

    if action == "on":
        current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
        if chat_id in current_chats:
            return await message.reply("<b>Chatbot sudah aktif di grup ini.</b>")
        
        dB.add_to_var(client.me.id, bot_var_key, chat_id)
        chat_name = message.chat.title or "Private Chat"
        return await message.reply(f"<b>Chatbot berhasil diaktifkan di: {chat_name}</b>")

    elif action == "off":
        if len(cmd) >= 3 and cmd[2].lower() == "all":
            current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if not current_chats:
                return await message.reply("<b>Tidak ada grup dengan chatbot aktif.</b>")
            
            # Clear all chatbot entries
            dB.set_var(client.me.id, bot_var_key, [])
            return await message.reply(f"<b>Chatbot dimatikan dari {len(current_chats)} grup.</b>")

        try:
            target_chat_id = int(cmd[2]) if len(cmd) >= 3 else chat_id
        except (ValueError, IndexError):
            target_chat_id = chat_id

        current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
        if target_chat_id not in current_chats:
            return await message.reply(f"<b>Chatbot tidak aktif di chat ID: `{target_chat_id}`</b>")

        dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
        
        try:
            chat_info = await client.get_chat(target_chat_id)
            chat_name = chat_info.title or "Private Chat"
        except:
            chat_name = f"Chat ID: {target_chat_id}"
            
        return await message.reply(f"<b>Chatbot berhasil dimatikan untuk: {chat_name}</b>")

    elif action == "status":
        chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
        if not chats:
            return await message.reply("<b>Tidak ada grup dengan chatbot aktif.</b>")
        
        status_msg = [f"<b>📋 Status Chatbot ({len(chats)} grup aktif):</b>\n"]
        
        for i, cid in enumerate(chats, 1):
            try:
                chat_info = await client.get_chat(cid)
                chat_name = chat_info.title or "Private Chat"
                status_msg.append(f"{i}. <b>{chat_name}</b> | <code>{cid}</code>")
            except Exception:
                status_msg.append(f"{i}. <b>Unknown Chat</b> | <code>{cid}</code>")
        
        return await message.reply("\n".join(status_msg))

    elif action == "role":
        if not message.reply_to_message:
            current_role = dB.get_var(client.me.id, "ROLE_CHATBOT")
            if current_role:
                return await message.reply(f"<b>Current role:</b>\n<code>{current_role}</code>\n\n<b>Reply to a message to set new role.</b>")
            else:
                return await message.reply(f"<b>Reply to a message to set chatbot role.</b>")
        
        role = message.reply_to_message.text or message.reply_to_message.caption
        if not role:
            return await message.reply("<b>Reply message must contain text.</b>")
            
        dB.set_var(client.me.id, "ROLE_CHATBOT", role)
        return await message.reply(f"<b>✅ Chatbot role berhasil diset.</b>\n\n<code>{role[:100]}{'...' if len(role) > 100 else ''}</code>")

    else:
        return await message.reply(f"<b>❌ Invalid action: `{action}`</b>\n<b>Available: on, off, status, role</b>")

async def chatbot_trigger(client, message):
    # Skip if chatbot not enabled in this chat
    active_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
    if message.chat.id not in active_chats:
        return
    
    # Skip if message from userbot or admin
    if message.from_user.id in userbot_ids or message.from_user.id in the_cegers:
        return
    
    # Skip if message is a command
    if message.text and message.text.startswith(('/', '!', '.')):
        return
    
    # Skip if no text content
    if not (message.text or message.caption):
        return
    
    try:
        # Send typing action
        await client.send_chat_action(
            chat_id=message.chat.id, action=enums.ChatAction.TYPING
        )
    except errors.ChatWriteForbidden:
        pass
    except Exception:
        pass
    
    # Generate response
    data = await gen_text(client, message)
    
    if data:
        try:
            # Add random reaction
            emoji = random.choice(RANDOM_EMOJIS)
            await client.send_reaction(
                chat_id=message.chat.id, 
                message_id=message.id, 
                emoji=emoji
            )
        except (errors.ReactionInvalid, errors.FloodWait, Exception):
            pass
        
        try:
            # Send reply
            await message.reply(data)
        except Exception as e:
            print(f"Error sending chatbot reply: {e}")
    
    try:
        # Cancel typing action
        await client.send_chat_action(
            chat_id=message.chat.id, action=enums.ChatAction.CANCEL
        )
    except (errors.ChatWriteForbidden, Exception):
        pass

# Message handler for all text messages
@ky.ubot("", group=999)  # Low priority to run after other handlers
async def handle_chatbot_messages(client, message, _):
    """Handle incoming messages for chatbot trigger"""
    # Only process text/caption messages
    if message.text or message.caption:
        await chatbot_trigger(client, message)

async def initialize_userbot_ids():
    """Initialize userbot IDs from active userbots"""
    global userbot_ids
    userbot_ids.clear()
    
    for userbot in nlx._ubot:
        try:
            if userbot.me:
                userbot_ids.add(userbot.me.id)
        except Exception as e:
            print(f"Error adding userbot ID: {e}")

async def ChatbotTask():
    """Initialize chatbot system"""
    await initialize_userbot_ids()
    print(f"Chatbot system initialized with {len(userbot_ids)} userbots")
