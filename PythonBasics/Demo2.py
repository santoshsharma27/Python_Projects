values = [1, 2, "Rahul", 4, 5]
# List is data type that allows multiple values and can de different data types
print(values[0])
print(values[3])
print(values[-1])
print(values[1:3])
values.insert(3, "Shetty")
print(values)   # [1, 2, 'Rahul', 'Shetty', 4, 5]
values.append("End")
print(values)   # [1, 2, 'Rahul', 'Shetty', 4, 5, 'End']
values[2] = "RAHUL"
print(values)
del values[0]   # updating
print(values)   # deleting

# Tuple- Same as LIST data type but immutable
val = (1, 2, "Rahul", 4.5)
# val[2] = "RAHUL"
print(val)

# Dictionary
dic = {"a": 2, 4: "abc", "c": "Hello world"}
print(dic[4])
print(dic["c"])

dict = {}
dict["firstname"] = "Santosh"
dict["lastname"] = "Sharma"
dict["gender"] = "Male"
print(dict)
print(dict["lastname"])
