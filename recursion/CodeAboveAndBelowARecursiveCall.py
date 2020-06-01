def sampleMethod(n):
    if n <= 1:
        print("basecase hit with {}".format(n))
    else:
        print("code above with {}".format(n))
        sampleMethod(n - 1)
        print("code below with {}".format(n))


if __name__ == "__main__":
    sampleMethod(5)
