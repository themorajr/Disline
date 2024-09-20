import os

# Define allowed file types and maximum file size (in bytes)
ALLOWED_FILE_TYPES = [
    "image/jpeg", "image/png", "application/pdf",
    "application/msword",  # Word (doc)
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # Word (docx)
    "application/vnd.ms-excel",  # Excel (xls)
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # Excel (xlsx)
    "application/vnd.ms-powerpoint",  # PowerPoint (ppt)
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",  # PowerPoint (pptx)
    "text/plain",  # TXT
    "text/markdown",  # MD
    "application/zip",  # ZIP
    "application/x-rar-compressed"  # RAR
]
MAX_FILE_SIZE = 25 * 1024 * 1024  # 10 MB

# Function to check if a file is allowed based on its type and size
def is_allowed_file(file_path, file_type):
    # Check if the file type is allowed
    if file_type not in ALLOWED_FILE_TYPES:
        print(f"File type '{file_type}' is not allowed.")
        return False

    # Check if the file size is within the allowed limit
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE:
        print(f"File size exceeds the allowed limit: {file_size} bytes.")
        return False

    return True

# Function to delete a file from the server
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' not found for deletion.")

if __name__ == "__main__":
    # Example usage (replace with actual path and file type)
    test_file_path = 'downloads/sample_file.bin'
    test_file_type = 'application/msword'
    
    # Check if the file is allowed
    if is_allowed_file(test_file_path, test_file_type):
        print(f"File '{test_file_path}' is allowed.")
    else:
        print(f"File '{test_file_path}' is not allowed.")

    # Delete the file after processing (if needed)
    delete_file(test_file_path)
