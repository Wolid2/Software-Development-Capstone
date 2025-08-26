# asking a user how many class is taking 
Class_names = input('How many classes are you taking this Semester? ')  

# we creating an empty list to store the class names
class_list = []


# looping over to get the class names
for i in range(int(Class_names)):
    class_name = input('Enter the name of the class: ')
    class_list.append(class_name)

# printing each class name on a separate lines
print('The classes you are taking this semester are:')
for class_name in class_list:
    print(class_name) 