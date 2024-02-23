import tkinter as tk
from tkinter import messagebox, END
from PIL import Image, ImageTk
import mysql.connector

# Connect to MySQL database
mydb_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Root123@",
    database="signup"
)
mycursor = mydb_connection.cursor()

def login_with_google():
    messagebox.showinfo("Login with Google", "Feature coming soon!")


def login_with_twitter():
    messagebox.showinfo("Login with Twitter", "Feature coming soon!")


def login_with_facebook():
    messagebox.showinfo("Login with Facebook", "Feature coming soon!")


def signup_page():
    login_window.destroy()
    # Redirect to the signup page
    import signup


def on_enter(event):
    if usernameEntry.get() == 'username':
        usernameEntry.delete(0, END)


def on_enter1(event):
    if passwordEntry.get() == 'password':
        passwordEntry.delete(0, END)

def forgot_password():
    # Create a new window for password recovery
    forgot_window = tk.Toplevel(login_window)
    forgot_window.title("Forgot Password")
    forgot_window.geometry("790x512")
    forgot_window.resizable(0,0)
    bg_image = Image.open("background.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(forgot_window, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.pack()

    heading_label = tk.Label(forgot_window, text="Reset Password", font=('Microsoft Yahei UI Light', 19, 'bold'),bg='white'
                             ,fg='red')
    heading_label.pack()
    heading_label.place(x=510,y=40)

    email_label = tk.Label(forgot_window, text="Email", font=('Microsoft Yahei UI Light', 11,'bold'),bg='white',fg='#9932CC')
    email_label.pack()
    email_label.place(x=452,y=100)


    email_entry = tk.Entry(forgot_window, font=('Microsoft Yahei UI Light', 11),bd=0)
    email_entry.pack()
    email_entry.place(x=455,y=122)
    tk.Frame(forgot_window, width=180, height=2, bd=0, bg='red').place(x=455, y=145)
    #

    new_password_label = tk.Label(forgot_window, text="New password",
                                  font=('Microsoft Yahei UI Light', 11,'bold'),bg='white',fg='#9932CC')
    new_password_label.pack()
    new_password_label.place(x=452,y=160)

    new_password_entry = tk.Entry(forgot_window, font=('Microsoft Yahei UI Light', 11), bd=0)
    new_password_entry.pack()
    new_password_entry.place(x=455,y=182)
    tk.Frame(forgot_window, width=180, height=2, bd=0, bg='red').place(x=455, y=205)



    confirm_password_label = tk.Label(forgot_window, text="Confirm password:",
                                      font=('Microsoft Yahei UI Light',11,'bold'),bg='white',fg='#9932CC')
    confirm_password_label.pack()
    confirm_password_label.place(x=452,y=230)

    confirm_password_entry = tk.Entry(forgot_window, font=('Microsoft Yahei UI Light', 11),bd=0)
    confirm_password_entry.pack()
    confirm_password_entry.place(x=455,y=260)
    tk.Frame(forgot_window, width=180, height=2, bd=0, bg='red').place(x=455, y=280)

    def submit_reset():
        email = email_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Check if the email exists in the database
        mycursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = mycursor.fetchone()

        if not user:
            messagebox.showerror("Error", "Email not found.")
            forgot_window.destroy()
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            forgot_window.destroy()

            return

        # Update the password in the database
        mycursor.execute("UPDATE users SET password=%s WHERE email=%s", (new_password, email))
        mydb_connection.commit()

        messagebox.showinfo("Success", "Password updated successfully.")
        forgot_window.destroy()

    submit_button = tk.Button(forgot_window, text="Submit",font=('Microsoft Yahei UI Light', 11,'bold'), command=submit_reset,bd=0,fg='#8B0A50')
    submit_button.pack()
    submit_button.place(x=550,y=350)



def login_page():
    username = usernameEntry.get()
    password = passwordEntry.get()

    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return

    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    mycursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = mycursor.fetchone()

    if not user:
        messagebox.showerror("Error", "Username not registered.")
        return

    mycursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user_with_password = mycursor.fetchone()

    if user_with_password:
        messagebox.showinfo("Login Successful", "Welcome, " + username)
        # Add code to proceed after successful login
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")


login_window = tk.Tk()
login_window.title("User Login")
login_window.geometry("850x534")
login_window.resizable(0, 0)
bg_image = Image.open("image3.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(login_window, image=bg_photo)
bg_label.image = bg_photo
bg_label.pack()

heading = tk.Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 19, 'bold'), fg='#8B1A1A',bd=0)
heading.place(x=390, y=100)

usernameEntry = tk.Entry(login_window, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=380, y=180)
usernameEntry.insert(0, 'username')
usernameEntry.bind('<FocusIn>', on_enter)
tk.Frame(login_window, width=180, height=2, bd=0, bg='red').place(x=380, y=200)

passwordEntry = tk.Entry(login_window, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=380, y=220)
passwordEntry.insert(0, 'password')
passwordEntry.bind('<FocusIn>', on_enter1)
tk.Frame(login_window, width=180, height=2, bg='red').place(x=380, y=243)

#forgotpassword
forgot_passwordbutton = tk.Button(login_window, text="Forgot password", font=('Microsoft Yahei UI Light', 8, 'bold'),
                        bg='#00BFFF', activebackground='green', cursor='hand2',command=forgot_password)
forgot_passwordbutton.place(x=445, y=250)


loginbutton = tk.Button(login_window, text="Login", font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white',
                        bg='firebrick1', activebackground='white', cursor='hand2', bd=0, width=18,command=login_page)
loginbutton.place(x=380, y=290)

# Load images for buttons
google_img = Image.open("google.png")
google_img = google_img.resize((30, 30))
google_photo = ImageTk.PhotoImage(google_img)

twitter_img = Image.open("twitter.png")
twitter_img = twitter_img.resize((30, 30))
twitter_photo = ImageTk.PhotoImage(twitter_img)

facebook_img = Image.open("facebook.png")
facebook_img = facebook_img.resize((30, 30))
facebook_photo = ImageTk.PhotoImage(facebook_img)

google_button = tk.Button(login_window, image=google_photo, borderwidth=0, bg='white', command=login_with_google)
google_button.image = google_photo
google_button.place(x=380, y=340)

twitter_button = tk.Button(login_window, image=twitter_photo, borderwidth=0, bg='white', command=login_with_twitter)
twitter_button.image = twitter_photo
twitter_button.place(x=450, y=340)

facebook_button = tk.Button(login_window, image=facebook_photo, borderwidth=0, bg='white', command=login_with_facebook)
facebook_button.image = facebook_photo
facebook_button.place(x=530, y=340)

signup_label = tk.Label(login_window, text="Don't have an account?", font=('Microsoft Yahei UI Light', 11, 'bold'),bd=0,
                        fg='#00BFFF')
signup_label.place(x=300, y=400)

signupbutton = tk.Button(login_window, text="Creat New account", font=('Microsoft Yahei UI Light', 12, 'bold'),
                        activebackground='white', cursor='hand2',bd=0,fg='#458B00',
                        command=signup_page)  # Assign login_page function here
signupbutton.place(x=485, y=395)

login_window.mainloop()