"""
Calculate the Hamming Distance between two DNA strands.
Implementation:
The Hamming distance is only defined for sequences of equal length, so an attempt to calculate it between sequences of different lengths should not work. The general handling of this situation (e.g., raising an exception vs returning a special value) may differ between languages.
"""


def distance(strand_a, strand_b):
    hamming_distance = 0
    if len(strand_a) == len(strand_b):
        for i in range(0, len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hamming_distance += 1
        return hamming_distance
    else:
        raise ValueError("Length of strand A and B are not same")
