# definine a class Author
class Author:
  def __init__(self, name ):
    # initialize name and books attributes
    self.name = name
    # creating an empty list to store book titles
    self.books = []

  def publish(self, title):
    if title not in self.books:
    # adding a book title to the books list
       self.books.append(title)
      
    else:
       print(f'Error: "{title}" has already been published.')

  def __str__(self):
    # converting the list of books title into a string
    # also if no books is publiushed then it will shows a default message
    titles = ', '.join(self.books) or 'No books published'
    return f' {self.name}, Books Published: {titles}'

def main():
# creating an author
  roone = Author('J.K. Rooneling')
  # which is publishing two books
  roone.publish('Harry Potter ') 
  roone.publish('Leaning Python') 
  # printing the author details
  print(roone)

# creating another author
  wolid = Author('Wolid Kamal')
  wolid.publish('Amazing Stories')
  wolid.publish('Good memories') 
  print(wolid)

main()



