import tkinter as tk
from tkinter import ttk
import subprocess
import tkinter
import tkinter.messagebox
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

        global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10
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


def abrir_programa_secundario(programa):
    subprocess.Popen(["py", programa], shell=True)
    #root.withdraw()
    root.destroy()

root = tk.Tk()
root.title("Sistema de seguridad Nodos")
    # Establecer el tamaño de la ventana al iniciar (ancho x alto)
root.geometry("1300x600")  # Cambia 800x600 al tamaño deseado

    # Personalizar el estilo de los botones
estilo = ttk.Style()
estilo.configure("TButton", foreground="black", background="blue", font=("Helvetica", 12))

    # Configurar una imagen de fondo
background_image = tk.PhotoImage(file="Comteco.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

    # Crear marcos para organizar widgets
frame1 = ttk.Frame(root, borderwidth=2, relief="groove")
frame1.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
frame2 = ttk.Frame(root, borderwidth=2, relief="groove")
frame2.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.2)

right_frame = tk.Frame(root, borderwidth=2, bg="lightgray")
#right_frame.place(x=200, y=50, width=100, height=50, relx=0.5, rely=0, relwidth=0.5, relheight=1, anchor="ne")
right_frame.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.7)

# Botones para abrir programas secundarios
programa1_button = ttk.Button(frame1, text="Esmeralda", command=lambda: abrir_programa_secundario("main1.py"))
#background_label.grid(row=0, column=0)
programa1_button.pack(pady=10)

#etiqueta_alarma = tk.Label(root, text="Alarma CHAP:")
#etiqueta_alarma.grid(row=0, column=1)
etiqueta_alarma = tk.Label(right_frame, text="Alarma CHAP:")
etiqueta_alarma.grid(row=0, column=0)


#alarma1 = tk.Entry(root, bg="white", width=10)  # Caja de texto para la alarma
#alarma1.grid(row=0, column=2)
alarma1 = tk.Entry(right_frame, bg="white", width=10)  # Caja de texto para la alarma
alarma1.grid(row=0, column=2)

programa2_button = ttk.Button(frame1, text="TUTI", command=lambda: abrir_programa_secundario("Tuti.py"))
#background_label.grid(row=1, column=0)
programa2_button.pack(pady=10)

#etiqueta_alarma = tk.Label(root, text="Alarma Tuti:")
etiqueta_alarma = tk.Label(right_frame, text="Alarma Tuti:")
etiqueta_alarma.grid(row=1, column=1)

alarma2 = tk.Entry(right_frame, bg="white", width=10)  # Caja de texto para la alarma
alarma2.grid(row=1, column=2)

programa3_button = ttk.Button(frame2, text="Capinota", command=lambda: abrir_programa_secundario("main.py"))
#background_label.grid(row=2, column=0)
programa3_button.pack(pady=10)

etiqueta_alarma = tk.Label(right_frame, text="Alarma:")
etiqueta_alarma.grid(row=2, column=1)

alarma3 = tk.Entry(right_frame, bg="white", width=10)  # Caja de texto para la alarma
alarma3.grid(row=2, column=2)

programa4_button = ttk.Button(frame2, text="Cocha", command=lambda: abrir_programa_secundario("cbba.py"))
#background_label.grid(row=3, column=0)
programa4_button.pack(pady=10)

etiqueta_alarma = tk.Label(right_frame, text="Alarma:")
etiqueta_alarma.grid(row=3, column=1)

alarma4 = tk.Entry(right_frame, bg="white", width=10)  # Caja de texto para la alarma
alarma4.grid(row=3, column=2)


client = connect_mqtt()
subscribe(client)


#root.mainloop()

if __name__ == "__main__":
    #main()
    while(1):
        client.loop_start()
        root.update()

#CODICION PARA ALARMA1
        if x9=="alarma":
            alarma1.config(bg="red")
        else:
            alarma1.config(bg="white")

#CODICION PARA ALARMA2
        if x19=="alarma":
            alarma2.config(bg="red")
        else:
            alarma2.config(bg="white")

#CODICION PARA ALARMA3
        if x29=="alarma":
            alarma3.config(bg="red")
        else:
            alarma3.config(bg="white")

#CODICION PARA ALARMA4
        if x39=="alarma":
            alarma4.config(bg="red")
        else:
            alarma4.config(bg="white")

        client.loop_stop()