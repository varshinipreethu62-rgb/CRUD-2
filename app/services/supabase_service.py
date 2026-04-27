from supabase import create_client, Client
from app.config import Config

print(f"DEBUG: Initializing Supabase client with URL: {Config.SUPABASE_URL}")
supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)
print("DEBUG: Supabase client initialized successfully.")
