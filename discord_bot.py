import os
import requests

# Load environment variables (Discord bot token and channel ID)
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
DISCORD_CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
DISCORD_API_URL = f"https://discord.com/api/v9/channels/{DISCORD_CHANNEL_ID}/messages"

# Function to post a file to a Discord channel
def post_to_discord(file_path, file_name):
    url = DISCORD_API_URL
    headers = {
        "Authorization": f"Bot {DISCORD_BOT_TOKEN}"
    }

    # Prepare file for uploading
    files = {
        'file': (file_name, open(file_path, 'rb'))
    }

    # Send POST request to Discord API
    response = requests.post(url, headers=headers, files=files)

    # Handle response
    if response.status_code == 200:
        print(f"File '{file_name}' successfully posted to Discord")
        return True
    else:
        print(f"Failed to post file to Discord: {response.status_code}")
        return False

if __name__ == "__main__":
    # Example usage (replace with actual path and file name)
    test_file_path = 'downloads/sample_file.bin'
    test_file_name = 'sample_file.bin'
    post_to_discord(test_file_path, test_file_name)