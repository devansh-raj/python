c=0
p=1.0
range = int(input("Enter the number of range: "))
while(c<range):
    x = float(input("Enter a number: "))
    c = c+1
    p = p * x
gm = pow(p,1.0/range)
print("The geometric mean is: ",gm)
