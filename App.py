from subprocess import call
import tkinter as tk
from Constants import *
import random

class ControlDatabase:
    pass

class DishData:
    def __init__(self) -> None:
        self._data = open("Dishes database.txt", "r")
        self._dishes = []
        self._chosen_dishes = []
        
    def draw_dish(self, num):
        for dish in self._data:
            dish = dish.split("\n")[0]
            self._dishes.append(dish)
        dish = random.choices(self._dishes, k = num)
        self._chosen_dishes = dish

class RecipeData:
    pass

class DatabaseView(tk.Frame):
    def __init__(self, master):
        super().__init__(bg="red")
        self._master = master
        self._dish_data = DishData()

        scroll_bar = tk.Scrollbar(self)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        data_list = tk.Listbox(
                self, 
                font=TEXT_FONT, 
                selectmode=tk.EXTENDED, 
                yscrollcommand=scroll_bar.set
            )
        for dish in self._dish_data._data:
            data_list.insert(tk.END, dish)
        data_list.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        scroll_bar.config(command=data_list.yview)

class ChosenDishView(tk.Frame):
    def __init__(self, master):
        super().__init__(bg="blue", width=500)
        self._master = master

    def draw_dish_label(self):
        pass

class Controler(tk.Frame):
    def __init__(self, master, callback) -> None:
        super().__init__(bg="green")
        self._master = master
        self._callback = callback
        self.draw_controller()
        self._no_draw = 0

    def draw_controller(self):
        self._no_draw_entry = tk.Entry(self, width=20)
        self._no_draw_entry.pack(side=tk.LEFT)
        self._no_draw = self._no_draw_entry.get()
        # not yet check type of input
        self._enter_btn = tk.Button(self, text="Enter", command=self._callback(self._no_draw))

def app():
    root = tk.Tk()
    root.geometry("700x600")
    root.resizable(0, 0)
    controler = Controler(root)
    controler.pack(side=tk.BOTTOM, fill=tk.X, ipady=20)
    database_view = DatabaseView(root)
    database_view.pack(side=tk.LEFT, fill=tk.Y)
    chosen_view = ChosenDishView(root)
    chosen_view.pack(side=tk.RIGHT, expand=True, fill=tk.Y)
    
    root.mainloop()

if __name__ == '__main__':
    app()