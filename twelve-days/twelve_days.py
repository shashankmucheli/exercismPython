def recite(start_verse, end_verse):
    """
    Output the lyrics to 'The Twelve Days of Christmas'.
    """
    return [recite_builder(i) for i in range(start_verse, end_verse+1)]


def recite_builder(lyric):
    """
    This is a builder function that takes one arguement and builds the lyrics upto the given number.
    """
    # if end_verse == 1:
    #     return str("On the first day of Christmas my true love gave to me: "
    #                "a Partridge in a Pear Tree.")
    nth = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    verse = [
        "and a Partridge in a Pear Tree.",
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
        "twelve Drummers Drumming, "
    ]
    tw_days = "On the "+nth[lyric]+" day of Christmas my true love gave to me: "
    for n in range(lyric-1, -1, -1):
        tw_days+=verse[n]
    print(tw_days)
    return str(tw_days)
