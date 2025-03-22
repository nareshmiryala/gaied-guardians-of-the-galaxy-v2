# Gen AI Email Classifier

This project is a Flask-based application designed to classify emails using OpenAI's GPT-4 and LangChain. It extracts emails and attachments from Outlook, processes them, and classifies their content. Additionally, it includes functionality for extracting text from PDFs and images via OCR and detecting duplicate emails using content hashing.

## Features

- Extracts emails and attachments from Outlook.
- Classifies email content using OpenAI GPT-4.
- Extracts text from PDF documents and images using OCR.
- Detects duplicate emails using content hashing.

## Project Structure

```
gen-ai-email-classifier
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── utils
│   │   ├── email_extraction.py
│   │   ├── classification.py
│   │   ├── ocr.py
│   │   └── hashing.py
├── templates
│   └── index.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gen-ai-email-classifier
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your configuration in `config.py`, including API keys and any necessary environment variables.

## Usage

1. Run the application:
   ```
   python app/main.py
   ```

2. Access the web interface at `http://127.0.0.1:5000`.

3. Use the `/process-emails` endpoint to process and classify emails.
