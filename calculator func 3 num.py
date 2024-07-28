def add(i,j):
    return i+j
def sub(i,j):
    return i-j
def mul(i,j):
    return i*j
def div(i,j):
    return i/j

def calculator():
    op=int(input("Enter \n1:+ \n2:- \n3:* \n4:/"))
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    c = int(input("Enter 3rd number: "))
    if op==1:
        print(add(add(a,b),c))
    elif op==2:
        print(sub(sub(a,b),c))
    elif op==3:
        print(mul(mul(a,b),c))
    elif op==4:
        print(div(div(a,b),c))
    else:
        print("error")

print(calculator())