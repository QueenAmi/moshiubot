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

# Initialize global variables properly
userbot_ids = set()
chatbot_active = {}  # This was missing in your code!

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
    try:
        cmd = message.command
        if len(cmd) < 2:
            return await message.reply(
                f"<b>Usage: <code>{cmd[0]} on|off|status|role|test|debug</code></b>\n\n"
                f"<b>Commands:</b>\n"
                f"• <code>on</code> - Aktifkan chatbot\n"
                f"• <code>off</code> - Matikan chatbot\n"
                f"• <code>status</code> - Lihat status\n"
                f"• <code>role</code> - Set/lihat role\n"
                f"• <code>test [text]</code> - Test response\n"
                f"• <code>debug</code> - Debug info"
            )

        action = cmd[1].lower()
        chat_id = message.chat.id
        bot_var_key = "CHATBOT"
        
        print(f"🔍 Processing chatbot command: {action} in chat {chat_id} by user {client.me.first_name}")

        if action == "on":
            try:
                current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                print(f"📋 Current active chats: {current_chats}")
                
                if chat_id not in current_chats:
                    dB.add_to_var(client.me.id, bot_var_key, chat_id)
                    
                    # Verify it was added
                    updated_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                    print(f"📋 Updated active chats: {updated_chats}")
                    
                    # Mark chatbot as active for this userbot
                    chatbot_active[client.me.id] = True
                    
                    return await message.reply("<b>✅ Chatbot berhasil diaktifkan.</b>")
                else:
                    return await message.reply("<b>⚠️ Chatbot sudah aktif di grup ini.</b>")
            except Exception as e:
                print(f"❌ Error in chatbot on: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "off":
            try:
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
                print(f"📋 Current chats before removal: {current_chats}")
                
                if target_chat_id not in current_chats:
                    return await message.reply(f"<b>⚠️ Chatbot tidak aktif di chat ID: <code>{target_chat_id}</code></b>")

                dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
                
                # Verify removal
                updated_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                print(f"📋 Updated chats after removal: {updated_chats}")
                
                try:
                    chat_info = await client.get_chat(target_chat_id)
                    name = chat_info.title or "Unknown"
                except:
                    name = f"Chat ID: {target_chat_id}"
                
                return await message.reply(f"<b>❌ Chatbot dimatikan untuk: {name}</b>")
            except Exception as e:
                print(f"❌ Error in chatbot off: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "status":
            try:
                chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                if not chats:
                    return await message.reply("<b>📝 Tidak ada grup yang mengaktifkan chatbot.</b>")
                
                # Get status lengkap
                status_info = []
                status_info.append("<b>📋 Status Chatbot:</b>\n")
                status_info.append(f"<b>🤖 Userbot:</b> {client.me.first_name}")
                status_info.append(f"<b>📊 Total Chat Aktif:</b> {len(chats)}")
                status_info.append(f"<b>🔄 Monitoring:</b> {'✅ Active' if client.me.id in chatbot_active else '❌ Inactive'}")
                status_info.append("")
                status_info.append("<b>📝 Daftar Chat Aktif:</b>")
                
                for i, cid in enumerate(chats, 1):
                    try:
                        chat_info = await client.get_chat(cid)
                        name = chat_info.title or "Unknown"
                        status_info.append(f"<b>{i}. {name}</b>")
                        status_info.append(f"   └ ID: <code>{cid}</code>")
                    except:
                        status_info.append(f"<b>{i}. Unknown Chat</b>")
                        status_info.append(f"   └ ID: <code>{cid}</code> (⚠️ Error)")
                
                return await message.reply("\n".join(status_info))
            except Exception as e:
                print(f"❌ Error in status: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "role":
            try:
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
            except Exception as e:
                print(f"❌ Error in role: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "test":
            try:
                # Test chatbot response
                test_text = " ".join(cmd[2:]) if len(cmd) > 2 else "hello"
                result = await test_chatbot_manual(client, message.chat.id, test_text)
                if result:
                    return await message.reply(f"<b>🧪 Test Response:</b>\n{result}")
                else:
                    return await message.reply("<b>❌ Test failed. Check API connection.</b>")
            except Exception as e:
                print(f"❌ Error in test: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "debug":
            try:
                # Debug info lengkap
                active_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
                current_role = dB.get_var(client.me.id, "ROLE_CHATBOT")
                
                # Check monitoring status
                monitoring_status = "✅ Active" if client.me.id in chatbot_active else "❌ Inactive"
                
                # Check API key
                api_status = "✅ Valid" if botcax_api else "❌ Missing"
                
                # Get total userbots
                total_ubot = len(nlx._ubot) if hasattr(nlx, '_ubot') else 0
                
                debug_info = f"""<b>🔍 Debug Info Chatbot:</b>

<b>📊 Status Umum:</b>
├ <b>Userbot ID:</b> <code>{client.me.id}</code>
├ <b>Userbot Name:</b> {client.me.first_name}
├ <b>Monitoring:</b> {monitoring_status}
├ <b>Total Userbot:</b> {total_ubot}
└ <b>API Key:</b> {api_status}

<b>⚙️ Konfigurasi:</b>
├ <b>Chat Aktif:</b> {len(active_chats)} chat
├ <b>Current Chat ID:</b> <code>{message.chat.id}</code>
├ <b>Chat Ini Aktif:</b> {'✅' if message.chat.id in active_chats else '❌'}
└ <b>Role Custom:</b> {'✅' if current_role else '❌ (Default)'}

<b>🧠 Memory:</b>
├ <b>Userbot IDs:</b> {len(userbot_ids)} tracked
├ <b>Active Instances:</b> {len(chatbot_active)}
└ <b>State Keys:</b> {len(state._state.get(str(client.me.id), {}))} items

<b>🔧 Commands:</b>
├ <code>.chatbot test hello</code> - Test response
├ <code>.chatbot on</code> - Aktifkan di chat ini
└ <code>.chatbot status</code> - Lihat status lengkap"""

                return await message.reply(debug_info)
            except Exception as e:
                print(f"❌ Error in debug: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        else:
            return await message.reply(f"<b>❌ Aksi tidak valid: <code>{action}</code></b>\n<b>Gunakan: on, off, status, role, test, atau debug</b>")
            
    except Exception as e:
        print(f"❌ Critical error in chatbot_cmd: {e}")
        print(traceback.format_exc())
        return await message.reply(f"<b>❌ Critical Error: {str(e)}</b>")

# Rest of your code remains the same...
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

async def handle_group_message(client, message):
    """Handle incoming group messages for chatbot"""
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
        if text.startswith(('.', '/', '!', '-', '+')):
            return
            
        print(f"🤖 Processing message from {message.from_user.first_name} in {message.chat.title}")
        await chatbot_trigger(client, message)
        
    except Exception as e:
        print(f"❌ Error in message handler: {e}")
        print(traceback.format_exc())

# Monitoring loop untuk chatbot (lebih reliable)
async def chatbot_monitoring_loop(client):
    """Loop monitoring untuk memproses pesan dengan chatbot"""
    processed_messages = {}
    
    while True:
        try:
            active_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
            
            if not active_chats:
                await asyncio.sleep(5)
                continue
                
            for chat_id in active_chats:
                try:
                    # Get latest messages (last 3)
                    messages = []
                    async for msg in client.get_chat_history(chat_id, limit=3):
                        messages.append(msg)
                    
                    for message in reversed(messages):  # Process dari yang lama ke baru
                        # Create unique message identifier
                        msg_key = f"{chat_id}_{message.id}"
                        
                        # Skip jika sudah diproses
                        if msg_key in processed_messages:
                            continue
                            
                        # Skip jika pesan terlalu lama (lebih dari 5 menit)
                        import time
                        if message.date and (time.time() - message.date.timestamp()) > 300:
                            processed_messages[msg_key] = True
                            continue
                        
                        # Skip jika tidak ada teks
                        if not (message.text or message.caption):
                            processed_messages[msg_key] = True
                            continue
                            
                        # Skip jika dari userbot atau user tertentu
                        if (message.from_user.id in userbot_ids or 
                            message.from_user.id in the_cegers or
                            message.from_user.id == client.me.id):
                            processed_messages[msg_key] = True
                            continue
                        
                        # Skip jika pesan adalah command
                        text = message.text or message.caption
                        if text.startswith(('.', '/', '!', '-', '+')):
                            processed_messages[msg_key] = True
                            continue
                        
                        print(f"🤖 Processing message ID {message.id} from {message.from_user.first_name} in chat {chat_id}")
                        
                        # Process dengan chatbot
                        await chatbot_trigger(client, message)
                        
                        # Mark sebagai sudah diproses
                        processed_messages[msg_key] = True
                        
                        # Delay untuk menghindari spam
                        await asyncio.sleep(2)
                        break  # Process satu pesan per chat per loop
                        
                except Exception as e:
                    print(f"Error processing chat {chat_id}: {e}")
                    
                await asyncio.sleep(1)  # Delay antar chat
            
            # Cleanup old processed messages (keep only last 1000)
            if len(processed_messages) > 1000:
                # Keep only recent entries
                recent_keys = list(processed_messages.keys())[-500:]
                processed_messages = {k: v for k, v in processed_messages.items() if k in recent_keys}
                
        except Exception as e:
            print(f"❌ Error in monitoring loop for {client.me.first_name}: {e}")
            print(traceback.format_exc())
            
        await asyncio.sleep(3)  # Main loop delay

async def ChatbotTask():
    """Initialize chatbot untuk semua userbot"""
    try:
        print("🚀 Starting Chatbot Task...")
        
        for userbot in nlx._ubot:
            try:
                # Add userbot ID ke set
                userbot_ids.add(userbot.me.id)
                
                # Start monitoring loop untuk setiap userbot
                asyncio.create_task(chatbot_monitoring_loop(userbot))
                print(f"✅ Chatbot monitoring started for {userbot.me.first_name}")
                
                # Mark sebagai aktif
                chatbot_active[userbot.me.id] = True
                
            except Exception as e:
                print(f"❌ Error starting chatbot for {userbot.me.first_name}: {e}")
                print(traceback.format_exc())
        
        print(f"✅ Chatbot Task initialized successfully for {len(nlx._ubot)} userbot(s)")
        
    except Exception as e:
        print(f"❌ Error in ChatbotTask: {e}")
        print(traceback.format_exc())

# Fungsi untuk restart chatbot jika diperlukan  
async def restart_chatbot():
    """Restart chatbot handlers"""
    try:
        print("🔄 Restarting chatbot...")
        
        # Clear existing state
        global chatbot_active, userbot_ids
        chatbot_active.clear()
        userbot_ids.clear()
        
        # Restart
        await ChatbotTask()
        print("🔄 Chatbot restarted successfully")
        
    except Exception as e:
        print(f"❌ Error restarting chatbot: {e}")
        print(traceback.format_exc())

# Fungsi untuk cek status chatbot
def get_chatbot_status():
    """Get status chatbot untuk semua userbot"""
    status = {}
    for userbot in nlx._ubot:
        user_id = userbot.me.id
        active_chats = dB.get_list_from_var(user_id, "CHATBOT") or []
        status[user_id] = {
            "name": userbot.me.first_name,
            "active": user_id in chatbot_active,
            "chat_count": len(active_chats),
            "chats": active_chats
        }
    return status

# Fungsi manual untuk test chatbot
async def test_chatbot_manual(client, chat_id, text):
    """Fungsi untuk test chatbot secara manual"""
    try:
        # Buat fake message object untuk testing
        class FakeUser:
            def __init__(self):
                self.id = 12345  # Fake user ID for testing
                self.first_name = "Test User"
        
        class FakeChat:
            def __init__(self, chat_id):
                self.id = chat_id
                self.title = "Test Chat"
        
        class FakeMessage:
            def __init__(self, text, chat_id):
                self.text = text
                self.caption = None
                self.from_user = FakeUser()
                self.chat = FakeChat(chat_id)
                self.id = 1
            
            async def reply(self, text):
                print(f"🧪 Test Response: {text}")
                return True
        
        fake_msg = FakeMessage(text, chat_id)
        
        # Test generate response
        response = await gen_text(client, fake_msg)
        
        if response:
            print(f"✅ Test successful - Generated: {response}")
            return response
        else:
            print("❌ Test failed - No response generated")
            return None
            
    except Exception as e:
        print(f"❌ Error in test: {e}")
        print(traceback.format_exc())
        return None

# Fungsi untuk auto-start chatbot saat bot startup
async def auto_start_chatbot():
    """Auto start chatbot saat bot startup"""
    try:
        await asyncio.sleep(5)  # Wait for all userbots to initialize
        await ChatbotTask()
        print("🚀 Auto-started chatbot monitoring")
    except Exception as e:
        print(f"❌ Error auto-starting chatbot: {e}")

# Fungsi untuk monitor health chatbot
async def chatbot_health_monitor():
    """Monitor kesehatan chatbot dan restart jika diperlukan"""
    while True:
        try:
            await asyncio.sleep(300)  # Check every 5 minutes
            
            # Check if any userbot needs restart
            for userbot in nlx._ubot:
                if userbot.me.id not in chatbot_active:
                    print(f"⚠️ Chatbot not active for {userbot.me.first_name}, restarting...")
                    chatbot_active[userbot.me.id] = True
                    asyncio.create_task(chatbot_monitoring_loop(userbot))
                    
        except Exception as e:
            print(f"❌ Error in health monitor: {e}")

# Export functions for external use
__all__ = [
    'ChatbotTask',
    'chatbot_cmd', 
    'restart_chatbot',
    'get_chatbot_status',
    'auto_start_chatbot',
    'chatbot_health_monitor'
]
