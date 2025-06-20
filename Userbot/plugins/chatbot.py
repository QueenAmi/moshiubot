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
processed_messages = set()  # Track processed messages to avoid duplicates

async def get_chat_history(client, chat_id, user_id):
    key = f"chat_history_{chat_id}_{user_id}"
    return state.get(client, key) or []

async def add_to_chat_history(client, chat_id, user_id, role, message):
    key = f"chat_history_{chat_id}_{user_id}"
    history = await get_chat_history(client, chat_id, user_id)
    history.append({"role": role, "content": message})
    # Keep only last 500 messages to avoid memory issues
    state.set(client, key, history[-500:])

async def gen_text(client, message):
    text = message.text or message.caption
    if not text:  # Skip if no text content
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

    try:
        payload = {"message": messages, "apikey": botcax_api}
        res = await fetch.post("https://api.botcahx.eu.org/api/search/openai-custom", json=payload)

        if res.status_code == 200:
            result = res.json().get("result")
            if result:  # Only add to history if we got a valid result
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
        try:
            name = (await client.get_chat(target_chat_id)).title
        except:
            name = f"Chat {target_chat_id}"
        return await message.reply(f"<b>Chatbot turned off for: {name}</b>")

    elif action == "status":
        chats = dB.get_list_from_var(client.me.id, bot_var_key)
        if not chats:
            return await message.reply("<b>No groups have chatbot enabled.</b>")
        
        msg_parts = []
        for i, cid in enumerate(chats):
            try:
                chat_info = await client.get_chat(cid)
                msg_parts.append(f"<b>{i+1}. {chat_info.title} | `{cid}`</b>")
            except:
                msg_parts.append(f"<b>{i+1}. Unknown Chat | `{cid}`</b>")
        
        return await message.reply("\n".join(msg_parts))

    elif action == "role":
        if not message.reply_to_message:
            return await message.reply(f"<b>Reply to a message to set chatbot role.</b>")
        role = message.reply_to_message.text or message.reply_to_message.caption
        if not role:
            return await message.reply(f"<b>No text found in replied message.</b>")
        dB.set_var(client.me.id, "ROLE_CHATBOT", role)
        return await message.reply(f"<b>Chatbot role set to:</b> `{role[:100]}...`" if len(role) > 100 else f"<b>Chatbot role set to:</b> `{role}`")

    else:
        return await message.reply(f"<b>Invalid action: `{action}`</b>")

async def chatbot_trigger(client, message):
    # Check if chatbot is enabled for this chat
    if message.chat.id not in dB.get_list_from_var(client.me.id, "CHATBOT"):
        return
    
    # Skip if message is from userbot or special users
    if message.from_user.id in userbot_ids or message.from_user.id in the_cegers:
        return
    
    # Skip if no text content
    if not (message.text or message.caption):
        return
    
    # Create unique message identifier to avoid processing duplicates
    msg_id = f"{message.chat.id}_{message.id}"
    if msg_id in processed_messages:
        return
    processed_messages.add(msg_id)
    
    # Clean up old processed messages (keep last 1000)
    if len(processed_messages) > 1000:
        processed_messages.clear()
    
    try:
        # Send typing action
        await client.send_chat_action(
            chat_id=message.chat.id, action=enums.ChatAction.TYPING
        )
    except (errors.ChatWriteForbidden, errors.ChatAdminRequired):
        pass
    except Exception as e:
        print(f"Error sending typing action: {e}")
    
    # Generate response
    data = await gen_text(client, message)
    
    if data:
        try:
            # Send random emoji reaction
            emoji = random.choice(RANDOM_EMOJIS)
            await client.send_reaction(
                chat_id=message.chat.id, message_id=message.id, emoji=emoji
            )
        except (errors.ReactionInvalid, errors.FloodWait, errors.ChatWriteForbidden):
            pass
        except Exception as e:
            print(f"Error sending reaction: {e}")
        
        try:
            # Send the response
            await message.reply(data)
        except Exception as e:
            print(f"Error sending reply: {e}")
    
    try:
        # Cancel typing action
        await client.send_chat_action(
            chat_id=message.chat.id, action=enums.ChatAction.CANCEL
        )
    except (errors.ChatWriteForbidden, errors.ChatAdminRequired):
        pass
    except Exception as e:
        print(f"Error canceling typing action: {e}")

# Remove the problematic task loop - this should be handled by message handlers instead
# The original chatbot_task_loop was causing infinite loops and unnecessary API calls

async def ChatbotTask():
    """Initialize chatbot for all userbots"""
    for userbot in nlx._ubot:
        try:
            userbot_ids.add(userbot.me.id)
            print(f"Chatbot initialized for {userbot.me.first_name}")
        except Exception as e:
            print(f"Error initializing Chatbot for userbot: {e}\n{traceback.format_exc()}")

# Note: The chatbot_trigger function should be called from your message handler
# Example integration in your main message handler:
# 
# @ky.on_message(filters.group & ~filters.bot)
# async def handle_group_messages(client, message):
#     await chatbot_trigger(client, message)
