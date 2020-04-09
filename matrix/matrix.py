"""
Given a string representing a matrix of numbers, return the rows and columns of that matrix.
code should be able to spit out:

    1. A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
    2. A list of the columns, reading each column top-to-bottom while moving from left-to-right.
"""


class Matrix:
    """this is the constructor of sorts in python, this method will run soon
    after the class is instanciated and the matrix string is assigned to the
    matrix instance variable of the object."""

    def __init__(self, matrix_string):
        self.matrix = matrix_string

    def row(self, index):
        """
        A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows
        """
        index = index - 1
        split_lines = self.matrix.splitlines()
        split_nums = str(split_lines[index]).split()
        for i in range(0, len(split_nums)):
            split_nums[i] = int(split_nums[i])
        return split_nums

    def column(self, index):
        """
        A list of the columns, reading each column top-to-bottom while moving from left-to-right.
        """
        index = index - 1
        col_vals = []
        split_lines = self.matrix.splitlines()
        for line in split_lines:
            line = line.split()
            for i in range(0, len(line)):
                line[i] = int(line[i])
            col_vals.append(line[index])
        return col_vals
