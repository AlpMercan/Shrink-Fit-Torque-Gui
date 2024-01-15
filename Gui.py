import tkinter as tk
import numpy as np
from PIL import Image, ImageTk


def create_image_label(path, row, column):
    img = Image.open(path)

    img_thumbnail = img.resize((100, 100), Image.LANCZOS)
    photo_thumbnail = ImageTk.PhotoImage(img_thumbnail)

    label = tk.Label(image=photo_thumbnail)
    label.image = photo_thumbnail
    label.grid(row=row, column=column)

    label.bind("<Button-1>", lambda e: open_enlarged_image(path))


def open_enlarged_image(path):
    new_window = tk.Toplevel()
    new_window.title("Enlarged Image")

    img = Image.open(path)
    photo = ImageTk.PhotoImage(img)

    label = tk.Label(new_window, image=photo)
    label.image = photo
    label.pack()


def calculate_torque():
    try:
        E_0 = float(entry_E0.get()) * 10**9
        E_i = float(entry_Ei.get()) * 10**9
        v_0 = float(entry_v0.get())
        v_i = float(entry_vi.get())
        d_0 = float(entry_d0.get())
        d_i = float(entry_di.get())
        d = float(entry_d.get())
        inter = float(entry_inter.get())
        u = float(entry_u.get())
        L = float(entry_L.get()) * 10**-2

        sag = (d / E_0) * ((d_0**2 + d**2) / (d_0**2 - d**2) + v_0)
        sol = (d / E_i) * ((d_i**2 + d**2) / (d**2 - d_i) - v_i)
        P = inter / (sag + sol)
        radius = d / 2
        A = 2 * np.pi * radius * L
        N = P * A
        T = u * N * radius

        result_label.config(text=f"Calculated Torque: {T:.2f} Nm")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers")


root = tk.Tk()
root.title("Torque Calculator")


tk.Label(root, text="E_0 (GPa):").grid(row=0, column=0)
entry_E0 = tk.Entry(root)
entry_E0.insert(0, "2.5")
entry_E0.grid(row=0, column=1)

tk.Label(root, text="E_i (GPa):").grid(row=1, column=0)
entry_Ei = tk.Entry(root)
entry_Ei.insert(0, "2.5")
entry_Ei.grid(row=1, column=1)

tk.Label(root, text="v_0:").grid(row=2, column=0)
entry_v0 = tk.Entry(root)
entry_v0.insert(0, "0.3")
entry_v0.grid(row=2, column=1)

tk.Label(root, text="v_i:").grid(row=3, column=0)
entry_vi = tk.Entry(root)
entry_vi.insert(0, "0.3")
entry_vi.grid(row=3, column=1)

tk.Label(root, text="d_0 (m):").grid(row=4, column=0)
entry_d0 = tk.Entry(root)
entry_d0.insert(0, "0.005")
entry_d0.grid(row=4, column=1)

tk.Label(root, text="d (m):").grid(row=5, column=0)
entry_d = tk.Entry(root)
entry_d.insert(0, "0.0045")
entry_d.grid(row=5, column=1)

tk.Label(root, text="d_i (m):").grid(row=6, column=0)
entry_di = tk.Entry(root)
entry_di.insert(0, "0")
entry_di.grid(row=6, column=1)

tk.Label(root, text="Interference (m):").grid(row=7, column=0)
entry_inter = tk.Entry(root)
entry_inter.insert(0, "0.0001")
entry_inter.grid(row=7, column=1)

tk.Label(root, text="Length L (m):").grid(row=8, column=0)
entry_L = tk.Entry(root)
entry_L.insert(0, "0.027")
entry_L.grid(row=8, column=1)

tk.Label(root, text="Friction Coefficient u:").grid(row=9, column=0)
entry_u = tk.Entry(root)
entry_u.insert(0, "0.3")
entry_u.grid(row=9, column=1)


calculate_button = tk.Button(root, text="Calculate Torque", command=calculate_torque)
calculate_button.grid(row=11, column=0, columnspan=2)


result_label = tk.Label(root, text="Calculated Torque: ")
result_label.grid(row=12, column=0, columnspan=2)
create_image_label("diagram.png", row=10, column=0)
create_image_label("formula.png", row=10, column=1)
# Start the GUI loop
root.mainloop()
