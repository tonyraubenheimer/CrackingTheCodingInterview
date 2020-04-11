import math

class LinkedList:
    header = None
    
    def __init__(self):
        pass
       
    def printLinkedList(self):
        runner = self.header
        while(runner is not None):
            print(runner.value)
            runner = runner.next
            
    def appendToList(self, value):
        new = Node(value)
        if self.header == None: #empty linked list
            self.header = new
        else:
            runner = self.header
            while(runner.next is not None):
                runner = runner.next
            runner.next = new 
            
    def appendNodeToList(self, node):
        if self.header == None: #empty linked list
            self.header = node
        else:
            runner = self.header
            while(runner.next is not None):
                runner = runner.next
            runner.next = node 
   
    def deleteNode(self, to_delete):
        #if value to delete is header, just update linked list header
        if(self.header.value == to_delete):
            self.header = self.header.next
            return 1
        #loop through linked list for to_delete
        runner = self.header    
        while(runner.next is not None):
            if(runner.next.value == to_delete):
                runner.next = runner.next.next
                return 1
            runner = runner.next
            
        return 0 #to_delete not found; nothing deleted
    
    def length(self):
        runner = self.header
        if(runner is None):
            return 0
        length = 1
        while(runner.next is not None):
            runner = runner.next
            length = length+1
        return length
    
    def getTail(self):
        runner = self.header
        while(runner.next is not None):
            runner = runner.next
        return runner
    
    #2.2 O(n) time complexity
    #O(1) space complexity (no additional space needed)
    #Note that 1st to last (k=1) returns the last element, k=2 returns penultimate, etc
    def kthToLast(self, k):
        runner = self.header
        length = 1
        while(runner.next is not None):
            length = length+1
            runner = runner.next

        runner = self.header
        current = 1
        while(current < length-k+1):
            current = current+1
            runner = runner.next
        return runner.value
    
    #2.3
    def deleteMiddleNode(self, node):
        runner = node
        while(runner.next.next is not None):
            runner.value = runner.next.value
            runner = runner.next
        runner.value = runner.next.value
        runner.next = None
        
    #2.4 O(n) time complexity
    #O(1) space complexity
    def partition(self, x):
        current = self.header
        prev = None
        i=0
        while(i<self.length()):
            if(current.value >= x):
                self.getTail().next = Node(current.value)
                try:
                    prev.next = current.next
                    prev = current
                except AttributeError:
                    self.header = current.next
            current = current.next
            i=i+1
    
    #2.5
    def sumLists(self, ll2, isForward):
        output = LinkedList()
        if(not isForward):
            cur1 = self.header
            cur2 = ll2.header
            left_over = 0
            while(cur1 is not None or cur2 is not None):
                try:
                    val1 = cur1.value
                except AttributeError:
                    val1 = 0
                try:
                    val2 = cur2.value
                except AttributeError:
                    val2 = 0
                cur_sum = val1+val2+left_over
                output.appendToList(cur_sum%10)
                left_over = cur_sum/10
                try:
                    cur1 = cur1.next
                except AttributeError:
                    pass
                try:
                    cur2 = cur2.next
                except AttributeError:
                    pass
            if(left_over>0):
                output.appendToList(left_over)
        else:
            try:
                num1 = self.header.value
                cur1 = self.header.next
            except AttributeError:
                num1 = 0
                cur1 = None
            try:
                num2 = ll2.header.value
                cur2 = ll2.header.next
            except AttributeError:
                num2 = 0
                cur2 = None
            while(cur1 is not None or cur2 is not None):
                try:
                    num1 = num1*10 + cur1.value
                except AttributeError:
                    pass
                try:
                    num2 = num2*10 + cur2.value
                except AttributeError:
                    pass
                try:
                    cur1 = cur1.next
                except AttributeError:
                    pass
                try:
                    cur2 = cur2.next
                except AttributeError:
                    pass
            sum = num1 + num2
            try:
                digits = int(math.log10(sum))+1
            except ValueError:
                digits = 0
            while(digits > 0):
                to_add = sum/int(math.pow(10, digits-1))
                sum = sum - to_add*int(math.pow(10, digits-1))
                output.appendToList(to_add)
                digits = digits-1  
        return output
    
    #2.6 O(n) time complexity
    #O(n) space complexity
    def isPalindrome(self):
        runner = self.header
        reverse = LinkedList()
        while(runner is not None):
            prev = reverse.header
            reverse.header = Node(runner.value)
            reverse.header.next = prev
            runner = runner.next
            
        i = 0
        runner = self.header
        runner2 = reverse.header
        while(i < self.length()):
            if(runner.value != runner2.value):
                return False
            runner = runner.next
            runner2 = runner2.next
            i=i+1
        return True
    
    #2.7
    def intersection(self, ll2):
        #runner1 should be for the longer linked list, runner2 for the shorter
        if(self.length() > ll2.length()):
            longer = self
            shorter = ll2
        else:
            longer = ll2
            shorter = self
        runner1 = longer.header
        runner2 = shorter.header
            
        #check if tails are the same, implying the linked lists have an intersection
        while runner1.next is not None:
            runner1 = runner1.next   
        while runner2.next is not None:
            runner2 = runner2.next 
        if runner1 is not runner2:
            return None
        
        #line the two linked lists up by moving the longer list's runner forward
        offset = abs(self.length()-ll2.length())
        i=0
        runner1 = longer.header
        runner2 = shorter.header #set this up for later
        while i < offset:
            runner1 = runner1.next
            i+=1
        
        #now the linked lists are lined up, keep comparing runners until we find the intersection
        while runner1.next is not None:
            if runner1 is runner2:
                return runner1
            runner1 = runner1.next
            runner2 = runner2.next
    
        print('error') #in theory, we shouldn't ever reach this point
        
    #2.8
    def detectLoop(self):
        #check special case where the only node points to itself
        if self.header.next == self.header:
            return self.header
        
        #fast runner will iterate through ll twice before slow runner iterates forward once
        #if they are the same, the loop origin has been located
        runner_slow = self.header
        runner_fast = self.header.next
        incrementSlow = False
        while True:
            if runner_fast is None: #there is no loop
                return None
            if runner_fast == runner_slow:
                return runner_slow
            runner_fast = runner_fast.next
            if incrementSlow:
                runner_slow = runner_slow.next
            incrementSlow = not incrementSlow
    
    def returnAsList(self):
        l = []
        runner = self.header
        while runner is not None:
            l.append(runner.value)
            runner = runner.next
        return l
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class DoublyLinkedList:
    header = None
    tail = None
    
    def __init__(self):
        pass
    
    def appendToList(self, value):
        new_node = DoublyLinkedNode(value)
        if (self.header == None):
            self.header = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node   
            
    def deleteNode(self, value):
        runner = self.header
        
        #delete head
        if(self.header.value == value):
            self.header = self.header.next
            return 1
        
        #delete tail
        if(self.tail.value == value):
            self.tail = self.tail.prev
            self.tail.next = None
            return 1
            
        while(runner is not None):
            if(runner.value == value):
                temp = runner.prev
                runner.next.prev = runner.prev
                temp.next = runner.next
                return 1
            runner = runner.next
            
        #nothing deleted
        return 0
            
    def traverseList(self, is_forward):
        if(is_forward):
            runner = self.header
            while(runner is not None):
                print(runner.value)
                runner = runner.next
        else:
            runner = self.tail
            while(runner is not None):
                print(runner.value)
                runner = runner.prev
    
    #2.1 O(n*n) time complexity
    #O(n) space complexity     
    def removeDups(self):
        check = self.header
        while(check is not None):
            runner = check.next
            while (runner is not None):
                if(check.value == runner.value):#delete runner
                    if(runner == self.header):
                        runner.next.prev = None
                        self.header = self.header.next
                    elif(runner == self.tail):
                        runner.prev.next = None
                        self.tail = self.tail.prev
                    else:
                        temp = runner.prev
                        runner.next.prev = runner.prev
                        temp.next = runner.next    
                runner = runner.next
            check = check.next
    
class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
def main():
    
    ll = LinkedList()
    #ll2 = LinkedList()
    
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    n11 = Node(11)
    
    #ll.appendNodeToList(n0)
    #ll.appendNodeToList(n1)
    #ll.appendNodeToList(n2)
    #ll.appendNodeToList(n3)
    #ll.appendNodeToList(n4)
    ll.appendNodeToList(n5)
    ll.appendNodeToList(n6)
    ll.appendNodeToList(n7)
    ll.appendNodeToList(n8)
    ll.appendNodeToList(n9)
    ll.appendNodeToList(n10)
    ll.appendNodeToList(n11)
    ll.appendNodeToList(n6)
    
    print(ll.detectLoop().value)
    
    #ll2.appendNodeToList(n0)
    #ll2.appendNodeToList(n4)
    #ll2.appendNodeToList(n5)
    #ll2.appendNodeToList(n6)
    #ll2.appendNodeToList(n6)
    #ll2.appendNodeToList(n7)
    #ll2.appendNodeToList(n8)
    #ll2.appendNodeToList(n9)
    #ll2.appendNodeToList(n10)
    #ll2.appendNodeToList(n11)
    
    #n = Node(1)
    #for i in range(10,0,-1):
        #ll.appendToList(i*i)
    #ll.printLinkedList()
    #ll.appendToList('a')
    #ll.appendToList(6)
    #ll.appendToList('a')
    #ll.appendNodeToList(n)
    #ll.appendToList(1)
    #ll2.appendToList(1)
    #ll2.appendToList(2)
    #ll2.appendToList(9)
    #ll2.appendToList(9)
    #ll2.appendNodeToList(n)
    #ll2.appendToList(9)
    #print()
    #output = ll.sumLists(ll2, True)
    
    #ll.partition(4)
    #ll.printLinkedList()
    
    
    
if __name__ == '__main__':
    main()
     
        
