class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        
    

    def show_info(self):
        print(f"""
Kitob Nomi: {self.title}
Muallifi: {self.author}
Yili: {self.year}
Holati: { "Mavjud" if self.is_available else "Mavjud emas"}
              """)

    def borrow_book(self):
        if self.is_available:
            self.is_available =False
            print("Kitob muvaffaqiyatli olindi")
        else:
            print("Kitob hozircha band!")
        
    def return_book(self):
        self.is_available = True
        print("Kitob muvaffaqtiyatli qaytarildi")


class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id=student_id
        self.borrowed_books = []
    
    def show_info(self):
        print(f"Talaba ismi:{self.name}\nTalaba id: {self.student_id}")
        if len(self.borrowed_books) > 0:
            print("Olgan kitoblari")
            for book in self.borrowed_books:
                book.show_info()
        else:
            print("Bu talaba kitob o'qimaydi")
    
    def take_book(self,book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.borrow_book()
            
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("BU talaba bunday kitob olmagan")

book = Book("Atomic Habits", "James Clear", 2018)

book.show_info()
student = Student("Ali", 101)

student.take_book(book)
student.show_info()

student.return_book(book)

student.show_info()
book.show_info()
