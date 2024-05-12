# ANSWER: 73682
from functools import cache

coins = [1, 2, 5, 10, 20, 50, 100, 200]


@cache
def dfs(ptr=0, rem=200):
    if rem == 0:
        return 1
    cnt = 0
    for i in range(ptr, len(coins)):
        if coins[i] > rem:
            continue
        cnt += dfs(i, rem - coins[i])
    return cnt


print(dfs())
