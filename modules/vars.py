import os

API_ID    = os.environ.get("API_ID", "27862677")
API_HASH  = os.environ.get("API_HASH", "e343ce2c81b2b6c2c0d6bee58284e3bd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7325518374:AAGwPkHstpJWHZBT2tl4QdVW3BGO7lpM_Ow") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
