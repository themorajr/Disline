import os

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'md', 'zip', 'rar', 'ppt', 'pptx'}

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to format file sizes into a human-readable format
def format_size(size_in_bytes):
    size_in_kb = size_in_bytes / 1024
    if size_in_kb < 1024:
        return f"{size_in_kb:.2f} KB"
    size_in_mb = size_in_kb / 1024
    return f"{size_in_mb:.2f} MB" if size_in_mb < 1024 else f"{size_in_mb / 1024:.2f} GB"

# Function to delete files after processing (optional)
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except OSError as e:
        print(f"Error deleting file {file_path}: {e}")
