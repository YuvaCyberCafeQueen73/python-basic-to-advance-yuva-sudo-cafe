

class bank:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
    def display(self):
        print(f"Hi {self.name}! and your age is {self.age} and current balance is: {self.balance}")

account = bank("Yuva", 27, 450.00)
account.display()
account1 = bank("Rani", 30, 100.00)
account1.display()

# how to call one class method into another class.

class A:
    def greet(self):
        print("Welcome to class A!")
obj_a = A()
class B:
    def display(self):
        print("I m new class B?")
        obj_a.greet()

obj_b = B()
obj_b.display()
#--------------------------------------------------------------

#what about static method:
class last_class():
    @staticmethod
    def last_with_static_keyword():
        print(" i m last class with static keyword")
#------------------------------------------------------------------

#Method 2: Pass the object to another class (better design)

class better_design:
    def method_2(self, obj):
        print("calling the A class function")
        obj.greet()
        last_class.last_with_static_keyword()

obj_c = better_design()
obj_c.method_2(obj_a)
#-------------------------------------------------------------










