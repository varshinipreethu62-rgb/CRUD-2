import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

print("Checking for 'students' table...")
try:
    res = supabase.table('students').select('*').limit(1).execute()
    print("Success: 'students' table exists.")
except Exception as e:
    print(f"Error for 'students': {e}")

print("\nChecking for 'tasks' table...")
try:
    res = supabase.table('tasks').select('*').limit(1).execute()
    print("Success: 'tasks' table exists.")
except Exception as e:
    print(f"Error for 'tasks': {e}")
