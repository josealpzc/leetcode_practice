def lengthOfLastWord(s):
    counter = 0
    
    for character in s:
        if(character!= ' '):
            counter +=1
            print('char: '+character)
            print('counter: ',counter)
            tmp = counter
        else:
            if counter != 0:
                tmp = counter 
            counter = 0
    return tmp
s = "luffy is still joyboy"

print(lengthOfLastWord(s))
