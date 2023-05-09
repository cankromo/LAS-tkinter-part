import tkinter as tk

root = tk.Tk()

# Create a label on page 1
label1 = tk.Label(root, text="Label on Page 1")
label1.place(x=50, y=50)

# Create a label on page 2
label2 = tk.Label(root, text="Label on Page 2")
label2.place(x=50, y=100)

root.mainloop()