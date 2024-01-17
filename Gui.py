import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import tkinter.ttk as ttk


def create_image_label(path, row, column):
    img = Image.open(path)

    img_thumbnail = img.resize((100, 100), Image.LANCZOS)
    photo_thumbnail = ImageTk.PhotoImage(img_thumbnail)

    label = tk.Label(image=photo_thumbnail)
    label.image = photo_thumbnail
    label.grid(row=row, column=column, sticky="nsew")

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
        result_label.config(text="Error: normal numbers")


materials = {
    "Steel": {"E": "200", "v": "0.3"},
    "Aluminum": {"E": "70", "v": "0.33"},
    "Copper": {"E": "120", "v": "0.34"},
    "Brass": {"E": "100", "v": "0.35"},
    "Nickel": {"E": "200", "v": "0.3"},
    "Zamak": {"E": "96", "v": "0.33"},
}


def update_outer(event):
    material = outer_material.get()
    properties = materials.get(material, {})
    entry_E0.delete(0, tk.END)
    entry_E0.insert(0, properties.get("E", ""))
    entry_v0.delete(0, tk.END)
    entry_v0.insert(0, properties.get("v", ""))


def update_inner(event):
    material = inner_material.get()
    properties = materials.get(material, {})
    entry_Ei.delete(0, tk.END)
    entry_Ei.insert(0, properties.get("E", ""))
    entry_vi.delete(0, tk.END)
    entry_vi.insert(0, properties.get("v", ""))


root = tk.Tk()
root.title("Torque Calculator")

tk.Label(root, text="Select Material for Outside:").grid(row=13, column=0)
outer_material = ttk.Combobox(root, values=list(materials.keys()))
outer_material.grid(row=13, column=1)
outer_material.bind("<<ComboboxSelected>>", update_outer)


tk.Label(root, text="Select Material for inner:").grid(row=14, column=0)
inner_material = ttk.Combobox(root, values=list(materials.keys()))
inner_material.grid(row=14, column=1)
inner_material.bind("<<ComboboxSelected>>", update_inner)


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

for i in range(15):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)


result_label = tk.Label(root, text="Calculated Torque: ")
result_label.grid(row=12, column=0, columnspan=2)
create_image_label("diagram.png", row=10, column=0)
create_image_label("formula.png", row=10, column=1)

root.mainloop()
