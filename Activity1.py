# identity operator
x=5
if (type(x) is int):
    print ("true")
else: 
    print("false")
x=5.5
if (type(x) is float): 
    print("true")
else:
    print("false")
x=5
y=5
if (x is y): 
    print("x and y have same identity")
y=20
if (x is not y):
    print("x and y have different identity")
    