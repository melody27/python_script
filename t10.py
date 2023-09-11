


def com(n):
    left = 0.0
    for i in range(n,21):
        if (i-1 == 0):continue
        left += (n-1)/(i-1)
    # return (21-n)/20*left/(21-n)
    return 1/20*left



if __name__ == "__main__":
    for i in range(1,21):
        print(str(i)+":"+str(com(i)))