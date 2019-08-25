from collections import Counter

LETTER_SCORE = {
    letter: score
    for letters, score in [
        ("A, E, I, O, U, L, N, R, S, T", 1),
        ("D, G", 2),
        ("B, C, M, P", 3),
        ("F, H, V, W, Y", 4),
        ("K", 5),
        ("J, X", 8),
        ("Q, Z", 10),
    ]
    for letter in letters.split(", ")
}

def score(word):
    return sum(
        LETTER_SCORE[letter] * count
        for letter, count in Counter(word.upper()).items()
    )
