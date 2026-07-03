#function - is reusable code block and hide  ur logic.
# syntax def function_name():
#call the function.
#************doubt session **** I called one function in another function but all the functions are executed.


#Types - Function with argument.
def greet(name):
    print(f"Welcome {name} to function!")

greet("yuva")

def sum(a, b):
    print(f"Addition of a, b", a+b)

result = sum(2,3)
print("Result become without return:", result)
#---------------------------------------------------------------------------
#return --> why to we use - we pass the result another function.
# to call this add function to another file.
# functionConcepts.py from import add
def add(a, b):
    return  a + b

print(add(5,9))
#--------------------------------------------------------------
#multiple arugments how to pass into function.

def multiple_arg(*yuva):
    total = 0
    for num in yuva:
        total += num
    return total


print("Multiple Arguments are:", multiple_arg(10,2,3))

#-------------------------------------------------------------

# key-value pair multiple argument to pass the function.

def key_value_func(**kvargu):
    print("user profile:")
    for k, v in kvargu.items():
        print(f"{k}: {v}")

key_value_func(name = "Yuva", age = 26,job="Developer" )