# python have 2 loop for and while.
#while - it will work untill my condition satisified otherwise it went out.
#for - it will iterate the array. no condition base check we have range option, like how many times it will run.



names = ["yuva", 'rani', "boss"]

for n in names:
    print(n.upper())

correct_pin = "1234"
entered_pin = ""

"""while correct_pin != entered_pin:
    entered_pin = input("enter the correct pin:")"""

print("access granted")

#continue
#break ---> break if my condition satsified it will come out the condition or loop.

"""for i in range(0,10):
    if i ==5:
        break
    print(i)"""


names = [1,2,3,4,6,7,8,9,10, 5]

for i in names:
    if i ==5:
        break
    print(i)

# find the duplicate value count
lang = "proagramming"
store = ''
result = []
final_op = ''
for l in lang:
    if l not in result:
        result.append(l)
    final_op = str(result).join("")
print(final_op)

#while loop count down.

count = 5

while count > 0:
    print(f" Count down starts:", count)
    count-= 1
print("Times Up!!")


#while loop add to cart item

items = []

while True:
    item = input("enter ur item type(done) to close the order:")
    if item.lower() == 'done':
        break
    items.append(item)
print("Your order successfully ordered!")