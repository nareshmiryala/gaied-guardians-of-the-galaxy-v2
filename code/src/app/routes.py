from flask import Blueprint, request, jsonify
from app.utils.email_extraction import extract_emails_and_attachments
from app.utils.classification import classify_email
from app.utils.ocr import extract_text_from_pdf, extract_text_from_image
from app.utils.hashing import hash_content

bp = Blueprint('routes', __name__)

@bp.route('/process-emails', methods=['POST'])
def process_emails():
    data = request.json
    emails, attachments = extract_emails_and_attachments(data.get('outlook_account'))
    
    results = []
    seen_hashes = set()

    for email in emails:
        email_hash = hash_content(email['body'])
        if email_hash in seen_hashes:
            continue
        seen_hashes.add(email_hash)

        classification = classify_email(email['body'])
        results.append({
            'subject': email['subject'],
            'classification': classification,
            'attachments': email.get('attachments', [])
        })

        for attachment in email.get('attachments', []):
            if attachment['type'] == 'pdf':
                text = extract_text_from_pdf(attachment['path'])
                results[-1]['attachment_text'] = text
            elif attachment['type'] in ['jpg', 'png']:
                text = extract_text_from_image(attachment['path'])
                results[-1]['attachment_text'] = text

    return jsonify(results)