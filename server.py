from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
import os
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, FileMessage
from file_manager import is_allowed_file, delete_file
from discord_bot import post_to_discord
from database.models import db, File

app = Flask(__name__)

# Load environment variables for LINE API
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with Flask
db.init_app(app)

# Initialize LINE Bot API and Webhook Handler
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Create database tables (only the first time)
with app.app_context():
    db.create_all()

# Define the route for LINE webhook
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Handle file messages from the LINE bot
@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    # Get file details
    message_id = event.message.id
    file_name = event.message.file_name
    file_extension = os.path.splitext(file_name)[1].lower()

    # Define file path for saving downloaded files
    file_path = f"downloads/{file_name}"

    # Download the file from LINE
    file_content = line_bot_api.get_message_content(message_id)
    with open(file_path, 'wb') as fd:
        for chunk in file_content.iter_content():
            fd.write(chunk)

    # Check if the file is allowed
    file_type = f"application/{file_extension[1:]}"  # Simple MIME type guess from extension
    if is_allowed_file(file_path, file_type):
        file_size = os.path.getsize(file_path) / 1024  # Get size in KB
        
        # Store file metadata in the database
        new_file = File(name=file_name, file_type=file_type, size=int(file_size))
        db.session.add(new_file)
        db.session.commit()

        # Post to Discord
        if post_to_discord(file_path, file_name):
            delete_file(file_path)  # Optionally delete after posting
    else:
        delete_file(file_path)  # Delete if file is not allowed

if __name__ == "__main__":
    app.run(port=5000)
