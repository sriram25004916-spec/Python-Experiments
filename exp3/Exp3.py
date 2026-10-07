# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 07:56:48 2026

@author: user
"""

s="Hello Python"
print("original string",s)
print("Length:",len(s))
print("Uppercase",s.upper())
print("lowercase",s.lower())
print("Characterstics at index:",s[7])
print("Position of python",s.find("Python"))
print("Slice",s[6:9])
print("Replac:",s.replace("Python","World"))
print(s)
print("Contain Python:","Python" in s)
print("Concatination:",s+"Programming")
s2="  Hello Sumit   "
print("Trim:",s2.strip())
