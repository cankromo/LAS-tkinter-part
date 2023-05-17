import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
#database ismi 3.satıra
with sqlite3.connect("details.db") as db:
    cursor=db.cursor()



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
options_frame.place(x=15,y=0)
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
#####################BUTTONS IN OPTION FRAME###########################
register_button = tk.Button(options_frame, text="Register", font=("Bold",10),fg="black",bd=0,bg="white",command=lambda: indicate(register_indicate, register_page))
register_button.place(x=10,y=5)
register_indicate = tk.Label(options_frame, text="",bg="white")
register_indicate.place(x=10, y=5, width=55, height= 5)

general_button=tk.Button(options_frame, text="General", font=("Bold", 10),fg="black",bd=0,bg="white",command=lambda: indicate(general_indicate, general_page))
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
    register_frame = tk.Frame(main_frame,bg="grey")
    register_frame.pack(fill="both", expand=True)

    label1 = Label(register_frame, text="Name-Surname:", bg="grey", font=("Arial", 14), fg="black")
    label1.place(x=300, y=100)
    label1.config

    username = Entry(register_frame, text="")
    username.place(x=450, y=100, width=200, height=25)

    label3 = Label(register_frame, text="ID number", bg="grey", font=("Arial", 14), fg="black")
    label3.place(x=300, y=150)
    label3.config

    IDnumber = Entry(register_frame, text="")
    IDnumber.place(x=450, y=150, width=200, height=25)

    label2 = Label(register_frame, text="E-mail:", bg="grey", font=("Arial", 14), fg="black")
    label2.place(x=300, y=200)
    label2.config

    password = Entry(register_frame, text="")
    password.place(x=450, y=200, width=200, height=25)

    label4 = Label(register_frame, text="Date of birth", bg="grey", font=("Arial", 14), fg="black")
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
        ############clearing input#############
        username.delete(0, 'end')
        password.delete(0, 'end')
        IDnumber.delete(0, 'end')
        Birthdate.delete(0, 'end')
        ########################################
    ##########################REGİSTER BUTTON#####################################
    button= Button(register_frame,text= "Register",font=("Arial", 12,),bg="green",command=add_new_user) #command=#kullanıcı ekleme fonksiyonu)
    button.place(x=300, y=400)
    ##############################################################################
    image_for_qr = Image.open("scan.png")
    photo_for_qr = ImageTk.PhotoImage(image_for_qr)
    image_for_qr = image_for_qr.resize((100,100), Image.ANTIALIAS)
    
    qr_button = Button(register_frame, text="", font=("Arial", 12), bg="green", command=add_new_user,width=100,height=100)
    qr_button.config(image=photo_for_qr, compound='center')  # Set the image and compound option
    qr_button.place(x=550,y=325)

    # Keep a reference to the PhotoImage object
    qr_button.image = photo_for_qr

def live_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    image = Image.open("aybuLogo.png")
    live_page.photo = ImageTk.PhotoImage(image)

    live_frame = tk.Frame(main_frame, bg="grey", width=1000, height=450)
    live_frame.pack_propagate(False)
    live_frame.pack()

    label1_live_page = tk.Label(live_frame,image=live_page.photo, width=100, height=100)
    label1_live_page.place(x=35,y=10)
    label2_live_page = tk.Label(live_frame,text="Current users", bg="black", font=("Arial", 14), fg="white")
    label2_live_page.place(x=270,y=10)
    fig, ax = plt.subplots()

    ################CURRENT OCCUPANCY GRAPH#########################
    #dataset
    
    rate=["current occupancy"]
    value=[50]#"value_of_rate=miktar/sınır"]
    positions = 50
    plt.bar(rate, positions)
    ax.set_ylim([0, 100])
    fig.subplots_adjust(left=0.26)
    canvas = FigureCanvasTkAgg(fig, master=live_frame)
    canvas.draw()   
    canvas.get_tk_widget().place(x=10, y=130, width=150, height=300)
    #################################################################
    # treescroll= ttk.Scrollbar(treeFrame)
    # treescroll.pack(side="right",fill="y")
    splitter = tk.Label(live_frame, bg="green", width=1, height=1) # Set height to 1 line
    splitter.place(x=200, y=0, height=460) # Adjust size to 50 pixels high
    treeFrame = ttk.Frame(live_frame,width=700,height=300,borderwidth=3)
    treeFrame.place(x=270,y=90)
    treescroll= ttk.Scrollbar(treeFrame)
    treescroll.pack(side="right",fill="y")
    cols=["User ID","Name-Surname","E-mail","Age","Entry time","Time spent "]
    treeview = ttk.Treeview(treeFrame, show="headings",yscrollcommand=treescroll.set,columns=cols,height=10)
    treeview.pack()
    treescroll.config(command=treeview.yview)
    treeview.column("Age", width=50)
    treeview.column("User ID", width=50)
    treeview.column("Name-Surname", width=50)
    treeview.column("Entry time", width=50)

    for col in cols:
        treeview.heading(col, text=col)

    
def general_page():
    for widget in main_frame.winfo_children():
        widget.destroy()
    general_frame = tk.Frame(main_frame, bg="grey", width=1000, height=450)
    general_frame.pack_propagate(False)
    general_frame.pack()
    # label1_live_page = Label(general_frame, text="rate:", bg="lightgreen", font=("Arial", 14), fg="black", width=10, height=10)
    # label1_live_page.place(x=10, y=50)
    
    ################PIE MONTHS GRAPH##################
    fig, ax = plt.subplots()
    slices=["January","February","March","April","May","June","July","Agust","Semptember","October","November","December"]
    share=[34,12,65,12,43,65,43,42,79,82,40,21]#number of visitors for every month
    explode = [0] * len(share)
    plt.pie(share, labels=slices, explode=explode)

    canvas_pie = FigureCanvasTkAgg(fig, master=general_frame)
    canvas_pie.draw()
    canvas_pie.get_tk_widget().place(x=10, y=10, width=270, height=150)
    canvas_pie.get_tk_widget().config(highlightthickness=3, highlightbackground="green")
    ################DAYS COLUMN GRAPH#################
    fig, ax = plt.subplots()
    rates_of_days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "S"]
    positions_of_days = [12, 24, 13, 15, 70, 16, 24]  # "values_of_days_as_a_list"]
    plt.bar(rates_of_days, positions_of_days)
    ax.set_ylim([0, 100])
    
    canvas1 = FigureCanvasTkAgg(fig, master=general_frame)
    canvas1.draw()
    canvas1.get_tk_widget().place(x=10, y=170, width=270, height=270)
    canvas1.get_tk_widget().config(highlightthickness=3, highlightbackground="green")
    ######################################################

    #######################POPULAR HOURS TABLE#########################################
    fig, ax = plt.subplots()
    empty_list=[20,40,60,80,100]
    values_of_rate=[12,0,0,0,0,0,0,0,0,0,55,72,90,34]
    x_hours=[9,12,15,18,21]
    hours=[9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    plt.stem(hours,values_of_rate)
    # Create a mask to filter the data points based on the specific hours
    # Plot the x-axis line
    plt.plot(hours, values_of_rate, color='black', linewidth=1)

    # Remove y-axis line, ticks, and data points
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.yaxis.grid(True, linestyle='dashed', color='gray', alpha=0.5)
    
    plt.xticks(x_hours)
    plt.yticks(empty_list)
    canvas3 = FigureCanvasTkAgg(fig, master=general_frame)
    fig.subplots_adjust(left=0.26)
    canvas3.draw()
    canvas3.get_tk_widget().place(x=300, y=170, width=290, height=270)
    canvas3.get_tk_widget().config(highlightthickness=3, highlightbackground="green")
    #############################################################################
   
    treeFrame = ttk.Frame(general_frame,width=200,height=500,borderwidth=3)
    treeFrame.place(x=600,y=100)
    treescroll= ttk.Scrollbar(treeFrame)
    treescroll.pack(side="right",fill="y")
    cols=["User ID","Name-Surname","E-mail","Age","Phone Number"]
    treeview = ttk.Treeview(treeFrame, show="headings",yscrollcommand=treescroll.set,columns=cols,height=700)
    treeview.pack()
    treescroll.config(command=treeview.yview)
    treeview.column("Age", width=40)
    treeview.column("User ID", width=50)
    treeview.column("Name-Surname", width=80)
    treeview.column("E-mail", width=80)
    treeview.column("Phone Number", width=100)

    for col in cols:
        treeview.heading(col, text=col)


window.mainloop()

