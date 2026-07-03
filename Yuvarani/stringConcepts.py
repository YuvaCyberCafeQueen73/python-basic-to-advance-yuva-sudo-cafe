# String can be number , special character, text.
# denoted as "", ''. eg: a= "yuva", b = 'rani'

driver_name = 'Raja'

#lower, upper
print(f"lower and upper:", driver_name.lower(), driver_name.upper())

#masked mobile number:
mobile_no = "9876543210"
masked_mobile_no = mobile_no[:2] + "******" + mobile_no[-2:]
print(masked_mobile_no)

#format every 1st letter will be captial.
song = "yuva new Song"
lyrist = "Yuva queen"

print(f"what a new song:", song.title())
print(f"writtern by:", lyrist.title())

#replace the location.
location = "palani"
fixed_loaction = "Chennai"
print(f"Your location currently changed into :", location.replace(location, fixed_loaction))

#get the id from the message and use split.
#strip - used for remove the space from front and back.
uber_msg = "your uber booking id is: UBER123. Please keep safe"
print("Get the uber id:", uber_msg.split(":")[1].split(".")[0].strip())

#get the offer id:
promo_msg = "zomato100 to get 100 off on your first order"
if "zomato100" in promo_msg:
    print("apply the discount")
else:
    print("No discount")


#for-loop concepts for string.

name = "yuva queen"
initials = "".join([word[0].upper() for word in name.split()])
print(initials)

#strip - it remove the space b/w front and back.
dirt_input = " airpot  "
print(dirt_input.strip())

#count
#split --> if ur provided split() --> it cut individual word.
#split(" and ") --> it splits the sentence into phrases around " and ".
word = "the trip was amazing and car was cleaned!"
word_count = len(word.split(" and "))
print(word_count)
