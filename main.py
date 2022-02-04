import requests


API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = '939128709221335112'
CLIENT_SECRET = 'AACznTBE5wCG5a7IsM1X0q_Ean-m5tdb'
REDIRECT_URI = "https://google.com"


def exchange_code(code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
    r.raise_for_status()
    return r.json()


def add_to_guild(access_token, userID, guildID):
    url = f"{API_ENDPOINT}/guilds/{guildID}/members/{userID}"
    botToken = "OTM5MTI4NzA5MjIxMzM1MTEy.Yf0VxA.6IDCz7vN_R1qGIyIGjzNO4ZImK4"
    data = {
        "access_token": access_token,
    }
    headers = {
        "Authorization": f"Bot {botToken}",
        'Content-Type': 'application/json'
    }
    response = requests.put(url=url, headers=headers, json=data)
    print(response.text)


def refresh_token(refresh_token):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
    r.raise_for_status()
    return r.json()


code = exchange_code('80jw8etPrx472v0IGIDAKo5NLsOQx')['access_token']
add_to_guild(code, 'USER_ID', 'GUILD_ID')

