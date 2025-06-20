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
        print(f"Error in gen_text: {e}")
    return None

@ky.ubot("chatbot")
async def chatbot_cmd(client, message, _):
    """Handle chatbot commands"""
    cmd = message.command
    if len(cmd) < 2:
        return await message.reply(
            f"<b>Usage: <code>{cmd[0]} on|off|status|role</code></b>"
        )

    action = cmd[1].lower()
    chat_id = message.chat.id
    bot_var_key = "CHATBOT"

    if action == "on":
        current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
        if chat_id not in current_chats:
            dB.add_to_var(client.me.id, bot_var_key, chat_id)
            return await message.reply("<b>✅ Chatbot berhasil diaktifkan.</b>")
        else:
            return await message.reply("<b>⚠️ Chatbot sudah aktif di grup ini.</b>")

    elif action == "off":
        if len(cmd) >= 3 and cmd[2] == "all":
            chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
            for cid in chats:
                dB.remove_from_var(client.me.id, bot_var_key, cid)
            return await message.reply("<b>🗑️ Semua chatbot group berhasil dihapus.</b>")

        try:
            target_chat_id = int(cmd[2]) if len(cmd) >= 3 else chat_id
        except (ValueError, IndexError):
            target_chat_id = chat_id

        current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
        if target_chat_id not in current_chats:
            return await message.reply(f"<b>⚠️ Chatbot tidak aktif di chat ID: <code>{target_chat_id}</code></b>")

        dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
        try:
            chat_info = await client.get_chat(target_chat_id)
            name = chat_info.title or "Unknown"
        except:
            name = f"Chat ID: {target_chat_id}"
        
        return await message.reply(f"<b>❌ Chatbot dimatikan untuk: {name}</b>")

    elif action == "status":
        chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
        if not chats:
            return await message.reply("<b>📝 Tidak ada grup yang mengaktifkan chatbot.</b>")
        
        msg_lines = ["<b>📋 Status Chatbot:</b>\n"]
        for i, cid in enumerate(chats, 1):
            try:
                chat_info = await client.get_chat(cid)
                name = chat_info.title or "Unknown"
                msg_lines.append(f"<b>{i}. {name}</b> | <code>{cid}</code>")
            except:
                msg_lines.append(f"<b>{i}. Unknown Chat</b> | <code>{cid}</code>")
        
        return await message.reply("\n".join(msg_lines))

    elif action == "role":
        if not message.reply_to_message:
            current_role = dB.get_var(client.me.id, "ROLE_CHATBOT")
            if current_role:
                return await message.reply(f"<b>🎭 Role saat ini:</b>\n<code>{current_role}</code>\n\n<b>Untuk mengubah, reply pesan yang berisi role baru.</b>")
            else:
                return await message.reply(f"<b>📝 Reply ke pesan yang berisi role chatbot untuk mengatur role.</b>")
        
        role = message.reply_to_message.text or message.reply_to_message.caption
        if not role:
            return await message.reply("<b>⚠️ Pesan yang di-reply tidak berisi teks.</b>")
            
        dB.set_var(client.me.id, "ROLE_CHATBOT", role)
        return await message.reply(f"<b>✅ Role chatbot berhasil diatur:</b>\n<code>{role[:200]}...</code>" if len(role) > 200 else f"<b>✅ Role chatbot berhasil diatur:</b>\n<code>{role}</code>")

    else:
        return await message.reply(f"<b>❌ Aksi tidak valid: <code>{action}</code></b>\n<b>Gunakan: on, off, status, atau role</b>")

# Event handler untuk menangani pesan masuk
async def setup_chatbot_handlers(client):
    """Setup message handlers untuk chatbot"""
    
    @client.on_message(filters.group & ~filters.bot & ~filters.via_bot)
    async def handle_group_message(client, message):
        """Handle incoming group messages"""
        try:
            # Skip jika tidak ada teks
            if not (message.text or message.caption):
                return
                
            # Skip jika dari userbot atau user tertentu
            if (message.from_user.id in userbot_ids or 
                message.from_user.id in the_cegers or
                message.from_user.id == client.me.id):
                return
            
            # Skip jika chatbot tidak aktif di grup ini
            active_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
            if message.chat.id not in active_chats:
                return
            
            # Skip jika pesan adalah command
            text = message.text or message.caption
            if text.startswith(('.', '/', '!', '-')):
                return
                
            await chatbot_trigger(client, message)
            
        except Exception as e:
            print(f"Error in message handler: {e}")

async def chatbot_trigger(client, message):
    """Process message dengan chatbot"""
    try:
        # Show typing indicator
        try:
            await client.send_chat_action(
                chat_id=message.chat.id, 
                action=enums.ChatAction.TYPING
            )
        except (errors.ChatWriteForbidden, errors.PeerFlood):
            pass
        
        # Generate response
        data = await gen_text(client, message)
        
        if data:
            # Add random reaction
            emoji = random.choice(RANDOM_EMOJIS)
            try:
                await client.send_reaction(
                    chat_id=message.chat.id, 
                    message_id=message.id, 
                    emoji=emoji
                )
            except (errors.ReactionInvalid, errors.FloodWait, Exception):
                pass
            
            # Send reply dengan delay untuk natural response
            await asyncio.sleep(random.uniform(1, 3))
            await message.reply(data)
        
        # Cancel typing
        try:
            await client.send_chat_action(
                chat_id=message.chat.id, 
                action=enums.ChatAction.CANCEL
            )
        except (errors.ChatWriteForbidden, Exception):
            pass
            
    except Exception as e:
        print(f"Error in chatbot_trigger: {e}")

async def ChatbotTask():
    """Initialize chatbot untuk semua userbot"""
    for userbot in nlx._ubot:
        try:
            # Add userbot ID ke set
            userbot_ids.add(userbot.me.id)
            
            # Setup message handlers
            await setup_chatbot_handlers(userbot)
            
            print(f"✅ Chatbot initialized for {userbot.me.first_name}")
            
        except Exception as e:
            print(f"❌ Error starting Chatbot for {userbot.me.first_name}: {e}")
            print(traceback.format_exc())

# Fungsi untuk restart chatbot jika diperlukan
async def restart_chatbot():
    """Restart chatbot handlers"""
    try:
        await ChatbotTask()
        print("🔄 Chatbot handlers restarted successfully")
    except Exception as e:
        print(f"❌ Error restarting chatbot: {e}")
