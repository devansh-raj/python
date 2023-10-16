num=int(input("Enter a number: "))
prime= 1
for i in range(2,num//2):
    if (num%i==0):
        prime = 0
        break
if(prime==1):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
