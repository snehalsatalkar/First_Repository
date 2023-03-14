def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)

num=int(input("Enter no"))
factorial(num)
print("factorial=",factorial(num))
