#if, elif, else
#nested if
# operators using if  -->and or .

mark = 55

if mark >= 90:
    print("grade A")
elif mark >=70:
    print("grade B")
elif mark >=50:
    print("grade C")
else:
    print("failed")

age = 18
has_licence = "yes"

if age >=18:
    print("your eligibale for take a licence")
    if has_licence == "yes":
        print("You can drive")

else:
    print("your too young")


reachrage_amount = 200
data_balance = 1.5

if reachrage_amount >= 399 or data_balance >= 1:
    print("your eligible for get the bonus")
else:
    print("your not eligible for get the bonus")

order_amount = 2000
days = "sat"
membership = "no"

if order_amount >= 2000 and days in ["sat", "sun"] or membership == "gold":
    print("20% discount applied")
else:
    print("not applied")

