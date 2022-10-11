"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return(0)
    return(1)
def primes(number_of_primes):
    i=2
    list=[]
    while(1):
        if number_of_primes<=0:
            raise ValueError('please enter a positive integer')
            break
        if(prime(i)):
            list.append(i)
            if(len(list)==number_of_primes):
                break
        i+=1
    return list
