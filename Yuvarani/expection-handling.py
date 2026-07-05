print('Step 1:')
#  types of error --? runtime, comile time
# able see the compile time error --> print hi -- without dobule quotes.
# runtime error --> called as expection error.
a=10
b= 10
result = a/b
print("step2: final result:", result)

#hy we do exception handling --> for ex. u withdraw more than balance amount in that time website will be crashed.
#at that moment next line not printing. blocked. ---> that time will use exception handling.

# try --> throw --> exception.
print("Welcome to zomato website!!")
num_of_items = int(input("How many items ?"))
total_price = 200 * num_of_items
average_price = total_price/ num_of_items
print("Average price is:", average_price)
print("Next code will execute!")

# --- above code throwing the error --> divide y zero.ZeroDivisionError: division by zero

# so we planned to try, except.

try:
    num_of_items = int(input("How many items ?"))
    total_price = 200 * num_of_items
    average_price = total_price/ num_of_items
    print("Average price is:", average_price)
except ZeroDivisionError:
    print("You cannot ordered 0 items!!")

print("Next code will execute..")
#-------------------------------------------------------------------------
#multiple error occur in exception handling.
#TypeError
#ValueError
#KeyError
#NameError
#IndentationError
#-------------------------------------------------------------------------------
#------ how to memorize the error ? instead of use Exception -----------------------------------------------


try:
    num_of_items = int(input("How many items ?"))
    total_price = 200 * num_of_items
    average_price = total_price/ num_of_items
    print("Average price is:", average_price)
except Exception:
    print("You cannot ordered 0 items!!")

#-------------------------------------------------------------------------------------

try:
    num_of_items = int(input("How many items multiple exception ?"))
    total_price = 200 * num_of_items
    average_price = total_price/ num_of_items
    print("Average price is:", average_price)
except ZeroDivisionError:
    print("You cannot ordered 0 items!!")
except FileNotFoundError:
    print("Your file is not found!")


#------ finally block always execute ------------------------------like once user login the back ebsite automatically logout hapening.that logic writtern in finally block.
try:
    num_of_items = int(input("How many items finally block ?"))
    total_price = 200 * num_of_items
    average_price = total_price/ num_of_items
    print("Average price is:", average_price)
except FileNotFoundError:
    print("Your file is not found!")
finally:
    print("Always execute!!!!")

print("next code not executed....")


#------------------------------------------------------------------------------------------------------


# why we cant handle the exception using if/else block.


num_of_items = int(input("enter number:"))

if num_of_items == 0:
    print("You cant divide by 0")
else:
    print("do division")