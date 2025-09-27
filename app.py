#Se importan las librerias necesarias
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Archivo base
FILE = "articulos.csv"

# Función para crear artículo
def guardar_articulo():
    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    cantidad = entry_cantidad.get()
#se crea la obligacion de llenar los campos
    if not (codigo and nombre and precio and cantidad):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    # Guardar en CSV
    df = pd.DataFrame([[codigo, nombre, precio, cantidad]],
                      columns=["Codigo", "Nombre", "Precio", "Cantidad"])
    if os.path.exists(FILE):
        df.to_csv(FILE, mode="a", index=False, header=False)
    else:
        df.to_csv(FILE, index=False)

    messagebox.showinfo("Éxito", "Artículo guardado con éxito")
    limpiar_campos() # una vez guardado, se ejecuta la funcion de limpiar campos (se crea abajo) para registrar mas articulos

def limpiar_campos():
    entry_codigo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

# Función para exportar artículos a Excel
def exportar_excel():
    if not os.path.exists(FILE):
        messagebox.showerror("Error", "No hay artículos registrados")
        return
    df = pd.read_csv(FILE)
    df.to_excel("articulos.xlsx", index=False)
    messagebox.showinfo("Éxito", "Artículos exportados a Excel")

# Interfaz Tkinter
root = tk.Tk() #se crea la interfaz (sin forma)
root.title("QuickStock - Prueba de Concepto") #titulo de la ventana

#se crean los campos a rellenar con la informacion de los articulos
tk.Label(root, text="Código:").grid(row=0, column=0) 
tk.Label(root, text="Nombre:").grid(row=1, column=0)
tk.Label(root, text="Precio:").grid(row=2, column=0)
tk.Label(root, text="Cantidad:").grid(row=3, column=0)

entry_codigo = tk.Entry(root)
entry_nombre = tk.Entry(root)
entry_precio = tk.Entry(root)
entry_cantidad = tk.Entry(root)

entry_codigo.grid(row=0, column=1)
entry_nombre.grid(row=1, column=1)
entry_precio.grid(row=2, column=1)
entry_cantidad.grid(row=3, column=1)

tk.Button(root, text="Guardar Artículo", command=guardar_articulo).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Exportar a Excel", command=exportar_excel).grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
