def is_isogram(string):
    """
    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
    """
    if len(string) <= 0:
        return True
    d = []
    for a in string:
        s = a.lower()
        if s == " " or s == "-":
            print(s)
        elif s not in d:
            d.append(s)
        else:
            return False
    return True