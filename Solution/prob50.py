# %%
# ANSWER: 997651
from utils.prime import get_all_primes_up_to


def main():
    primes = get_all_primes_up_to(99999)
    seen = set(primes)
    prefix_sum = [0]
    for p in primes:
        prefix_sum.append(prefix_sum[-1] + p)

    ans = longest = 0
    for i in range(len(prefix_sum)):
        for j in range(i + longest, len(prefix_sum)):
            diff = prefix_sum[j] - prefix_sum[i]
            if diff in seen and j - i > longest:
                longest = j - i
                ans = diff
                print(longest)
    # print(prefix_sum)
    return ans

    # ans = longest = 0
    # ptr = 0
    # for i, prefix in enumerate(prefix_sum):
    #     diff = prefix_sum[j] - prefix_sum[ptr]
    #     if diff in seen:
    #         longest = j - i
    #         ans = diff
    #     else:
    #         ptr += 1
    # print(prefix_sum)
    # return ans


print(main())

# %%
