import tkinter as tk
from Constants import *
import random

class ControlDatabase:
    pass

class DishData:
    """Get the dishes name from database and draw dishes"""
    def __init__(self) -> None:
        self._data = open("Dishes database.txt", "r")
        self._dishes = []
        self._all_dishes = self._data.readlines()
        for i in self._all_dishes:
            i = i.split("\n")[0]
            self._dishes.append(i)
        self._chosen_dish = None
        
    def draw_dish(self):
        """Try draw 1 dish"""
        # print(self._dishes)
        self._chosen_dish = random.choices(self._dishes)
        # self._chosen_dishes = dish
        print(self._chosen_dish)
        self._callback()

    def set_callback(self, callback):
        self._callback = callback
        

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

    def draw_dish_label(self, name):
        var = tk.Label(self, text=name, font=TEXT_FONT)
        var.pack(side=tk.TOP, fill=tk.X)

class Controler(tk.Frame):
    """Controler"""
    def __init__(self, master, data) -> None:
        super().__init__(bg="green")
        self._master = master
        self._data = data
        self._callback = self._data.draw_dish
        self.draw_controller()
        self._no_draw = 0

    def draw_controller(self):
        # self._no_draw_entry = tk.Entry(self, width=20)
        # self._no_draw_entry.pack(side=tk.LEFT)
        # self._no_draw = self._no_draw_entry.get()
        # not yet check type of input
        self._enter_btn = tk.Button(self, text="Enter", command=self._callback)
        self._enter_btn.pack()

def app():
    root = tk.Tk()
    root.geometry("700x600")
    root.resizable(0, 0)
    
    dish_data = DishData()
    
    controller = Controler(root, dish_data)
    controller.pack(side=tk.BOTTOM, fill=tk.X, ipady=20)

    database_view = DatabaseView(root, dish_data)
    database_view.pack(side=tk.LEFT, fill=tk.Y)

    chosen_view = ChosenDishView(root)
    chosen_view.pack(side=tk.RIGHT, fill=tk.Y)

    dish_data.set_callback(chosen_view.draw_dish_label(dish_data._chosen_dish))
    
    root.mainloop()

if __name__ == '__main__':
    app()