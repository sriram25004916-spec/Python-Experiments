employee={"name":"kukdukoo",
          "age":26,
          "department":"management",
          "id":4669123,
          "criminal background":"2 half murders",
          "father occupation":"rowdy sheeter"}


print("the dict is ",employee)
print("name is ", employee["name"])


employee["working days"]=27
print("updated dictionary ", employee)


employee["age"]=28
print("updated age ", employee["age"])


del employee["working days"]
print("again dict",employee)

# printing keys
print(employee.keys())


# printing values
print(employee.values())


# printing items
print(employee.items())


#get()= checks if given key is available
print("name",employee.get("name"))
print("mother",employee.get("mother"))

         
