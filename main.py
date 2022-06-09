from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import time
api_id = 0123456  # your api_id
api_hash = "5b7e9263d4sfbpkowagjo3qt498df"  # your api_hash
client = TelegramClient("anon", api_id, api_hash)


async def main():
      with open("song.txt", "r", encoding='utf-8') as file:
        for line in file:
            txt = line.strip()
            time.sleep(10)
            print(txt)
            await client(UpdateProfileRequest(about=txt))
with client:
    while True:
         try:
             client.loop.run_until_complete(main())
             time.sleep(10)
         except Exception: time.sleep(10)
