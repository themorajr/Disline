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
