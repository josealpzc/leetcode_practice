class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,val):
        newNode = ListNode(val)
        if(self.head):
            current = self.head
            while(current.next!=None):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def printList(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next            

def generateList(list1):
    ll=LinkedList()
    for element in list1:
        ll.insert(element)
    return ll 

def mergeTwoLists(list1, list2):
    head1 = list1.head
    print(head1.val)

        
my_list1 = [1,2,4]
my_list2 = [1,3,4]
list1 = generateList(my_list1)
list2 = generateList(my_list2)

print(list1.head.val)
#mergeTwoLists(list1,list2)



