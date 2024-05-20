def Armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print("It is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
def Pallindrome(num):
    temp = num  
    rev = 0  
    dig=0
    while(num > 0):  
        dig = num % 10  
        rev = rev * 10 + dig  
        num = num // 10  
    if(temp == rev):  
        print("This value is a palindrome number!")  
    else:  
        print("This value is not a palindrome number!")
def average(l):
    avg=(sum(l)/len(l))
    print(avg)
def sumnums(n):  
    if n == 1:  
        return 1  
    return n + sumnums(n - 1) 
def power_of_num(num, topwr):  
    if topwr == 0:  
        return 1  
    else:  
        return num * power_of_num(num, topwr - 1)  
def LCM(x, y):  
  z = x % y  
  if z == 0:  
        return x  
  return x * LCM(y, z) / z  
def factorial(n):
    if n==0:  
        return 1  
    else:  
        return n*factorial(n-1)
def even_or_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
def fibonacci(x):
    if(x==0):
        return 1
    if(x==1):
        return 1
    return fibonacci(x-1)+fibonacci(x-2)
def diamond(n):
    for i in range(0,n):
        print(" "*(4-i),"* "*i)
    for i in range(0,n):
        print(" "*i,"* "*(4-i))
def prime(n):
    c=0
    for i in range(2,n-1):
        if(n%i==0):
            c=c+1
        if(c>0):
            break
    if(c==0):
        print("Prime")
    else:
        print("Not Prime")
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=' ')
        print()
