from transformers import pipeline
from app.models import load_config

CONFIG = load_config("config.json")

# Initialize the text classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_email(email_data):
    """Classifies emails based on request types using a language model."""
    detected_request_type = None
    detected_sub_request_type = None
    confidence_score = 0

    content_sources = [email_data["body"]] + email_data["attachments"]
    candidate_labels = [req["request_type"] for req in CONFIG["request_types"]]

    for content in content_sources:
        if content:
            result = classifier(content, candidate_labels)
            detected_request_type = result["labels"][0]
            confidence_score = result["scores"][0] * 100

            for req in CONFIG["request_types"]:
                if req["request_type"] == detected_request_type:
                    sub_candidate_labels = req["sub_request_types"]
                    sub_result = classifier(content, sub_candidate_labels)
                    detected_sub_request_type = sub_result["labels"][0]
                    confidence_score += sub_result["scores"][0] * 30
                    break

    return {
        "request_type": detected_request_type,
        "sub_request_type": detected_sub_request_type,
        "confidence_score": min(confidence_score, 100)
    }