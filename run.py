from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import os
api_id = 2429786
api_hash = '992cd4665a7b141dc5c9a340b58b9b4d'

 
print(f"[*] Automation Scraping Member Group Telegram!\n[*] Author: RJD")
target = input(f"[*] Input Link/@ Group (example: @defiandmore): ")

try:
    client = TelegramClient('sess', api_id, api_hash)

    client.connect()
    if not client.is_user_authorized():
        phone = input(f"[*] Input Number (example: +6213232323232): ")
        client.send_code_request(phone)
        client.sign_in(phone, input('[*] Enter the code: '))

    print('[*] Fetching Members...')
    all_participants = []
    cwd = os.getcwd()
    try:

        all_participants = client.get_participants(target, aggressive=True)

        print('[*] Saving In file...')
 

        if "https://t.me/" in target:
            new_target = target.split("https://t.me/")
            target = new_target[1]

        with open(f"{cwd}/{target}.csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            i = 0
            for user in all_participants:
                if user.username:
                    username = user.username
                    writer.writerow([username])
                    i = i + 1
        
        print(f'[*] {i} Members scraped successfully.\n[*] Saved to {target}.csv')
    except Exception as e:
        print(f"[*] Failed Scrapping: {e}")
except Exception as e:
    print(f"[*] Eror First: {e}")
