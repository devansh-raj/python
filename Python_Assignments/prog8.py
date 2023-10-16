sum = 0
num=int(input("Enter an number: "))
while(num!=0):
    digit = num%10
    sum = sum+digit
    num=num//10
print("Sum of digits is: ", sum)
