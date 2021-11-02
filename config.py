import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAWkilQyDXW0RDJxY4SUVRwWdTUi3VDQtsmLQhadyJuOg1VhfJINsDs-VNvQuPJbGKOEyRqJL0G7haGXazAwXOo59l6UNJGiVanBpviu_HcNJI7f39JODggZ-pumT8RUbEh28fAYnii_2ekwWa0kOGOS7oq3_ySAJb5hwDp2RnXF1JjMfauy-NF3ut8ralAli-F7laO0Hc7fi0m4ggerhAfDnDPwK8hq50fwma25T8lT9W32ykey8SWpncn-huWTGETzfik22mhcAdXZ9xS6oJufdYUXHR8Fx6BydcsLarq5BzKDZ5LPH_zskq4YK1dScg1v9CXIWMxBDHS-wSZs67aaT9o4gA")
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
