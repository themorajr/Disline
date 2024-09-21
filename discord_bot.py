import os
import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

# Enable necessary intents explicitly
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

async def post_to_discord(file_path, file_name):
    channel = client.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        try:
            with open(file_path, 'rb') as f:
                await channel.send(file_name, file=discord.File(f, file_name))
            print(f"Posted {file_name} to Discord.")
            return True
        except Exception as e:
            print(f"Failed to post to Discord: {e}")
            return False
    else:
        print(f"Channel {DISCORD_CHANNEL_ID} not found.")
        return False

client.run(DISCORD_TOKEN)