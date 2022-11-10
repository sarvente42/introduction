a = int(input("number 1->>"))
b = int(input('number 2->>'))
action = input("action->>")
if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "avg":
    print((a+b)/2)
elif action == "*":
    print(a * b)
else:
    print("The action is not found")