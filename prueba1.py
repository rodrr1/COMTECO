import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def open_add_window():
    add_window = tk.Toplevel(root)
    add_window.title("Añadir elemento")

    fields = [
        "ID", "Hora y Fecha", "Nombre", "Estado de Alarma", "Tópicos", "IP ESP32", "Condición"
    ]
    entry_widgets = {}

    for field in fields:
        label = tk.Label(add_window, text=field)
        label.pack()
        entry = tk.Entry(add_window)
        entry.pack()
        entry_widgets[field] = entry

    add_button = tk.Button(
        add_window,
        text="Añadir",
        command=lambda: add_item(add_window, entry_widgets)
    )
    add_button.pack()

def add_item(window, entries):
    item_values = [entries[field].get() for field in entries]
    tree.insert("", "end", values=item_values)
    window.destroy()

def delete_item():
    if not tree.selection():
        messagebox.showinfo("Alerta", "No has seleccionado ningún elemento.")
        return
    selected_item = tree.selection()[0]
    tree.delete(selected_item)

def open_edit_window():
    if not tree.selection():
        messagebox.showinfo("Alerta", "No has seleccionado ningún elemento para editar.")
        return

    edit_window = tk.Toplevel(root)
    edit_window.title("Editar elemento")

    selected_item = tree.selection()[0]
    item_values = tree.item(selected_item)['values']

    fields = [
        "ID", "Hora y Fecha", "Nombre", "Estado de Alarma", "Tópicos", "IP ESP32", "Condición"
    ]
    entry_widgets = {}

    for field, value in zip(fields, item_values):
        label = tk.Label(edit_window, text=field)
        label.pack()
        entry = tk.Entry(edit_window)
        entry.pack()
        entry.insert(0, value)
        entry_widgets[field] = entry

    edit_button = tk.Button(
        edit_window,
        text="Guardar cambios",
        command=lambda: edit_item(edit_window, entry_widgets, selected_item)
    )
    edit_button.pack()

def edit_item(window, entries, item):
    new_values = [entries[field].get() for field in entries]
    tree.item(item, values=new_values)
    window.destroy()

def search_item():
    search_term = search_entry.get().lower()
    if search_term:
        found = False
        for item in tree.get_children():
            values = tree.item(item, 'values')
            if any(search_term in str(value).lower() for value in values):
                tree.selection_set(item)
                tree.focus(item)
                found = True
                break
        if not found:
            messagebox.showinfo("Alerta", f"No se encontró '{search_term}' en la tabla.")
    else:
        messagebox.showinfo("Alerta", "Ingresa un nombre para buscar.")


root = tk.Tk()
root.title("Tabla de Alarmas")
root.geometry("900x600")  # Cambia 800x600 al tamaño deseado


# Configurar la imagen de fondo
background_image = tk.PhotoImage(file="Comteco.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
# Cargar la imagen
logo_image = tk.PhotoImage(file="Comteco1.png")

# Mostrar la imagen en un Label
logo_label = tk.Label(root, image=logo_image)
logo_label.place(relx=0, rely=0, anchor='nw')

# Cargar la imagen Univalle.png
univalle_image = tk.PhotoImage(file="UNIVALLE.png")

# Redimensionar la imagen
univalle_image_resized = univalle_image.subsample(19, 19)  # Cambia los valores para ajustar el tamaño

# Mostrar la imagen redimensionada en un Label
univalle_label = tk.Label(root, image=univalle_image_resized)
univalle_label.place(relx=1, rely=0, anchor='ne')


frame = tk.Frame(root, bg='white', bd=2)
frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.6, anchor='n')


columns = ('ID', 'Hora y Fecha', 'Nombre', 'Estado de Alarma', 'Tópicos', 'IP ESP32', 'Condición')
tree = ttk.Treeview(frame, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(side="left", fill="y")

tree_scroll = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree_scroll.pack(side="right", fill="y")

tree.configure(yscrollcommand=tree_scroll.set)

add_button = tk.Button(root, text="Añadir Nodo", command=open_add_window)
add_button.place(relx=0.2, rely=0.9, relwidth=0.15, relheight=0.07)

delete_button = tk.Button(root, text="Eliminar", command=delete_item)
delete_button.place(relx=0.4, rely=0.9, relwidth=0.15, relheight=0.07)

edit_button = tk.Button(root, text="Editar", command=open_edit_window)
edit_button.place(relx=0.6, rely=0.9, relwidth=0.15, relheight=0.07)

search_entry = tk.Entry(root)
search_entry.place(relx=0.7, rely=0.14, relwidth=0.15, relheight=0.05)

search_button = tk.Button(root, text="Buscar por Nombre", command=search_item)
search_button.place(relx=0.55, rely=0.14, relwidth=0.15, relheight=0.05)

root.mainloop()
