classmate= set("Kiwi","Strawberry",",Mango","Banana","Peaches")

print("Hello!")
user= set()

fruit_1= input
print("Enter your first favorite fruit:"), input
user.add(input)

print("Enter your second favorite fruit:"), input()
user.add(input)

print("Enter your third favorite fruit:"), input()
user.add(input)

common= set.intersection(user,classmate)

if common==classmate :
    print("Our common favorite fruit(s):")
else:
    print("We have no common favorite fruits.")