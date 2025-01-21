#the proces of converting a variable from one data type to another 
#                                     str() , int() , float() , bool() 

name =  "arindam"
age = 21
gpa = 0.2
is_student = True

#gpa mess
print(type(gpa))

gpa = int(gpa)

print(gpa)
print(type(gpa))

#messing with age

print(age)
print(type(age))

age = str(age)
age += "1"

print(age)

#name =  is something is there then it will return true , if blank then false
name = bool(name)

print(name)