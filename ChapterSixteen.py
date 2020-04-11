#16.3
def intersection(start1, end1, start2, end2):
    #start1 = (x1, y1)
    #end1 = (x, y)
    m1 = (end1[1]-start1[1])/(end1[0]-start1[0])
    m2 = (end2[1]-start2[1])/(end2[0]-start2[0])
    b1 = start1[1] - (m1*start1[0])
    b2 = start2[1] - (m2*start2[0])
    
    x0 = (b1-b2)/(m2-m1)
    y0 = m1*x0 + b1
    
    return (x0, y0)

#16.5
def factZeroes(n):
    zeroes = 0
    for i in range(1, n+1):
        zeroes+=factorsOf5(i)
    
    return zeroes

def factorsOf5(i):
    count = 0
    while i%5 == 0:
        count+=1
        i/=5
        
    return count

#16.6
def partition(a, start, end):  
    pivot = a[end]
    
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i],a[j] = a[j],a[i] 
            i+=1
    
    a[i],a[end] = a[end],a[i]
    
    return i

def _quickSort(a, start, end):
    if start < end:
        pivot = partition(a, start, end)
        _quickSort(a, start, pivot-1)
        _quickSort(a, pivot+1, end)
        
def quickSort(a):
    _quickSort(a, 0, len(a)-1)
    
def smallestDiff(a, b):
    if len(a) > len(b):
        long = quickSort(a)
        short = quickSort(b)
    else:
        long = quickSort(b)
        short = quickSort(a)

    smallestDiff = float("inf")
    i=0
    j=0
    while j+len(short) <= len(long):
        while i+j < len(long):
            if abs(long[a]-short[b]) < smallestDiff:
                smallestDiff = abs(long[a]-short[b])
        j+=1

        
def englishInt(n):
    num = n
    englishNum = ''
    
    billions = (int)(num/1000000000)
    if billions:
        englishNum += englishInt(billions) + " billion "
        num -= billions*1000000000
    
    millions = (int)(num/1000000)
    if millions:
        englishNum += englishInt(millions) + " million "
        num -= millions*1000000
    
    thousands = (int)(num/1000)
    if thousands:
        englishNum += englishInt(thousands) + " thousand "
        num -= thousands*1000

    englishNum += englishSmallNum(num)
    
    return englishNum
        
def englishSmallNum(n):
    if n == 0:
        return ""
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "three"
    elif n == 4:
        return "four"
    elif n == 5:
        return "five"
    elif n == 6:
        return "six"
    elif n == 7:
        return "seven"
    elif n == 8:
        return "eight"
    elif n == 9:
        return "nine"
    elif n == 10:
        return "ten"
    elif n == 11:
        return "eleven"
    elif n == 12:
        return "twelve"
    elif n == 13:
        return "thirteen"
    elif n == 14:
        return "fourteen"
    elif n == 15:
        return "fifteen"
    elif n == 16:
        return "sixteen"
    elif n == 17:
        return "seventeen"
    elif n == 18:
        return "eighteen"
    elif n == 19:
        return "nineteen"
    elif n == 20:
        return "twenty"
    elif n > 20 and n < 30:
        return "twenty-" + englishSmallNum(n-20)
    elif n == 30:
        return "thirty"
    elif n > 30 and n < 40:
        return "thirty-" + englishSmallNum(n-30)
    elif n == 40:
        return "forty"
    elif n > 40 and n < 50:
        return "forty-" + englishSmallNum(n-40)
    elif n == 50:
        return "fifty"
    elif n > 50 and n < 60:
        return "fifty-" + englishSmallNum(n-50)
    elif n == 60:
        return "sixty"
    elif n > 60 and n < 70:
        return "sixty-" + englishSmallNum(n-60)
    elif n == 70:
        return "seventy"
    elif n > 70 and n < 80:
        return "seventy-" + englishSmallNum(n-70)
    elif n == 80:
        return "eighty"
    elif n > 80 and n < 90:
        return "eighty-" + englishSmallNum(n-80)
    elif n == 90:
        return "ninety"
    elif n > 90 and n < 100:
        return "ninety-" + englishSmallNum(n-90) 
    elif n > 100 and n < 1000:
        hundreds = (int)(n/100)
        return englishSmallNum(hundreds) + " hundred " + englishSmallNum(n - (100*hundreds))
    
def main():
    print(englishInt(839))
    
if __name__ == '__main__':
    main()