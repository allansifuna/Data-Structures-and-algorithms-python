# -*- coding: utf-8 -*-
"""
Created on Sat March 23 23:44:20 2020

@author: allan sifuna,https://github.com/allansifuna
"""

def iCoinChange(amt, den):
    """Iterative coinChange
        :param amt: Amount as int
        :param den: A list of the coin denominations

    """
    den = sorted(den, reverse=True)
    change = {k: 0 for k in den}
    j = 0
    while amt > 0:
        curr = den[j]
        if curr > amt:
            j += 1
            continue
        else:
            change[curr], amt = divmod(amt, curr)
            j += 1
    return change


print(iCoinChange(1800, [500, 200, 100]))


def rCoinChange(amt, den, found={}):
    """Recursive coinChange
        :param amt: Amount as int
        :param den: A list of the coin denominations
        :param found: An optional parameter, A dictionary that maps
        coin denominations to the number of times they will be given.

    """
    den = sorted(den, reverse=True)
    if amt == 0:
        return found
    else:
        curr = den[0]
        found[curr], amt = divmod(amt, curr)
        return rCoinChange(amt, den[1:], found)


print(rCoinChange(1800, [500, 200, 100]))


def weightedCoinChange(amt, den, rems, found={}):
    """Recursive coinChange
        :param amt: Amount as int
        :param den: A list of the coin denominations
        :param rems: A dictionary of coin denomintions: number of coins of same value in stock
        :param found: An optional parameter, A dictionary that maps
        coin denominations to the number of times they will be given.

    """
    den = sorted(den, reverse=True)
    if amt == 0:
        return found
    else:
        curr = den[0]
        f, _ = divmod(amt, curr)
        if f <= rems[curr]:
            found[curr], amt = divmod(amt, curr)
        else:
            found[curr] = rems[curr]
            amt = amt - (curr * rems[curr])
        return weightedCoinChange(amt, den[1:], rems, found)


print(weightedCoinChange(1800, [500, 200, 100], {500: 1, 200: 4, 100: 5}))
