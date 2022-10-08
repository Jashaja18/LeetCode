# import sys
# # import numpy as np
# # import pandas as pd
# # from sklearn import ...
# #Your program should read lines from standard input. Each line contains a list of space-delimited numbers, followed by a colon, followed by the indexes to be swapped. The first position in the list is at index 0. If there is more than one pair of indexes to be swapped, process each pair in the order they appear in the input, left to right.
#
# # 1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3
# # 1 4 3 2 5 6 7 8 9 10
#
# for line in sys.stdin:
#     line = line.strip()
#     if line:
#         line = line.strip().split(':')
#         nums = line[0].split(' ')
#         swaps = line[1].split(', ')
#         for swap in swaps:
#             swap = swap.split('-')
#             nums[int(swap[0])], nums[int(swap[1])] = nums[int(swap[1])], nums[int(swap[0])]
#     print(' '.join(nums))

import typing as t
import sys
from typing import Tuple

Value = t.Union[str, int]
VALID_INT_CHARS = "0123456789"
SPECIAL_CHARS = ",()"


# You may need to modify this function for it to work properly
def consumeNextToken(s: str) -> tuple[None, None] | tuple[None, str] | tuple[str, str] | tuple[int, str]:
    # YOUR CODE HERE
    # RETURN A TUPLE OF THE TOKEN AND THE REMAINDER OF THE STRING
    # IF THERE IS NO TOKEN RETURN (None, None)
    # IF THERE IS NO REMAINDER RETURN (TOKEN, None)
    # IF THERE IS A TOKEN AND A REMAINDER RETURN (TOKEN, REMAINDER)
    if s[0] in SPECIAL_CHARS:
        return s[0], s[1:]
    elif s[0] in VALID_INT_CHARS:
        return int(s[0]), s[1:]
    else:
        return None, None


def main():
    # YOUR CODE HERE
    # READ INPUT FROM STDIN, THERE WILL ONLY BE ONE LINE OF INPUT WITH ONE EXPRESSION
    # PRINT RESULT TO STDOUT
    for line in sys.stdin:
        line = line.strip()
        if line:
            while line:
                token, line = consumeNextToken(line)
                print(token)



    # FOR VECTORS YOU CAN TO STRING YOUR VECTOR RESULT AND THEN USE str.replace(' ', '') TO REMOVE THE SPACES
    ...


