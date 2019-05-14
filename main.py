from tkinter import *
from tkinter import messagebox
import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS student(id integer primary key autoincrement, NAME TEXT , ADRESS TEXT, CONTACT INT, CLASS TEXT, BOOK1 TEXT, BOOK2 TEXT, AADHAR INT)")
        self.conn.commit()

    def insert(self, NAME, CONTACT, ADRESS, CLASS, BOOK1, BOOK2, AADHAR):
        self.cur.execute("INSERT INTO student VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)",
                         (NAME, CONTACT, ADRESS, CLASS, BOOK1, BOOK2, AADHAR))
        self.conn.commit()

    def delete(self, student_id):
        self.cur.execute("DELETE FROM student WHERE id = ?", (student_id,))
        self.conn.commit()

    def view(self):
        self.cur.execute('SELECT * FROM student')
        rows = self.cur.fetchall()
        return rows

    def select(self):
        self.cur.execute("SELECT * FROM student")

    def search(self, NAME):
        self.cur.execute("select * from student where name = ?", (NAME))


class Gui:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Library Management App")
        self.root.geometry("700x400")
        self.root.resizable(False, False)
        self.frame = Frame(root, width=350, height=400)
        self.frame.pack(side="left")

        #Menu bar
        menubar = Menu(root)
        root.config(menu=menubar)
        
        # File menu list
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New",  )
        filemenu.add_command(label="Open",  )
        filemenu.add_command(label="Save",  )
        filemenu.add_command(label="Save as...",  )
        filemenu.add_command(label="Close",  )
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        # Edit MENU
        editmenu = Menu(menubar)
        editmenu.add_command(label="Undo",  )
        editmenu.add_separator()
        editmenu.add_command(label="Cut",  )
        editmenu.add_command(label="Copy",  )
        editmenu.add_command(label="Paste",  )
        editmenu.add_command(label="Delete",  )
        editmenu.add_command(label="Select All",  )
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        # Help MENU
        helpmenu = Menu(menubar)
        helpmenu.add_command(label="Help Index",  )
        helpmenu.add_command(label="About...",  )
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Labels on the left side so user can fill the boxes
        self.lbl_font = ("Times", 15)
        self.name_lbl = Label(self.frame, text="Name: ", font=self.lbl_font)
        self.name_lbl.place(x=30, y=20)
        self.contact_lbl = Label(
            self.frame, text="Contact: ", font=self.lbl_font)
        self.contact_lbl.place(x=30, y=60)
        self.add_lbl = Label(self.frame, text="Address: ", font=self.lbl_font)
        self.add_lbl.place(x=30, y=100)
        self.class_lbl = Label(self.frame, text="class: ", font=self.lbl_font)
        self.class_lbl.place(x=30, y=180)
        self.book_lbl = Label(self.frame, text="books: ", font=self.lbl_font)
        self.book_lbl.place(x=30, y=220)
        self.aadhar_lbl = Label(
            self.frame, text="aadhar: ", font=self.lbl_font)
        self.aadhar_lbl.place(x=30, y=300)

        # Entry of everything so user can enter details to add
        self.name_txtvar = StringVar()
        self.name_ent = Entry(self.frame, width=25,
                              textvariable=self.name_txtvar)
        self.name_ent.place(x=150, y=20)

        self.contact_txtvar = StringVar()
        self.contact_ent = Entry(self.frame, width=25,
                                 textvariable=self.contact_txtvar)
        self.contact_ent.place(x=150, y=60)

        self.address_entry = Text(self.frame, width=19, height=3)
        self.address_entry.place(x=150, y=100)

        self.class_txtvar = StringVar()
        self.class_ent = Entry(self.frame, width=25,
                               textvariable=self.class_txtvar)
        self.class_ent.place(x=150, y=180)

        self.book1_txtvar = StringVar()
        self.book1_ent = Entry(self.frame, width=25,
                               textvariable=self.book1_txtvar)
        self.book1_ent.place(x=150, y=220)

        self.book2_txtvar = StringVar()
        self.book2_ent = Entry(self.frame, width=25,
                               textvariable=self.book2_txtvar)
        self.book2_ent.place(x=150, y=260)

        self.aadhar_txtvar = StringVar()
        self.aadhar_ent = Entry(self.frame, width=25,
                                textvariable=self.aadhar_txtvar)
        self.aadhar_ent.place(x=150, y=300)

        # Right frame for main output and buttons
        self.rframe = Frame(root, width=350, height=400)
        self.rframe.pack(side="right")

        # Buttons for add, delete, search to do work
        self.button_font = ("times", 12)
        self.add_butt = Button(
            self.rframe, text="Add", font=self.button_font, width=9, command=self.add_command)
        self.add_butt.place(x=10, y=20)
        self.del_button = Button(self.rframe, text="Delete",
                                 font=self.button_font, width=9, command=self.delete_selection)
        self.del_button.place(x=110, y=20)
        self.search_button = Button(self.rframe, text="Search",
                                    font=self.button_font, width=9, command = self.search)
        self.search_button.place(x=210, y=20)

        self.view_button = Button(self.rframe, text="View all",
                                  font=self.button_font, width=9, command=self.view_all)
        self.view_button.place(x=10, y=60)
        self.update_button = Button(
            self.rframe, text="Update", font=self.button_font, width=9)
        self.update_button.place(x=110, y=60)
        self.clear_button = Button(
            self.rframe, text="clear", font=self.button_font, width=9, command=self.clear)
        self.clear_button.place(x=210, y=60)

        self.show_txt = Listbox(self.rframe, width=50, height=15)
        self.show_txt.place(x=10, y=100)
        self.show_txt.bind("<Double-Button-1>", self.selection)

    # Selection
    def selection(self, Event):
        self.clear()
        selected = self.show_txt.curselection()         # selection
        data_list = self.db.view()                      # database view importing to select
        one_element = data_list[selected[0]]
        self.name_txtvar.set(one_element[1])
        self.contact_txtvar.set(one_element[2])
        self.address_entry.insert(END, one_element[3])
        self.class_txtvar.set(one_element[4])
        self.book1_txtvar.set(one_element[5])
        self.book2_txtvar.set(one_element[6])
        self.aadhar_txtvar.set(one_element[7])
        self.student_id = one_element[0]
        return self.student_id

    # delete
    def delete_selection(self):
        student_id = self.selection(Event)
        self.db.delete(int(student_id))
        self.view_all()
        self.clear()
        self.add_succesful("Deleted", "Deleted Succesfully")

    # Error message pop up
    def error_message(self, message):
        messagebox.showerror("Error", "Please enter " + str(message))

    # Succesfully added message pop up
    def add_succesful(self, info, message):
        messagebox.showinfo(info, message)

    # Clear 
    def clear(self):
        self.name_txtvar.set('')
        self.contact_txtvar.set('')
        self.address_entry.delete('1.0', 'end')
        self.class_txtvar.set('')
        self.book1_txtvar.set('')
        self.book2_txtvar.set('')
        self.aadhar_txtvar.set('')

    # Data add command
    def add_command(self):
        if self.name_txtvar.get() == '':
            self.error_message("Name.")
        elif self.contact_txtvar.get() == '':
            self.error_message("Contact Number.")
        elif self.address_entry.get("1.0", "end-1c") == '':
            self.error_message("Address.")
        elif self.class_txtvar.get() == '':
            self.error_message("Class.")
        elif self.book1_txtvar.get() == '':
            self.error_message("minimum one Book.")
        elif self.aadhar_txtvar.get() == '':
            self.error_message("Aadhar Number.")
        else:
            self.db.insert(self.name_txtvar.get(), self.contact_txtvar.get(), self.address_entry.get(
                "1.0", 'end-1c'), self.class_txtvar.get(), self.book1_txtvar.get(), self.book2_txtvar.get(), self.aadhar_txtvar.get())
            self.clear()
            self.view_all()
            self.add_succesful("added", "Succesfully added")

    # View data on database
    def view_all(self):
        self.show_txt.delete(0, END)
        for row in self.db.view():
            self.show_txt.insert(END, row)

    #SEARCH 
    def search(self):
        name = str(self.name_txtvar.get())
        self.db.search(self.name_txtvar.get())
        print("done")


if __name__ == "__main__":
    root = Tk()
    database = Database("students.db")
    gui = Gui(root, database)
    root.mainloop()
