num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
num3=int(input("enter number 3:"))
if (num1>=num2) and (num1>=num3):
	greatest=num1
elif (num2>=num1) and (num2>=num3):
	greatest=num2
else:
	greatest=num3
print("the greatest number is :"+str(greatest))
