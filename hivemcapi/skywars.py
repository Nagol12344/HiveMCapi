import requests
import json
def mleaderbord():
    # https://api.playhive.com/v0/game/monthly/sky
    r = requests.get('https://api.playhive.com/v0/game/monthly/sky')
    return r.text
