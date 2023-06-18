my_list = ["Andhra", 1, 12.345, True]

print(my_list[0])
print(my_list[2])
print(my_list[-1])

my_list[0] = "Andhra Pradesh"
print(my_list[0])
print(my_list[0:3])

my_list.append("Karnataka")
print(my_list)

my_list.insert(1, "Telangana")
print(my_list)

del my_list[True]
print(my_list)

del my_list[3]
print(my_list)