from tkinter import *

import pymysql as ms
from tkinter import messagebox

# Add your own database name and password here to reflect in the code
mypass = "Midterm Project"
mydatabase = "library"

con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"  # Book Table


def deleteBook():
    bid = en1.get()
    try:
        a = int(bid)
        type1 = type(a)

        if type1 == int:
            print(True)
            cur.execute('select Book_Id from books')
            print(True)
            list = []
            for i in cur:
                getId = i[0]
                list.append(getId)
            print(True)
            if a in list:
                deleteSql = "delete from " + bookTable + " where Book_Id = '" + bid + "'"
                cur.execute(deleteSql)
                print(True)
                con.commit()
                print(True)
                # messagebox.showinfo('success',"Successfully deleted Book Id "+bid+" ")
                lb6 = Label(labelFrame, text="Successfully deleted book ", bg='black', fg='white',
                            font=("times new roman", 18, "bold"))
                lb6.place(relx=0.3, rely=0.75)
                print(True)
            else:
                lb6 = Label(labelFrame, text="Book deletion failed ", bg='black', fg='white',
                            font=("times new roman", 18, "bold"))
                lb6.place(relx=0.3, rely=0.75)

                # messagebox.showinfo('Error', "Please insert correct Book ID")

    except:
        messagebox.showinfo('Error', 'Invalid Book ID, must be number')

    print(bid)


def delete():
    global en1, con, cur, bookTable, root, labelFrame

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1350x700+0+0")
    root.config(bg='#0099cc')
    title = Label(root, text="Jungseok Library Management", bd=15, relief=GROOVE,
                  font=("algerian", 40, "bold"), bg="red", fg="white")
    title.pack(side=TOP, fill=X)

    labelFrame = Frame(root, bg='#333945', bd=10, relief=GROOVE)
    labelFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.35)

    headingFrame1 = Frame(root, bg="blue", bd=10, relief=GROOVE)
    headingFrame1.place(relx=0.25, rely=0.15, relwidth=0.60, relheight=0.13)

    headingLabel = Label(headingFrame1, text="DELETE BOOK", bg='blue', fg='white',
                         font=("bookman old style", 34, "bold"))
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=("bookman old style", 20, "bold"))
    lb2.place(relx=0.1, rely=0.33)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.15)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', font=("times new roman", 18, "bold"),
                       relief=GROOVE, bd=10, command=deleteBook)
    SubmitBtn.place(relx=0.28, rely=0.75, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=("times new roman", 18, "bold"), relief=GROOVE,
                     bd=10, command=root.quit)
    quitBtn.place(relx=0.53, rely=0.75, relwidth=0.18, relheight=0.08)

    root.mainloop()



