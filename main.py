# Importa el módulo tkinter y lo renombra como tk para la interfaz gráfica
from logging import root
import tkinter as tk
# Importa messagebox de tkinter para mostrar cuadros de diálogo
from tkinter import messagebox
# Importa ttk de tkinter para widgets mejorados
from tkinter import ttk
# Importa el módulo re para expresiones regulares
import re


def basic_config(hostname, enable_secret, user_name, user_password, banner):
    """
    Generates a basic Cisco router configuration.

    Args:
        hostname (str): The hostname for the router.
        enable_secret (str): The enable secret password.
        user_name (str): The username for local login.
        user_password (str): The password for the user.
        banner (str): The message of the day banner.

    Returns:
        str: The generated configuration as a string.
    """
    config = f"""
hostname {hostname}
enable secret {enable_secret}
username {user_name} privilege 15 secret {user_password}
line console 0
login local
exit
line vty 0 15
login local
transport input ssh
exit
banner motd #{banner}#
"""
    return config


# Crea la ventana principal
root = tk.Tk()
root.title("Cisco Router Config Generator")
root.geometry("600x600")

# Etiquetas y entradas
tk.Label(root, text="Hostname:").pack()
entrada_hostname = tk.Entry(root, width=50)
entrada_hostname.pack()

tk.Label(root, text="Enable Secret:").pack()
entrada_enable = tk.Entry(root, width=50)
entrada_enable.pack()

tk.Label(root, text="Username:").pack()
entrada_username = tk.Entry(root, width=50)
entrada_username.pack()

tk.Label(root, text="User Password:").pack()
entrada_password = tk.Entry(root, width=50)
entrada_password.pack()

tk.Label(root, text="Banner:").pack()
entrada_banner = tk.Entry(root, width=50)
entrada_banner.pack()

# Area para mostrar el texto
texto_salida = tk.Text(root, height=20, width=80)
texto_salida.pack(pady=10)

# Funcion para generar el texto


def generar():
    # obtener valores
    hostname = entrada_hostname.get()
    enable_secret = entrada_enable.get()
    username = entrada_username.get()
    user_password = entrada_password.get()
    banner = entrada_banner.get()

    # Validaciones
    if not hostname:
        messagebox.showerror("Error", "Por favor ingresa hostname")
        return
    if not enable_secret:
        messagebox.showerror("Error", "Por favor ingresa Enable secret")
        return
    if not username:
        messagebox.showerror("Error", "Por favor ingresa Username")
        return
    if not user_password:
        messagebox.showerror("Error", "Por favor ingresa User Password")
        return
    if not banner:
        messagebox.showerror("Error", "Por favor ingresa Banner")
        return

    # llamar a la funcion que genera la configuracion
    configuracion = basic_config(
        hostname, enable_secret, username, user_password, banner)

    # mostra el texto
    # Limpiar el área de texto antes de insertar nuevo texto
    texto_salida.delete(1.0, tk.END)
    texto_salida.insert(tk.END, configuracion)


# Botón para generar la configuración
boton_generar = tk.Button(root, text="Generar Configuración", command=generar)
boton_generar.pack()

# Iniciar el bucle principal de la interfaz
root.mainloop()
