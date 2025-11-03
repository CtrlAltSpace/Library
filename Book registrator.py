import random

# ISBN number
def generate_isbn():
    isbn = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    return isbn

# Get book information
title = input("Enter book title: ")
author = input("Enter book author: ")

# Generate ISBN number
isbn = generate_isbn()

# Print the result
print(f"{title} by {author}, ISBN = {isbn}")