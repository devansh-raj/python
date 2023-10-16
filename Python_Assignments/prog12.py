num=int(input("Enter the range to generate the prime number: "))
for n in range(2,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)
