#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 1747534
API_HASH = "5a2684512006853f2e48aca9652d83ea"
BOT_TOKEN = "5362536299:AAHO5KiPA9FkGd8Gm7uZqazzfP9RI519mM0"
SESSION = "1BVtsOLUBu42DJOCKeixSoUwMhY5xW2iSdGIWzjxRVDcnSuPWQpNtHy2xLhNavX0onWAgpylEIUzZ-coXSLwgfrTkPbajsuZ6xRxann-0fTT7-1qoLQWGIdbPdJQoKPbcvEs45I9aN1MliMKQX1TrQ9KGq9sGevGBkBIDfS82O35-eiRpgE1MydXVDL4vrLLIDMnrHlhkzHFdASOY27qNlj1L7pbdMmyBV8AibIfoH1kS9UBGKjZUns5dbS09WbC_r2QbbohZCbGZbwNL_y4zbAJwaJ9kQMsnaYnQd883qQedWaegeYD7xP7fzeJ8zfRcGvyqnwQNVL_Hcb-gKHpJ0cZQXPdlUfU="
FORCESUB = "AwesomeModz"
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
