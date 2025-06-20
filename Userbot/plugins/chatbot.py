import random
import traceback
import asyncio
import logging

from pyrogram import enums, errors
from config import bot_id, botcax_api, the_cegers
from Userbot.helper.database import dB, state
from Userbot.helper.tools import ky, fetch
from Userbot import nlx

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RANDOM_EMOJIS = [
    "😀", "😂", "😍", "😎", "😢", "😡", "👍", "👎",
    "🙏", "👏", "❤️", "🗿", "😭", "🔥"
]
userbot_ids = set()

async def get_chat_history(client, chat_id, user_id):
    try:
        key = f"chat_history_{chat_id}_{user_id}"
        return state.get(client, key) or []
    except Exception as e:
        logger.error(f"Error getting chat history: {e}")
        return []

async def add_to_chat_history(client, chat_id, user_id, role, message):
    try:
        key = f"chat_history_{chat_id}_{user_id}"
        history = await get_chat_history(client, chat_id, user_id)
        history.append({"role": role, "content": message})
        state.set(client, key, history[-500:])
    except Exception as e:
        logger.error(f"Error adding to chat history: {e}")

async def gen_text(client, message):
    try:
        text = message.text or message.caption
        if not text:
            return None
            
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
        res = await fetch.post("https://api.botcahx.eu.org/api/search/openai-custom", json=payload, timeout=30)

        if res.status_code == 200:
            result = res.json().get("result")
            if result:
                await add_to_chat_history(client.me.id, chat_id, user_id, "user", text)
                await add_to_chat_history(client.me.id, chat_id, user_id, "assistant", result)
                return result
        else:
            logger.error(f"API request failed with status: {res.status_code}")
            
    except Exception as e:
        logger.error(f"Error in gen_text: {e}")
        
    return None

@ky.ubot("chatbot")
async def chatbot_cmd(client, message, _):
    try:
        cmd = message.command
        logger.info(f"Chatbot command received: {cmd}")
        
        if len(cmd) < 2:
            response_text = f"<b>Usage: <code>{cmd[0]} on|off|status|role</code></b>\n\n" \
                           f"<b>Commands:</b>\n" \
                           f"• <code>{cmd[0]} on</code> - Enable chatbot\n" \
                           f"• <code>{cmd[0]} off</code> - Disable chatbot\n" \
                           f"• <code>{cmd[0]} status</code> - Check status\n" \
                           f"• <code>{cmd[0]} role</code> - Set role (reply to message)"
            return await message.reply(response_text)

        action = cmd[1].lower()
        chat_id = message.chat.id
        bot_var_key = "CHATBOT"

        if action == "on":
            # Check if already enabled
            current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if chat_id in current_chats:
                return await message.reply("<b>❗ Chatbot sudah aktif di grup ini!</b>")
            
            # Add to database
            dB.add_to_var(client.me.id, bot_var_key, chat_id)
            
            # Verify it was added
            updated_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if chat_id in updated_chats:
                chat_title = message.chat.title or "Private Chat"
                response_text = f"<b>✅ Chatbot berhasil diaktifkan!</b>\n" \
                               f"<b>Grup:</b> {chat_title}\n" \
                               f"<b>ID:</b> <code>{chat_id}</code>"
                logger.info(f"Chatbot enabled for chat {chat_id}")
            else:
                response_text = "<b>❌ Gagal mengaktifkan chatbot. Coba lagi.</b>"
                logger.error(f"Failed to enable chatbot for chat {chat_id}")
                
            return await message.reply(response_text)

        elif action == "off":
            if len(cmd) >= 3 and cmd[2] == "all":
                current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                for cid in current_chats:
                    dB.remove_from_var(client.me.id, bot_var_key, cid)
                return await message.reply(f"<b>✅ Chatbot dimatikan dari {len(current_chats)} grup.</b>")

            try:
                target_chat_id = int(cmd[2]) if len(cmd) >= 3 else chat_id
            except ValueError:
                return await message.reply(f"<b>❌ Chat ID tidak valid: <code>{cmd[2]}</code></b>")

            current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if target_chat_id not in current_chats:
                return await message.reply(f"<b>❗ Chatbot tidak aktif di chat ID <code>{target_chat_id}</code></b>")

            dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
            try:
                chat_info = await client.get_chat(target_chat_id)
                name = chat_info.title or "Private Chat"
            except:
                name = f"Chat ID: {target_chat_id}"
            return await message.reply(f"<b>✅ Chatbot dimatikan untuk: {name}</b>")

        elif action == "status":
            chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if not chats:
                return await message.reply("<b>❗ Tidak ada grup yang mengaktifkan chatbot.</b>")
            
            msg_lines = [f"<b>📊 Status Chatbot ({len(chats)} grup aktif):</b>\n"]
            for i, cid in enumerate(chats):
                try:
                    chat_info = await client.get_chat(cid)
                    chat_name = chat_info.title or "Private Chat"
                    msg_lines.append(f"{i+1}. <b>{chat_name}</b> | <code>{cid}</code>")
                except Exception as e:
                    msg_lines.append(f"{i+1}. <b>Unknown Chat</b> | <code>{cid}</code> (Error: {str(e)[:50]})")
            
            return await message.reply("\n".join(msg_lines))

        elif action == "role":
            if not message.reply_to_message:
                current_role = dB.get_var(client.me.id, "ROLE_CHATBOT")
                if current_role:
                    response_text = f"<b>🎭 Role saat ini:</b>\n<code>{current_role}</code>\n\n" \
                                   f"<b>Untuk mengubah role, reply pesan yang berisi role baru.</b>"
                else:
                    response_text = "<b>❗ Reply ke pesan yang berisi role untuk chatbot.</b>"
                return await message.reply(response_text)
                
            role = message.reply_to_message.text or message.reply_to_message.caption
            if not role:
                return await message.reply("<b>❌ Pesan yang di-reply tidak berisi teks.</b>")
                
            dB.set_var(client.me.id, "ROLE_CHATBOT", role)
            return await message.reply(f"<b>✅ Role chatbot berhasil diatur:</b>\n<code>{role}</code>")

        else:
            return await message.reply(f"<b>❌ Aksi tidak valid: <code>{action}</code></b>\n" \
                                     f"Gunakan: on, off, status, atau role")

    except Exception as e:
        logger.error(f"Error in chatbot_cmd: {e}\n{traceback.format_exc()}")
        return await message.reply(f"<b>❌ Terjadi kesalahan: {str(e)}</b>")

async def chatbot_trigger(client, message):
    try:
        # Check if chatbot is enabled for this chat
        enabled_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
        if message.chat.id not in enabled_chats:
            return

        # Skip if message is from userbot or admin
        if message.from_user.id in userbot_ids or message.from_user.id in the_cegers:
            return

        # Skip if no text content
        if not (message.text or message.caption):
            return

        # Send typing action
        try:
            await client.send_chat_action(
                chat_id=message.chat.id, action=enums.ChatAction.TYPING
            )
        except errors.ChatWriteForbidden:
            logger.warning(f"Cannot send typing action in chat {message.chat.id}")

        # Generate response
        data = await gen_text(client, message)
        
        if data:
            # Send reaction
            emoji = random.choice(RANDOM_EMOJIS)
            try:
                await client.send_reaction(
                    chat_id=message.chat.id, message_id=message.id, emoji=emoji
                )
            except (errors.ReactionInvalid, errors.FloodWait) as e:
                logger.warning(f"Cannot send reaction: {e}")

            # Send reply
            await message.reply(data)
            logger.info(f"Chatbot responded in chat {message.chat.id}")

        # Cancel typing action
        try:
            await client.send_chat_action(
                chat_id=message.chat.id, action=enums.ChatAction.CANCEL
            )
        except errors.ChatWriteForbidden:
            pass

    except Exception as e:
        logger.error(f"Error in chatbot_trigger: {e}\n{traceback.format_exc()}")

async def chatbot_task_loop(client):
    """Background task loop - currently disabled as it may cause spam"""
    return  # Disabled for now
    
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
            logger.error(f"Error in Chatbot task for {client.me.first_name}: {e}\n{traceback.format_exc()}")
            await asyncio.sleep(5)

async def ChatbotTask():
    """Initialize chatbot for all userbots"""
    try:
        for userbot in nlx._ubot:
            try:
                userbot_ids.add(userbot.me.id)
                logger.info(f"Chatbot initialized for {userbot.me.first_name}")
                # Commented out task loop as it may cause issues
                # asyncio.create_task(chatbot_task_loop(userbot))
            except Exception as e:
                logger.error(f"Error starting Chatbot for {userbot.me.first_name}: {e}\n{traceback.format_exc()}")
    except Exception as e:
        logger.error(f"Error in ChatbotTask: {e}\n{traceback.format_exc()}")

# Make sure the chatbot trigger is properly registered
# You may need to add this to your message handler
async def handle_message(client, message):
    """Message handler that should be called for all incoming messages"""
    await chatbot_trigger(client, message)
