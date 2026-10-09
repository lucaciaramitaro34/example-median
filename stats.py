#!/usr/bin/env python3
'''
Basic descriptive statistics for a sequence of numbers.

Each function takes a non-empty list or tuple and returns a single
number.  None of them modify their argument.
'''


def mean(data):
    '''
    The arithmetic mean of data.

    >>> mean([1, 2, 3, 4])
    2.5
    '''
    return sum(data) / len(data)


def median(data):
    '''
    The middle value of data when sorted.

    >>> median([3, 1, 2])
    2
    >>> median([1, 2, 3, 4])
    2.5
    '''
    ordered = sorted(data)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 0:
        return (ordered[mid - 1] + ordered[mid]) / 2
    return ordered[mid]


def mode(data):
    '''
    The most common value in data.

    Ties are broken by first appearance.

    >>> mode([1, 2, 2, 3])
    2
    '''
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    best = None
    for value in data:
        if best is None or counts[value] > counts[best]:
            best = value
    return best
