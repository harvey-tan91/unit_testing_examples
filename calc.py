
def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def mutiply(x,y):
    return x * y 

def divide(x,y):
    if y == 0:
        raise ValueError('You cannot divide by zero')
    return x / y