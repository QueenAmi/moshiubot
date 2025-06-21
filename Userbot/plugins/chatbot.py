# chatbot_diagnostic.py - Script untuk debug chatbot issues
import sqlite3
import json
import os
from config import db_name

def diagnose_chatbot_database():
    """Diagnose database issues untuk chatbot"""
    db_path = f"./{db_name}.db"
    
    print("🔍 CHATBOT DATABASE DIAGNOSTIC")
    print("=" * 50)
    
    # Check if database exists
    if not os.path.exists(db_path):
        print(f"❌ Database file tidak ditemukan: {db_path}")
        return
    
    print(f"✅ Database file ditemukan: {db_path}")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check variabel table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='variabel'")
        if not cursor.fetchone():
            print("❌ Tabel 'variabel' tidak ditemukan")
            return
        
        print("✅ Tabel 'variabel' ditemukan")
        
        # Get all data from variabel table
        cursor.execute("SELECT _id, vars FROM variabel")
        rows = cursor.fetchall()
        
        print(f"\n📊 Total entries di variabel table: {len(rows)}")
        
        for _id, vars_json in rows:
            print(f"\n👤 User ID: {_id}")
            
            try:
                vars_data = json.loads(vars_json) if vars_json else {}
                print(f"   📝 Vars data type: {type(vars_data)}")
                
                if 'vars' in vars_data:
                    vars_section = vars_data['vars']
                    print(f"   📋 Vars section keys: {list(vars_section.keys()) if isinstance(vars_section, dict) else 'Not dict'}")
                    
                    if 'CHATBOT' in vars_section:
                        chatbot_data = vars_section['CHATBOT']
                        print(f"   🤖 CHATBOT data: {chatbot_data} (type: {type(chatbot_data)})")
                        
                        # Try to parse as list
                        if isinstance(chatbot_data, str):
                            try:
                                if chatbot_data.strip():
                                    chat_ids = [int(x) for x in chatbot_data.split()]
                                    print(f"   ✅ Parsed chat IDs: {chat_ids}")
                                else:
                                    print(f"   ⚠️  Empty CHATBOT string")
                            except ValueError as e:
                                print(f"   ❌ Error parsing CHATBOT string: {e}")
                        elif isinstance(chatbot_data, list):
                            print(f"   ✅ CHATBOT is already list: {chatbot_data}")
                        else:
                            print(f"   ❌ CHATBOT data unexpected type: {type(chatbot_data)}")
                    else:
                        print(f"   ⚠️  No CHATBOT key found")
                else:
                    print(f"   ⚠️  No 'vars' section found")
                    
            except json.JSONDecodeError as e:
                print(f"   ❌ JSON decode error: {e}")
                print(f"   📄 Raw data: {vars_json}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")

def fix_chatbot_database():
    """Fix common database issues"""
    db_path = f"./{db_name}.db"
    
    print("\n🔧 FIXING DATABASE ISSUES")
    print("=" * 50)
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all problematic entries
        cursor.execute("SELECT _id, vars FROM variabel")
        rows = cursor.fetchall()
        
        fixed_count = 0
        
        for _id, vars_json in rows:
            try:
                vars_data = json.loads(vars_json) if vars_json else {}
                
                if 'vars' in vars_data and 'CHATBOT' in vars_data['vars']:
                    chatbot_data = vars_data['vars']['CHATBOT']
                    
                    # Fix if CHATBOT data is not a string
                    if isinstance(chatbot_data, list):
                        # Convert list to string
                        new_chatbot_data = " ".join(map(str, chatbot_data))
                        vars_data['vars']['CHATBOT'] = new_chatbot_data
                        
                        # Update database
                        new_vars_json = json.dumps(vars_data)
                        cursor.execute("UPDATE variabel SET vars = ? WHERE _id = ?", (new_vars_json, _id))
                        
                        print(f"✅ Fixed user {_id}: {chatbot_data} -> '{new_chatbot_data}'")
                        fixed_count += 1
                        
            except Exception as e:
                print(f"❌ Error fixing user {_id}: {e}")
        
        conn.commit()
        conn.close()
        
        print(f"\n🎉 Fixed {fixed_count} entries")
        
    except Exception as e:
        print(f"❌ Fix error: {e}")

def clean_chatbot_database():
    """Clean up corrupt or invalid data"""
    db_path = f"./{db_name}.db"
    
    print("\n🧹 CLEANING DATABASE")
    print("=" * 50)
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT _id, vars FROM variabel")
        rows = cursor.fetchall()
        
        cleaned_count = 0
        
        for _id, vars_json in rows:
            try:
                vars_data = json.loads(vars_json) if vars_json else {}
                
                if 'vars' in vars_data and 'CHATBOT' in vars_data['vars']:
                    chatbot_data = vars_data['vars']['CHATBOT']
                    
                    if isinstance(chatbot_data, str):
                        # Clean up string data
                        if chatbot_data.strip():
                            # Remove invalid characters and normalize
                            parts = chatbot_data.split()
                            valid_parts = []
                            
                            for part in parts:
                                try:
                                    chat_id = int(part)
                                    # Validate chat ID (should be negative for groups)
                                    if chat_id != 0:  # Exclude zero
                                        valid_parts.append(str(chat_id))
                                except ValueError:
                                    print(f"⚠️  Removing invalid chat ID: '{part}' for user {_id}")
                            
                            new_chatbot_data = " ".join(valid_parts)
                            
                            if new_chatbot_data != chatbot_data:
                                vars_data['vars']['CHATBOT'] = new_chatbot_data
                                new_vars_json = json.dumps(vars_data)
                                cursor.execute("UPDATE variabel SET vars = ? WHERE _id = ?", (new_vars_json, _id))
                                
                                print(f"✅ Cleaned user {_id}: '{chatbot_data}' -> '{new_chatbot_data}'")
                                cleaned_count += 1
                        
            except Exception as e:
                print(f"❌ Error cleaning user {_id}: {e}")
        
        conn.commit()
        conn.close()
        
        print(f"\n🎉 Cleaned {cleaned_count} entries")
        
    except Exception as e:
        print(f"❌ Clean error: {e}")

def test_database_operations():
    """Test basic database operations"""
    print("\n🧪 TESTING DATABASE OPERATIONS")
    print("=" * 50)
    
    try:
        from Userbot.helper.database import dB
        
        test_user_id = 999999999  # Test user ID
        test_chat_id = -1001234567890  # Test chat ID
        
        print(f"Testing with user_id: {test_user_id}, chat_id: {test_chat_id}")
        
        # Test 1: Get empty list
        result = dB.get_list_from_var(test_user_id, "CHATBOT")
        print(f"✅ Get empty list: {result} (type: {type(result)})")
        
        # Test 2: Add to var
        dB.add_to_var(test_user_id, "CHATBOT", test_chat_id)
        result = dB.get_list_from_var(test_user_id, "CHATBOT")
        print(f"✅ After add: {result} (type: {type(result)})")
        
        # Test 3: Remove from var
        dB.remove_from_var(test_user_id, "CHATBOT", test_chat_id)
        result = dB.get_list_from_var(test_user_id, "CHATBOT")
        print(f"✅ After remove: {result} (type: {type(result)})")
        
        # Test 4: Clean up
        dB.remove_var(test_user_id, "CHATBOT")
        print("✅ Cleanup completed")
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🔍 CHATBOT DIAGNOSTIC TOOL")
    print("=" * 50)
    
    while True:
        print("\nPilih aksi:")
        print("1. Diagnose database")
        print("2. Fix database issues")
        print("3. Clean database")
        print("4. Test database operations")
        print("5. Exit")
        
        choice = input("\nMasukkan pilihan (1-5): ").strip()
        
        if choice == "1":
            diagnose_chatbot_database()
        elif choice == "2":
            fix_chatbot_database()
        elif choice == "3":
            clean_chatbot_database()
        elif choice == "4":
            test_database_operations()
        elif choice == "5":
            print("👋 Bye!")
            break
        else:
            print("❌ Pilihan tidak valid")
