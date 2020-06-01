# cachdict is a dictionary of n elements
def Fi_dp(n, cachdict):
    if n <= 1:
        return n
    if n not in cachdict:
        cachdict[n] = Fi_dp(n - 1, cachdict) + Fi_dp(n - 2, cachdict)
    return cachdict[n]


myDict = {}

for i in range(0, 10):
    print(Fi_dp(i, myDict))
