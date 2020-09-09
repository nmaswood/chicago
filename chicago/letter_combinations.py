from typing import List, Set


MAPPING = {
    "0": "_",
    "1": None,
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

"""
Given a digit string, return all possible letter combinations that the number
could represent.
A mapping of digit to letters (just like on the telephone buttons) is given 
below.
Input:Digit string "23"
Output: {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
"""


def letter_combinations(digits: List[str]) -> Set[str]:
    return set()
