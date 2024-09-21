from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, FileMessage, JoinEvent
from file_manager import is_allowed_file, delete_file
from discord_bot import post_to_discord
from database.models import db, File

app = Flask(__name__)

# Set up absolute path for SQLite database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "database", "db.sqlite3")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with Flask
db.init_app(app)

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables for LINE API
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

# Initialize LINE Bot API and Webhook Handler
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Create database tables (only the first time)
with app.app_context():
    db.create_all()

# Route for LINE webhook
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    if not signature:
        abort(400, 'Missing signature')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        logging.error("Invalid signature error")
        abort(400, 'Invalid signature')
    return 'OK'

# Handle when the bot joins a group
@handler.add(JoinEvent)
def handle_join(event):
    logging.info("Bot joined the group")
    # Send a message when the bot joins a group
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Hello! I'm here to collect files and post them to Discord.")
    )

# Handle file messages from the LINE bot
@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    logging.debug("Handling file message")
    # Get file details
    message_id = event.message.id
    file_name = event.message.file_name
    file_extension = os.path.splitext(file_name)[1].lower()

    # Define file path for saving downloaded files
    file_path = f"downloads/{file_name}"

    logging.debug(f"Downloading file: {file_name}")

    # Download the file from LINE
    file_content = line_bot_api.get_message_content(message_id)
    with open(file_path, 'wb') as fd:
        for chunk in file_content.iter_content():
            fd.write(chunk)

    logging.debug(f"File downloaded: {file_name}")

    # Check if the file is allowed
    file_type = f"application/{file_extension[1:]}"  # Simple MIME type guess from extension
    if is_allowed_file(file_path, file_type):
        file_size = os.path.getsize(file_path) / 1024  # Get size in KB

        # Store file metadata in the database
        new_file = File(name=file_name, file_type=file_type, size=int(file_size))
        db.session.add(new_file)
        db.session.commit()

        logging.debug(f"File saved to database: {file_name}, Size: {file_size}KB")

        # Post to Discord
        if post_to_discord(file_path, file_name):
            delete_file(file_path)  # Optionally delete after posting
            logging.debug(f"File posted to Discord and deleted: {file_name}")
    else:
        delete_file(file_path)  # Delete if file is not allowed
        logging.debug(f"File not allowed, deleted: {file_name}")

# Run the app
if __name__ == "__main__":
    logging.debug("Starting the Flask app...")
    app.run(port=5000)
