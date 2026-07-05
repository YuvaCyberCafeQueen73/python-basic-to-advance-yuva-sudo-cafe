# HOF
#High order function is either :
  # - Take another function as a argument.
  # - Return a function as its output.
from fontTools.misc.cython import returns


# Used to make a more readable , flexible and dynamic.

def build_email(username, provider):
    if provider == "gmail":
        return f"{username}@gmail.com"
    if provider == "yahoo":
        return f"{username}@yahoo.com"
    if provider == "hotmail":
        return f"{username}@hotmail.com"
    else:
        return f"{username}@unknow.com"

print(build_email('yuva', 'gmail'))
print(build_email('rani', 'hotmail'))
print(build_email('raja', 'yahoo'))

# i have to add new provider "tcsgmail.com" ---> need to change the existing code so we need to go HOF.

# so we need to create everything as a function.
 # predefined function.
def gmail_func(username, domain = "gmail.com"):
    return f"{username}@{domain}"

def ymail_func(username, domain = "gmail.com"):
    return f"{username}@{domain}"


def hmail_func(username):
    return f"{username}@hotmail.com"

def build_email(username, email_func):
    return  email_func(username)
username = "Queen"
result = build_email("Queen", gmail_func)
print("result:", result)

#--------------------------------------------------------------------another way return output as param--------

def email_domain(domain):
    def build_email(uname):
        return f"{uname}@{domain}"

    return build_email

final_result = email_domain("yahoo.com")
print("final_result -->", final_result("Queenboss"))

#------------------------Impure function-------------------------------------------------------
total = 0
def balance(amount):
    global total
    total += amount
    print('Balance amount is from balance function:', total)

balance(200)
print("total assigned as global value:", total)
#how total coming as 200 means this is the side effect above function override.
#--------------------------------------------------------------------------------------------------

#----------------------Pure Function-----------------------------------------------------------
total=0
def balance(amount):
     total += amount
     print('Balance amount is from balance function:', total)

balance(20)
print("total assigned as global value:", total)


