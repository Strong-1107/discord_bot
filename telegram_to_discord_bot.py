from telethon import TelegramClient, events
import discord
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

#define folders
IMAGE_FOLDER = "images"
VIDEO_FOLDER = "videos"
os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

#initialize the telegram client
telegram_client = TelegramClient('session_name', API_ID, API_HASH)




