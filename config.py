import json
import sys
from base64 import b64decode
from os import getenv

import requests
from dotenv import load_dotenv

black = int(b64decode("MTA1NDI5NTY2NA=="))

ERROR = "Maintained ? Yes Oh No Oh Yes Ngentot\n\nBot Ini Haram Buat Lo Bangsat!!\n\n@ CREDIT : NAN-DEV"
DIBAN = "LAH LU DIBAN BEGO DI @UserbotTele"


def get_tolol():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi90b2xvbC5qc29u"
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


def get_blgc():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL25heWExNTAzL3dhcm5pbmcvbWFpbi9ibGdjYXN0Lmpzb24="
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        return f"An error occurred: {str(e)}"
        sys.exit(1)


TOLOL = get_tolol()

NO_GCAST = get_blgc()

load_dotenv()

id_button = {}
CMD_HELP = {}


DEVS = [1371054078, 2136402531, 7975039370, 6874760603, 6544280065]

devs_boong = list(map(int, getenv("devs_boong", "").split()))
api_id = int(getenv("api_id", 21140865))
api_hash = getenv("api_hash", "9dbae6c11aa0a1c06da19d52deada7b9")
bot_token = getenv("bot_token", "8069560635:AAFNF8Nsujr3yOhG7Q9L5Dent1hql_gsOjs")
bot_id = int(getenv("bot_id", "8069560635"))
db_name = getenv("db_name", "syncmultinew")
log_pic = getenv("log_pic", "https://files.catbox.moe/i3hey9.jpg")
def_bahasa = getenv("def_bahasa", "toxic")
owner_id = int(getenv("owner_id", "2136402531"))

the_cegers = list(
    map(
        int,
        getenv(
            "the_cegers",
            "1371054078 6769771279 7975039370 2136402531",
        ).split(),
    )
)
dump = int(getenv("dump", "-1002639054633"))
bot_username = getenv("bot_username", "@MoshixUbot")
log_userbot = int(getenv("log_userbot", "2136402531"))
nama_bot = getenv("nama_bot", "MoshixUbot")
gemini_api = getenv("gemini_api", "cQNivoaVFjorUvgZTRzM1mNv")
botcax_api = getenv("botcax_api", "Avalance")
