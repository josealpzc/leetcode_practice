def removeElement(nums, val):
    last = len(nums)-1
    current = 0

    while(current < last):
        if(nums[current] == val and nums[last]!=val):
            tmp = nums[current]
            nums[current] = nums[last]
            nums[last] = tmp

        if(nums[current] == val and nums[last]==val):
            print('aqui')
            last -=1
            tmp = nums[current]
            nums[current] = nums[last]
            nums[last] = tmp
        current+=1
    return current

def removeElement2(nums,val):
    last = len(nums)-1
    current = 0
    cnt = 0
    if(len(nums) ==1 and nums[0] == val):
        return current
    elif(len(nums)==1 and nums[0]!=val):
        return current +1
    else:
        while(current<=last):
            if(nums[current]==val):
                print('current: ',current)
                cnt +=1
                print('nums: ',nums)
                if(current!=last):
                    while(nums[last] ==val and last!=current):
                        cnt+=1
                        last-=1
                    tmp = nums[current]
                    nums[current]=nums[last]
                    nums[last] = tmp
                    last-=1
            current+=1
        return (len(nums)-cnt)
"""
nums=[2,3,3]
print(removeElement2(nums,3))
print(nums)
print()
"""

nums=[0,1,2,2,3,0,4,2]
print(removeElement2(nums,2))
print(nums)
print()

"""
nums=[4,5]
print(removeElement2(nums,5))
print(nums)
print()
"""

