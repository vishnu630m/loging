import tkinter as tk
from tkinter import messagebox, END
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

# Connect to MySQL
mydb_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Root123@",
    database="signup"
)
mycursor = mydb_connection.cursor()

def login_page():
    signup_window.destroy()
    import signin

def clear_entry(event, entry_widget, default_text):
    if entry_widget.get() == default_text:
        entry_widget.delete(0, END)

def signup_page():
    username = usernameEntry.get()
    password = passwordEntry.get()
    confirm_password = confirm_passwordEntry.get()
    email = emailEntry.get()
    agreed = agree_var.get()

    if not all([username, password, confirm_password, email]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
    elif not agreed:
        messagebox.showerror("Error", "Please agree to the terms and conditions.")
        return

    try:
        # Check if user already exists
        mycursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        existing_user = mycursor.fetchone()
        if existing_user:
            messagebox.showerror("Error", "Username or Email already exists.")
        else:
            # Insert new user details into the database
            mycursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
            mydb_connection.commit()
            messagebox.showinfo("Success", "Registration successful!")
    except Exception as e:
        messagebox.showerror("Error", f"Registration failed: {e}")

# Create main window
signup_window = tk.Tk()
signup_window.title("Signup")
signup_window.geometry("900x500")  # Set window size
signup_window.resizable(0,0)

# Background Image
bg_image = Image.open("image.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(signup_window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

heading = tk.Label(signup_window, text='CREATE AN ACCOUNT', font=('Arial', 18, 'bold'), fg='blue')
heading.place(x=500, y=50)

# Entry fields
default_text_color = 'firebrick1'

emailEntry = tk.Entry(signup_window, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg=default_text_color)
emailEntry.place(x=550, y=110)
emailEntry.insert(0, 'Email')
emailEntry.bind('<FocusIn>', lambda event: clear_entry(event, emailEntry, 'Email'))
tk.Frame(signup_window, width=180, height=2, bd=0, bg='red').place(x=550, y=130)


usernameEntry = tk.Entry(signup_window, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg=default_text_color)
usernameEntry.place(x=550, y=160)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', lambda event: clear_entry(event, usernameEntry, 'Username'))
tk.Frame(signup_window, width=180, height=2, bd=0, bg='red').place(x=550, y=180)

passwordEntry = tk.Entry(signup_window, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg=default_text_color, show='*')
passwordEntry.place(x=550, y=210)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', lambda event: clear_entry(event, passwordEntry, 'Password'))
tk.Frame(signup_window, width=180, height=2, bd=0, bg='red').place(x=550, y=230)

confirm_passwordEntry = tk.Entry(signup_window, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg=default_text_color)
confirm_passwordEntry.place(x=550, y=260)
confirm_passwordEntry.insert(0, 'Confirm Password')
confirm_passwordEntry.bind('<FocusIn>', lambda event: clear_entry(event, confirm_passwordEntry, 'Confirm Password'))
tk.Frame(signup_window, width=180, height=2, bd=0, bg='red').place(x=550, y=280)

agree_var = tk.BooleanVar()
agree_check = tk.Checkbutton(signup_window, text="I agree to the terms and conditions", variable=agree_var,
                             font=('Arial', 10))
agree_check.place(x=550, y=320)

register_button = tk.Button(signup_window, text="Register", command=signup_page, font=('Arial', 11, 'bold'), fg='white',
                            bg='green', bd=2, cursor='hand2')
register_button.place(x=550, y=360, width=100, height=30)

loginLable = tk.Label(signup_window, text='Already have an account?', font=('Arial', 9), fg='gray')
loginLable.place(x=550, y=400)

loginbutton = tk.Button(signup_window, text="Login", font=('Arial', 11, 'bold'), fg='white', bg='#CDAD00', bd=2,
                        cursor='hand2', command=login_page)
loginbutton.place(x=700, y=390, width=100, height=30)

signup_window.mainloop()
