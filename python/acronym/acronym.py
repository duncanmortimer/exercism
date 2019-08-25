import re

def abbreviate(words):
    return "".join(match[0] for match in re.findall(r"[A-Z']+", words.upper()))
