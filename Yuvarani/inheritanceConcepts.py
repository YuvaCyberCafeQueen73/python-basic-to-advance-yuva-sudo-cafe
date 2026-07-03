#nheritance allows one class (child/derived class) to reuse the properties and methods of another class (parent/base class).
from loop import result


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

"""class Teacher:
    def stu1(self):
        print("I m stud1 1st rank in the school")

class Award(Teacher):
    # def stu1(self):
    #     print("I m stud1 i m a 2nd rank!")

    def price(self):
        print("Award goes to stud 2")


result = Award()
result.stu1()
result.price()"""