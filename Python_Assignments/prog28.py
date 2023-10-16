print("28.Python program to print Fibonacci series using iteration.")
x= 0
y= 1
n=int(input("Enter the number of terms in the sequence: "))
print(x,y,end=" ")
while(n-2):
    z=x+y
    x,y = y,z
    print(z,end=" ")
    n=n-1
