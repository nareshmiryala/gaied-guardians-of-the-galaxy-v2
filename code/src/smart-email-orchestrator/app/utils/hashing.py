def hash_string(input_string: str) -> str:
    import hashlib
    return hashlib.sha256(input_string.encode()).hexdigest()

def verify_hash(input_string: str, hashed_string: str) -> bool:
    return hash_string(input_string) == hashed_string