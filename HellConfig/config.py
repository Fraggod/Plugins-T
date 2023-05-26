# IF YOU ARE HOSTING WARBOT ON OTHER VPS OR LOCALLY RATHER THAN HEROKU
# THEN DON'T EDIT THIS FILE.
# GO AND EDIT ex_config.py AND RENAME TO config.py
# AND FILL THE REQUIRED VARS THERE.

# !!! DO NOT EDIT THIS FILE !!!

import os


class Config(object):
    LOGGER = True
    ABUSE = os.environ.get("ABUSE", None)
    API_HASH = os.environ.get("API_HASH", None)
    APP_ID = os.environ.get("APP_ID", None)
    BL_CHAT = set(int(x) for x in os.environ.get("BL_CHAT", "").split())
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "\/")
    BOT_LIBRARY = os.environ.get("BOT_LIBRARY", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    BUTTONS_IN_HELP = int(os.environ.get("BUTTONS_IN_HELP", 7))
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
    CURRENCY_API = os.environ.get("CURRENCY_API", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    EMOJI_IN_HELP = os.environ.get("EMOJI_IN_HELP", "✧")
    FBAN_LOG_GROUP = os.environ.get("FBAN_LOG_GROUP", None)
    if FBAN_LOG_GROUP:
        FBAN_LOG_GROUP = int(FBAN_LOG_GROUP)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GBAN_LOG_GROUP = os.environ.get("GBAN_LOG_GROUP", None)
    if GBAN_LOG_GROUP:
        GBAN_LOG_GROUP = int(GBAN_LOG_GROUP)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    HANDLER = os.environ.get("HANDLER", ".")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    IG_SESSION = os.environ.get("INSTAGRAM_SESSION", None)
    INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", None)
    LOGGER_ID = os.environ.get("LOGGER_ID", None)
    if LOGGER_ID:
        LOGGER_ID = int(LOGGER_ID)
    LYRICS_API = os.environ.get("LYRICS_API", None)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    MAX_SPAM = int(os.environ.get("MAX_SPAM", 3))
    MY_CHANNEL = os.environ.get("YOUR_CHANNEL", "waruserbot")
    MY_GROUP = os.environ.get("YOUR_GROUP", "waruserbotsupport")
    OCR_API = os.environ.get("OCR_API", None)
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", None)
    if PLUGIN_CHANNEL:
        PLUGIN_CHANNEL = int(PLUGIN_CHANNEL)
    PM_LOG_ID = os.environ.get("PM_LOG_ID", None)
    if PM_LOG_ID:
        PM_LOG_ID = int(PM_LOG_ID)
    PM_PERMIT = os.environ.get("PM_PERMIT", None)
    REMOVE_BG_API = os.environ.get("REMOVE_BG_API", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    SESSION_2 = os.environ.get("SESSION_2", None)
    SESSION_3 = os.environ.get("SESSION_3", None)
    SESSION_4 = os.environ.get("SESSION_4", None)
    SESSION_5 = os.environ.get("SESSION_5", None)
    SUDO_HANDLER = os.environ.get("SUDO_HANDLER", ".")
    SUDO_USERS = []
    TAG_LOGGER = os.environ.get("TAG_LOGGER", None)
    if TAG_LOGGER:
        TAG_LOGGER = int(TAG_LOGGER)
    TELEGRAPH_NAME = os.environ.get("TELEGRAPH_NAME", "[ THE WARUSERBOT ]")
    TEMP_DIR = os.environ.get("TEMP_DIR", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    THUMB_IMG = os.environ.get("THUMB_IMG", "./HellConfig/resources/pics/hellbot_logo.jpg")
    UNLOAD = list(os.environ.get("UNLOAD", "").split())
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/MeAbhish3k/waruserbot")
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")
    WEATHER_API = os.environ.get("WEATHER_API", None)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True