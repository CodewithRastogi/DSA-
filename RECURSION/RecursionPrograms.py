"""
Function calling itself is called recursion.
Approach To solve question By Question
1.Suppose that function is already exist which u want to create.
2.Make it Recursive case.
3.Make an Base Case.
Conclusion-
a->In recursion,problem is solved in terms of problem itself.
b->Each time recursive function call to itself for little simpler version of the original problem.

"""

#Print First N natural number
def printNNatural(n):
    if n>0:
        printNNatural(n-1)
        print(n,end=' ')
printNNatural(10)
print()
#Print First N natural number in reverse order
def printNNaturalReverseOrder(n):
    if n>0:
        print(n,end=' ')
        printNNaturalReverseOrder(n-1)
        
printNNaturalReverseOrder(10)
print()
#Print First N odd natural number
def printNOdd(n):
    if n>0:
        
        printNOdd(n-1)
        print(2*n-1,end=' ')
        
printNOdd(10)
print()
#Print First N odd natural number in reverse order
def printNOddReverse(n):
    if n>0:
        print(2*n-1,end=' ')
        printNOdd(n-1)
        
        
printNOddReverse(10)
print()
#Print First N even natural number
def printNEven(n):
    if n>0:
        
        printNEven(n-1)
        print(2*n,end=' ')
        
printNEven(10)
print()
#Print First N even natural number in reverse order
def printNEvenReverse(n):
    if n>0:
        print(2*n,end=' ')
        printNEvenReverse(n-1)
       
        
printNEvenReverse(10)
print()
#Print Sum of first N natural number.
def sumN(n):
    if n == 1:
        return 1
    return n + sumN(n-1)
print(sumN(10))
print()
#Print Sum of first N odd natural number.
def sumNOdd(n):
    if n == 1:
        return 1
    return 2*n - 1 + sumNOdd(n-1)
print(sumNOdd(10))
print()
#Print Sum of first N even natural number.
def sumNEven(n):
    if n == 1:
        return 1
    return 2*n + sumNEven(n-1)
print(sumNEven(10))
print()
#Print Factorial Of a number.
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
print(fact(5))
#Print Sum of square of first N natural number
def sumNSquare(n):
    if n==1:
        return 1
    return n*n + sumNSquare(n-1)
print(sumNSquare(10))





