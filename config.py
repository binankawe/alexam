import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAXeq46obeHQL6Sz_iJwbMAk_jnT4Ytbg5hfCZnRmCjZHP_fXb6iP9EiHULcJhYmfSpF70gOCOjz1_C1h1-AEOcdb3PabzVR4Xow5gtRGefxQ1kay3dzWnIIAhVlzR5I_-cQoqO-RzPh8aESfdz4jHyXxTO1pEFR6bMPTvweTRmpIOFR156D8XIdiZBc0st-4dZYn2B9WVxWSDs9M1FQdRM1elQ59Vp0qO4sP8Kheq3m523oY0aS7odrkpnUvXLg8YraY0q7yGDe7F8p5BYUNx_akw_SRJyoFZ5MenlaMHR-aBw_FnB-AoBMWMKCSy4vmnBbvYiCGCzpJf35LK0vPmvaT9o4gA")
BOT_TOKEN = getenv("BOT_TOKEN", "2072190749:AAHz8P1_ADtIp4n9p4UdRvS1pyGxldjnD4Q")
BOT_NAME = getenv("BOT_NAME", "Alexa")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "-1001319845035")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/36256d986b9c69902e4c4.png")
admins = {}
API_ID = int(getenv("API_ID", "3371945"))
API_HASH = getenv("API_HASH", "880695522786b34a4e943902db6e4f64")
BOT_USERNAME = getenv("BOT_USERNAME", "alexagroup_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "alexaassisten")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "robotprojectx")
PROJECT_NAME = getenv("PROJECT_NAME", "Alexa")
DATABASE_URL = os.environ.get("mongodb+srv://alexam:sad1899@cluster0.f5kx3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER = getenv("OWNER", "justthetech")
OWNER_NAME = getenv("OWNER", "justthetech")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Vckyou/Geez-MusicProject")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1652454077 1034473881 927625147").split()))
