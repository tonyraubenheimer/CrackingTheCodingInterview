from __future__ import print_function
import array
from itertools import count
from scipy import str_



#1.1
#TIME COMPLEXITY: O(c*n) where c is number chars in alphabet, n is length of input
#SPACE COMPLEXITY: O(1)
#does not include spaces as a character
def isUnique(input):
    #if input length > number chars in alphabet, return false
    if len(input) > 26:
        return False
    
    #loop through alphabet and check string for more than one occurrence of char
    for i in range(ord('a'), ord('z')+1):
        hasChar=0
        for c in input:
            if i==ord(c):
                hasChar=hasChar+1
            if hasChar>1:
                return False
    
    #if we have finished checking all alphabet chars and no duplicates were found, return true
    return True 

#1.2
#TIME COMPLEXITY: O(n+a) where n is length of str1 and a is size of alphabet (i.e. 26)
#SPACE COMPLEXITY: O(a) 
def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    offset=ord('a')
    #initialize list of integers for each char in alphabet
    alph = [0]*26 
    
    offset=ord('a')
    #count each char in str1 and record in alph list
    for c in str1:
        alph[ord(c)-offset] = alph[ord(c)-offset]+1
    
    #now decrement ints in alph corresponding to each char in str2
    for c in str2:
        alph[ord(c)-offset] = alph[ord(c)-offset]-1
    
    #check that alph has been zeroed out
    hasOne = False
    for i in alph:
        if i!=0:
            return False
    
    #we can return True now, since we have passed all our checks
    return True

#1.3
#TIME COMPLEXITY: O(n)
#SPACE COMPLEXITY: O(n)
def urlify(input, true_length):
    
    str = list(input)
    
    numSpaces=0
    for i,c in enumerate(str):
        if c==' ' and i<true_length:
            numSpaces=numSpaces+1
    
    new_length = true_length+(numSpaces*2)
    offset = new_length-true_length
    for i in range(true_length-1, -1, -1):
        if str[i]==' ':
            str[i+offset] = '0'
            str[i+offset-1] = '2'
            str[i+offset-2] = '%'
            offset=offset-2
        else:
            str[i+offset] = str[i]
        
    return ''.join(str)
    
#1.4
#TIME COMPLEXITY: O(a+n)          
#SPACE COMPLEXITY: O(a)

def palin_perm(input):
    
    import string
    d = dict.fromkeys(list(string.ascii_lowercase), 0)
    
    for c in input:
        if ('A' <= c <= 'Z') or ('a' <= c <= 'z'): 
            d[c.lower()] = d[c.lower()]+1
        
    hasOdd = 0
    for key, value in d.items():
        if value%2 == 1:
            hasOdd = hasOdd+1
            
    if hasOdd > 1:
        return False
    else:
        return True
    
#1.5
#TIME COMPLEXITY: O(n)
#SPACE COMPLEXITY: O(n) because string converted to list

def one_away(input1, input2):
    
    if len(input1) > len(input2):
        str1 = list(input1)
        str2 = list(input2)
    else:
        str1 = list(input2)
        str2 = list(input1)
    
    if len(str1)-len(str2) > 1:
        return False
    
    numDiff = 0
    if len(str1) == len(str2):
        for i,c in enumerate(str1):
            if str1[i] != str2[i]:
                numDiff = numDiff+1
    else:
        for i,c in enumerate(str2):
            if str1[i+numDiff] != str2[i]:

                if str1[i+1] != str2[i]:
                    return False
                            
                numDiff = numDiff+1
    
    if numDiff>1:
        return False
    else:
        return True
    
#1.6 
#TIME COMPLEXITY: O(n)
#SPACE COMPLEXITY: O(1)

def string_comp(input):
    
    str = list(input)
    output = ""
    
    i=0
    while i < len(input):
        
        count = 1

        while (i+count < len(input)) and (str[i+count] == str[i]):
            count = count+1
            
        output += str[i]
        output += str_(count)
        
        i=i+count
     
    if len(output) < len(input):
        return output 
    else:
        return input

        
#1.7
#TIME COMPLEXITY: O(n^2) for rotate only
#SPACE COMPLEXITY: O(n^2) 

def rotate_matrix(m):
    
    n=len(m)
    
    for inset in range(0,n/2):
           
        for offset in range(0,n-1-(2*inset)):
            
            temp = m[inset][offset+inset]  
            m[inset][offset+inset] = m[n-1-offset-inset][inset]
            m[n-1-offset-inset][inset] = m[n-1-inset][n-1-offset-inset]
            m[n-1-inset][n-1-offset-inset] = m[offset+inset][n-1-inset]
            m[offset+inset][n-1-inset] = temp

def create_matrix(n):
    import random
    
    m = list()
    for i in range(0,n):
        row = list()
        
        for i in range(0,n):
            rand = random.randint(1,99)
            row.append(rand)
            
        m.append(row)
    
    return m
        
def print_matrix(m):
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            if m[i][j]<10:
                print(m[i][j], end='  ')
            else:
                print(m[i][j], end=' ')
        print('\n', end='')   
    print('\n', end='')  
    
#1.8
#TIME COMPLEXITY: O(m*n)
#SPACE COMPLEXITY: O(m*n) for create only

def zero_matrix(matrix):
    
    #check if first row should be zeroed
    zero_first_row = False 
    for i in range(0,len(matrix[0])):
        if matrix[0][i] == 0: 
            zero_first_row = True
    
    #check if first col should be zeroed        
    zero_first_col = False
    for i in range(0, len(matrix)):
        if matrix[i][0] == 0:
            zero_first_col = True
            
    #check all other rows and cols
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0] = 0
                matrix[0][j] = 0
            
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][0] == 0:
                matrix[i][j] = 0
            if matrix[0][j] == 0:
                matrix[i][j] = 0
    
    if zero_first_row:
        for j in range(0, len(matrix[0])):
            matrix[0][j] = 0
            
    if zero_first_col:
        for i in range(0, len(matrix)):
            matrix[i][0] = 0

def create_matrix_mn(m, n):
    import random
    
    matrix = list()
    for i in range(0,m):
        row = list()
        
        for i in range(0,n):
            rand = random.randint(0,20)
            row.append(rand)
            
        matrix.append(row)
    
    return matrix 

#1.9
#TIME COMPLEXITY: O(1)
#SPACE COMPLEXITY: O(n) where n is length of string

def string_rotation(s1, s2):
    
    double_s1 = s1+s1
    
    if len(s1) != len(s2):
        return False
    
    if s2 in double_s1:
        return True
    else:
        return False

if __name__ == '__main__':
    s1 = "waterbottle"
    s2 = "bottlewate"
    r = string_rotation(s1, s2)
    print(r)