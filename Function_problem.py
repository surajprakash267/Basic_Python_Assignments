5.try to write it in a function, is_prime(23).
Ans.
#enter number
num= int(input("enter number: "))
#Define a function
def isPrime(num):
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i)==0:
            return False
    return True
if (isPrime(num)==True):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")