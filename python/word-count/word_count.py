from collections import Counter
from functools import partial
import re


STRIP_LEFT_QUOTE = partial(re.sub, r"^'", "")
STRIP_RIGHT_QUOTE = partial(re.sub, r"'$", "")
UNQUOTE = lambda word: STRIP_LEFT_QUOTE(STRIP_RIGHT_QUOTE(word))


def count_words(sentence):
    words = re.findall(r"[a-z0-9']+", sentence.lower())
    return Counter(map(UNQUOTE, words))
