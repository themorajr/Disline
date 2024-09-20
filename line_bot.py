import os
import requests
from flask import Flask, request, jsonify

# Load environment variables (LINE channel secret, access token, etc.)
LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
LINE_API_URL = "https://api.line.me/v2/bot/message/"

# Set up the Flask app
app = Flask(__name__)

# Function to download a file from LINE
def download_line_file(message_id):
    url = f"{LINE_API_URL}{message_id}/content"
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }

    # Send a request to download the file
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:
        file_path = os.path.join("downloads", f"{message_id}.bin")
        # Save the file to the server
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return file_path
    else:
        print(f"Failed to download file: {response.status_code}")
        return None

# Webhook endpoint for LINE
@app.route("/webhook", methods=["POST"])
def webhook():
    # Parse the incoming request
    payload = request.json

    # Check if the event contains a message (file)
    for event in payload.get("events", []):
        if event["type"] == "message":
            message = event["message"]
            if message["type"] == "file":
                message_id = message["id"]
                file_path = download_line_file(message_id)
                if file_path:
                    return jsonify({"status": "success", "file_path": file_path})
    
    return jsonify({"status": "no_file"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)