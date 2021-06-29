def add(a,b):
    result=a+b
    print("a+b=" ,result)

def sub(a,b):
    result=a-b
    print("a-b=" ,result)


def mul(a, b):
    result = a * b
    print("a*b=" ,result)


def div(a, b):
    result = a / b
    print("a/b=" ,result)

def modu(a, b):
    result = a % b
    print("a%b=" ,result)


a=float(input("Enter Your First Number : "))
b=float(input("Enter Your Second Number :"))
op=input("Enter Your Operation : ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    sub(a,b)
elif op=="/":
    sub(a,b)
elif op=="%":
    sub(a,b)
else:
    print('Syntax Error !')



