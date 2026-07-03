#L --> Local variable

def order():
    food = "Dhosa"
    print("Your order is:", food)

order()
# print(food) # local variable cant access outside the function scope.

#Enclosing --> Closure
#outer function varibale can be access the inner function is called --> enclosure.

def cart():
    discount = 10

    def checkout():
        print("Applying the discount:", discount)

    checkout()

cart()

#G --> Global function --->

user_id = 'Yuvarani'

def homepage():
    print("welcome to ",user_id)

def profile():
    print(user_id, "Your profile is ready!")

homepage()
profile()

#built-in varibale --> it print path

print(__file__)

#use-case
delivery_partner = "zomato"

def hotel():
    item = "Pizza"

    def order_now():
        quantity = 5
        print(f"ordeing {item} with {quantity} using {delivery_partner}")

    order_now()

hotel()