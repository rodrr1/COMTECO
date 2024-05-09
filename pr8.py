import tkinter as tk
from tkinter import ttk
import subprocess
import tkinter
import tkinter.messagebox
import time
import json
import random
import sys
import os
import customtkinter
import webbrowser
from paho.mqtt import client as mqtt_client
"""MQTT Parameters"""
#broker = '52.67.47.167'
#broker = 'localhost'
broker = '192.168.188.193'
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

last_update_time = ""  
last_topic1_row_index = None  # Para rastrear la última fila de testtopic/1

last_update_time_topic2 = ""  
last_topic2_row_index = None  # Para rastrear la última fila de testtopic/1
# Agrega esto al código donde configuras tu GUI


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
        global last_topic1_row_index
        global last_update_time
        global last_update_time_topic2
        global last_topic2_row_index
        global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, ip1
        global x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, ip2
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
            ip1=y1["IP"]
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
            print(ip1)
            last_update_time = time.strftime('%Y-%m-%d %H:%M:%S')
            
            # Si ya se ha creado una fila para testtopic/1, actualiza esa fila
            
            if last_topic1_row_index is not None:
                tree.item(last_topic1_row_index, values=["1",
                    last_update_time, "ESMERALDA", "Desactivada", "Tópico 1", ip1, "Condición"
                ])
            else:  # Si no se ha creado una fila, inserta una nueva
                last_topic1_row_index = tree.insert("", "end", values=["1",
                    last_update_time, "ESMERALDA", "Desactivada", "Tópico 1", ip1, "Condición"
                ])
            # Condiciones para activar la alarma
            if x9 == "alarma":
                # Actualizar la fila correspondiente con el estado de la alarma
                tree.item(last_topic1_row_index, values=["1",
                    last_update_time, "ESMERALDA", "Activada", "Tópico 1", ip1, "Condición"
                ])
                tree.item(last_topic1_row_index, tags=("Red.Row",))
                tree.tag_configure("Red.Row", background="red")
            else:
                tree.item(last_topic1_row_index, values=["1",
        last_update_time, "ESMERALDA", "Desactivada", "Tópico 1", ip1, "Activo"
    ])
        
    # Eliminar la configuración del tag que cambia el color de fondo
                tree.item(last_topic1_row_index, tags=())
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
            ip2=y1["IP"]
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
            print(ip2)
            last_update_time_topic2 = time.strftime('%Y-%m-%d %H:%M:%S')  # Obtener la hora actual
            if last_topic2_row_index is not None:
                tree.item(last_topic2_row_index, values=["2",
            last_update_time_topic2, "CAPINOTA", "Estado_2", "Tópico_2", ip2, "Condición_2"
        ])
            else:
                last_topic2_row_index = tree.insert("", "end", values=["2",
            last_update_time_topic2, "CAPINOTA", "Estado_2", "Tópico_2", ip2, "Condición_2"
        ])
            if x19 == "alarma":
                tree.item(last_topic2_row_index, values=["2",
            last_update_time_topic2, "CAPINOTA", "Activada", "Tópico_2", ip2, "Condición_2"
            ])
                tree.item(last_topic2_row_index, tags=("Red.Row",))
                tree.tag_configure("Red.Row", background="red")
            else:
                tree.item(last_topic2_row_index, values=["2",
                last_update_time_topic2, "CAPINOTA", "Desactivada", "Tópico_2", ip2, "Activo"
            ])
                tree.item(last_topic2_row_index, tags=())
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


def update_tree(client, tree, last_topic1_row_index):
    #client.loop_start()
    root.update_idletasks()
    root.after(100, update_tree, client, tree, last_topic1_row_index)  # Actualizar cada 100 ms

def abrir_programa(nombre_alarma):
    if nombre_alarma == "ESMERALDA":
        subprocess.Popen(["python", "main.py"])
    elif nombre_alarma == "TUTI":
        subprocess.Popen(["python", "main1.py"])
    elif nombre_alarma == "CAPINOTA":
        subprocess.Popen(["python", "main.py"])
    root.destroy()

def on_tree_click(event):
    item = tree.item(tree.focus())
    nombre_alarma = item['values'][1]
    abrir_programa(nombre_alarma)

root = tk.Tk()
style = ttk.Style()
style.configure("Red.TLabel", background="red")
root.title("Sistema de seguridad Nodos")
    # Establecer el tamaño de la ventana al iniciar (ancho x alto)
root.geometry("1300x600")  # Cambia 800x600 al tamaño deseado

# Configurar imagen de fondo
background_image = tk.PhotoImage(file="Comteco.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Crear un frame para centrar la tabla
frame = tk.Frame(root)
frame.pack(expand=True)  # Para expandir y ocupar toda la ventana


columns = ('ID','Hora y Fecha', "Nombre", 'Estado de Alarma', 'Tópicos', 'IP ESP32', 'Condición')
tree = ttk.Treeview(frame, columns=columns, show='headings')

# Crear un scrollbar vertical
tree_scroll_y = tk.Scrollbar(frame)
tree_scroll_y.pack(side='right', fill='y')

# Crear la tabla y asociarla al scrollbar
tree = ttk.Treeview(frame, columns=columns, show='headings', yscrollcommand=tree_scroll_y.set)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.pack()  # Usando el pack dentro del frame

data = [
    [time.strftime('%Y-%m-%d %H:%M:%S'), "TUTI", "Desactivada", "Descripción 2", "Recurso 2", "Condición 2"]
    # [time.strftime('%Y-%m-%d %H:%M:%S'), "CAPINOTA", "Desactivada", "Descripción 3", "Recurso 3", "Condición 3"]
]

# Mantener el índice de la última fila actualizada
last_row_index = None  

for item in data:
    tree.insert("", "end", values=item)

tree.bind("<Double-1>", on_tree_click)


client = connect_mqtt()
subscribe(client)


#root.mainloop()

if __name__ == "__main__":
    #main()
    while(1):
        client.loop_start()
        # Condiciones para activar la alarma
        root.mainloop()
        update_tree(client, tree, last_topic1_row_index)
        root.mainloop()  # Iniciar el bucle principal de tkinter
