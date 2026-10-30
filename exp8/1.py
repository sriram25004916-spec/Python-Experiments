#implement regular expression module in python
import re
date=input("enter date")
pattern=r'^\d{2}/\d{2}/\d{4}$'
pat=re.fullmatch(pattern,date)
if pat:
    print("given valid date")
else:
    print("invalid")
#fullmatch used to check if the given pattern is fully correct or not.
