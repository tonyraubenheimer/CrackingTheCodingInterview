import random

#5.1
def numSteps(n):
    memo = [0 for _ in range(0, n+1)]
    return _numSteps(n, memo)

def _numSteps(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    if(memo[n] == 0):
        memo[n] = _numSteps(n-3, memo) + _numSteps(n-2, memo) + _numSteps(n-1, memo)
    
    return memo[n]

def numStepsIter(n):
    if n==0: 
        return 1
    
    a = 1#n==1
    b = 2#n==2
    c = 4#n==3
    
    i=4#n==4; we use i instead of n because n is already taken
    while i<n:
        d = a+b+c
        a = b
        b = c
        c = d
        i+=1
    
    return a+b+c

#5.2
#REDO
class Grid:
    def __init__(self, r, c):
        self.rows = r
        self.columns = c
        self.grid = [[1 for x in range(0, c)] for y in range(0, r)]
        self.path = []
    
    def printGrid(self):
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[0])):
                rand = random.randint(0, 101)
                if rand <= 15 and (y != self.rows-1 or x != self.columns-1) and (y != 0 or x != 0):
                    self.grid[y][x] = 0
                print(self.grid[y][x])
            print('')
            
    def robotGrid(self, grid, x, y):
        path = [(0,0)]
        self._robotGrid(grid, x, y, path)
            
    def _robotGrid(self, grid, x, y, path):
        height = self.rows
        width = self.columns
          
        if self.path != []:
            return
        
        print(str(x) + ', ' + str(y))
        
        if path[-1] == (self.columns-1, self.rows-1):
            print(path[-1])
            self.path = path
            return
        
        if x<=width-2 and grid[y][x+1] != 0:
            path.append((x+1, y))
            self._robotGrid(grid, x+1, y, path)
        if y<=height-2 and grid[y+1][x] != 0 and self.path == []:
            path.append((x, y+1))
            self._robotGrid(grid, x, y+1, path)
            
#5.3
def magicIndex(a):
    return _magicIndex(a, 0, len(a)-1)

def _magicIndex(a, start, end):
    h = (start+end)/2
    if a[h] == h:
        return h 
    if start == end:
        return None   
    elif a[h] > h:
        return _magicIndex(a, start, h-1)
    elif a[h] < h:
        return _magicIndex(a, h+1, end)
    
#8.4
def powerSet(s):
    power = [[]] #power set starts with null set
    _powerSet(s, power)
    printPower(power)
    
    return power

def _powerSet(s, power):
    
    if(len(s) == 0): #once s is empty, the power set is complete
        return
    
    #we'll take an element from s and build new subsets by adding this element to all existing subsets
    temp = []
    element = s.pop() #remove an element from s
    
    for sub in power:
        new = sub + [element]
        temp.append(new)
    
    power.extend(temp)
    
    _powerSet(s, power) #call again now that s is smaller by one element
    
def printPower(power):
    for p in power:
        print(p)

#8.5
def recursiveMult(a, b):
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return _recursiveMult(abs(a), abs(b), 0)
    else:
        return 0-_recursiveMult(abs(a), abs(b), 0)
    
def _recursiveMult(a, b, temp):
    if b==0:
        return temp
    
    temp = temp+a
    b = b-1
    return _recursiveMult(a, b, temp)

#8.6
class Stack:
    def __init__(self):
        self.items = []
        
    def pop(self):
        if self.items == []:
            return None
        return self.items.pop()
    
    def add(self, item):
        self.items.append(item)
        
    def peek(self):
        if self.items == []:
            return None
        return self.items[-1]
    
    def length(self):
        return len(self.items)
    
    def printStack(self):
        print(self.items)
        
def printStacks(s1, s2, s3):
    s1.printStack()
    s2.printStack()
    s3.printStack()

def towersOfHanoi():
    s1 = Stack() #from_stack
    s1.add(5)
    s1.add(4)
    s1.add(3)
    s1.add(2)
    s1.add(1)
    s2 = Stack() #aux_stack
    s3 = Stack() #to_stack
    printStacks(s1, s2, s3)
    _towersOfHanoi(s1.length(), s1, s3, s2)
    printStacks(s1, s2, s3)
    
def _towersOfHanoi(n, from_stack, to_stack, aux_stack):
    if n==0:
        return
    _towersOfHanoi(n-1, from_stack, aux_stack, to_stack)
    to_stack.add(from_stack.pop())
    _towersOfHanoi(n-1, aux_stack, to_stack, from_stack)
    
#8.7    
def permsNoDups(input):
    perms = ['']
    
    for c in input:
        temp_list = []     
        for p in perms:
            for i in range(0, len(p)+1):
                temp_str = p[0: i] + c + p[i:len(p)+1]
                temp_list.append(temp_str)
        perms = temp_list 
        
    print(perms)
    print(len(perms))
    
#8.8
def permsWithDups(input):
    perms = {''}
    
    for c in input:
        temp_list = set()    
        for p in perms:
            for i in range(0, len(p)+1):
                temp_str = p[0: i] + c + p[i:len(p)+1]
                temp_list.add(temp_str)
        perms = temp_list 
        
    print(perms)
    print(len(perms))
    
#8.9
#def parens(n):

#8.10
def picture(w, h):
    grid = [[0 for x in range(0, w)] for y in range(0, h)]
    for x in range(0, w):
        for y in range(0,h):
            rand = random.randint(0,100)
            if rand < 25:
                grid[y][x] = 1
            elif rand >= 25 and rand < 50:
                grid[y][x] = 2
    
    return grid
                
def printPicture(grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            print(str(grid[y][x]) + ' ')
        print('') #newline

def paintFill(grid, x, y, new_color):
    old_color = grid[y][x]
    grid[y][x] = new_color
    _paintFill(grid, x+1, y, new_color, old_color)
    _paintFill(grid, x-1, y, new_color, old_color)
    _paintFill(grid, x, y+1, new_color, old_color)
    _paintFill(grid, x, y-1, new_color, old_color)

def _paintFill(grid, x, y, new_color, old_color):
    if x>=len(grid[0]):
        return
    if y>=len(grid):
        return
    if x<0 or y<0:
        return
    cur_color = grid[y][x]
    if cur_color == old_color:
        grid[y][x] = new_color
        _paintFill(grid, x+1, y, new_color, old_color)
        _paintFill(grid, x-1, y, new_color, old_color)
        _paintFill(grid, x, y+1, new_color, old_color)
        _paintFill(grid, x, y-1, new_color, old_color)
   
#8.11       
def _coins(amount, denom, denom_index):
    if denom_index >= len(denom)-1:
        return 1
    
    cur_denom = denom[denom_index]
    
    num_ways = 0
    i=0
    while i <= amount:
        num_ways += _coins(amount - i, denom, denom_index+1)
        i+=cur_denom
        
    return num_ways
    
def coins(n):
    denom = [25, 10, 5, 1]
    return _coins(n, denom, 0)
    
#    
    

def main():
    #g = Grid(4,5)
    #grid = g.grid
    #g.printGrid()
    #path = []
    #g.robotGrid(grid, 0, 0)
    #print(g.path)
    
    #a = [-15,0,2,4,5,7,9,24]
    #print(magicIndex(a))
    
    #s = {1,2,3}
    #powerSet(s)
    
    #towersOfHanoi()
    #permsNoDups('hey')
    #permsWithDups('eyy')
    
    #grid = picture(5,10)
    #printPicture(grid)
    #paintFill(grid, 0, 0, 3)
    #print ''
    #printPicture(grid)
    
    print(coins(100))
    
    
if __name__ == '__main__':
    main()