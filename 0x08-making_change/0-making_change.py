#!/usr/bin/python3
"""Making Change"""


def make_change(coins, total):
    """
    Returns the minimum number of coins required to make the given total,
    or -1 if it's not possible to make the total with the given coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    remaining_total = total

    for coin in coins:
        if remaining_total >= coin:
            count += remaining_total // coin
            remaining_total %= coin

    if remaining_total == 0:
        return count
    else:
        return -1

