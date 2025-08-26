# Asking a user for their names and store it in the variables
name = input('what is your name? ')
# Asking the user for the month of their birthdays
Months_of_your_Birthday = input('What month were you born in? ')
# Printing a message with the user's name and birth month
print('Hello ' + name + '!')

# Checking if the user's birth month is January
if Months_of_your_Birthday.lower() == 'january':
  print('Happy birth month!')
# printing the number of letters in the user's name
print(f'There are {len(name)} letters in your name')