import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def plot_shaded_function(a, b, func):
    x = np.linspace(-10, 10, 400)  
    y = eval(func)  

    plt.figure()
    plt.plot(x, y, 'b-', label='f(x)')  
    plt.fill_between(x, y, where=[(xi >= a and xi <= b) for xi in x], color='gray', alpha=0.5)  
    plt.axhline(0, color='black', linewidth=0.5)  # Добавляем горизонтальную ось y
    plt.axvline(a, color='red', linestyle='--', linewidth=1)  
    plt.axvline(b, color='red', linestyle='--', linewidth=1)  

    plt.xlabel('x')
    plt.ylabel('y')


    plt.grid(True)
    plt.legend()

    return plt.gcf()


def plot_from_entry():
    a = float(entry_a.get())  
    b = float(entry_b.get())  
    func = entry_func.get()   

    fig = plot_shaded_function(a, b, func)


    for widget in frame_plot.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame_plot)
    canvas.draw()
    canvas.get_tk_widget().pack()



root = tk.Tk()
root.title("Построение графика функции")


label_func = tk.Label(root, text="Функция f(x):")
label_func.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

entry_func = tk.Entry(root)
entry_func.grid(row=0, column=1, padx=10, pady=5)

label_a = tk.Label(root, text="Значение a:")
label_a.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1, padx=10, pady=5)

label_b = tk.Label(root, text="Значение b:")
label_b.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1, padx=10, pady=5)

plot_button = tk.Button(root, text="Построить график", command=plot_from_entry)
plot_button.grid(row=3, columnspan=2, padx=10, pady=10)


frame_plot = tk.Frame(root)
frame_plot.grid(row=4, columnspan=2, padx=10, pady=10)


root.mainloop()

