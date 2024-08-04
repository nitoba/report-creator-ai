from supabase import Client, create_client

from src.env import env

url = env.SUPABASE_URL
key = env.SUPABASE_KEY

supabase: Client = create_client(url, key)
