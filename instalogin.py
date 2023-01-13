from tkinter import *
import webbrowser as wb
import time
import pyautogui as pg

root = Tk()

root.geometry("800x599")

root.title("Instagram Login Page")

def fun():
    username = USER.get()
    password = PASSWORD.get()
    wb.open("https://www.instagram.com")

    time.sleep(12)

    pg.click(1186, 339)

    pg.write(username)

    time.sleep(2)

    pg.click(1144, 394)

    time.sleep(1)

    pg.write(password)

    pg.click(1276, 452)

    time.sleep(5)

    pg.click(1155, 612)




USER = StringVar()
PASSWORD = StringVar()

Label(text="Username",font="helvatica 10 bold").grid(row=0,column=7)
Label(text="Password",font="helvatica 10 bold").grid(row=1,column=7)

E_I = Entry(textvariable=USER).grid(row=0,column=8)
E_II = Entry(textvariable=PASSWORD).grid(row=1,column=8)

Button(text="Login",font="helvatica 10 bold",command=fun).grid(row=3,column=5)



root.mainloop()
