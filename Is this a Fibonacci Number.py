txt = int(input("Please enter an integer to see if it is a Fibonacci Number "))
import math 
def is_PS(n): 
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 

def isFibonacci(n):
    if (is_PS(n) == True): 
        print("Your integer",txt,"is a Fibonacci Number")
    else: 
        print("Your integer",txt,"is a not Fibonacci Number")
isFibonacci(txt)