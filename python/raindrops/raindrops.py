from typing import Tuple

FACTOR_TO_SOUND = (
    (3, "Pling"),
    (5, "Plang"),
    (7, "Plong"),
)

def convert(number: int):
    sounds: Tuple[str] = [
        sound
        for factor, sound in FACTOR_TO_SOUND
        if number % factor == 0
    ]
    return "".join(sounds) if sounds else str(number)
