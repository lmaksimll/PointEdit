import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

class PointPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Point Edit")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)

        self.points = []

        self.canvas.mpl_connect('button_press_event', self.on_click)

        self.import_button = tk.Button(self.root, text="Import csv file", command=self.import_points, height=2)
        self.import_button.grid(row=1, column=0, padx=15, pady=15)

        self.export_button = tk.Button(self.root, text="Export csv file", command=self.export_points, height=2)
        self.export_button.grid(row=1, column=1, padx=15, pady=15)

        self.delete_button = tk.Button(self.root, text="Apply changes", command=self.delete_points, height=2)
        self.delete_button.grid(row=1, column=2, padx=15, pady=15)

    def on_click(self, event):
        for point in self.points:
            if abs(event.xdata - point[0]) < 0.1 and abs(event.ydata - point[1]) < 0.1:
                self.ax.plot(point[0], point[1], 'gx')
                self.points.remove(point)
                self.canvas.draw()
                return

    def import_points(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
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
        self.plot_points()

    def plot_points(self):
        self.ax.clear()

        for point in self.points:
            self.ax.plot(point[0], point[1], 'ro')

        self.canvas.draw()

root = tk.Tk()
app = PointPlotterApp(root)
root.mainloop()
