"""
raindrops is simple python program to generate specific sounds if a given number is a factor of either 3,
5 or 7 and returns a string
"""


def convert(number):
    ret_val = ''
    if number % 3 == 0:
        ret_val += "Pling"
    if number % 5 == 0:
        ret_val += "Plang"
    if number % 7 == 0:
        ret_val += "Plong"
    # if number is not a factor of any of the three numbers. i.e., 3,5,7 then we convert the number to a string and
    # return the value
    if not ret_val:
        ret_val += str(number)
    return ret_val
