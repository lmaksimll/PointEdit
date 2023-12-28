import ClassField


import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

class PointPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Point Plotter")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.points = []

        self.canvas.mpl_connect('button_press_event', self.on_click)

        self.clear_button = tk.Button(self.root, text="Clear Points", command=self.clear_points)
        self.clear_button.pack()

        self.show_button = tk.Button(self.root, text="Show Points", command=self.show_points)
        self.show_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_app)
        self.quit_button.pack()

        self.load_points_from_csv("PointCsv.csv")

    def on_click(self, event):
        for point in self.points:
            if abs(event.xdata - point[0]) < 0.1 and abs(event.ydata - point[1]) < 0.1:
                self.points.remove(point)
                self.plot_points()
                return

    def clear_points(self):
        self.ax.clear()
        self.points = []
        self.canvas.draw()

    def show_points(self):
        if not self.points:
            print("No points to display")
        else:
            for point in self.points:
                print(f"({point[0]}, {point[1]})")

    def load_points_from_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';', quotechar='"')
            for row in reader:
                x, y = row['x'], row['y']
                self.points.append((x, y))
        self.plot_points()

    def plot_points(self):
        self.ax.clear()

        for point in self.points:
            self.ax.plot(point[0], point[1], 'ro')

        self.canvas.draw()

    def quit_app(self):
        self.root.quit()


root = tk.Tk()
app = PointPlotterApp(root)
root.mainloop()


#---------------------------------

cf = ClassField.Field()

btn = 'add_file'  # Нажатие кнопки
name_file = 'PointCsv.csv'

if btn == 'add_file':
    cf.add_file(name_file)

if btn == 'edit_file':
    cf.edit_file(cf.list_file[0])

if btn == 'delete_point':
    del_list_points = []
    cf.delete_point(del_list_points)






