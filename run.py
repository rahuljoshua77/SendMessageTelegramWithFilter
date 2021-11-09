from telethon import TelegramClient, events, sync
import time
from re import search
import re
api_id = 'masukin api id'
api_hash = 'masukin api hash'
 
kamus = "kata1|kata2"
client = TelegramClient('session_name', api_id, api_hash)
username_sumber = "GROUP/CHANNEL SUMBER" #Masukkan username group target, misalnya: AirdropfindX
username_tujuan = "TUJUAN KIRIM"  #Masukkan username target, misalnya
@client.on(events.NewMessage(chats=username_sumber))
async def handle_new_message(event):
    send = await event.get_sender()
    sender = send.username
    print(f"[{time.strftime('%d-%m-%y %X')}] {sender}: {event.message.message.lower()}")
  
    clear_data = re.sub(f"({kamus})","",event.message.lower())
    await client.send_message(f"{username_tujuan}", f"From:{sender}\n{clear_data}")
    print(f"[{time.strftime('%d-%m-%y %X')}] Sent Succesfully")
with client:
    client.run_until_disconnected()
