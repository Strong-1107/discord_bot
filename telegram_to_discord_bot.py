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

#initialize the discord client with intents

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
discord_client = discord.Client(intents=intents)

#use the channel username or id
channel_username = '@strong1107'

@telegram_client.on(events.NewMessage(chats = channel_username))
async def telegram_handler(event):
    message_text = event.message.text or "No text in this message."

    if event.message.photo:
        print(f"Image detected! Message: {message_text}")
        file_path = await event.message.download_media(file = IMAGE_FOLDER)
        print(f"Image saved to : {file_path}")
        await send_photo_to_discord(file_path, message_text)
    
    elif event.message.video:
        print(f"🎥 Video detected! Message: {message_text}")
        file_path = await event.message.download_media(file=VIDEO_FOLDER)
        print(f"✅ Video saved to: {file_path}")
        await send_video_to_discord(file_path, message_text)
    
    else:
        print(f"💬 Text Message: {message_text}")
        await send_text_to_discord(message_text)

#implementation of functions
async def send_text_to_discord(message):
    channel = discord_client.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send(message)

async def send_photo_to_discord(file_path, message_text):
    channel = discord_client.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        try:
            with open(file_path, 'rb') as fp:
                await channel.send(file=discord.File(fp, filename=os.path.basename(file_path)), content=message_text)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"Error sending photo to Discord: {e}")

async def send_video_to_discord(file_path, message_text):
    channel = discord_client.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        try:
            with open(file_path, 'rb') as fp:
                await channel.send(file=discord.File(fp, filename=os.path.basename(file_path)), content=message_text)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"Error sending video to Discord: {e}")

@discord_client.event
async def on_ready():
    print(f'Logged in as {discord_client.user}')

