class Books(object): #класс Книжки
    def __init__(self,FIO,UDC,name,publication_data,count_of_copies):
        """"Constructor"""
        self.FIO = FIO
        self.UDC = UDC
        self.name = name
        self.publication_data = publication_data
        self.count_of_copies = count_of_copies


class List_book_take:
    def __init__(self, c, book):
        self.Book = book
        self.code = c
