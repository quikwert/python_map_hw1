from data import build_dataset_2020
from data import build_dataset_2026
from render import export_map
from render import create_map, create_artists
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.state = 2020
        self.data2020 = build_dataset_2020()
        self.data2026 = build_dataset_2026()
        export_map("flights.png",[self.data2020, self.data2026])



        self.fig, self.ax = create_map()
        self.lines = create_artists(self.ax, max(len(self.data2026),len(self.data2020)))
        
        self.ax.text(0.5,1.08,"") 
        self.ax.set_title("Direct Flights from Tallinn Airport\nDmitri Rodzik\n Year: 2020")

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()

        self.canvas_widget.pack(fill="both", expand=True)

        self.button = tk.Button(root, text="Switch to 2026", command=self.toggle)
        self.button.place(x=10, y=10)  # floating overlay
        toolbar = NavigationToolbar2Tk(self.canvas, root)
        toolbar.update()
        toolbar.pack()

        self.canvas.draw()
        self.toggle()

    def toggle(self):
        dataset = []
        if self.state == 2020:
            self.state = 2026
            self.ax.set_title("Direct Flights from Tallinn Airport\nDmitri Rodzik\n Year: 2026")
            self.button.config(text="Switch to 2020")
            dataset = self.data2026

        else:
            self.state = 2020
            self.ax.set_title("Direct Flights from Tallinn Airport\nDmitri Rodzik\n Year: 2020")
            self.button.config(text="Switch to 2026")
            dataset = self.data2020
        for line in self.lines:
            line.set_data([], [])
        for line, (lons, lats) in zip(self.lines, dataset):
            line.set_data(lons, lats)
        self.canvas.draw_idle()

def main():

    root = tk.Tk()
    root.geometry("800x600")

    App(root)

    root.mainloop()


if __name__ == "__main__":
    main()
