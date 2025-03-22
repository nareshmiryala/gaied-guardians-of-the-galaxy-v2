import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    EMAIL_SERVICE = os.environ.get('EMAIL_SERVICE') or 'outlook'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for uploads