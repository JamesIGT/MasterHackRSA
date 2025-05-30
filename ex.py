import random
import tkinter as tk
from tkinter import messagebox
from funtions import *

def generar_claves():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        if not es_primo(p) or not es_primo(q) or p == q:
            raise ValueError("Los valores de p y q deben ser primos y diferentes.")
        n = p * q
        ø = (p - 1) * (q - 1)
        lista_e = calcular_e(ø)
        
        # Seleccionar un valor aleatorio de e
        e = random.choice(lista_e)
        
        d = calcular_d(e, ø)
        key_public = [n, e]
        key_private = [n, d]
        
        # Mostrar resultados en la interfaz
        label_resultado_publico.config(text=f"Clave Pública: {key_public}")
        label_resultado_privado.config(text=f"Clave Privada: {key_private}")
        entry_e.delete(0, tk.END)
        entry_e.insert(0, str(e))
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def cifrar():
    try:
        mensaje = entry_mensaje.get()
        key_public = eval(label_resultado_publico.cget("text").split(": ")[1])
        mensaje_cifrado = cifrar_mensaje(mensaje, key_public)
        label_resultado_cifrado.config(text=f"Mensaje Cifrado: {mensaje_cifrado}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def descifrar():
    try:
        mensaje_cifrado = entry_mensaje_cifrado.get()
        key_private = eval(label_resultado_privado.cget("text").split(": ")[1])
        mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, key_private)
        label_resultado_descifrado.config(text=f"Mensaje Descifrado: {mensaje_descifrado}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz RSA")
ventana.geometry("600x500")
ventana.configure(bg="#2c3e50")

# Crear el frame principal con un fondo oscuro
frame = tk.Frame(ventana, bg="#2c3e50", padx=20, pady=20)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

tk.Label(frame, text="CIFRADO RSA", bg="#2c3e50",fg="#ecf0f1", font=("Arial", 22, "bold")).grid(column=0, row=0, padx=0, pady=5)
# Etiquetas y entradas para p, q, e
tk.Label(frame, text="Valor de p:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 13, "bold")).grid(column=0, row=1, padx=0, pady=5)
entry_p = tk.Entry(frame, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12))
entry_p.grid(column=1, row=1, padx=0, pady=5)

tk.Label(frame, text="Valor de q:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 13, "bold")).grid(column=0, row=2, padx=0, pady=5)
entry_q = tk.Entry(frame, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12))
entry_q.grid(column=1, row=2, padx=0, pady=5)

tk.Label(frame, text="Valor de e:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 13, "bold")).grid(column=0, row=3, padx=60, pady=5 )
entry_e = tk.Entry(frame, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 13, "bold"))
entry_e.grid(column=1, row=3, padx=10, pady=5)

# Botones para generar claves, cifrar y descifrar
frame_botones = tk.Frame(frame, bg="#2c3e50", pady=10)
frame_botones.grid(column=0, row=4, columnspan=2, pady=10)

btn_generar_claves = tk.Button(frame_botones, text="Generar Claves", bg="#6187ad", fg="#ffffff", font=("Helvetica", 12, "bold"), command=generar_claves)
btn_generar_claves.pack(side=tk.LEFT, padx=5)

btn_cifrar = tk.Button(frame_botones, text="Cifrar Mensaje", bg="#6187ad", fg="#ffffff", font=("Helvetica", 12, "bold"), command=cifrar)
btn_cifrar.pack(side=tk.LEFT, padx=5)

btn_descifrar = tk.Button(frame_botones, text="Descifrar Mensaje", bg="#6187ad", fg="#ffffff", font=("Helvetica", 12, "bold"), command=descifrar)
btn_descifrar.pack(side=tk.LEFT, padx=5)

# Etiquetas para mostrar resultados
label_resultado_publico = tk.Label(frame, text="Clave Pública:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
label_resultado_publico.grid(column=0, row=5, columnspan=2, padx=10, pady=5)

label_resultado_privado = tk.Label(frame, text="Clave Privada:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
label_resultado_privado.grid(column=0, row=5, columnspan=2, padx=10, pady=5)

label_resultado_cifrado = tk.Label(frame, text="Mensaje Cifrado:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
label_resultado_cifrado.grid(column=0, row=6, columnspan=2, padx=10, pady=5)

label_resultado_descifrado = tk.Label(frame, text="Mensaje Descifrado:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
label_resultado_descifrado.grid(column=0, row=7, columnspan=2, padx=10, pady=5)

# Entradas para mensajes
tk.Label(frame, text="Mensaje a cifrar:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12, "bold")).grid(column=0, row=8, padx=10, pady=5)
entry_mensaje = tk.Entry(frame, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12, "bold"))
entry_mensaje.grid(column=1, row=8, padx=10, pady=5)

tk.Label(frame, text="Mensaje cifrado:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12, "bold")).grid(column=0, row=9, padx=10, pady=5)
entry_mensaje_cifrado = tk.Entry(frame, bg="#ecf0f1", fg="#2c3e50", font=("Helvetica", 12, "bold"))
entry_mensaje_cifrado.grid(column=1, row=9, padx=10, pady=5)

# Ejecutar la aplicación
ventana.mainloop()