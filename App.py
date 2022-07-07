from glob import glob
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Constants import *
import random

class ControlDatabase:
    pass

class DishData:
    """Get the dishes name from database and draw dishes"""
    def __init__(self, path) -> None:
        self._path = path
        self._chosen_dish = None
        self._chosen_dishes = []
        with open(self._path, "r", encoding="utf8") as self._data:
            self._dishes = []
            self._all_dishes = self._data.readlines()
            for i in self._all_dishes:
                i = i.split("\n")[0]
                self._dishes.append(i)

        
    def draw_dish(self):
        """Try draw 1 dish"""
        self._chosen_dish = random.choices(self._dishes)

        print(self._dishes) #checking

        print(self._chosen_dish) #checking
        self._chosen_dishes.append(self._chosen_dish[0])
        print(self._chosen_dishes) #checking

        self._dishes.remove(self._chosen_dish[0])
        print(self._dishes) #checking

    def check_empty(self):
        """Check if the current drawing database is empty"""
        if self._dishes:
            return False
        else:
            return True

    def enter_new_database(self):
        """If the current drawing database is empty, clear all previous data and prompt user to enter a new database"""
        if self.check_empty():
            path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            global dish_data
            dish_data = DishData(path)

            global root
            global database_view
            database_view.clear()
            database_view = DatabaseView(root, dish_data)
            database_view.pack(side=tk.LEFT, fill=tk.Y)

            global chosen_view
            chosen_view.clear()
            chosen_view = ChosenDishView(root)
            chosen_view.pack(side=tk.TOP, fill=tk.BOTH)

            global controller
            controller.clear()
            controller = Controller(root, dish_data, database_view, chosen_view)
            controller.pack(side=tk.BOTTOM, fill=tk.BOTH, ipady=20)

    def update_database(self):
        """Update the current database when close the program"""
        with open("Current Round.txt", 'w', encoding="utf8") as f:
            f.write('\n'.join(self._dishes))

class RecipeData:
    pass

class DatabaseView(tk.Frame):
    """Show all the dishes in the database"""
    def __init__(self, master, dish_data):
        super().__init__(bg="red")
        self._master = master
        self._dish_data = dish_data

        self._scroll_bar = tk.Scrollbar(self)
        self._scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        self._data_list = tk.Listbox(
                self, 
                font=TEXT_FONT, 
                selectmode=tk.EXTENDED, 
                yscrollcommand=self._scroll_bar.set
            )
        for dish in self._dish_data._dishes:
            self._data_list.insert(tk.END, dish)
        self._data_list.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        self._scroll_bar.config(command=self._data_list.yview)

    def clear(self):
        self.destroy()

    def just_draw(self):
        self._data_list.delete(0, tk.END)
        for dish in self._dish_data._dishes:
            self._data_list.insert(tk.END, dish)

class ChosenDishView(tk.Frame):
    """Show all chosen dishes"""
    def __init__(self, master):
        super().__init__(bg="blue", width=500)
        self._master = master
        self._label1 = tk.Label(self, text="Chosen One").pack()

    def draw_dish_label(self, name):
        """Draw dish name label on the screen"""
        var = tk.Label(self, text=name, font=TEXT_FONT)
        var.pack(side=tk.TOP, fill=tk.X)

    def clear(self):
        self.destroy()

class Controller(tk.Frame):
    """Controler"""
    def __init__(self, master, data, database, dishes) -> None:
        super().__init__(bg="green")
        self._master = master
        self._data = data
        self._database = database
        self._dishes = dishes
        self._callback1 = self._data.draw_dish
        self._callback2 = self._dishes.draw_dish_label
        self._callback3 = self._data.enter_new_database
        self._callback4 = self._database.just_draw
        self.draw_controller()
        self._no_draw = 0
        self._new_dish = None

    def yes(self):
        self._new_dish = self._data._chosen_dish

    def draw_controller(self):
        """Draw control buttons on the screen"""
        # self._no_draw_entry = tk.Entry(self, width=20)
        # self._no_draw_entry.pack(side=tk.LEFT)
        # self._no_draw = self._no_draw_entry.get()
        # not yet check type of input
        self._enter_btn = tk.Button(self, text="Enter", command=lambda:[self._callback1(), self.yes(), self._callback2(self._new_dish), self._callback3(), self._callback4()])
        self._enter_btn.pack()

    def clear(self):
        self.destroy()

class FileMenu(DishData):
    def __init__(self, master, data) -> None:
        self._master = master
        self._data = data
        self.set_up_file_menu()

    def set_up_file_menu(self):
        """Set up file menu on the root window"""
        menubar = tk.Menu(self._master)
        self._master.config(menu=menubar)

        actionmemu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Action", menu=actionmemu)
        actionmemu.add_command(label="Change Posibility")
        actionmemu.add_command(label="Quit", command=self.quit)

    def quit(self):
        self._master.quit()
        self._data.update_database()

def app():
    global root
    root = tk.Tk()
    root.geometry("700x600")
    root.resizable(0, 0)

    global dish_data
    dish_data = DishData("Current Round.txt")

    FileMenu(root, dish_data)

    global database_view
    database_view = DatabaseView(root, dish_data)
    database_view.pack(side=tk.LEFT, fill=tk.Y)

    global chosen_view
    chosen_view = ChosenDishView(root)
    chosen_view.pack(side=tk.TOP, fill=tk.BOTH)

    global controller
    controller = Controller(root, dish_data, database_view, chosen_view)
    controller.pack(side=tk.BOTTOM, fill=tk.BOTH, ipady=20)

    def on_closing():
        """Prompt user the app is closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            dish_data.update_database()
            print("Bye 9 Bye")
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == '__main__':
    app()