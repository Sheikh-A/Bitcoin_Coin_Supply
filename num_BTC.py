import math

def num_BTC(b):
    block_half = 210000
    block_start = 50

    integer_value = int(b / block_half)
    mod_value = b % block_half

    btc_rewards = 50.0
    c = float(0)

    for i in range(integer_value):
        c = c + (btc_rewards * block_half)
        btc_rewards = btc_reward / 2

    c = c + mod_value * btc_rewards

    return c


# Calculating the number of circulating tokens at a given block height
# Bitcoin tokens are generated through block rewards.
# Initially, the block reward was 50 BTC, and the reward halves every 210,000 blocks.
# Thus at Block 1 there were 50 BTC in circulation. At Block 2, there were 100 BTC etc.
# Write a script called “num_BTC.py” that contains a function “num_BTC.”
# The function should take as input a block height (integer) and
# return the total number of tokens that have been mined so far
# (up to and including the given block). The returned value should be a float.
