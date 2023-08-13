def plusOne(digits):
    return_list = []
    mult = 1
    total = 0
    for i in range (0, len(digits)):
        currentValue = digits[len(digits)-1-i]
        value = currentValue * mult
        mult = mult * 10
        total = total + value    
    total = total + 1
    """
    a = str(total) 
    for element in a:
        print(element)
    """

    while(total !=0):
        print('This is the current total %s'%(total))

        a = total % 10
        return_list.insert(0,a)
        total = (total - a ) // 10 
        total = int(total)
        print('Total %s' %(total))

        print(return_list)

digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3] 
plusOne(digits)
