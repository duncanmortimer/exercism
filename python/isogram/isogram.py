import re

def is_isogram(string: str) -> bool:
    relevant_characters = re.sub(r"[^a-z]", "", string.lower())
    return len(set(relevant_characters)) == len(relevant_characters)
