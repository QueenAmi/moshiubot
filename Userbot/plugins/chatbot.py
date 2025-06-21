import random
import traceback
import asyncio

from pyrogram import enums, errors, filters, handlers
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

        print(f"Processing chatbot command: {action} in chat {chat_id}")

        if action == "on":
            try:
                current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                print(f"Current chats: {current_chats}")
                
                if chat_id not in current_chats:
                    # Ensure we're working with a list
                    if not isinstance(current_chats, list):
                        current_chats = []
                    
                    success = dB.add_to_var(client.me.id, bot_var_key, chat_id)
                    print(f"Add to var result: {success}")
                    
                    # Verify it was added
                    updated_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                    print(f"Updated chats after adding: {updated_chats}")
                    
                    if chat_id in updated_chats:
                        return await message.reply("<b>✅ Chatbot berhasil diaktifkan.</b>")
                    else:
                        return await message.reply("<b>❌ Gagal mengaktifkan chatbot. Coba lagi.</b>")
                else:
                    return await message.reply("<b>⚠️ Chatbot sudah aktif di grup ini.</b>")
            except Exception as e:
                print(f"Error in 'on' command: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "off":
            try:
                if len(cmd) >= 3 and cmd[2] == "all":
                    chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                    for cid in chats:
                        dB.remove_from_var(client.me.id, bot_var_key, cid)
                    # Clear the entire list
                    dB.set_var(client.me.id, bot_var_key, [])
                    return await message.reply("<b>🗑️ Semua chatbot group berhasil dihapus.</b>")

                try:
                    target_chat_id = int(cmd[2]) if len(cmd) >= 3 else chat_id
                except (ValueError, IndexError):
                    target_chat_id = chat_id

                current_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                print(f"Current chats before removal: {current_chats}")
                
                if target_chat_id not in current_chats:
                    return await message.reply(f"<b>⚠️ Chatbot tidak aktif di chat ID: <code>{target_chat_id}</code></b>")

                success = dB.remove_from_var(client.me.id, bot_var_key, target_chat_id)
                print(f"Remove from var result: {success}")
                
                # Verify removal
                updated_chats = dB.get_list_from_var(client.me.id, bot_var_key) or []
                print(f"Updated chats after removal: {updated_chats}")
                
                try:
                    chat_info = await client.get_chat(target_chat_id)
                    name = chat_info.title or "Unknown"
                except:
                    name = f"Chat ID: {target_chat_id}"
                
                if target_chat_id not in updated_chats:
                    return await message.reply(f"<b>❌ Chatbot dimatikan untuk: {name}</b>")
                else:
                    return await message.reply(f"<b>❌ Gagal mematikan chatbot untuk: {name}</b>")
            except Exception as e:
                print(f"Error in 'off' command: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "status":
            try:
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
            except Exception as e:
                print(f"Error in 'status' command: {e}")
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
                print(f"Error in 'role' command: {e}")
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
                print(f"Error in 'test' command: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        elif action == "debug":
            try:
                # Debug info
                active_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
                current_role = dB.get_var(client.me.id, "ROLE_CHATBOT")
                
                debug_info = f"""<b>🔍 Debug Info:</b>
                
<b>Userbot ID:</b> <code>{client.me.id}</code>
<b>Active Chats:</b> {len(active_chats)}
<b>Active Chat List:</b> <code>{active_chats}</code>
<b>Current Chat ID:</b> <code>{message.chat.id}</code>
<b>Chat Active:</b> {'✅' if message.chat.id in active_chats else '❌'}
<b>Role Set:</b> {'✅' if current_role else '❌'}
<b>API Key:</b> {'✅' if botcax_api else '❌'}
<b>Bot Var Key:</b> <code>{bot_var_key}</code>

<b>Userbot IDs in memory:</b> {len(userbot_ids)}
<b>Database connection:</b> {'✅' if dB else '❌'}
"""
                return await message.reply(debug_info)
            except Exception as e:
                print(f"Error in 'debug' command: {e}")
                return await message.reply(f"<b>❌ Error: {str(e)}</b>")

        else:
            return await message.reply(f"<b>❌ Aksi tidak valid: <code>{action}</code></b>\n<b>Gunakan: on, off, status, role, test, atau debug</b>")

    except Exception as e:
        print(f"Critical error in chatbot_cmd: {e}")
        print(traceback.format_exc())
        return await message.reply(f"<b>❌ Critical Error: {str(e)}</b>")

# Global variable untuk menyimpan handler
message_handlers = {}

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
            
        print(f"🤖 Processing message from {message.from_user.first_name} in {message.chat.title}")
        await chatbot_trigger(client, message)
        
    except Exception as e:
        print(f"❌ Error in message handler: {e}")
        print(traceback.format_exc())

def setup_chatbot_handlers():
    """Setup message handlers untuk semua userbot"""
    for userbot in nlx._ubot:
        try:
            # Add userbot ID ke set
            userbot_ids.add(userbot.me.id)
            
            # Register handler jika belum ada
            if userbot.me.id not in message_handlers:
                handler = userbot.add_handler(
                    handlers.MessageHandler(
                        handle_group_message,
                        filters.group & ~filters.bot & ~filters.via_bot
                    )
                )
                message_handlers[userbot.me.id] = handler
                print(f"✅ Handler registered for {userbot.me.first_name}")
            
        except Exception as e:
            print(f"❌ Error setting up handler for {userbot.me.first_name}: {e}")
            print(traceback.format_exc())

# Alternative: Polling method (lebih simple dan reliable)
async def chatbot_polling_loop(client):
    """Polling loop untuk check pesan baru"""
    last_message_ids = {}
    
    while True:
        try:
            # Use proper error handling for database access
            try:
                active_chats = dB.get_list_from_var(client.me.id, "CHATBOT") or []
            except Exception as db_error:
                print(f"Database error in polling: {db_error}")
                await asyncio.sleep(5)
                continue
            
            for chat_id in active_chats:
                try:
                    # Get latest message
                    async for message in client.get_chat_history(chat_id, limit=1):
                        # Skip jika pesan sudah diproses
                        if chat_id in last_message_ids and message.id <= last_message_ids[chat_id]:
                            break
                            
                        # Skip jika tidak ada teks
                        if not (message.text or message.caption):
                            last_message_ids[chat_id] = message.id
                            break
                            
                        # Skip jika dari userbot atau user tertentu
                        if (message.from_user.id in userbot_ids or 
                            message.from_user.id in the_cegers or
                            message.from_user.id == client.me.id):
                            last_message_ids[chat_id] = message.id
                            break
                        
                        # Skip jika pesan adalah command
                        text = message.text or message.caption
                        if text.startswith(('.', '/', '!', '-')):
                            last_message_ids[chat_id] = message.id
                            break
                        
                        print(f"🤖 Processing message from {message.from_user.first_name} in chat {chat_id}")
                        await chatbot_trigger(client, message)
                        last_message_ids[chat_id] = message.id
                        break
                        
                except Exception as e:
                    print(f"Error processing chat {chat_id}: {e}")
                    
                await asyncio.sleep(0.5)  # Small delay between chats
                
        except Exception as e:
            print(f"Error in polling loop for {client.me.first_name}: {e}")
            
        await asyncio.sleep(2)  # Main loop delay

async def ChatbotTask():
    """Initialize chatbot untuk semua userbot"""
    try:
        # Method 1: Try event handlers first
        setup_chatbot_handlers()
        
        # Method 2: Fallback to polling (more reliable)
        for userbot in nlx._ubot:
            try:
                userbot_ids.add(userbot.me.id)
                asyncio.create_task(chatbot_polling_loop(userbot))
                print(f"✅ Polling started for {userbot.me.first_name}")
            except Exception as e:
                print(f"❌ Error starting polling for {userbot.me.first_name}: {e}")
        
        print("✅ Chatbot Task initialized successfully")
    except Exception as e:
        print(f"❌ Error in ChatbotTask: {e}")
        print(traceback.format_exc())

# Fungsi manual untuk test chatbot
async def test_chatbot_manual(client, chat_id, text):
    """Fungsi untuk test chatbot secara manual"""
    try:
        # Buat fake message object untuk testing
        class FakeUser:
            def __init__(self):
                self.id = 12345
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
                print(f"Bot would reply: {text}")
        
        fake_msg = FakeMessage(text, chat_id)
        result = await gen_text(client, fake_msg)
        print(f"Generated response: {result}")
        return result
        
    except Exception as e:
        print(f"Error in test: {e}")
        return None

# Fungsi untuk cek database health
def check_database_health():
    """Check if database is working properly"""
    try:
        # Test basic database operations
        test_key = "test_chatbot_db"
        test_value = ["test_chat_123"]
        
        # Try to set and get a value
        dB.set_var(12345, test_key, test_value)
        retrieved = dB.get_var(12345, test_key)
        
        # Clean up test data
        dB.del_var(12345, test_key)
        
        if retrieved == test_value:
            print("✅ Database health check passed")
            return True
        else:
            print("❌ Database health check failed - value mismatch")
            return False
            
    except Exception as e:
        print(f"❌ Database health check failed: {e}")
        return False
        # Tambahkan di akhir file
if __name__ == "__main__":
    check_database_health()
