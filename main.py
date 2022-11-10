a = int(input("number 1->>"))
b = int(input("number 2->>"))
c = int(input("number 3->>"))
action = input('action->>')
if action == '+':
    print(a + b + c)
elif action == '*':
    print(a * b * c)
else:
    print("Action is not found")