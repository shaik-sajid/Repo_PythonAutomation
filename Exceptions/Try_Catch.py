list = ["AP", "Karnataka", "Tamilnadu"]

try:
    print(list[3-1+2])
except Exception as e:
    print(e)
    print("There was some error in try block")
finally:
    print("Hello World")