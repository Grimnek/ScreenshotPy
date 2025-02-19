import time
from tkinter import Tk, Menu, messagebox, StringVar, Label, Entry, Button
from tkinter.filedialog import asksaveasfilename
import pyautogui as pg


def screenshot_tk():
    try:
        root.withdraw()
        time.sleep(3)
        img = pg.screenshot("image.png")
        file = asksaveasfilename(defaultextension=f".png",
                                 filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        img.save(file)
    except Exception as e:
        messagebox.showerror("Error", "Specify the folder where the screenshot will be saved.")
    finally:
        root.deiconify()


def info():
    messagebox.showinfo("Info",
                        "For a screenshot, press F10 and wait. The program will disappear for a while and after 3 seconds will return to its place.")


root = Tk()
root.title("Screenshot")
main_menu = Menu()
main_menu.add_cascade(label="Info", command=info)

message_button = Button(text="Screenshot", padx="20", pady="15", background="#555", foreground="#fff", command=screenshot_tk)
message_button.place(relx=.5, rely=.4, anchor="center")

root.config(menu=main_menu)
root.mainloop()
