print("inherit concepts")

class app1:
    def v1(self):
        print("orders")

version1 = app1()
version1.v1()

class app2:
    def v2(self):
        print("refund")
version2 = app2()
version2.v2()

#---------------------------------------------------
#Types -> 5 type.

#single inheritance.

class Teacher:
    def stu1(self):
        print("I m stud1 1st rank in the school")

class Award(Teacher):
    def stu1(self):
      print("I m stud1 i m a 2nd rank!")

    def price(self):
        print("Award goes to stud 2")


result = Award()
result.stu1()
result.price()
#--------------------------------
#override 1st class method.
result.stu1()
#--------------------------------------S
#2. Multiple Inheritance
#One child inherits from multiple parents.

class Authentication:
    def login(self):
        print("Employee login successfully1")

class Email():
    def sendEmail(self):
        print("send the email!")

class Employee(Authentication, Email):
    pass

emp = Employee()
emp.login()
emp.sendEmail()

#-----------------------------------------------------------
#Multilevel Inheritance

#A chain of inheritance.

class Person:
    def pernoal_info(self):
        print("get the personal info")

class Employee(Person):
    def employee_info(self):
        print("get the employee info")

class Manager(Employee):
    def manager_info(self):
        print("Get All the info")


result = Manager()
result.pernoal_info()
result.employee_info()
result.manager_info()

#------------------------------------
#Rule 2
#If many classes inherit from the same parent, it's Hierarchical Inheritance.

class Employee:

    def login(self):
        print("Login Successful")


class Developer(Employee):

    def code(self):
        print("Writing Code")


class Tester(Employee):

    def test(self):
        print("Testing Application")


class Manager(Employee):

    def manage(self):
        print("Managing Team")


developer = Developer()
developer.login()
developer.code()

tester = Tester()
tester.login()
tester.test()

manager = Manager()
manager.login()
manager.manage()
#---------------------------------------
#Hybrid Inheritance

class Employee:

    def login(self):
        print("Login")


class Developer(Employee):

    def code(self):
        print("Writing Code")


class Tester(Employee):

    def test(self):
        print("Testing Application")


class TechLead(Developer, Tester):
    pass


t = TechLead()

t.login()
t.code()
t.test()