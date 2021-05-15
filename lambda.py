# a lambda function is a small anonymous function
# a lambda functon can take any number of arguments but can only have one expression

# lambda arguments : expression
x = lambda a: a + 10
print(x(15))
y=lambda a,b:a*b
print("the multiply ",y(5,6))
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))

print("hello himanshu")
