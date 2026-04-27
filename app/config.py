import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SUPABASE_URL = os.getenv("SUPABASE_URL", "https://iinhsrcceiapscezbhgn.supabase.co")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlpbmhzcmNjZWlhcHNjZXpiaGduIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY3NDI4NjQsImV4cCI6MjA5MjMxODg2NH0.HDvKaDAfrdQmd00lA9WRpYZ0QqV_T_57ao5b8PAMV8w")
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
