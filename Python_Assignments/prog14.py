n=int(input("Enter the range :"))
def print_till_zero(n):
    if (n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(n)
