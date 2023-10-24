num = input("enter a number")
num = int(num)
print(num)
if num> 10:
    print("big")
    print("********")
else:
    print("small")
print("on we go")

response = ""
while response != "y" and response != "n":
    response = input("y or n")
print("you said", response)


