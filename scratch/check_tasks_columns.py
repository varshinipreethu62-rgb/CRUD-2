import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

print("Fetching 1 row from 'tasks' to see columns...")
try:
    res = supabase.table('tasks').select('*').limit(1).execute()
    if res.data:
        print(f"Columns: {res.data[0].keys()}")
    else:
        print("Table 'tasks' is empty. Cannot determine columns easily via anon key.")
except Exception as e:
    print(f"Error: {e}")
