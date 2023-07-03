from math import e
from math import sqrt
#You can calculate basic trigonometric functions and hyperbolic functions
#You can only enter numbers not degrees or radians or gradians
op = input("Please enter an operator(Trigonometric/Hyperbolic): ")
if op == "Trigonometric":
    a = float(input("Please enter a number: ")) #vertical
    b = float(input("Please enter second number: ")) #horizontal
    c = sqrt(a**2 + b**2) #hypotenuse formula
    op1 = input("Please enter an operator: ")
    if op1 == "sin":
        d = a/c #sine
        print(d)
    elif op1 == "cos":
        f = b/c #cosine
        print(f)
    elif op1 == "tan":
        g = a/b #tangent
        print(g)
    elif op1 == "cot":
        h = b/a #cotangent
        print(h)
elif op == "Hyperbolic":
    x = float(input("Please enter a number: "))
    op2 = input("Please enter a operator: ")
    if op2 == "sinh":
        y = (e**x - e**-x)/2 #Hyperbolic Sine
        print(y)
    elif op2 == "cosh":
        z = (e**x + e**-x)/2 #Hyperbolic Cosine
        print(z)
    elif op2 == "tanh":
        t = (e**x - e**-x) / (e**x + e**-x) #Hyperbolic Tangent
        print(t)
    elif op2 == "coth":
        j = (e**x + e**-x) / (e**x - e**-x) #Hyperbolic Cotangent
        print(j)
#This is the first version of the calculator I am develope this calculator as soon as possible