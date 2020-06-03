from tkinter import *
from backend import Database


database = Database("books.db")

window= Tk()
window.wm_title("BookStore")


l1 = Label(window, text ="Title")
l1.grid(row=0, column=0)


l2 = Label(window, text ="Author")
l2.grid(row=0, column=2)


l3 = Label(window, text ="Year")
l3.grid(row=1, column=0)


l4 = Label(window, text ="ISBN")
l4.grid(row=1, column=2)

#title entry field
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

#year entry field
year_text = StringVar()
y1 = Entry(window, textvariable=year_text)
y1.grid(row=1, column=1)

#author entry field
author_text = StringVar()
a1 = Entry(window, textvariable=author_text)
a1.grid(row=0, column=3)



#isbn entry field
isbn_text = StringVar()
isbn1 = Entry(window, textvariable=isbn_text)
isbn1.grid(row=1, column=3)


#list box
list1 =Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)






def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,
                 (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index= list1.curselection()[0]
        selected_tuple = list1.get(index)
        #return (selected_tuple)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        y1.delete(0, END)
        y1.insert(END, selected_tuple[2])
        a1.delete(0, END)
        a1.insert(END, selected_tuple[3])
        isbn1.delete(0, END)
        isbn1.insert(END, selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())





#buttons
b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b1=Button(window, text="Search Entry", width=12, command=search_command)
b1.grid(row=3, column=3)

b1=Button(window, text="Add Entry", width=12, command=add_command)
b1.grid(row=4, column=3)

b1=Button(window, text="Update Selected", width=12,command = update_command)
b1.grid(row=5, column=3)

b1=Button(window, text="Delete Selected", width=12, command=delete_command)
b1.grid(row=6, column=3)

b1=Button(window, text="Close", width=12,command=window.destroy)
b1.grid(row=7, column=3)


#scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

#adding list and scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()