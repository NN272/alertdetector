from telethon import TelegramClient, events
from playsound import playsound
from config import api_id, api_hash, channelId
import dearpygui.dearpygui

client = TelegramClient('NN_ALERT', api_id, api_hash)

client.start()
dearpygui.create_context()
dearpygui.create_viewport(title='Alert Detector by NN', width=600, height=300)

@client.on(events.NewMessage(chats=[channelId]))
async def handler(event):
    message = event.message.message
    print(f"{message}. Тривоги немає") if message.lower().find("тривога") == -1 else playsound('./alert.mp3')

client.run_until_disconnected()