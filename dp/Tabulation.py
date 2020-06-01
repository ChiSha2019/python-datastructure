def fi_tab(n):
    fibList = [0] * (n+1)  # list to store result of subproblems
    for k in range(0, n + 1):
        if k <= 1:
            f = k
        else:
            #reuse previous result from memo
            f = fibList[k - 1] + fibList[k - 2]
            #store the new result into memo
        fibList[k] = f
    return fibList[n]


for i in range(0, 10):
    print(fi_tab(i))

