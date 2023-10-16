print("Python program to find the odd numbers in an array :")
numbers=[6,3,1,8,2,4,5,9,11,10,13]
count=0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count=count+1
print("The number of odd numbers in the list are: ", count)
