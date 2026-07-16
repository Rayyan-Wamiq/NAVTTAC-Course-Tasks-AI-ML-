class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def checkout(self):
        if self.is_checked_out:
            print(f'"{self.title}" is already checked out')
        else:
            self.is_checked_out = True
            print(f'You have checked out "{self.title}"')

    def return_book(self):
        self.is_checked_out = False
        print(f'"{self.title}" has been returned')

Book1 = Book("Harry Potter", "J.K. Rowling")
Book2 = Book("Game of Thrones", "George R.R. Martin")

Book1.checkout()
Book1.checkout()

print(f'"{Book1.title}" Checked out: {Book1.is_checked_out}')
print(f'"{Book2.title}" Checked out: {Book2.is_checked_out}')

Book1.return_book()
print(f'"{Book1.title}" Checked out: {Book1.is_checked_out}')