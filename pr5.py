import tkinter as tk
from tkinter import ttk
import subprocess
import tkinter.messagebox
import json
import random
import time
import sys
import os
import customtkinter
import webbrowser
from paho.mqtt import client as mqtt_client

# Definiciones de MQTT y otras variables globales
# ...
"""MQTT Parameters"""
#broker = '52.67.47.167'
#broker = 'localhost'
broker = 'greenopr3.shop'
port = 1883
topic = "testtopic/1"
#PRUEBAAAAA---------------------------------
topic2 = "testtopic/2"
topic3 = "testtopic/3"
topic4 = "testtopic/4"
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'Luis Perez'
password = 'SisComIII'
x1=0
x2=0
x3=0
x4=0
x5=0
x6=0
x7=0
x8=0
x9=0
x10=0

x11=0
x12=0
x13=0
x14=0
x15=0
x16=0
x17=0
x18=0
x19=0
x20=0

x21=0
x22=0
x23=0
x24=0
x25=0
x26=0
x27=0
x28=0
x29=0
x30=0

x31=0
x32=0
x33=0
x34=0
x35=0
x36=0
x37=0
x38=0
x39=0
x40=0
"""MQTT CONNECT"""

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):

        global x1, x2, x3, x4, x5, x6, x7, x8, x9
        global x11, x12, x13, x14, x15, x16, x17, x18, x19, x20
        global x21, x22, x23, x24, x25, x26, x27, x28, x29, x30
        global x31, x32, x33, x34, x35, x36, x37, x38, x39, x40

        y = msg.payload.decode()
        print(y)
        print(f"Mensaje recibido en el tópico: {msg.topic}")
        print(y)

        if msg.topic == topic:
            y1 = json.loads(y)
            x1 = y1.get("VAC1", x1)
            x2 = y1.get("VAC2", x2)
            x3 = y1.get("VDC1", x3)
            x4 = y1.get("VDC2", x4)
            x5 = y1.get("TEMP", x5)
            x6 = y1.get("HUM", x6)
            x7 = y1.get("DOOR1", x7)
            x8 = y1.get("DOOR2", x8)
            x9 = y1.get("ALAR", x9)
            x10 = y1.get("AL_Bocina", x10)
            print(x1)
            print(x2)
            print(x3)
            print(x4)
            print(x5)
            print(x6)
            print(x7)
            print(x8)
            print(x9)
            print(x10)

        elif msg.topic == topic2:
            y1 = json.loads(y)
            x11 = y1.get("VAC1", x11)
            x12 = y1.get("VAC2", x12)
            x13 = y1.get("VDC1", x13)
            x14 = y1.get("VDC2", x14)
            x15 = y1.get("TEMP", x15)
            x16 = y1.get("HUM", x16)
            x17 = y1.get("DOOR1", x17)
            x18 = y1.get("DOOR2", x18)
            x19 = y1.get("ALAR", x19)
            x20 = y1.get("AL_Bocina", x20)
            print(x11)
            print(x12)
            print(x13)
            print(x14)
            print(x15)
            print(x16)
            print(x17)
            print(x18)
            print(x19)
            print(x20)
            # Manejar el mensaje recibido en topic2
            pass  # Agrega aquí la lógica para manejar el mensaje de topic2

        elif msg.topic == topic3:
            y1 = json.loads(y)
            x21 = y1.get("VAC1", x21)
            x22 = y1.get("VAC2", x22)
            x23 = y1.get("VDC1", x23)
            x24 = y1.get("VDC2", x24)
            x25 = y1.get("TEMP", x25)
            x26 = y1.get("HUM", x26)
            x27 = y1.get("DOOR1", x27)
            x28 = y1.get("DOOR2", x28)
            x29 = y1.get("ALAR", x29)
            x30 = y1.get("AL_Bocina", x30)
            print(x21)
            print(x22)
            print(x23)
            print(x24)
            print(x25)
            print(x26)
            print(x27)
            print(x28)
            print(x29)
            print(x30)
            # Manejar el mensaje recibido en topic3
            pass  # Agrega aquí la lógica para manejar el mensaje de topic3

        elif msg.topic == topic4:
            y1 = json.loads(y)
            x31 = y1.get("VAC1", x31)
            x32 = y1.get("VAC2", x32)
            x33 = y1.get("VDC1", x33)
            x34 = y1.get("VDC2", x34)
            x35 = y1.get("TEMP", x35)
            x36 = y1.get("HUM", x36)
            x37 = y1.get("DOOR1", x37)
            x38 = y1.get("DOOR2", x38)
            x39 = y1.get("ALAR", x39)
            x40 = y1.get("AL_Bocina", x40)
            print(x31)
            print(x32)
            print(x33)
            print(x34)
            print(x35)
            print(x36)
            print(x37)
            print(x38)
            print(x39)
            print(x40)
            # Manejar el mensaje recibido en topic4

            pass  # Agrega aquí la lógica para manejar el mensaje de topic4


    client.subscribe(topic)
    client.subscribe(topic2)
    client.subscribe(topic3)
    client.subscribe(topic4)
    client.on_message = on_message

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de seguridad Nodos")
root.geometry("1300x600")

# Configurar estilo de botones
estilo = ttk.Style()
estilo.configure("TButton", foreground="black", background="blue", font=("Helvetica", 12))

# Configurar imagen de fondo
background_image = tk.PhotoImage(file="Comteco.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Crear un frame para centrar la tabla
frame = tk.Frame(root)
frame.pack(expand=True)  # Para expandir y ocupar toda la ventana

# Crear marcos para organizar widgets
# ...
def abrir_programa(nombre_alarma):
    if nombre_alarma == "ESMERALDA":
        subprocess.Popen(["python", "main.py"])
    elif nombre_alarma == "TUTI":
        subprocess.Popen(["python", "main.py"])
    elif nombre_alarma == "CAPINOTA":
        subprocess.Popen(["python", "main.py"])
    # Reanudar la actualización después de 1 segundo
    root.after(3000, update_alarm_table)

def on_tree_click(event):
    item = tree.item(tree.focus())
    nombre_alarma = item['values'][1]
    tree.unbind("<Button-1>")  # Deshabilitar temporalmente el clic en la tabla
    abrir_programa(nombre_alarma)

    # Función para actualizar la tabla de alarmas
def update_alarm_table():
    for row in tree.get_children():
        tree.delete(row)

    # Ejemplo de datos ficticios para la tabla de alarmas
    last_data_time = time.strftime('%Y-%m-%d %H:%M:%S')  # Hora y fecha actual
    estado_alarma = "Activa"
    nombre_alarma = "ESMERALDA"
    descripcion = "Descripción de la alarma"
    recurso = "Recurso asociado"
    condicion = "Condición de la alarma"
    #ALARMA TUTI
    last_data_time1 = time.strftime('%Y-%m-%d %H:%M:%S')  # Hora y fecha actual
    estado_alarma1 = "Desactivada"
    nombre_alarma1 = "TUTI"
    descripcion1 = "Descripción de la alarma"
    recurso1 = "Recurso asociado"
    condicion1 = "Condición de la alarma"
    #ALARMA CAPINOTA
    last_data_time2 = time.strftime('%Y-%m-%d %H:%M:%S')  # Hora y fecha actual
    estado_alarma2 = "Desactivada"
    nombre_alarma2 = "CAPINOTA"
    descripcion2 = "Descripción de la alarma"
    recurso2 = "Recurso asociado"
    condicion2 = "Condición de la alarma"

    tree.insert("", "end", values=(last_data_time,nombre_alarma, estado_alarma, descripcion, recurso, condicion))
    tree.insert("", "end", values=(last_data_time1,nombre_alarma1, estado_alarma1, descripcion1, recurso1, condicion1))
    tree.insert("", "end", values=(last_data_time2,nombre_alarma2, estado_alarma2, descripcion2, recurso2, condicion2))
    

    # Actualizar cada segundo
    root.after(1000, update_alarm_table)


# Crear Treeview para mostrar la tabla de alarmas
columns = ('Hora y Fecha', "Nombre", 'Estado de Alarma', 'Descripción', 'Recurso', 'Condición')
tree = ttk.Treeview(root, columns=columns, show='headings')

# Configurar encabezados de las columnas
for col in columns:
    tree.heading(col, text=col)

# Definir tamaños de columnas
tree.column("Hora y Fecha", width=150)
tree.column("Estado de Alarma", width=100)
tree.column("Descripción", width=200)
tree.column("Recurso", width=100)
tree.column("Condición", width=100)

# Colocar el Treeview en la ventana principal
tree.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)

# Iniciar actualización de la tabla de alarmas
update_alarm_table()

# Resto de tu código...
# ...

# Loop principal de la aplicación
if __name__ == "__main__":
    while True:
        root.update()
