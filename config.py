import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("BQB6TMb1Kz8fOOnpDWt7wYJ2VpLV5D0v7bRpzfi5Jn1B1qf9igGOVnLEUmfOZ41PBO7WQm2AxR_ATQW3J6URAf2a7_Ms2qa_4435fvDcFUk6zb7aYPBFE5oP591SZq3pDI7V7rdKUMUuHPu9_BKjNSLPvW4vfO0OJV6n0MpjIWoPWU4EPfmB3eS4uTqUnz1eZrFrCs8uYuVwCOXWRFd3cf3XaiCbXHwVLVj-eSnTf4A1ESG9WJFRbpDKoqtaukKTF83vG6wQh1HL0Mt2srv1dNp2_R5U4jJCvFgFs3r7E2nB99ZvbzE0pjRRIJasiQnupQ71BXUIeAjBt29lKKnUpi0BAAAAAEsk1DYA", "session")
BOT_TOKEN = getenv("5452659833:AAG2A9j-WD8FKxjiGSiDSdpoOxTE33_0Kyk")
BOT_NAME = getenv("ultrastreambot", "")
API_ID = int(getenv("11004381"))
API_HASH = getenv("8e0588044fcf7672cfe1341185bfc94c")
OWNER_NAME = getenv("Ashish", "")
ALIVE_NAME = getenv("Ashish", "")
BOT_USERNAME = getenv("ultrastreambot", "")
ASSISTANT_NAME = getenv("blackinfinity11", "")
GROUP_SUPPORT = getenv("flixwarriorz", "")
UPDATES_CHANNEL = getenv("flixwarriorzchannel", "")
SUDO_USERS = list(map(int, getenv("1260704822").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("60", ""))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
