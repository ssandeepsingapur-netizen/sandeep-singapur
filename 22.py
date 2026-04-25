class book:
    def __init__(self, title, author="unknown"):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
book1 = book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = book("To Kill a Mockingbird")
book1.display_info()
book2.display_info()