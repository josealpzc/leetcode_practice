def addBinary(a,b):
    aLen = len(a)
    bLen = len(b)

    max = 0

    if(aLen > bLen):
        max = aLen
    else:
        max = bLen

    for i in range(max):
        print(i)


