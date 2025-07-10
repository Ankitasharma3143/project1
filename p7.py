a = int(input("enter the number="))
if a%3 & a%5==0 & a%10!=0:
    print("divisible by both 3 and 5 but not by 10")
else:
    print("does not meet the condition")