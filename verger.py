#!/usr/bin/python3
# -*- coding: utf-8 -*-

import fractions

_cache = {}

def proba(crow, *fruits, basket_num_fruits=1):
    assert crow + sum(fruits) > 0
    cache_key = (crow, fruits, basket_num_fruits)
    if cache_key in _cache:
        return _cache[cache_key]

    # End of game cases:
    if crow == 0:
        return 0
    elif sum(fruits) == 0:
        return 1

    def _decrement_most_common(L):
        argmax = max((n, i) for (i, n) in enumerate(L))[1]
        if L[argmax] > 0:
            L[argmax] -= 1

    # Probabilities of possible dice outcomes.
    probas = []
    # - dice indicates crow
    probas.append(proba(crow - 1, *fruits,
        basket_num_fruits=basket_num_fruits))
    # - dice indicates basket
    fruits_after_turn = list(fruits)
    for _ in range(basket_num_fruits):
        _decrement_most_common(fruits_after_turn)
    probas.append(proba(crow, *fruits_after_turn,
        basket_num_fruits=basket_num_fruits))
    # - dice indicates a remaining fruit
    fruits_after_turn = list(fruits)
    for i in range(len(fruits_after_turn)):
        if fruits_after_turn[i] > 0:
            fruits_after_turn[i] -= 1
            probas.append(proba(crow, *fruits_after_turn,
                basket_num_fruits=basket_num_fruits))
            fruits_after_turn[i] += 1

    # Dice outcomes are equally likely.
    rv = fractions.Fraction(1, len(probas)) * sum(probas)
    _cache[cache_key] = rv
    return rv

def jeu_du_verger():
    p = proba(9, 10, 10, 10, 10, basket_num_fruits=2)
    print("Jeu du verger")
    print(p)
    print(float(p))

def premier_verger():
    p = proba(6, 4, 4, 4, 4, basket_num_fruits=1)
    print("Premier verger")
    print(p)
    print(float(p))

if __name__ == "__main__":
    jeu_du_verger()
    premier_verger()
