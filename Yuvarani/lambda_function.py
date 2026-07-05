#lambda - lambda function when we need to use --> one line function need to writtern.
#it called anyonoyms function.
# syntax --> lambda: argument -> expression.
# we need to use lambda in  map, filter and reduce.

add = lambda a, b : a + b
print(add(1,3))

flist = ["Apple", "orange", "banana"]
result = list(map(lambda  f: f.upper(), flist))
print("result--->",result)

nums = [1,3,4, 2, 8]
even = list(filter(lambda n: n%2 == 0, nums))
print(even)

from functools import reduce, partial

nums = [1,2,3,4]
red = reduce(lambda a, b: a+b, nums)
print(red)

nums = [10, 5,33, 7]
max = reduce(lambda a, b : a if a > b else b, nums)
print('maximum no:', max)

#--closure --> outer function variable we can able to use inner function.

def outer(msg):
    def inner():
        return f"Welcome to my partner:Mr.{msg}"

    return inner

out = outer("Boss")
print(out())

#------------------------------------------------------------

# partial function.

def calculate_price(base_rice, tax_rate):
    return  base_rice * (1 + tax_rate)

price = calculate_price(100, 0.18)
print("Price:", price)

# apply partial --> value.
price = partial(calculate_price, tax_rate = 0.18)
print("New Price value:", price(500))
