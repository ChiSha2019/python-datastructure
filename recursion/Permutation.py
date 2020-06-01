"""
array = [1, 2, 3]
# use iteration
for i in range(3):
    permArr = [i + 1]
    for j in range(3):
        if j != i:
            permArr.append(j + 1)
            for k in range(3):
                if k != j and k != i:
                    permArr.append(k + 1)
                    print(permArr)
                    permArr.pop()
            permArr.pop()
"""


# use recursion
def permutation(origArr, permArr):
    if len(permArr) >= len(origArr):
        print(permArr)
    else:
        for num in origArr:
            if not isNumInArray(num, permArr):
                permArr.append(num)
                permutation(origArr, permArr)
                permArr.pop()


# can use a hashmap to decrease the time complexity
def isNumInArray(num, arr):
    for item in arr:
        if num == item:
            return True
    return False


# drive code
permutation([1, 2, 3, 4], [])
