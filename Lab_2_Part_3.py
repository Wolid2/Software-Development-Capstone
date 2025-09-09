# importing dataclass from dataclasses module
from dataclasses import dataclass
# defining a dataclass for Student
@dataclass

# defining the Student class
class Student :
  name: str
  college_id: str
  gpa: float  
# it is Overriding the string representation method
  def __str__(self):
    return f'Name: {self.name}, College ID: {self.college_id}, GPA: {self.gpa}'

# defining the main function
def main():
  # creating student names ,Id and gpa
  wolid = Student('wolid', '1234rwd5', 3.5)
  print(wolid.name)
  print(wolid.college_id)
  print(wolid)

# creating another student name ,Id and gpa
  kamal = Student('Kamal', '6789abcd', 3.8)
  print(kamal)

# calling the main function to run the program
main()