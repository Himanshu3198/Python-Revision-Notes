# function is a block of code which only runs when it is cal

def my_function():
  print("Hello from a function")
# my_function()

def show(fname):
    print(fname + "refsnes")
show("fruits")
# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def arb_argument(*kids):
    print("the youngest child is\t" + kids[2])
arb_argument("chintu", "mintu", "pintu")
fruits =["apple", "orange", "banana"]
def my_taste(food):
    for x in food:
        print(x)


# my_taste(fruits)   

def my_table(x):
    return 5*x
print(my_table(3))     
print(my_table(4))   
print(my_table(5))   


