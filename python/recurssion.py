def count_to_cero(n):
    """
    This function prints a count down from N to 0
    using recurssion.
    """
    if(n < 0 ):
        return 1
    else:
        print(n)
        count_to_cero(n-1)

def fibonacci(n):
    """
    This function print a fibonnaci serie.
    """
    a=0
    b=1
    cnt = 0
    print(a)
    print(b)
    while (cnt < n):
        if cnt !=1:
            c = a + b
            print(c)
            a = b
            b = c
        cnt +=1
def recursive_fibonacci(n):
    """
    This function print fibonacci serie using recurssion.
    """
    if (n==0):
        return n
    elif(n==1):
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

def factorial(n):
    """
    This funtion prints the fa
    """
cnt = 0
value=5
while(cnt <=value):
    print(recursive_fibonacci(cnt))
    cnt+=1

