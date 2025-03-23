# gen-ai-email-classifier

## Overview
The gen-ai-email-classifier is a web application designed to classify emails using artificial intelligence techniques. It extracts content from various email formats, processes the data, and classifies it based on predefined categories.

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
│   ├── index.html
│   └── output.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── requirements.txt
├── config.py
└── README.md
```

## Features
- **Email Extraction**: Extracts content from various email formats.
- **Classification**: Classifies emails based on their content using AI algorithms.
- **Optical Character Recognition (OCR)**: Extracts text from images attached to emails.
- **User Interface**: A simple web interface for users to interact with the application.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gen-ai-email-classifier.git
   ```
2. Navigate to the project directory:
   ```
   cd gen-ai-email-classifier
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python app/main.py
   ```
2. Open your web browser and go to `http://localhost:5000` to access the application.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.