from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "24132032"))
API_HASH = getenv("API_HASH", "528c5163fcbe0a4b3300c92f73ea8cb3")
BOT_TOKEN = getenv("BOT_TOKEN", "5616509509:AAEKd4kyD0Hu61nxB5RTQelw_vxh3nIuCM0")
BOT_NAME = getenv("BOT_NAME","RAMPAGE MUSIC")
BOT_USERNAME = getenv("BOT_USERNAME", "rm_vc_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Hm_apke_hai_kaun")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "loggervi")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "200"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME","AQAZTmq-qTAM11k0zKBYCmJgt40-A7ucDimDTcJYi35lt_pbHpuKfj9HwMdXdGUGChIj7nTRlrF7kNjkfH91kvQ82wT7St8AaRi4w4bu1VM59_cM8bVsC43sT8uoyCTN8DEZzBaX3194f6-S_eruD87zgSFkoYsU7Alz3OvezgydDVCu6tRewPOBpoGSF7HrgG7tZtYPCahY4W7VOxlX-zzUc5EBUlNcRbdhIg5oa12R_1AOI7yAH-jNN9y7MNKKYBlR9IX9dGUuyYtufUruGrnlITIsW-iAg2wbhIxUyrZSTrqjt3jH4st_hohC5apvWgpWgXo7Q5VAYhfKylxvWq2iAAAAAVVvwEQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5717137175").split()))
