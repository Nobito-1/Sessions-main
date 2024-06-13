from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "28453104"))
API_HASH = getenv("API_HASH","83151aed003895d0f9a3aefe8906adbb")

BOT_TOKEN = getenv("BOT_TOKEN", "7100574645:AAHowKlop3_RkDVINYIygKMTHgeikTX7RXg" )
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://abood:king@cluster0.rbp1cqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MUST_JOIN = getenv("MUST_JOIN", None)
