import os
from telethon.tl.types import ChatBannedRights
ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os
    class Config(object):
        API_KEY = os.environ.get("TELEGRAM_API_KEY", None)
        APP_ID = os.environ.get("TELEGRAM_API_KEY", None)
        API_HASH = os.environ.get("TELEGRAM_API_HASH", None)
        STRING_SESSION = os.environ.get("TELEGRAM_STRING_SESSION", None)
        BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))
        GENIUS = os.environ.get("GENIUS_API_TOKEN", None)
        GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None) 
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)
        AFK_MESSAGE = os.environ.get("AFK_MESSAGE", None)
        ALIVE_S_MESSAGE = os.environ.get("ALIVE_S_MESSAGE", None)
        BIO_MESSAGE = os.environ.get("BIO_MESSAGE", None)
        ALIVE_E_MESSAGE = os.environ.get("ALIVE_E_MESSAGE", None)
        CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
        BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
        DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
        LASTFM_API = os.environ.get("LASTFM_API", None)
        LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
        LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
        LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
        LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
        CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
        PM_AUTO_BAN = os.environ.get("PM_PROTECTOR", "True")
        TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY","./downloads")
        LOGGER = True
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
        LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
        PM_MESSAGE = os.environ.get(f"PM_MESSAGE", None)
        KYNE_NAME = os.environ.get("KYNE_NAME", None)
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        ALIVE_NAME = os.environ.get("YOUR_SHORT_NAME", None)
        BLOCK_MESSAGE = os.environ.get("BLOCK_MESSAGE", None)
        HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
        HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
        UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL","https://github.com/obsq/kyne3301")
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "kyne")
        CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
        TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
        COUNTRY = str(os.environ.get("COUNTRY", ""))
        TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
        PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -100))   
        TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        PRIVATE_GROUP_ID = os.environ.get("BOTLOG_CHATID", None)
        DB_URI = os.environ.get("DATABASE_URL", None)

else:
    class Config(object):
        DB_URI = None
