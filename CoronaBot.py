from telethon import TelegramClient, events
import json
import requests
from sample_config import Config

APP_ID=2192067 #my.telegram.org
APP_HASH='d2e0ba99f1b9cdb632b43633edb76f11' #my.telegram.org
BOTT='1689002354:AAFuYEPqZ_crEHPCCP7agFFI-clYikjSrus'#@botfather

bot = TelegramClient('bot', APP_ID, APP_HASH).start(bot_token=BOTT)

def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "https://telegra.ph/file/9a67dc2f6f011f10b9fac.png",
    "caption": "ශ්‍රී ලංකාවේ කොරෝනා තතු එසැනින් දැනගන්න. @Corona_SlRobot  Group එකට Add කරගත් පසු ස්වයංක්‍රියව නවතම කොරෝනා තතු ලබාගත හැක. 🙈 ",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": "➕ Add me to your Group 🦠",
                    "url": "https://t.me/Corona_SlRobot?startgroup=new"
                }
            ]
        ]
    }
}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)

def staa():
    r = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
    jsondata = json.loads(r.text)
    update_date_time    = str(jsondata['data']['update_date_time'])
    local_new_cases     = str(jsondata['data']['local_new_cases'])
    local_active_cases  = str(jsondata['data']['local_active_cases'])
    local_total_cases   = str(jsondata['data']['local_total_cases'])
    local_deaths        = str(jsondata['data']['local_deaths'])
    local_recovered     = str(jsondata['data']['local_recovered'])
    local_total_number_of_individuals_in_hospitals = str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
    global_new_cases    = str(jsondata['data']['global_new_cases'])
    global_total_cases  = str(jsondata['data']['global_total_cases'])
    global_deaths       = str(jsondata['data']['global_deaths'])
    global_new_deaths   = str(jsondata['data']['global_deaths'])
    global_recovered    = str(jsondata['data']['global_recovered'])

    textt = str(
                    '<b>CURRENT SITUATION</b>' + '\n' + '\n' + '<u>' +
                    update_date_time + '📰 වන විට 🦠</u>' + '\n' + '\n' +
                    '<u>ශ්‍රී ලංකාවේ තත්ත්වය 🇱🇰</u>' + '\n' + '\n' +
                    'තහවුරු කරනලද රෝගීන් සංඛ්‍යාව 🤒 ➡️ ' +
                    local_total_cases + '\n' +
                    'ප්‍රතිකාර ලබන රෝගීන් සංඛ්‍යාව 🤕 ➡️ ' + local_active_cases +
                    '\n' + 'නව රෝගීන් සංඛ්‍යාව 😷 ➡️ ' + local_new_cases +
                    '\n' +
                    'දැනට රෝහල්වල විමර්ශන යටතේ සිටින පුද්ගලයින් 🤧  ➡️ ' +
                    local_total_number_of_individuals_in_hospitals + '\n' +
                    'සුවය ලබා පිටව ගිය සංඛ්‍යාව 😌 ➡️ ' + local_recovered +
                    '\n' + 'මරණ සංඛ්‍යාව ⚰️ ➡️ ' + local_deaths + '\n' +
                    '\n' + '<u>ලොව පුරා තත්ත්වය 🌎</u>' + '\n' +
                    '\n' + 'තහවුරු කරනලද රෝගීන් සංඛ්‍යාව 🤒 ➡️ ' +
                    global_total_cases + '\n' + 'නව රෝගීන් සංඛ්‍යාව 😷 ➡️ ' +
                    global_new_cases + '\n' + 'මරණ සංඛ්‍යාව ⚰️ ➡️ ' +
                    global_deaths + '\n' + 'සුවය ලැබූ සංඛ්‍යාව 😌 ➡️ ' +
                    global_recovered + '\n' + '\n' + '\n' +
                    '🗞සියලු තොරතුරු රජයේ සහ පිලිගත් මුලාශ්‍ර මගිනි 📰' + '\n' +
                    '[Corona_SlRobot](https://t.me/Corona_SlRobot?startgroup=new)')
    return textt



@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    staat(event.original_update.message.peer_id.user_id)
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/corona'))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation

@bot.on(events.NewMessage(pattern='/help'))
async def help(event):
    await event.respond('use /corona command to view latest corona news')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
