import hashlib

def hash_content(content: str) -> str:
    """Generate a SHA256 hash of the given content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def is_duplicate(existing_hashes: set, new_content: str) -> bool:
    """Check if the new content is a duplicate based on its hash."""
    new_hash = hash_content(new_content)
    return new_hash in existing_hashes