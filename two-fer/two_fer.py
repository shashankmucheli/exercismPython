"""
Two-fer or 2-fer is short for two for one. One for you and one for me.

Given a name, return a string with the message:

One for X, one for me.

Where X is the given name.

However, if the name is missing, return the string:

One for you, one for me.

"""


# two_fer is an overloaded function which works with or without the name parameter.
def two_fer(name=None):
    if name is not None:
        return "One for "+name+", one for me."
    else:
        return "One for you, one for me."
