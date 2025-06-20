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
        state.set(client, key, history[-500:])  # Keep last 500 messages
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
        res = await fetch.post("https://api.botcahx.eu.org/api/search/openai-custom", json=payload)

        if res.status_code == 200:
            result = res.json().get("result")
            if result:
                await add_to_chat_history(client.me.id, chat_id, user_id, "user", text)
                await add_to_chat_history(client.me.id, chat_id, user_id, "assistant", result)
                return result
        else:
            logger.error(f"API request failed with status {res.status_code}")
        return None
    except Exception as e:
        logger.error(f"Error in gen_text: {e}")
        return None

@ky.ubot("chatbot")
async def chatbot_cmd(client, message, _):
    try:
        cmd = message.command
        if len(cmd) < 2:
            return await message.reply(
                f"<b>Usage: <code>{cmd[0]} on|off|status|role</code></b>\n"
                f"<b>• <code>{cmd[0]} on</code> - Turn on chatbot</b>\n"
                f"<b>• <code>{cmd[0]} off [chat_id|all]</code> - Turn off chatbot</b>\n"
                f"<b>• <code>{cmd[0]} status</code> - Check chatbot status</b>\n"
                f"<b>• <code>{cmd[0]} role</code> - Set chatbot role (reply to message)</b>"
            )

        action = cmd[1].lower()
        chat_id = message.chat.id
        bot_var_key = "CHATBOT"

        if action == "on":
            # Get current list and add chat_id if not already present
            current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if chat_id not in current_chats:
                dB.add_to_var(client.me.id, bot_var_key, chat_id)
                logger.info(f"Chatbot enabled for chat {chat_id}")
                return await message.reply("<b>✅ Chatbot turned on for this chat.</b>")
            else:
                return await message.reply("<b>⚠️ Chatbot is already enabled for this chat.</b>")

        elif action == "off":
            if len(cmd) >= 3 and cmd[2].lower() == "all":
                current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                for cid in current_chats:
                    dB.remove_from_var(client.me.id, bot_var_key, cid)
                logger.info("All chatbot entries removed")
                return await message.reply("<b>✅ Chatbot turned off for all chats.</b>")

            try:
                target_chat_id = int(cmd[2]) if len(cmd) >= 3 else chat_id
            except (ValueError, IndexError):
                target_chat_id = chat_id

            current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if target_chat_id not in current_chats:
                return await message.reply(f"<b>⚠️ Chatbot is not enabled for chat ID <code>{target_chat_id}</code></b>")

            dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
            try:
                chat_info = await client.get_chat(target_chat_id)
                name = chat_info.title or "Unknown Chat"
            except:
                name = f"Chat ID {target_chat_id}"
            
            logger.info(f"Chatbot disabled for chat {target_chat_id}")
            return await message.reply(f"<b>✅ Chatbot turned off for: {name}</b>")

        elif action == "status":
            chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            if not chats:
                return await message.reply("<b>📊 No chats have chatbot enabled.</b>")
            
            msg_lines = ["<b>📊 Chatbot Status:</b>\n"]
            for i, cid in enumerate(chats):
                try:
                    chat_info = await client.get_chat(cid)
                    name = chat_info.title or "Unknown Chat"
                except:
                    name = "Unknown Chat"
                msg_lines.append(f"<b>{i+1}. {name}</b> | <code>{cid}</code>")
            
            return await message.reply("\n".join(msg_lines))

        elif action == "role":
            if not message.reply_to_message:
                current_role = dB.get_var(client.me.id, "ROLE_CHATBOT")
                if current_role:
                    return await message.reply(f"<b>🤖 Current chatbot role:</b>\n<code>{current_role}</code>\n\n<b>Reply to a message to set new role.</b>")
                else:
                    return await message.reply(f"<b>🤖 Reply to a message to set chatbot role.</b>")
            
            role = message.reply_to_message.text or message.reply_to_message.caption
            if not role:
                return await message.reply("<b>⚠️ No text found in the replied message.</b>")
            
            dB.set_var(client.me.id, "ROLE_CHATBOT", role)
            logger.info("Chatbot role updated")
            return await message.reply(f"<b>✅ Chatbot role updated:</b>\n<code>{role[:200]}{'...' if len(role) > 200 else ''}</code>")

        else:
            return await message.reply(f"<b>❌ Invalid action: <code>{action}</code></b>")
            
    except Exception as e:
        logger.error(f"Error in chatbot_cmd: {e}")
        await message.reply(f"<b>❌ Error: {str(e)}</b>")

async def chatbot_trigger(client, message):
    try:
        # Check if message is valid
        if not message or not message.from_user:
            return
            
        # Check if chatbot is enabled for this chat
        enabled_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
        if message.chat.id not in enabled_chats:
            return
            
        # Skip if message is from userbot or special users
        if message.from_user.id in userbot_ids or message.from_user.id in the_cegers:
            return
            
        # Skip if no text content
        if not (message.text or message.caption):
            return
            
        # Skip if message is a command
        if message.text and message.text.startswith('/'):
            return

        try:
            await client.send_chat_action(
                chat_id=message.chat.id, action=enums.ChatAction.TYPING
            )
        except (errors.ChatWriteForbidden, errors.UserBannedInChannel):
            logger.warning(f"Cannot send typing action in chat {message.chat.id}")
            return
        except Exception as e:
            logger.error(f"Error sending typing action: {e}")

        data = await gen_text(client, message)
        
        if data:
            try:
                # Send reaction first
                emoji = random.choice(RANDOM_EMOJIS)
                await client.send_reaction(
                    chat_id=message.chat.id, 
                    message_id=message.id, 
                    emoji=emoji
                )
            except (errors.ReactionInvalid, errors.FloodWait) as e:
                logger.warning(f"Cannot send reaction: {e}")
            except Exception as e:
                logger.error(f"Error sending reaction: {e}")
            
            # Send reply
            try:
                await message.reply(data)
                logger.info(f"Chatbot replied in chat {message.chat.id}")
            except Exception as e:
                logger.error(f"Error sending reply: {e}")

        try:
            await client.send_chat_action(
                chat_id=message.chat.id, action=enums.ChatAction.CANCEL
            )
        except Exception:
            pass
            
    except Exception as e:
        logger.error(f"Error in chatbot_trigger: {e}")

# Remove the task loop as it's not needed and can cause issues
# Instead, rely on message handlers

async def setup_chatbot():
    """Initialize chatbot for all userbots"""
    try:
        for userbot in nlx._ubot:
            try:
                if hasattr(userbot, 'me') and userbot.me:
                    userbot_ids.add(userbot.me.id)
                    logger.info(f"Chatbot setup completed for {userbot.me.first_name}")
            except Exception as e:
                logger.error(f"Error setting up chatbot for userbot: {e}")
    except Exception as e:
        logger.error(f"Error in setup_chatbot: {e}")

# Call this function when your bot starts
# asyncio.create_task(setup_chatbot())
