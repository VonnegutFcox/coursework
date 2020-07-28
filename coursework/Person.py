from DoublyLinkedList import *
#--Person's-class--------------------------
class Person:
    login = ''
    password = ''
    name = ''
    book_list = {}
#--конструктор-----------------------------
    def __init__(self, n, log, pas):
        self.login = log
        self.password = pas
        self.name = n

#--set------------------------------------
    def set_login(self, log):
        self.login = log

    def set_password(self, pas):
        self.password = pas

    def set_name(self, n):
        self.name = n


#--get------------------------------------
    def get_log(self):
        return self.login

    def get_password(self):
        return self.password

    def get_name(self):
        return self.name



personL = DoublyLinkedList()
code_list = DoublyLinkedList()
