from collections import deque
from collections import OrderedDict
from CrackingTheCodingInterview.ChapterTwo import LinkedList

class Stack:
    
    def __init__(self):
        self.items = []
        self.min = None
    
    def pop(self):
        popped = self.items.pop()
        if(popped == self.min):
            self.min = self.minElement()
        return popped
    
    def push(self, item):
        self.items.append(item)
        if(item < self.min or self.min == None):
            self.min = item
        
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def getStack(self):
        return self.items
    
    def size(self):
        return len(self.items)
    
    def minElement(self):
        min = None
        for item in self.items:
            if(item < min or min == None):
                min = item
        return min
    
#3.5
class SortStack:
    def __init__(self):
        self.sorted = Stack()
        self.stack = Stack()
        
    def push(self, item):
        numPopped = 0
        while(not self.sorted.isEmpty() and self.sorted.peek() < item):
            self.stack.push(self.sorted.pop())
            numPopped = numPopped+1
        self.sorted.push(item)
        while(numPopped > 0):
            self.sorted.push(self.stack.pop())
            numPopped = numPopped-1
        self.stack.push(item)
        
    def pop(self):
        popped = self.stack.pop()
        numPopped = 0
        while(not self.sorted.isEmpty() and self.sorted.peek() < popped):
            self.stack.push(self.sorted.pop())
            numPopped = numPopped+1
        self.sorted.pop()
        while(numPopped > 0):
            self.sorted.push(self.stack.pop())
            numPopped = numPopped-1
    
    def peek(self):
        return self.stack.peek()
    
    def isEmpty(self):
        return self.stack.isEmpty()
    
    def getStacks(self):
        d = OrderedDict()
        d['stack'] = self.stack.items
        d['sorted'] = self.sorted.items
        return d
    
#3.3 
class SetOfStacks:
    MAX_STACK_LEN = 2
    
    def __init__(self):
        self.stacks = []
        self.stacks.append(Stack())
        
    def pop(self):
        popped = self.stacks[-1].pop()
        if(len(self.stacks[-1].items) == 0):
            self.stacks.pop()
        if(self.stacks == []):
            self.stacks.append(Stack())
        return popped
    
    def push(self, item):
        if(len(self.stacks[-1].items) == self.MAX_STACK_LEN):            
            self.stacks.append(Stack())
        self.stacks[-1].items.append(item)
        
    def peek(self):
        return self.stacks[-1].items[-1]
        
    def isEmpty(self):
        return self.stacks[0].isEmpty()
    
    def size(self):
        num = 0
        for s in self.stacks:
            for item in s.items:
                num = num+1
        return num
    
    def getSetOfStacks(self):
        d = OrderedDict()
        i = 0
        for s in self.stacks:
            d[i] = self.stacks[i].items
            i=i+1
        return d
    
#3.4
class MyQueue:
    def __init__(self):
        self.forward = Stack()
        self.reverse = Stack()
    
    def push(self, item):
        if(self.forward.isEmpty()):
            self.reverse.push(item)
        else:
            while(not self.forward.isEmpty()):
                self.reverse.push(self.forward.pop())
            self.reverse.push(item)
                
    def pop(self):
        if(self.reverse.isEmpty()):
            return self.forward.pop()
        else:
            while(not self.reverse.isEmpty()):
                self.forward.push(self.reverse.pop())
            return self.forward.pop()
        
    def getStacks(self):
        d = OrderedDict()
        d['forward'] = self.forward.items
        d['reverse'] = self.reverse.items
        return d
    
    def isEmpty(self):
        return self.reverse.isEmpty() and self.forward.isEmpty()
    
class Queue:
    def __init__(self):
        self.items = deque()
        
    def add(self, item):
        self.items.append(item)
        
    def remove(self):
        return self.items.popleft()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return not bool(self.items)
    
    def getQueue(self):
        return self.items
    
    def size(self):
        return len(self.items)
        
#3.6
class AnimalShelterLinkedList:
    def __init__(self):
        self.head = None
        
    def enqueue(self, type, value):
        new_node = AnimalShelterNode(type, value)
        if(self.head == None):
            self.head = new_node
        else:
            runner = self.head
            while(runner.next is not None):
                runner = runner.next
            runner.next = new_node
      
    def dequeue(self):
        if(self.head == None):
            return None
        elif(self.head.next == None):
            d = dict()
            d['type'] = self.head.type
            d['value'] = self.head.value
            self.head = None
            return d
        else:
            runner = self.head
            while(runner.next.next is not None):
                runner = runner.next
            d = dict()
            d['type'] = runner.next.type
            d['value'] = runner.next.value
            runner.next = None
            return d
        
    #mistake, I make a dequeue newest dog not oldest dog    
    def dequeueNewestDog(self):
        if(self.head == None):
            return None
        elif(self.head.next == None):
            if(self.head.type == 'dog'):
                d = dict()
                d['type'] = self.head.type
                d['value'] = self.head.value
                self.head = None
                return d
            else:
                return None
        else:
            oldestDog = None
            oldestDog_prev = None
            runner = self.head
            while(runner.next is not None):
                if(runner.next.type == 'dog'):
                    oldestDog_prev = runner
                    oldestDog = runner.next
                runner = runner.next
            if(oldestDog == None):
                return None
            else:
                d = dict()
                d['type'] = oldestDog.type
                d['value'] = oldestDog.value
                oldestDog_prev.next = oldestDog.next
                return d
    
    def printQueue(self):
        runner = self.head
        while(runner is not None):
            d = dict()
            d['type'] = runner.type
            d['value'] = runner.value
            print(d)
            runner = runner.next
            
    def dequeueDog(self):
        if(self.head == None): #empty linked list
            return None
        elif(self.head.type == 'dog'): #head node is a dog
            d = dict()
            d['type'] = self.head.type
            d['value'] = self.head.value
            self.head = self.head.next
            return d
        else: 
            runner = self.head
            while(runner.next is not None):
                if(runner.next.type == 'dog'):
                    d = dict()
                    d['type'] = runner.next.type
                    d['value'] = runner.next.value
                    runner.next = runner.next.next
                    return d
                runner = runner.next
            return None 
        
    def dequeueCat(self):
        if(self.head == None): #empty linked list
            return None
        elif(self.head.type == 'cat'): #head node is a cat
            d = dict()
            d['type'] = self.head.type
            d['value'] = self.head.value
            self.head = self.head.next
            return d
        else: 
            runner = self.head
            while(runner.next is not None):
                if(runner.next.type == 'cat'):
                    d = dict()
                    d['type'] = runner.next.type
                    d['value'] = runner.next.value
                    runner.next = runner.next.next
                    return d
                runner = runner.next
            return None    
    
class AnimalShelterNode:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.next = None
    
def main():    
    a = AnimalShelterLinkedList()

if __name__ == '__main__':
    main()
     
        
    
    