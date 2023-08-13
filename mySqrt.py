def mySqrt(self,x:int)-> int:
    result= 0
    cnt=1
    while(result <= x):
        result =  cnt ** cnt
        cnt += 1
        print(result)
               
def main():
    print("Hello world!")

if __name__=="__main__":
    main()
