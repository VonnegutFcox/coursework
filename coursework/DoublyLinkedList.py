from Books import *

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    def append(self,data):#добавление элемента в конец списка(двунаправленного)
            self.size+=1
            if self.head is None:
                new_node = Node(data)
                new_node.prev=None
                self.head=new_node
            else:
                new_node=Node(data)
                cur=self.head
                while cur.next:
                    cur=cur.next
                cur.next=new_node
                new_node.prev=cur
                new_node.next=None

    def print_list(self): #вывод элементов списка(двунаправленного)
        if self.size == 0:
            print("Список пуст")
            return
        cur=self.head
        while cur:
            print(cur.data.__dict__)
            cur=cur.next

    def searchNode(self,value):
            i = 0
            flag = False
            current = self.head
            if(self.head == None):
                print("List is empty")
                return
            while(current != None):
                if(current.data.name == value):
                    flag = True
                    break
                current = current.next
                i = i + 1
            if(flag):
                if(current.data.count_of_copies!=0):
                    return(current.data)
                else:
                    return False
            else:
                return False
    def search_and_minus_count_book(self,value):
            i = 0
            flag = False
            current = self.head
            if(self.head == None):
                print("List is empty")
                return
            while(current != None):
                if(current.data.name == value):
                    flag = True
                    break
                current = current.next
                i = i + 1
            if(flag):
                if(current.data.count_of_copies!=0):
                    current.data.count_of_copies = int(current.data.count_of_copies-1)
                    return(current.data)
                else:
                    return Exception
            else:
                return False
    def searchPerson(self,valueL,valueP):
            i = 0
            flag = False
            current = self.head
            if(self.head == None):
                print("List is empty")
                return
            while(current != None):
                if(current.data.login == valueL)and(current.data.password == valueP):
                    flag = True
                    break
                current = current.next
                i = i + 1
            if(flag):
                return(current.data)
            else:
                return False
    def searchCodeOfBook(self,value):
            i = 0
            flag = False
            current = self.head
            if(self.head == None):
                print("List is empty")
                return
            while(current != None):
                if(current.data.code == value):
                    flag = True
                    break
                current = current.next
                i = i + 1
            if(flag):
                return(current.data)
            else:
                return False

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
