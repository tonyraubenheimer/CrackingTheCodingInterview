import math
import random

#5.1
def insertion(n, m, i, j):
    #create a sequence of 1s of length m 
    n_mask = (1 << (j-i+1)) - 1 
    #move this sequence over i so it's located where m is to go
    n_mask = n_mask << i
    #flip n_mask so it's 0s where m is to go and 1s everywhere else
    n_mask = ~n_mask
    #anding n_mask with n clears n where m is to go, leaving n intact everywhere else
    n_mask = n & n_mask
    
    #m_mask is m where m is to go and 0s everywhere else
    m_mask = m << i
    
    return n_mask | m_mask 

def intString(num):
    exp = 8 

#5.2

#NEED TO REVIEW AND COMMENT


def binString(num):
    if num<0:
        sign_str = '1'
        num = -num #we'll use the positive representation from here on
    else:
        sign_str = '0'
    
    exp = (math.log(num) / math.log(2))
    if exp < 0:
        exp = math.floor(exp)
    
    i=0
    exp_str = ''
    while i < 8:
        if (int)(exp+127) & (1 << i) != 0:
            exp_str = '1' + exp_str
        else:
            exp_str = '0' + exp_str
        i+=1
    print(exp_str)
        
    #normalize the number
    mantissa = num / (2 ** exp)
    #drop the leading 1
    mantissa -= 1

    mantissa_str = ''
    i=1
    while i < 24:
        if mantissa >= 2**-i:
            mantissa -= 2**-i
            mantissa_str = mantissa_str + '1'
        else:
            mantissa_str = mantissa_str + '0'
        i+=1  
    print(mantissa_str)
    
    if mantissa > 2**-23: #number cannot be accurately represented
        print('error')
        return
        
    return sign_str + exp_str + mantissa_str

#5.3
def flipBitToWin(num):
    numBits = (int)(math.log(num) / math.log(2)) + 1
    i = 0
    maxOnes = 0
    
    while i < numBits:
        flippedBit_mostOnes = _findMostOnes(num | (1 << i))
        if flippedBit_mostOnes > maxOnes:
            maxOnes = flippedBit_mostOnes
        i+=1
            
    return maxOnes

def _findMostOnes(num):
    numBits = (int)(math.log(num) / math.log(2)) + 1
    maxOnes = 0
    tempOnes = 0
    i = 0
    
    while i < numBits:
        if num & (1 << i) != 0: # bit == 1
            tempOnes += 1
            if tempOnes > maxOnes:
                maxOnes = tempOnes
        else: # bit == 0
            tempOnes = 0
        i+=1
        
    return maxOnes

#5.4
def nextNumber(num):
    numBits = (int)(math.log(num) / math.log(2)) + 1
    lastOne = numBits+1
    lastZero = numBits+1
    numOnes = 0
    numZeroes = 0
    i = 0
    while i < numBits:
        if num & (1<<i) != 0: #bit==1
            numOnes+=1
            if i<lastOne:
                lastOne = i
        else:
            numZeroes+=1
            if i<lastZero:
                lastZero = i
        i+=1
        
    if numOnes == 0:
        print('Error: Input cannot be 0')
        return
    
    #next largest
    nextLargest = ~(1<<lastOne) & num #clear least significant 1 to 0
    i = lastOne+1
    while i < numBits:
        if num & (i<<i) == 0: #bit == 0
            nextLargest = num | (1<<i) #set least significant 0 to 1
            break
        i+=1
        if i==numBits: #we never hit the break, so there wasn't a least significant 0 to set
            nextLargest = num*2 #add a zero to the end of num
                        
    print('Next largest = ' + str(bin(nextLargest)))
    
    #next smallest
    i = lastZero+1
    while i < numBits:
        if num & (1<<i) != 0: #bit == 1
            nextSmallest = num & ~(1<<i) #set 1 to 0
            nextSmallest = (1<<(i-1)) | num #set previous 0 to 1
            break
        i+=1
    
    if numZeroes == 0:
        print('Next smallest not possible')
    else:
        print('Next smallest = ' + str(bin(nextSmallest)))
    
#5.6
def conversion(a, b):
    numABits = (math.log(a) / math.log(2)) + 1
    numBBits = (math.log(b) / math.log(2)) + 1
    if numABits > numBBits:
        numBits = numABits
    else:
        numBits = numBBits
    
    diff = a ^ b
    numFlipped = 0
    i=0
    while i < numBits:
        if diff & (1<<i) != 0:
            numFlipped += 1
        i+=1
        
    return numFlipped

#5.7
def pairwiseSwap(num):
    numBits = (math.log(num) / math.log(2)) + 1
    output = num
    i=1
    while i < numBits:
        if num & (1<<i) != 0:
            cur_bit = 1
        else:
            cur_bit = 0
        if num & (1<<i-1) != 0:
            prev_bit = 1
        else:
            prev_bit = 0
        output = output & ~(1<<i) | (cur_bit << i)
        output = output & ~(1<<(i-1)) | (prev_bit << (i-1))
        i+=2

#5.8
def drawLine(height, width, x1, x2, y):
    screen = _screen(height, width)
    print('')
    screen = _drawLine(screen, width, x1, x2, y)
    _printScreen(screen, width)

def _drawLine(screen, width, x1, x2, y): 
    x1=x1-1   
    screen_index = (width/8)*(y-1) + (x1/8)
    byte_index = x1%8
    total_line_width = abs(x1-x2)
    cur_line_width = 0
    
    i = screen_index
    while cur_line_width < total_line_width:
        screen[screen_index] = screen[screen_index] | (1<<(8-byte_index-1))
        cur_line_width+=1
        byte_index+=1
        if byte_index == 8:
            byte_index = 0
            screen_index+=1
        
    return screen
    
def _screen(height, width):
    screen = bytearray(height*width/8)
    i = 0
    while i < (height*width/8):
        rand = random.randint(0,255)
        screen[i] = rand
        i+=1
    _printScreen(screen, width)
    return screen

def _printScreen(screen, width):
    cur_width=0
    for b in screen:
        print('{0:08b}'.format(b))
        cur_width+=8
        if cur_width==width:
            print('')
            cur_width=0

def main():
    drawLine(3, 64, 8, 18, 2)
    #print('here')
    
if __name__ == '__main__':
    main()
