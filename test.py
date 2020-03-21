def foo(a, b, c):
    a += 1
    b += 1
    c += 1
    return a, b, c

a, b, c = 4, 4, 4

a, b, c = foo(a, b, c)
print(a,b,c)