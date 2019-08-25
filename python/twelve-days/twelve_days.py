GIFTS = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]

ORDINALS = [
    "first", "second", "third", "fourth", "fifth", "sixth",
    "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
]

def gift_list(verse):
    return ''.join(reversed(GIFTS[:1] + (["and "] if verse > 1 else []) + GIFTS[1:verse]))

def opening_line(verse):
    return f"On the {ORDINALS[verse - 1]} day of Christmas my true love gave to me:"

def full_verse(verse):
    return f"{opening_line(verse)} {gift_list(verse)}"

def recite(start_verse, end_verse):
    return [full_verse(verse) for verse in range(start_verse, end_verse + 1)]
