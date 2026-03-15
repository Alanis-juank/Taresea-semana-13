# Importar la librería Tkinter
import tkinter as tk
from tkinter import messagebox

# Función para agregar datos
def agregar():
    texto = entrada.get()

    # Verificar que el campo no esté vacío
    if texto == "":
        messagebox.showwarning("Aviso", "Debe ingresar un dato")
    else:
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)

# Función para eliminar un elemento seleccionado
def eliminar():
    try:
        seleccion = lista.curselection()
        lista.delete(seleccion)
    except:
        messagebox.showwarning("Aviso", "Seleccione un elemento")

# Función para limpiar toda la lista
def limpiar():
    lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos - Aplicación GUI")
ventana.geometry("350x300")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Botón eliminar
boton_eliminar = tk.Button(ventana, text="Eliminar seleccionado", command=eliminar)
boton_eliminar.pack(pady=5)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar lista", command=limpiar)
boton_limpiar.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
