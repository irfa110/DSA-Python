def SumN(n):
    if n == 0:
        return 0
    return n + SumN(n-1)


def SumOdd(n):
    if n == 1:
        return 1
    return 2*n - 1 + SumOdd(n - 1)


def SumEven(n):
    if n == 1:
        return 1
    return 2*n + SumEven(n - 1)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def SumSquare(n):
    if n == 1:
        return 1
    return n*n + SumSquare(n - 1)


# print(SumN(3))
# print(fact(5))

# print firt N natural number 

def Nnatural(n):
    if n > 0:
        Nnatural(n - 1)
        print(n, end=' ')


# Nnatural(10)

# print first N natural number reverse order


def Nnaturalreverse(n):
    if n > 0:
        print(n, end=' ')
        Nnaturalreverse(n - 1)


# Nnaturalreverse(10)

# write a recursive fuction to print first N odd natural number


def NoddNumber(n):
    if n > 0:
        NoddNumber(n - 1)
        print(2*n - 1, end=' ')


# NoddNumber(10)

# write a recursive fuction to print first N Even natural number


def NEvenNumber(n):
    if n > 0:
        NEvenNumber(n - 1)
        print(2*n, end=' ')


# NEvenNumber(10)

# write a recursive fuction to print first N Even natural number reverse order


def NEvenNumberverse(n):
    if n > 0:
        print(2*n, end=' ')
        NEvenNumberverse(n - 1)


NEvenNumberverse(10)
