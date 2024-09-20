# Line-Discord-File-Manager

This project is a file management system that integrates with LINE and Discord, designed to automatically collect and download files posted in a LINE group chat, store them temporarily on a server, and then forward them to a specific Discord channel. 

Additionally, it features a web-based user interface where you can view, manage, and delete uploaded files.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Contributing](#contributing)

## About

In Thailand, LINE is one of the most widely used messaging platforms. This project aims to create a solution where files shared in LINE group chats are automatically collected and forwarded to a Discord channel. It also provides a web-based management interface to handle file operations like filtering, viewing, and deleting files.

## Features

- Automatically downloads files from LINE group chats.
- Supports a wide range of file types: PDF, Word (DOC, DOCX), Excel (XLS, XLSX), Text (TXT, MD), ZIP, RAR, PowerPoint (PPT, PPTX), Images (JPEG, PNG).
- Forwards files to a designated Discord channel.
- Provides a web-based interface to view and manage the uploaded files.
- Option to delete files from the server after being posted to Discord.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher.
- A LINE Developer account to create a LINE bot.
- A Discord account with permission to create a bot.
- Access to a server or local environment where you can run Python applications.

## Project Structure

```plaintext
Line-Discord-File-Manager/
│
├── .env                           # Environment variables for LINE and Discord tokens
├── README.md                      # Project overview and setup instructions
├── server.py                      # Main Flask server handling LINE bot interactions
├── discord_bot.py                 # Logic for sending files to Discord
├── file_manager.py                # File handling logic (uploading, deleting, etc.)
├── utils/
│   ├── helpers.py                 # Utility functions for validation and file size formatting
├── database/
│   ├── db.sqlite3                 # SQLite database storing file metadata
│   └── models.py                  # Database models for storing file metadata
├── templates/
│   ├── index.html                 # Frontend HTML template for the file manager
├── static/
│   ├── css/
│   │   └── styles.css             # Styles for the web UI
│   ├── js/
│   │   └── app.js                 # JavaScript functionality for the web UI
├── downloads/                     # Directory where files from LINE are temporarily stored
└── requirements.txt               # Python dependencies
```

## Setup

### 1. Clone the Repository

```
bashCopy codegit clone https://github.com/your-username/Line-Discord-File-Manager.git
cd Line-Discord-File-Manager
```

### 2. Install Dependencies

Use `pip` to install all the required packages from the `requirements.txt` file:

```
bash


Copy code
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the root of your project and add your LINE and Discord credentials:

```
plaintextCopy codeLINE_CHANNEL_SECRET=your_line_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
DISCORD_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_discord_channel_id
```

- `LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` are provided by the LINE Developer Console when creating a bot.
- `DISCORD_TOKEN` is your bot’s token from Discord Developer Portal.
- `DISCORD_CHANNEL_ID` is the ID of the Discord channel where you want to send files.

### 4. Initialize the Database

You need to initialize the SQLite database by running the Flask application once. This will create the required tables:

```
bash


Copy code
python server.py
```

The database will be created in the `database/` folder.

### 5. Running the Project

Start the Flask server to handle incoming requests from LINE and manage file uploads:

```
bash


Copy code
python server.py
```

The server will start running on `http://localhost:5000`.

You can also deploy the application with a production-grade server like `gunicorn`:

```
bash


Copy code
gunicorn --bind 0.0.0.0:5000 server:app
```

## Environment Variables

Make sure the `.env` file contains the following variables:

- **LINE_CHANNEL_SECRET**: Secret key from LINE Developer Console.
- **LINE_CHANNEL_ACCESS_TOKEN**: Access token from LINE Developer Console.
- **DISCORD_TOKEN**: Your bot’s token from Discord.
- **DISCORD_CHANNEL_ID**: ID of the Discord channel where files will be sent.

Example `.env` file:

```
plaintextCopy codeLINE_CHANNEL_SECRET=your_line_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
DISCORD_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_discord_channel_id
```

## Usage

Once the server is running:

1. **LINE Bot**: Add the LINE bot to your group chat, and it will automatically start receiving and downloading files.
2. **Discord Bot**: The bot will post the files to the specified Discord channel after they are received from LINE.
3. **Web Interface**: Navigate to `http://localhost:5000` to view and manage the files.

You can delete files after posting them to Discord or leave them in the server for archiving purposes.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request