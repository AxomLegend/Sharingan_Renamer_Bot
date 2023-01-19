import re, os

id_pattern = re.compile(r'^.\d+$')
# The Telegram API things
API_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
# get a token from @BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
# Update channel for Force Subscribe
FORCE_SUB = os.environ.get("FORCE_SUB", "")
# Database Name
DB_NAME = os.environ.get("DB_NAME","")
# Database url
DB_URL = os.environ.get("DB_URL","")
# Flood Control
FLOOD = int(os.environ.get("FLOOD", "10"))
#Welcome Banner Image URL
WELCOME_BANNER = os.environ.get("WELCOME_BANNER", "")
# Array to store users who are authorized to use the bot
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '677682427').split()]
#PORT SET to 8080 for Global
PORT = os.environ.get('PORT', '8080')
