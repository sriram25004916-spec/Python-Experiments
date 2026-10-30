import re
data=input("enter email or mobile number")
email_pattern=r'^[a-zA-z0-9.%+-]+@[a-zA-z0-9.-]+.[a-zA-Z]{3}$'
mobile_pattern=r'^[0-9]{10}$'
if re.fullmatch(email_pattern,data):
    print("Valid Email")
elif re.fullmatch(mobile_pattern,data):
    print("Valid Mobile Number")
else:
    print("invalid")
