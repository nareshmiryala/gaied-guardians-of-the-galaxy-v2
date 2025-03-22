class Email:
    def __init__(self, subject, sender, recipients, body, attachments):
        self.subject = subject
        self.sender = sender
        self.recipients = recipients
        self.body = body
        self.attachments = attachments

class ClassificationResult:
    def __init__(self, email_id, classification, confidence):
        self.email_id = email_id
        self.classification = classification
        self.confidence = confidence

class ProcessedEmail:
    def __init__(self, email, classification_result):
        self.email = email
        self.classification_result = classification_result

class DuplicateEmail:
    def __init__(self, email_id, hash_value):
        self.email_id = email_id
        self.hash_value = hash_value