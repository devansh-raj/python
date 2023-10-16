print("Python program to insert a number to any position in a list: ")
numbers = [2,3,4,1,9,6,5,8,10,12]
print(numbers)
x = int(input("Enter the number to be inserted: "))
y = int(input("Enter the position: "))
numbers.insert(y,x)
print(numbers)
