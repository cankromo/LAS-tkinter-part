import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
#database ismi 3.satıra
with sqlite3.connect("details.db") as db:
    cursor=db.cursor()


###############################################
# error = Message(text="",width=160)
# error.place(x=30,y=10)
# error.config(padx=0)
################################################

#############MAİN WİNDOW PART###############
window = Tk()
style = ttk.Style(window)
window.tk.call("source", "forest-light.tcl")
window.tk.call("source", "forest-dark.tcl")
window.geometry("1000x500")
window.title("LAS")
# frame = tk.Frame(window, height=300, width= 500, bg="blue", bd=1, relief=FLAT)
# frame.place(x=250,y=70 )
#########################################

cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username text NO NULLL, password text NOT NULL) ; """)
options_frame=tk.Frame(window, bg="white")

##########OPTIONS#############
options_frame.pack()
options_frame.pack_propagate(False)
options_frame.place(x=30,y=0)
options_frame.configure(width=270, height=30)

main_frame = tk.Frame(window, highlightbackground="white",highlightthickness="3")



main_frame.pack(side=tk.BOTTOM)
main_frame.pack_propagate(False)
main_frame.configure(height=450, width= 1000)
###############################
##########FUNCTION FOR INDICATOR FRAMES#######
def indicate(lb, page):
    hide_indicators()
    lb.config(bg="black")
    page()
def hide_indicators():
    register_indicate.config(bg="white")
    general_indicate.config(bg="white")
    live_indicate.config(bg="white")
    exit_indicate.config(bg="white")
################################################
register_button = tk.Button(options_frame, text="Register", font=("Bold",10),fg="black",bd=0,bg="white",command=lambda: indicate(register_indicate, register_page))
register_button.place(x=10,y=5)
register_indicate = tk.Label(options_frame, text="",bg="white")
register_indicate.place(x=10, y=5, width=55, height= 5)

general_button=tk.Button(options_frame, text="General", font=("Bold", 10),fg="black",bd=0,bg="white",command=lambda: indicate(general_indicate,))
general_button.place(x=80,y=5)
general_indicate = tk.Label(options_frame, text="",bg="white")
general_indicate.place(x=80, y=5, width=53, height= 5)


live_button=tk.Button(options_frame, text="Live", font=("Bold", 10),fg="black",bd=0,bg="white",command=lambda: indicate(live_indicate, live_page))
live_button.place(x=150,y=5)
live_indicate = tk.Label(options_frame, text="",bg="white")
live_indicate.place(x=150, y=5, width=30, height= 5)

exit_button=tk.Button(options_frame, text="Exit", font=("Bold", 10),fg="black",bd=0,bg="white",command=quit)
exit_button.place(x=200,y=5)
exit_indicate = tk.Label(options_frame, text="",bg="white")
exit_indicate.place(x=200, y=5, width=30, height= 5)
###############################




#################REGİSTER PART#############

#
def register_page():
    # Önceki sayfadaki widget'ların silinmesi
    for widget in main_frame.winfo_children():
        widget.destroy()
        
    # Register sayfası için özel bir Frame oluşturma
    register_frame = tk.Frame(main_frame)
    register_frame.pack(fill="both", expand=True)

    label1 = Label(register_frame, text="Name-Surname:", bg="lightgreen", font=("Arial", 14), fg="black")
    label1.place(x=300, y=100)
    label1.config

    username = Entry(register_frame, text="")
    username.place(x=450, y=100, width=200, height=25)

    label3 = Label(register_frame, text="ID number", bg="lightgreen", font=("Arial", 14), fg="black")
    label3.place(x=300, y=150)
    label3.config

    IDnumber = Entry(register_frame, text="")
    IDnumber.place(x=450, y=150, width=200, height=25)

    label2 = Label(register_frame, text="E-mail:", bg="lightgreen", font=("Arial", 14), fg="black")
    label2.place(x=300, y=200)
    label2.config

    password = Entry(register_frame, text="")
    password.place(x=450, y=200, width=200, height=25)

    label4 = Label(register_frame, text="Date of birth", bg="lightgreen", font=("Arial", 14), fg="black")
    label4.place(x=300, y=250)
    label4.config

    Birthdate = Entry(register_frame, text="")
    Birthdate.place(x=450, y=250, width=200, height=25)
    def add_new_user():

        newUsername= username.get()
        newPassword= password.get()
        newIDnumber= IDnumber.get()
        newBirthdate=Birthdate.get()

        print(newUsername,newIDnumber,newBirthdate,newPassword)
    button= Button(register_frame,text= "Register",font=("Arial", 12,),bg="green",command=add_new_user) #command=#kullanıcı ekleme fonksiyonu)
    button.place(x=300, y=400)
    
    

    #     cursor.execute("SELECT COUNT(*) from users WHERE username = '" + newUsername +"' ")    
    #     result= cursor.fetchone()

    #     if int(result[0]) > 0:
    #         pass

    #     else:
            
    #         cursor.execute("INSERT INTO users(username,password,IDnumber,Birthdate)VALUES(?,?,?,?)",(newUsername),(newPassword),(newIDnumber),(newBirthdate))    
    #     db.commit
##########################################
def live_page():
    live_frame = tk.Frame(main_frame, bg="white", width=1000, height=450)
    live_frame.pack_propagate(False)
    live_frame.pack()

    label1_live_page = Label(live_frame, text="Name-Surname:", bg="lightgreen", font=("Arial", 14), fg="black", width=10, height=10)
    label1_live_page.place(x=10, y=50)

window.mainloop()

