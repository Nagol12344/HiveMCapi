import requests
import json
def mleaderboard():
    r = requests.get('https://api.playhive.com/v0/game/monthly/drop')
    return r.text

def mplayer(player):
    r = requests.get('https://api.playhive.com/v0/game/monthly/player/drop/' + player)
    if r.status_code == 200:
        return r.text
    else:
        return '{"index":404,"human_index":404,"username":"Not Found","xp":404,"played":404,"victories":404,"kills":404,"mystery_chests_destroyed":404,"ores_mined":404,"spells_used":404,"uncapped_xp":404}'

def leaderboard(player):
    r = requests.get("https://api.playhive.com/v0/game/all/drop")
    return r.text

def player(player):
    r = requests.get('https://api.playhive.com/v0/game/all/drop/' + player)
    if r.status_code == 200:
        return r.text
    else:
        return '{"index":404,"human_index":404,"username":"Not Found","xp":404,"played":404,"victories":404,"kills":404,"mystery_chests_destroyed":404,"ores_mined":404,"spells_used":404,"uncapped_xp":404}'