# variable is a container for a value (String , integer , float , boolean)
#           a variable behaves as if it contains the assigned value

#these are strings , we treat them as characters even the numbers
first_name = "Arindam"
last_name = "Deb"
food = "pizza"
email = "debarindam225@gmail.com"


print(first_name)
print(f"Hello {first_name}")  
print(f"I like {food}")
print(f"Here's my email: {email}")


#integers
age = 21
quantity = 4
no_of_students = 56

print(f"you are {age} years old")
print(f"you are buying {quantity} nos of blankets")
print(f"my class has {no_of_students} students")

#float
marks = 54.67

print(f"bro got {marks} marks in english")

#boolean

isStudent = True
in_sale = False

print(f"Are you a student ? {isStudent}")

if isStudent:
    print("he is a student")
else:
    print("he isnt a student")

if in_sale:
    print("the item is in sale")
else:
    print("the item is not in sale")


