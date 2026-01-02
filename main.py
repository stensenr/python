output = ""
value = None

while value is None:
   
    try:
        value = int(input("How old are you? "))
    except ValueError:
        print("that is not a valid integer")


0
if value > 18:
    output = "You are an adult"
else:
    output = "You are a child"

print(output)

