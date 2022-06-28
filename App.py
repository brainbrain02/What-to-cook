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
        self._data = open(path, "r")
        self._dishes = []
        self._all_dishes = self._data.readlines()
        for i in self._all_dishes:
            i = i.split("\n")[0]
            self._dishes.append(i)
        self._chosen_dish = None
        self._chosen_dishes = []
        
    def draw_dish(self):
        """Try draw 1 dish"""
        # print(self._dishes)
        self._chosen_dish = random.choices(self._dishes)
        # self._chosen_dishes = dish
        print(self._chosen_dish)
        self._chosen_dishes.append(self._chosen_dish)
        print(self._chosen_dishes)
        # self._callback()

    # def set_callback(self, callback):
    #     self._callback = callback
        

class RecipeData:
    pass

class DatabaseView(tk.Frame):
    """Show all the dishes in the database"""
    def __init__(self, master, dish_data):
        super().__init__(bg="red")
        self._master = master
        self._dish_data = dish_data

        scroll_bar = tk.Scrollbar(self)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        data_list = tk.Listbox(
                self, 
                font=TEXT_FONT, 
                selectmode=tk.EXTENDED, 
                yscrollcommand=scroll_bar.set
            )
        for dish in self._dish_data._dishes:
            data_list.insert(tk.END, dish)
        data_list.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        scroll_bar.config(command=data_list.yview)

class ChosenDishView(tk.Frame):
    """Show all chosen dishes"""
    def __init__(self, master):
        super().__init__(bg="blue", width=500)
        self._master = master
        self._label1 = tk.Label(self, text="Chosen One").pack()

    def draw_dish_label(self, name):
        var = tk.Label(self, text=name, font=TEXT_FONT)
        var.pack(side=tk.TOP, fill=tk.X)

class Controller(tk.Frame):
    """Controler"""
    def __init__(self, master, data, dishes) -> None:
        super().__init__(bg="green")
        self._master = master
        self._data = data
        self._dishes = dishes
        self._callback1 = self._data.draw_dish
        self._callback2 = self._dishes.draw_dish_label
        self.draw_controller()
        self._no_draw = 0
        self._new_dish = None

    def yes(self):
        self._new_dish = self._data._chosen_dish

    def draw_controller(self):
        # self._no_draw_entry = tk.Entry(self, width=20)
        # self._no_draw_entry.pack(side=tk.LEFT)
        # self._no_draw = self._no_draw_entry.get()
        # not yet check type of input
        self._enter_btn = tk.Button(self, text="Enter", command=lambda:[self._callback1(), self.yes(), self._callback2(self._new_dish)])
        self._enter_btn.pack()

class FileMenu(DishData):
    def __init__(self, master) -> None:
        self._master = master
        self.set_up_file_menu()

    def set_up_file_menu(self):
        menubar = tk.Menu(self._master)
        self._master.config(menu=menubar)

        filememu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filememu)
        filememu.add_command(label="Load File")
        filememu.add_command(label="Save File")

        actionmemu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Action", menu=actionmemu)
        actionmemu.add_command(label="Change Posibility")
        actionmemu.add_command(label="Quit", command=self._master.quit)

    def load_file(self):
        return

    def save_file(self):
        return

    def change_posibility(self):
        return



def app():
    root = tk.Tk()
    root.geometry("700x600")
    root.resizable(0, 0)

    FileMenu(root)

    path = filedialog.askopenfilename()
    
    dish_data = DishData(path)

    database_view = DatabaseView(root, dish_data)
    database_view.pack(side=tk.LEFT, fill=tk.Y)

    chosen_view = ChosenDishView(root)
    chosen_view.pack(side=tk.TOP, fill=tk.BOTH)

    controller = Controller(root, dish_data, chosen_view)
    controller.pack(side=tk.BOTTOM, fill=tk.BOTH, ipady=20)

    root.mainloop()

if __name__ == '__main__':
    app()