#⁠Take a number n and print its factorial using a for loop.
n = int(input("enter the number="))
factorial = 1
for i in range(1,n+1):
    factorial *= i  
print(f"The factorial of {n} is: {factorial}") 