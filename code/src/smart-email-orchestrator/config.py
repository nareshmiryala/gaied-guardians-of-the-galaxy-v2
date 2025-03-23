import os

UPLOAD_FOLDER = "uploaded_emails"
OUTPUT_FILE = "output.json"
CONFIG_FILE = "config.json"

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)