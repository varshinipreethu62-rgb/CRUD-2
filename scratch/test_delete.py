import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# 1. Insert a test record
print("Inserting test record...")
res_insert = supabase.table('tasks').insert(
    {'name': 'Delete Test', 'email': 'delete@test.com'}).execute()
test_id = res_insert.data[0]['id']
print(f"Inserted record with ID: {test_id}")

# 2. Delete the test record
print("Deleting test record...")
res_delete = supabase.table('tasks').delete().eq('id', test_id).execute()
print(f"Delete response data: {res_delete.data}")
print(f"Is response data falsy? {not res_delete.data}")
