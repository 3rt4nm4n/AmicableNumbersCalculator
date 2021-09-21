#Assume that a!=b
#If d(a) = b and d(b) = a then a and b are amicable numbers
#which means if sum of proper divisors of a add up to b
#and if sum of proper divisors of b add up to a, then these are amicable
#e.g. d(220)=284 & d(284)=220
#Task in problem 21 is to find sum of all the amicable numbers under 10000
import time
#Note that a and b cannot be same, a and b cannot be prime.
s=time.time()

def DivisorsFinder(n):
    divisors=list()
    i=1
    while(i<n):
        if(n%i==0):
            divisors.append(i)
        i+=1
    return divisors#returns divisors in a list

def PrimeCheck(n):
    if(DivisorsFinder(n)==False):
        return True

def AmicableCheck(a,b):#boolean return
    if(sum(DivisorsFinder(a))==b and sum(DivisorsFinder(b))==a):
        return True

amicablenums=list()
maxim=int(input("Input a number, the program will find the amicable numbers under the input number and sum of the amicable numbers under your input: "))
for j in range(2,maxim):    
    for k in range(j+1,maxim):
        if(j!=k and PrimeCheck(j)!=True and PrimeCheck(k)!=True and AmicableCheck(j,k)==True):
                if(j not in amicablenums and k not in amicablenums):
                    print(j," and ",k," are amicable")
                    amicablenums.append(j)
                    amicablenums.append(k)
                    
print("\n\nSum of Amicable Numbers under ",maxim," is ",sum(amicablenums))
e=time.time()
totaltime=e-s
print("Elapsed time: ",totaltime," seconds.")
    
        