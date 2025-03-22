import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_email(email_body):
    # Example prompt for classification
    prompt = f"""
    You are an AI assistant that classifies emails.
    Extract:
    - Request Type
    - Sub Request Type
    - Important fields (amount, due dates, etc.)
    Example Email: "{email_body}"
    Response:
    """
    
    # Use OpenAI GPT-4 for classification
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    # Parse the response
    classification = response.choices[0].text.strip()
    
    return classification