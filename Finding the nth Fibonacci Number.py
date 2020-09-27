def Fibonacci_R(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci_R(n-1)+Fibonacci_R(n-2)
txt = int(input("To find the nth Fibonacci Number, type in an integer for that position: "))
print("Your integer",txt,"references the Fibonacci Number",Fibonacci_R(txt))