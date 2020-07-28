from Library import *
from Person import *
from Books import *
#------используемые-библиотеки----------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random
#---------------------------------------------------------------------------------------------
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
    #Просмотр библиотеки
        self.add_img = tk.PhotoImage(file="стопка-книг.gif")
        self.img=tk.PhotoImage(file="книга.gif")
        btn_open_dialog = tk.Button(text='Welcome to the Library', command=self.open_dialog, bd=0,
                                    compound=tk.TOP, image=self.add_img,font="10")
        btn_open_dialog.place(x=40, y=30)

    def open_dialog(self):
        Child_enter()
        Main.destroy(self)


class Child_enter(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
    def init_child(self):
        self.title('Библиотека')
        self.geometry('370x360')
        self.config(background="#555")
        self.resizable(width=False, height=False)
        label_enter=Label(self, text="Enter the System",background="#555",foreground="#ccc",font=16 ).place(x=110, y=20)
        label_reg=Label(self, text="if you are visiting the program for the first \ntime then go to the registration",
                        background="#555",foreground="#ccc").place(x=75, y=215)

        self.Login = StringVar()
        label_Login = Label(self, text="Login :",background="#555",foreground="#ccc").place(x=50, y=80)
        entry_Login = Entry(self, width=30,textvariable=self.Login,background="#555",foreground="#ccc").place(x=100, y=80)

        self.password = StringVar()
        label_password = Label(self, text="Password :", background="#555", foreground="#ccc").place(x=30, y=120)
        entry_password = Entry(self, width=30, textvariable=self.password, background="#555", foreground="#ccc", show="*").place(x=100, y=130)

        button_enter = Button(self, text="Enter", width=20, background="#555", foreground="#ccc", command=self.enter_system)
        button_enter.place(x=115, y=180)

        button_reg = Button(self, text="Registration", width=20, background="#555", foreground="#ccc", command=self.open_reg)
        button_reg.place(x=115, y=260)

    def enter_system(self):
        if (self.Login.get()=="admin" and self.password.get()=="123"):
            print("OK")
            Child()#admin
        elif personL.searchPerson(self.Login.get(), self.password.get()):
            cuR = personL.searchPerson(self.Login.get(), self.password.get())
            print("OK\n" +"Name :"+ cuR.name+"\tLogin : "+cuR.login+"\tPassword :"+cuR.password)
            messagebox.showinfo("Info", "The enter was successful")
            Child1(cuR)#user
        else:
            messagebox.showerror("Error", "WRONG USERNAME OR PASSWORD")

    def open_reg(self):
        Child_registration()

class Child_registration(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
    def init_child(self):
        self.title('Библиотека')
        self.geometry('370x360')
        self.config(background="#555")
        self.resizable(width=False, height=False)
        label_enter=Label(self, text="Pass the Registration",background="#555",foreground="#ccc",font=16).place(x=95, y=20)

        self.Name = StringVar()
        label_Name=Label(self, text="Name :",background="#555",foreground="#ccc").place(x=50, y=80)
        entry_Name=Entry(self, width=30,textvariable=self.Name,background="#555",foreground="#ccc").place(x=100, y=80)

        self.Login = StringVar()
        label_Login=Label(self, text="Login :",background="#555",foreground="#ccc").place(x=50, y=120)
        entry_Login=Entry(self, width=30,textvariable=self.Login,background="#555",foreground="#ccc").place(x=100, y=120)

        self.Password = StringVar()
        label_Password=Label(self, text="Password :",background="#555",foreground="#ccc").place(x=30, y=160)
        entry_Password=Entry(self, width=30,textvariable=self.Password,background="#555",foreground="#ccc").place(x=100, y=160)

        label_reg=Label(self, text="you should fill in all the fields \nand then click on the button",
                        background="#555",foreground="#ccc").place(x=110, y=190)

        button_enter = Button(self, text="Enter", width=20,background="#555",foreground="#ccc", command=self.save_file)
        button_enter.place(x=115, y=230)

        button_e = Button(self, text="TEST", width=20,background="#555",foreground="#ccc", command=self.output)
        button_e.place(x=115, y=260)

    def save_file(self):    # сохранить данные файл при регистрации
        personL.append(Person(self.Name.get(), self.Login.get(), self.Password.get()))
        messagebox.showinfo("Info", "The registration was successful")
        Child_registration.destroy(self)

    def output(self):
        personL.print_list()

#---форма--админа--
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
    def init_child(self):
        self.title('Библиотека')
        self.config(background="#555")
        self.geometry('900x500')
        self.resizable(False, False)
    #****** Toolbar ********
        toolbar = Canvas(self,width=800,height=130,bg='#555', bd=5)
        toolbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

        button_delete = Button(toolbar, text=" remove the selected book from the list ", width=20,
                   background="#555", foreground="#ccc", command=self.book_delete)
        button_delete.pack(side=tk.TOP, fill=tk.X)

        f_top = LabelFrame(toolbar, height=100, width=500, text='adding a new book',background="#555",foreground="#ccc")
        f_top.pack(side=BOTTOM, padx=10, pady=10, ipadx=10, ipady=10)

        self.FIO = StringVar()
        label_FIO=Label(f_top, text="FIO :",background="#555",foreground="#ccc").grid(row=0, column=0, sticky=W, pady=10, padx=10)
        entry_FIO=Entry(f_top, width=30,textvariable=self.FIO,background="#555",foreground="#ccc").grid(row=0, column=1, sticky=W+E, padx=10)

        self.name=StringVar()
        label_name=Label(f_top, text=" Name of the book :",background="#555",foreground="#ccc").grid(row=0, column=5)
        entry_name=Entry(f_top, width=30,textvariable=self.name,background="#555",foreground="#ccc").grid(row=0, column=6, columnspan=3)

        self.UDC=StringVar()
        label_UDC=Label(f_top, text=" UDC :",background="#555",foreground="#ccc").grid(row=2, column=0, sticky=W, padx=10, pady=10)
        entry_UDC=Entry(f_top, width=30,textvariable=self.UDC,background="#555",foreground="#ccc").grid(row=2, column=1, columnspan=3)

        self.data=StringVar()
        label_publication_data=Label(f_top, text=" publication data :",background="#555",foreground="#ccc").grid(row=2, column=5)
        entry_publication_data=Entry(f_top, width=30,textvariable=self.data,background="#555",foreground="#ccc").grid(row=2, column=6, columnspan=3)

        self.copies=StringVar()
        label_count_of_copies=Label(f_top, text=" count of copies :",background="#555",foreground="#ccc").grid(row=2, column=9, sticky=W, padx=10, pady=10)
        entry_count_of_copies=Entry(f_top, width=15,textvariable=self.copies,background="#555",foreground="#ccc").grid(row=2, column=10, columnspan=3)

        #добавление в список
        button_add = Button(f_top,text="ADD",background="#555",width=20,
                             foreground="#ccc",command=self.book_append)
        button_add.grid(row=0, column=9, columnspan=3, sticky=E)

        #создание колонок
        self.tree = ttk.Treeview(self, columns=('author', 'UDC', 'name', 'publication data','count of copies'),
                                 height=15, show='headings')
        self.style = ttk.Style()
        self.style.configure("Treeview", font=(None, 10),background="#555", fieldbackground="red",
                             foreground="#ccc")
        # обращение к колонкам
        self.tree.column("author", width=200, anchor=tk.CENTER)
        self.tree.column("UDC", width=200, anchor=tk.CENTER)
        self.tree.column("name", width=200, anchor=tk.CENTER)
        self.tree.column("publication data", width=150, anchor=tk.CENTER)
        self.tree.column("count of copies", width=150, anchor=tk.CENTER)
        # наименование колонок
        self.tree.heading("author", text='AUTHOR')
        self.tree.heading("UDC", text='UDC')
        self.tree.heading("name", text='NAME')
        self.tree.heading("publication data", text='PUBLICATION DATA')
        self.tree.heading("count of copies", text='COUNT OF COPIES')
        select=self.tree.selection()
 #вывод книг
        cur=dllist.head
        index=iid=0
        while cur:
            self.tree.insert("",index,iid,value=(cur.data.FIO,cur.data.UDC,
                                                 cur.data.name,cur.data.publication_data,
                                                 cur.data.count_of_copies))
            index=iid=index+1
            cur=cur.next

        self.tree.pack()
        self.grab_set()
        self.focus_set()
    def book_append(self):
        #messagebox.showinfo('Error')
        dllist.append(Books(self.FIO.get(), self.UDC.get(), self.name.get(), self.data.get(), self.copies.get()))
        self.tree.delete(*self.tree.get_children())
        cur=dllist.head
        index=iid=0
        while cur:
            self.tree.insert("",index,iid,value=(cur.data.FIO,cur.data.UDC,
                                                 cur.data.name,cur.data.publication_data,
                                                 cur.data.count_of_copies))
            index=iid=index+1
            cur=cur.next
    def book_delete(self):
        cur = self.tree.set(self.tree.selection())
        b = Books(cur['author'], cur['UDC'], cur['name'], cur['publication data'], cur['count of copies'])
        dllist.delete(dllist.searchNode(b.name))
        self.tree.delete(self.tree.selection())


#--форма--пользователя--
class Child1(tk.Toplevel):
    def __init__(self,user):
        self.current_user = user
        super().__init__(root)
        self.init_child1()

    def init_child1(self):

        self.title('Библиотека')
        self.geometry('900x450')
        self.resizable(False, False)
    #****** Toolbar ********
    #создаем toolbar
        toolbar = Canvas(self,width=750,height=50,bg='#555', bd=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        toolbarV = Canvas(self,width=800,height=120,bg='#555', bd=5)
        toolbarV.pack(side=tk.BOTTOM, fill=tk.BOTH)
        label_info = tk.Label(toolbarV,text='if you want to take a book then select it and then click on the button   -->'
                            , background="#555", foreground="#ccc")
        label_info.place(x=50, y=10)

        label_return = tk.Label(toolbarV,text='if you want to return a book then enter the code of book what you taken and then click on the button   -->'
                            , background="#555", foreground="#ccc")
        label_return.place(x=50, y=60)

        label_ID = tk.Label(toolbarV,text='Code of the book witch you want to return    --> ', background="#555", foreground="#ccc")
        label_ID.place(x=50, y=90)

        self.label_code = tk.Label(toolbarV, text='***', background="#555", foreground="#ccc")
        self.label_code_info = tk.Label(toolbarV, text='this is your personal book code,'
                                                       ' it will be visible for some period of time    -->', background="#555", foreground="#ccc")

        button_take = Button(toolbarV, text="TAKE", width=10, background="#555", foreground="#ccc", command=self.take_book)
        button_take.place(x=450, y=10)

        self.entry = StringVar()
        entry_return = Entry(toolbarV, width=20, textvariable=self.entry, background="#555", foreground="#ccc")
        entry_return.place(x=320, y=90)
        button_return = Button(toolbarV, text="RETURN", width=10, background="#555", foreground="#ccc",command=self.return_book)
        button_return.place(x=620, y=60)

        label_search = tk.Label(toolbar, text='Search the Book by title : '
                              , background="#555", foreground="#ccc", padx="10", pady="8",font="2")
        label_search.place(x=20, y=10)

        self.name = StringVar()
        entry_search = Entry(toolbar, textvariable=self.name, width=45)
        entry_search.place(x=290, y=23)
        button_search=Button(toolbar,text="SEARCH",background="#555",width=15,
                             foreground="#ccc",padx="15",pady="7",command=self.show_search)
        button_search.place(x=680, y=13)
        button_X=Button(toolbar,text="X", background="#555", width=5, pady=7, command=self.return_table, foreground="#ccc")
        button_X.place(x=830, y=13)

    #-------------------------------
    #создание колонок
        self.tree = ttk.Treeview(self, columns=('author', 'UDC', 'name', 'publication data','count of copies'),
                                 height=15, show='headings')
    # обращение к колонкам
        self.tree.column("author", width=200, anchor=tk.CENTER)
        self.tree.column("UDC", width=200, anchor=tk.CENTER)
        self.tree.column("name", width=200, anchor=tk.CENTER)
        self.tree.column("publication data", width=150, anchor=tk.CENTER)
        self.tree.column("count of copies", width=150, anchor=tk.CENTER)
    # наименование колонок
        self.tree.heading("author", text='AUTHOR')
        self.tree.heading("UDC", text='UDC')
        self.tree.heading("name", text='NAME')
        self.tree.heading("publication data", text='PUBLICATION DATA')
        self.tree.heading("count of copies", text='COUNT OF COPIES')
    #вывод книг
        cur=dllist.head
        index=iid=0
        while cur:
            self.tree.insert("",index,iid,value=(cur.data.FIO,cur.data.UDC,
                                                 cur.data.name,cur.data.publication_data,cur.data.count_of_copies))
            index=iid=index+1
            cur=cur.next

        self.tree.pack()
        self.grab_set()
        self.focus_set()
    #-------------------------------
    #=====Сторонние==функции========
    def show_search(self):
        if dllist.searchNode(self.name.get()) !=False:
            self.tree.delete(*self.tree.get_children())
            current = dllist.searchNode(self.name.get())
            i = 0
            self.tree.insert('', 'end', text=str(i), values=(current.FIO, current.UDC,
                                                             current.name, current.publication_data,
                                                             current.count_of_copies))
            i += 1
        else:
            messagebox.showerror('Error',"The book is NOT found")
    def return_table(self):
        self.tree.delete(*self.tree.get_children())
        cur=dllist.head
        index=iid=0
        while cur:
            self.tree.insert("",index,iid,value=(cur.data.FIO,cur.data.UDC,
                                                 cur.data.name,cur.data.publication_data, cur.data.count_of_copies))
            index=iid=index+1
            cur=cur.next


    def take_book(self):
        cur = self.tree.set(self.tree.selection())
        b = Books(cur['author'], cur['UDC'], cur['name'], cur['publication data'], cur['count of copies'])
        if (dllist.search_and_minus_count_book(b.name) != False):
            cuR = dllist.search_and_minus_count_book(b.name)
            print(cuR.__dict__)
        text = random.randint(100000, 999999)
        self.label_code_info.place(x=50, y=38)
        self.label_code.config(text="{}".format(text))
        self.label_code.place(x=480, y=38)
        print(text)
        code_list.append(List_book_take(str(text), b))
        messagebox.showinfo("Info", "You take:\n\n" + "author: " + b.FIO + "\nname: " + b.name)

    def output(self):
        print("OOKKKKKK")
        if code_list.size == 0:
            print("Список пуст")
            return
        cur = code_list.head
        while cur:
            print(cur.data.Book.__dict__)
            print(cur.data.code)
            cur = cur.next

    def return_book(self):
        if code_list.searchCodeOfBook(self.entry.get()):
            current_b = code_list.searchCodeOfBook(self.entry.get())
            messagebox.showinfo("Info", "Thanks for returning the book")
            code_list.delete(current_b)
        else:
            messagebox.showerror("Error!", "Sorry, the book on this key has already been returned\n"
                                           " or you entered an invalid key")




#---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("LIBRARY")
    root.geometry("380x400+300+200")
    #root.config(background="#555")

    root.resizable(False, False)
    root.mainloop()
