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
chatbot_tasks = {}  # Store running tasks for each userbot
processed_messages = {}  # Track processed messages per userbot

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
        "balasan kamu harus super minimal maksimal 1-3 kata saja. "
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
            f"<b>Usage: `{cmd[0]} on|off|status|role|stop|start`</b>"
        )

    action = cmd[1]
    chat_id = message.chat.id
    bot_var_key = "CHATBOT"

    if action == "on":
        dB.add_to_var(client.me.id, bot_var_key, chat_id)
        # Auto start task if not running
        if client.me.id not in chatbot_tasks:
            task = asyncio.create_task(chatbot_task_loop(client))
            chatbot_tasks[client.me.id] = task
            processed_messages[client.me.id] = set()
        return await message.reply("<b>Chatbot turned on.</b>")

    elif action == "off":
        if len(cmd) >= 3 and cmd[2] == "all":
            for cid in dB.get_list_from_var(client.me.id, bot_var_key):
                dB.remove_from_var(client.me.id, bot_var_key, cid)
            # Stop task if no chats enabled
            if client.me.id in chatbot_tasks:
                chatbot_tasks[client.me.id].cancel()
                del chatbot_tasks[client.me.id]
                if client.me.id in processed_messages:
                    del processed_messages[client.me.id]
            return await message.reply("<b>All chatbot group entries removed and task stopped.</b>")

        try:
            target_chat_id = int(cmd[2]) if len(cmd) >= 3 else chat_id
        except ValueError:
            return await message.reply(f"<b>Invalid chat ID: `{cmd[2]}`</b>")

        if target_chat_id not in dB.get_list_from_var(client.me.id, bot_var_key):
            return await message.reply(f"<b>Chat ID `{target_chat_id}` not found.</b>")

        dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
        name = (await client.get_chat(target_chat_id)).title
        
        # Check if no more chats enabled, stop task
        remaining_chats = dB.get_list_from_var(client.me.id, bot_var_key)
        if not remaining_chats and client.me.id in chatbot_tasks:
            chatbot_tasks[client.me.id].cancel()
            del chatbot_tasks[client.me.id]
            if client.me.id in processed_messages:
                del processed_messages[client.me.id]
            return await message.reply(f"<b>Chatbot turned off for: {name} and task stopped (no active chats).</b>")
        
        return await message.reply(f"<b>Chatbot turned off for: {name}</b>")

    elif action == "stop":
        # Force stop the chatbot task
        if client.me.id in chatbot_tasks:
            chatbot_tasks[client.me.id].cancel()
            del chatbot_tasks[client.me.id]
            if client.me.id in processed_messages:
                del processed_messages[client.me.id]
            return await message.reply("<b>Chatbot task force stopped.</b>")
        else:
            return await message.reply("<b>No chatbot task running.</b>")

    elif action == "start":
        # Manually start the chatbot task
        if client.me.id in chatbot_tasks:
            return await message.reply("<b>Chatbot task already running.</b>")
        
        chats = dB.get_list_from_var(client.me.id, bot_var_key)
        if not chats:
            return await message.reply("<b>No groups have chatbot enabled. Use 'chatbot on' first.</b>")
            
        task = asyncio.create_task(chatbot_task_loop(client))
        chatbot_tasks[client.me.id] = task
        processed_messages[client.me.id] = set()
        return await message.reply("<b>Chatbot task started.</b>")

    elif action == "status":
        chats = dB.get_list_from_var(client.me.id, bot_var_key)
        task_status = "🟢 Running" if client.me.id in chatbot_tasks else "🔴 Stopped"
        
        if not chats:
            return await message.reply(f"<b>No groups have chatbot enabled.\nTask Status: {task_status}</b>")
        
        msg = f"<b>Task Status: {task_status}</b>\n"
        msg += f"<b>Active Chats: {len(chats)}</b>\n\n"
        msg += "\n".join([
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
    
    # Check if message was already processed
    user_id = client.me.id
    msg_id = f"{message.chat.id}_{message.id}"
    
    if user_id in processed_messages and msg_id in processed_messages[user_id]:
        return
        
    # Add to processed messages
    if user_id not in processed_messages:
        processed_messages[user_id] = set()
    processed_messages[user_id].add(msg_id)
    
    # Limit processed messages size
    if len(processed_messages[user_id]) > 5000:
        # Keep only the last 2500 messages
        processed_list = list(processed_messages[user_id])
        processed_messages[user_id] = set(processed_list[-2500:])
    
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
    user_id = client.me.id
    last_message_ids = {}  # Track last processed message ID per chat
    
    while True:
        try:
            chats = dB.get_list_from_var(user_id, "CHATBOT") or []
            
            if not chats:
                await asyncio.sleep(10)
                continue
            
            for chat_id in chats:
                try:
                    # Get recent messages
                    messages_to_process = []
                    async for msg in client.get_chat_history(chat_id, limit=3):
                        # Skip if this is an old message we've seen before
                        if chat_id in last_message_ids:
                            if msg.id <= last_message_ids[chat_id]:
                                break
                        messages_to_process.append(msg)
                    
                    # Process new messages (reverse order - oldest first)
                    for msg in reversed(messages_to_process):
                        # Skip very old messages (older than 10 minutes)
                        if msg.date and (asyncio.get_event_loop().time() - msg.date.timestamp()) > 600:
                            continue
                            
                        await chatbot_trigger(client, msg)
                        last_message_ids[chat_id] = max(last_message_ids.get(chat_id, 0), msg.id)
                        await asyncio.sleep(3)  # Delay between message processing
                        
                except Exception as chat_error:
                    print(f"Error processing chat {chat_id} for {client.me.first_name}: {chat_error}")
                    continue
                    
            await asyncio.sleep(5)  # Main loop delay
            
        except asyncio.CancelledError:
            print(f"Chatbot task cancelled for {client.me.first_name}")
            break
        except errors.FloodWait as e:
            print(f"FloodWait for {client.me.first_name}: {e.value} seconds")
            await asyncio.sleep(e.value)
        except Exception as e:
            print(f"Error in Chatbot task for {client.me.first_name}: {e}\n{traceback.format_exc()}")
            await asyncio.sleep(10)

async def ChatbotTask():
    for userbot in nlx._ubot:
        try:
            userbot_ids.add(userbot.me.id)
            
            # Check if chatbot is enabled for any chats
            chats = dB.get_list_from_var(userbot.me.id, "CHATBOT") or []
            if chats:
                # Cancel existing task if running
                if userbot.me.id in chatbot_tasks:
                    chatbot_tasks[userbot.me.id].cancel()
                
                # Create new task
                task = asyncio.create_task(chatbot_task_loop(userbot))
                chatbot_tasks[userbot.me.id] = task
                processed_messages[userbot.me.id] = set()
                print(f"Chatbot task started for {userbot.me.first_name}")
            
        except Exception as e:
            print(f"Error starting Chatbot for {userbot.me.first_name}: {e}\n{traceback.format_exc()}")

async def stop_all_chatbot_tasks():
    """Function to stop all chatbot tasks"""
    for user_id, task in list(chatbot_tasks.items()):
        task.cancel()
        del chatbot_tasks[user_id]
        if user_id in processed_messages:
            del processed_messages[user_id]
    print("All chatbot tasks stopped")

# Add this function to be called on shutdown
async def cleanup_chatbot():
    """Cleanup function to be called when shutting down"""
    await stop_all_chatbot_tasks()
