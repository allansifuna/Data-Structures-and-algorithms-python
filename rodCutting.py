# -*- coding: utf-8 -*-
"""
Created on Thur March 19 12:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""


def rodcutting(toConsider, weights, length):
    # print("H")

    if toConsider == [] or length == 0:
        # print("B")
        result = (0, ())
    elif toConsider[0] > length:
        # print("A")
        result = rodcutting(toConsider[1:], weights, length)
    else:
        # print("C")
        nextItem = toConsider[0]
        wv, wc = rodcutting(toConsider, weights, length - nextItem)
        wv += weights[nextItem]
        wov, woc = rodcutting(toConsider[1:], weights, length)
        if wv > wov:
            result = (wv, wc + (nextItem,))
        else:
            result = (wov, woc)
    print(result)
    return result


s = {k: v for k, v in zip([1, 2, 3, 4], [1, 5, 8, 9])}
a = rodcutting([1, 2, 3, 4], s, 10)
print(a)
