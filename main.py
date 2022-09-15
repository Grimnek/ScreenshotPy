import time
from tkinter import Tk, Menu, messagebox
from tkinter.filedialog import asksaveasfilename
import pyautogui as pg


def screenshot_tk(event):
    try:
        root.withdraw()
        time.sleep(3)
        img = pg.screenshot("image.png")
        file = asksaveasfilename(defaultextension=f".png",
                                 filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
        img.save(file)
    except Exception as e:
        messagebox.showerror("Помилка", "Вкажіть папку, в яку буде збережено скріншот.")
    finally:
        root.deiconify()


def info():
    messagebox.showinfo("Інформація",
                        "Для скріншоту натисніть на F10 та чекайте. Програма зникне на час і після 3 секунд повернеться на своє місце.")


root = Tk()
root.title("Скріншотник")
main_menu = Menu()
main_menu.add_cascade(label="Інформація", command=info)

key = "F10"
root.bind(f"<{key}>", screenshot_tk)

root.config(menu=main_menu)
root.mainloop()
