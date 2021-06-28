# Calculating the number of circulating tokens at a given block height
# Bitcoin tokens are generated through block rewards.
# Initially, the block reward was 50 BTC, and the reward halves every 210,000 blocks.
# Thus at Block 1 there were 50 BTC in circulation. At Block 2, there were 100 BTC etc.
# Write a script called “num_BTC.py” that contains a function “num_BTC.”
# The function should take as input a block height (integer) and
# return the total number of tokens that have been mined so far
# (up to and including the given block). The returned value should be a float.

import math

def num_BTC(b):

    block_size_break = 210000

    modulo_block = b % block_size_break

    int_block = int(b / block_size_break)

    block_reward = 50.00
    halvening = 2
    c = float(0)

    for i in range(int_block):
        c = c + block_reward * block_size_break
        block_reward = block_reward / halvening
    c = c + modulo_block * block_reward
    return c
