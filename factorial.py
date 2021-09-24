def factorial(x):
    if (x==0 or x==1):
        return 1
    return x*factorial(x-1)
a = int(input("Enter the number : "))
factorial(a)
