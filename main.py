import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
import csv

class PointPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Point Edit")

        self.figure, self.ax = plt.subplots()
        self.rect = Rectangle((0, 0), 1, 1, facecolor='None', edgecolor='green')
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)

        self.points = []
        self.del_points = []
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None

        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('button_press_event', self.on_press)
        self.canvas.mpl_connect('button_release_event', self.on_release)

        self.import_button = tk.Button(self.root, text="Import csv file", command=self.import_points, height=2)
        self.import_button.grid(row=1, column=0, padx=15, pady=15)

        self.export_button = tk.Button(self.root, text="Export csv file", command=self.export_points, height=2)
        self.export_button.grid(row=1, column=1, padx=15, pady=15)

        self.delete_button = tk.Button(self.root, text="Apply changes", command=self.delete_points, height=2)
        self.delete_button.grid(row=1, column=2, padx=15, pady=15)

    def on_press(self, event):
        self.x0 = event.xdata
        self.y0 = event.ydata

    def on_release(self, event):
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.ax.add_patch(self.rect)
        self.canvas.draw()

        if len(self.points) > 0:
            self.selection_points()

    def on_click(self, event):
        if len(self.del_points) == 0:
            return

        for del_point in self.del_points:
            if abs(event.xdata - del_point[0]) < 0.1 and abs(event.ydata - del_point[1]) < 0.1:
                self.ax.plot(del_point[0], del_point[1], 'ro')
                self.del_points.remove(del_point)
                self.canvas.draw()
                return

    def import_points(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.points.clear()
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';', quotechar='"')
                for row in reader:
                    x, y = float(row['x']), float(row['y'])
                    self.points.append((x, y))
            self.plot_points()

    def export_points(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path,'w',encoding='utf-8',newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['x','y'], delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writeheader()
                for point in self.points:
                    writer.writerow({'x': point[0], 'y': point[1]})

    def delete_points(self):
        if len(self.del_points) == 0:
            return

        for del_point in self.del_points:
            for point in self.points:
                if point[0] == del_point[0] and point[1] == del_point[1]:
                    self.points.remove(point)

        self.del_points.clear()
        self.plot_points()

    def plot_points(self):
        self.ax.clear()

        for point in self.points:
            self.ax.plot(point[0], point[1], 'ro')

        self.canvas.draw()

    def selection_points(self):
        for point in self.points:
            if self.x1 > self.x0:
                if point[0] >= self.x0 and point[0] <= self.x1 and point[1] <= self.y0 and point[1] >= self.y1:
                    self.ax.plot(point[0], point[1], 'gx')
                    self.del_points.append(point)
                    self.canvas.draw()
            else:
                if point[0] <= self.x0 and point[0] >= self.x1 and point[1] >= self.y0 and point[1] <= self.y1:
                    self.ax.plot(point[0], point[1], 'gx')
                    self.del_points.append(point)
                    self.canvas.draw()

root = tk.Tk()
app = PointPlotterApp(root)
root.mainloop()