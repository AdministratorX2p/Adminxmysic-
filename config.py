from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/3c5ba5eaddad3b9aa2790.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/3c61dd910606440ee8f66.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/YorXsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/YorXsupport")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6843311998").split()))


FAILED = "https://graph.org/file/165eef1799e0edd83b56d.jpg"
