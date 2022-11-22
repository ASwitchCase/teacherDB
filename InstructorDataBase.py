import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

conn = sqlite3.connect("Instructors.db")
c = conn.cursor()

window = tk.Tk()
window.geometry("650x200") 
window.title("Instructor DataBase")
scrollbar = tk.Scrollbar(orient="horizontal")


tf1 = tk.Label(window,text = "First Name:")
tf1.place(x = 20,y = 30)

tf2 = tk.Label(window,text = "Last Name: ")
tf2.place(x = 20,y = 60)

tf3 = tk.Label(window,text = "ID: ")
tf3.place(x = 20,y = 90)

tf4 = tk.Label(window,text = "Subject: ")
tf4.place(x = 20,y = 120)

tf5 = tk.Label(window,text = "Search Instrutor by: ")
tf5.place(x = 300,y = 30)

find = tk.Entry(window,width =20)
find.place(x = 520,y = 30)

menu = ttk.Combobox(window,width = 10,values=["First Name","Last Name","ID","Subject"])
menu.place(x = 420,y = 30)
menu.current(0)


fname = tk.Entry(window)
fname.place(x = 130,y = 30)

lname = tk.Entry(window)
lname.place(x = 130,y = 60)

tid = tk.Entry(window)
tid.place(x = 130,y = 90)

subject = tk.Entry(window)
subject.place(x = 130,y = 120)   

result = tk.Entry(window,width = 50,xscrollcommand=scrollbar.set)
result.place(x = 300,y = 60)

result.focus()

scrollbar.pack(fill="x")
scrollbar.config(command=result.xview)

def is_table():
    #get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='teachers' ''')

    #if the count is 1, then table exists
    if c.fetchone()[0]==1:
        return True
    else:
        return False


def add_instructor():
    if is_table() == False:
        c.execute("""CREATE TABLE teachers (first text, last text, tid integer,subject text)""")
        
    c.execute("INSERT INTO teachers VALUES ('" + fname.get() + "','" + lname.get() + "'," + tid.get() + ",'" + subject.get() + "')")
    print("Added")
    conn.commit()

def find_instructor():
    if menu.current() == 0:  
        c.execute("SELECT * FROM teachers WHERE first ='" +find.get()+"'")
    elif menu.current() == 1:
        c.execute("SELECT * FROM teachers WHERE last ='" +find.get()+"'")
    elif menu.current() == 2:
        c.execute("SELECT * FROM teachers WHERE tid ='" +find.get()+"'")
    elif menu.current() == 3:
        c.execute("SELECT * FROM teachers WHERE subject ='" +find.get()+"'")

    result.delete(0,"end")
    result.insert(0,c.fetchall())
    

def clear():
    fname.delete(0,"end")
    lname.delete(0,"end")
    tid.delete(0,"end")
    subject.delete(0,"end")
    print("Cleared")

def show_data():
    c.execute("SELECT * FROM teachers ")
    result.delete(0,"end")
    result.insert(0,c.fetchall())
    
     
b1 = tk.Button(window, text = "Add Instructor", width = 20, command = add_instructor)
b1.place(x = 20, y = 150)
b2 = tk.Button(window, text = "Find Instructor", width = 20, command = find_instructor)
b2.place(x = 300, y = 90)
b4 = tk.Button(window, text = "Show All Data", width = 20, command = show_data)
b4.place(x = 300, y = 120)
b3 = tk.Button(window, text = "clear", width = 10, command = clear)
b3.place(x = 200, y = 150)


window.mainloop()
conn.close()
