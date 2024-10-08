classmate= {"Kiwi","Strawberry","Mango","Banana","Peach"}

print("Hello!")
user= set()
 
print("Enter your first favorite fruit:")
fruit_1= input()
user.add(fruit_1)

print("Enter your second favorite fruit:")
fruit_2= input()
user.add(fruit_2)

print("Enter your third favorite fruit:")
fruit_3= input()
user.add(fruit_3)

if set.intersection(user,classmate):
    print("Our common favorite fruit(s):",set.intersection(user,classmate))
else:
    print("We have no common favorite fruits.")