import tkinter as tk
from tkinter import ttk
import subprocess
import tkinter
import tkinter.messagebox
from tkinter import messagebox
import json
import time
from datetime import datetime, timedelta
import random
import threading
import sys
import os
import customtkinter
import webbrowser
from paho.mqtt import client as mqtt_client
"""MQTT Parameters"""
#broker = '52.67.47.167'
broker = 'localhost'
#broker = '192.168.33.101'
port = 1883
topic = "testtopic/1"
#topic_list = ['topic/1', 'topic/2']
topic_list1 = ['topic/4', 'topic/3']
#topics = ['topic/3', 'topic/4']
ping_active = True
#INCREMENTABLE ID
last_item_id = 0  # Inicializar el último ID utilizado
topic_list = []#asdasdasdasd
subscribed_topics = []
table_data = []
topic1_active = False
#PRUEBAAAAA---------------------------------
topic2 = "testtopic/2"
topic3 = "testtopic/3"
topic4 = "testtopic/4"
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'Luis Perez1'
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

"""MQTT CONNECT"""
def connect_mqtt() -> mqtt_client:
    global topic_list  # Indica que estás usando la variable global topic_list

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            # Cargar datos del archivo JSON
            topics_to_subscribe = load_table_data_from_json()
            if topics_to_subscribe:
                for item in topics_to_subscribe:
                    topic = item.get('Tópicos')
                    if topic:
                        if topic not in topic_list:
                            topic_list.append(topic)
                        client.subscribe(topic)
                        print(f"Subscribed to {topic}")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def check_connection(hostname):
    global ping_active
    try:
        while ping_active:
            ping_process = subprocess.Popen(['ping', '-n', '1', hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = ping_process.communicate()
            if "Tiempo de espera agotado para esta solicitud." in output or "Host de destino inaccesible" in output:
                print("Inactivo")
            else:
                print("Activo")
                time.sleep(4)  # Esperar 2 segundos antes de realizar el próximo ping
    except Exception as e:
        print(f"Error: {e}")

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        ##PRUEBA
        global ping_active
        ping_active = False
        print("Deteniendo la función de ping...")
        global last_topic1_row_index, topic1_active
        global last_update_time, current_time
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

        if msg.topic == 'topic/1':
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
            topic1_active = True
            last_update_time_str = time.strftime('%Y-%m-%d %H:%M:%S')  # Obtén la hora y fecha actual
            last_update_time = datetime.strptime(last_update_time_str, '%Y-%m-%d %H:%M:%S')
            # Sumar 10 segundos al tiempo actual
            last_update_time += timedelta(seconds=10)
            # Actualizar la columna de hora y fecha en current_value
            # Obtener el tiempo actual
            current_time = datetime.now()
            found_topic1_row = None
            for child in tree.get_children():
                topic = tree.item(child)['values'][4]  # Obtener el valor de la columna de tópicos
                if 'topic/1' in topic:
                    found_topic1_row = child
                    break
            
            if found_topic1_row:
                # Obtener los valores actuales en la fila
                current_values = tree.item(found_topic1_row)['values']
                
                # Actualizar solo la columna de "Hora y Fecha" en la lista de valores
                current_values[1] = last_update_time_str  # Actualiza con la hora actual
                current_values[5] = ip1
                time_difference = current_time - last_update_time
            # Estado de conexion
            if time_difference.total_seconds() > 10:
                current_values[6] = "Inactivo"
                tree.item(found_topic1_row, values=current_values)  
            else:
                current_values[6] = "Activo"
                tree.item(found_topic1_row, values=current_values)  
            # TERMINAAAAA
            if x9 == "alarma":
                current_values[3] = "Activada"
                tree.tag_configure("Red.Row", background="red")
                #current_values[6] = "Activo"
                tree.item(found_topic1_row, tags=("Red.Row",), values=current_values)
                    #print(ip1)
            else:
                current_values[3] = "Desactivada"
                #current_values[6] = "Activo"
                tree.tag_configure("Normal.Row", background="white")
                tree.item(found_topic1_row, tags=("Normal.Row",),values=current_values)
            
            #print("Guardando datos en JSON...")  # Mensaje de verificación
            update_table_data()
            save_table_data_to_json()
                # Actualizar la fila en el Treeview con los nuevos valores
        elif msg.topic == 'topic/2':
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
            last_update_time_topic2 = time.strftime('%Y-%m-%d %H:%M:%S')
            found_topic2_row = None
            for child in tree.get_children():
                topic = tree.item(child)['values'][4]  # Obtener el valor de la columna de tópicos
                if 'topic/2' in topic:
                    found_topic2_row = child
                    break
            
            if found_topic2_row:
                # Obtener los valores actuales en la fila
                current_values_topic2 = tree.item(found_topic2_row)['values']
                
                # Actualizar solo la columna de "Hora y Fecha" en la lista de valores
                current_values_topic2[1] = last_update_time_topic2  # Actualiza con la hora actual
                current_values_topic2[5] = ip2
                current_values_topic2[6] = "Activo"
            if x19 == "alarma":
                    current_values_topic2[3] = "Activada"
                    # Configurar la etiqueta para aplicar el color rojo a la fila
                    tree.tag_configure("Red.Row", background="red")
    # Aplicar la etiqueta a la fila que cumple la condición
                    tree.item(found_topic2_row, tags=("Red.Row",), values=current_values_topic2)
                    #print(ip2)
            else:
                    current_values_topic2[3] = "Desactivada"
                    tree.tag_configure("Normal.Row", background="white")
                    tree.item(found_topic2_row, tags=("Normal.Row",), values=current_values_topic2)
            update_table_data()
            save_table_data_to_json()
                    #print(ip2)
                # Actualizar la fila en el Treeview con los nuevos valores
        elif msg.topic == 'topic/3':
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

        elif msg.topic == 'topic/4':
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

    for topic in topic_list:
        client.subscribe(topic)

    client.on_message = on_message
    #client.subscribe(topic)
    #client.subscribe(topic2)
    #client.subscribe(topic3)
    #client.subscribe(topic4)
    #client.on_message = on_message
def connect_and_subscribe(client: mqtt_client, topics_to_subscribe):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            for topic in topics_to_subscribe:
                client.subscribe(topic)
                print(f"Subscribed to {topic}")
        else:
            print("Failed to connect, return code %d\n", rc)

    client.on_connect = on_connect
    client.connect(broker, port)

    client.loop_start()
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


columns = ('ID', 'Hora y Fecha', 'Nombre', 'Estado de Alarma', 'Tópicos', 'IP ESP32', 'Conexión ESP32')
tree = ttk.Treeview(frame, columns=columns, show='headings')
tree.column('Hora y Fecha', width=1000)  # Establecer el ancho a 150 píxeles
#CODIGO VERF TIME
def mark_topic1_inactive():
    global topic1_active
    while True:
        time.sleep(15)  # Espera 15 segundos
        if not topic1_active:
            # Aquí colocarías el código para actualizar la tabla con el nuevo estado "Inactivo"
            print("Topic 1 marked as inactive in the table")  # Simulación de actualización de la tabla
        topic1_active = True

# Función que se ejecuta cuando llega un mensaje al topic/1
def on_message_received():
    global topic1_active
    topic1_active = True
    print("Message received for topic 1. Marking as active.")

    # Reiniciar el temporizador si se recibe un mensaje
    timer.cancel()  # Cancelar el temporizador actual
    timer.start()   # Iniciar uno nuevo

# Función que ejecuta la lógica del temporizador
def timeout():
    on_message_received()  # Marcar como activo

# Inicializar el temporizador
timer = threading.Timer(15, timeout)  # Timer inicial, 15 segundos
timer.daemon = True
timer.start()
#message_thread = threading.Thread(target=simulate_message_arrival)
#message_thread.daemon = True
#message_thread.start()

# Iniciar el hilo para marcar el topic/1 como inactivo si pasa el tiempo límite
inactive_thread = threading.Thread(target=mark_topic1_inactive)
inactive_thread.daemon = True
inactive_thread.start()
# CODIGO VIEW
def topic_already_exists(topic_to_check):
    for child in tree.get_children():
        topic = tree.item(child)['values'][4]  # Obtenemos el valor de la columna de tópicos
        if topic_to_check in topic:
            return True
    return False
def reconnect_and_subscribe():
        client.disconnect()  # Desconectar el cliente MQTT

    # Realizar la reconexión
        client.reconnect()

    # Suscribirse a los nuevos tópicos en topic_list
        connect_and_subscribe(client, topic_list)
def open_add_window():
    add_window = tk.Toplevel(root)
    add_window.title("Añadir elemento")

    label_name = tk.Label(add_window, text="Nombre")
    label_name.pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    label_topics = tk.Label(add_window, text="Selecciona hasta 5 tópicos:")
    label_topics.pack()

    topics = ['topic/1', 'topic/2', 'topic/3', 'topic/4', 'topic/5']
    selected_topics = [] #--------------

    def add_topic():
        selected_topic = topic_var.get()
        if len(selected_topics) < 5:
            if selected_topic in selected_topics:
                messagebox.showinfo("Alerta", f"El tópico '{selected_topic}' ya está en la lista.")
            elif any(topic == selected_topic for topic in selected_topics) or topic_already_exists(selected_topic):
                messagebox.showinfo("Alerta", f"El tópico '{selected_topic}' ya está en la lista.")
            else:
                selected_topics.append(selected_topic)
                update_listbox()
        else:
            messagebox.showinfo("Alerta", "Ya has seleccionado el máximo de tópicos permitidos.")
    def remove_topic():
        if selected_topic_listbox.curselection():
            index = selected_topic_listbox.curselection()[0]
        
        # Eliminar el tema de selected_topics
        removed_topic = selected_topics.pop(index)
        update_listbox()
        
        # Eliminar el tema correspondiente de topic_list si existe
        if removed_topic in topic_list:
            topic_list.remove(removed_topic)
            print(f"El tema {removed_topic} fue eliminado de topic_list")


    def update_listbox():
        selected_topic_listbox.delete(0, tk.END)
        for topic in selected_topics:
            selected_topic_listbox.insert(tk.END, topic)

    topic_var = tk.StringVar(add_window)
    topic_var.set("Seleccionar Tópico")
    topic_dropdown = tk.OptionMenu(add_window, topic_var, *topics)
    topic_dropdown.pack()

    add_topic_button = tk.Button(add_window, text="Agregar Tópico", command=add_topic)
    add_topic_button.pack()

    remove_topic_button = tk.Button(add_window, text="Eliminar Tópico", command=remove_topic)
    remove_topic_button.pack()

    selected_topic_listbox = tk.Listbox(add_window, selectmode=tk.MULTIPLE)
    selected_topic_listbox.pack()

    add_button = tk.Button(
        add_window,
        text="Añadir",
        command=lambda: add_item(add_window, entry_name.get(), selected_topics)
    )
    add_button.pack()

def update_table_data():
    global table_data
    table_data = []
    for child in tree.get_children():
        values = tree.item(child)['values']
        item_data = {
            "ID": values[0],
            "Hora y Fecha": values[1],
            "Nombre": values[2],
            "Estado de Alarma": values[3],
            "Tópicos": values[4],
            "IP ESP32": values[5],
            "Conexión ESP32": values[6]
        }
        table_data.append(item_data)
# Función para guardar los datos en un archivo JSON
def save_table_data_to_json():
    with open("table_data.json", "w") as file:
        json.dump(table_data, file)
def load_table_data_from_json():
    table_data = []
    try:
        with open("table_data.json", "r") as file:
            table_data = json.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo 'table_data.json'.")
    return table_data
table_data = load_table_data_from_json()
print(table_data)

#PRUEBA GUARDADO*******************************************
def add_item(window, name, topics):
    global last_item_id  # Indicar que se utilizará la variable global

    # Verificar si el "Tópico 1" ya existe en la tabla
    if "Tópico 1" in topics and topic_already_exists("Tópico 1"):
        messagebox.showinfo("Alerta", "El 'Tópico 1' ya existe en la tabla.")
        window.destroy()
        return

    # Incrementar el ID
    last_item_id += 1

    # Obtener la fecha y hora actual (aquí deberías usar la función para obtener la fecha y hora actual)
    timestamp = "Fecha y Hora" 
    tree.insert("", "end", values=[last_item_id, timestamp, name, "", ', '.join(topics), "", "", ""])
    print("topics recibidos:", topics)
    print("topic_list ahora ", topic_list)
    #AÑADIR EL IF DE FECHA Y HORA 
    for topic in topics:
        if topic not in topic_list:
            topic_list.append(topic)
            print("topic_list modificada ", topic_list)
            #print("topic", topic_list1)
        connect_and_subscribe(client, topic_list) #---comentar----**************************
        update_table_data() #CODIGO MODIF
    save_table_data_to_json()
    window.destroy()
def delete_item():
    if not tree.selection():
        messagebox.showinfo("Alerta", "No has seleccionado ningún elemento.")
        return

    selected_item = tree.selection()[0]
    topic_to_remove = tree.item(selected_item)['values'][4]  # Obtener el tópico asociado a la fila

    # Eliminar la fila del Treeview
    tree.delete(selected_item)

    # Eliminar el tópico específico de la lista topic_list
    if topic_to_remove in topic_list:
        topic_list.remove(topic_to_remove)
        print("Tópico eliminado:", topic_to_remove)
    else:
        print("El tópico no está en la lista:", topic_to_remove)
    
    update_table_data()
    save_table_data_to_json()

def open_edit_window():
    global edit_window

    if not tree.selection():
        messagebox.showinfo("Alerta", "No has seleccionado ningún elemento para editar.")
        return

    edit_window = tk.Toplevel(root)
    edit_window.title("Editar elemento")

    selected_item = tree.selection()[0]
    item_values = tree.item(selected_item)['values']

    label_name = tk.Label(edit_window, text="Nombre")
    label_name.pack()
    entry_name = tk.Entry(edit_window)
    entry_name.pack()
    entry_name.insert(0, item_values[2])

    label_topics = tk.Label(edit_window, text="Selecciona hasta 5 tópicos:")
    label_topics.pack()

    topics = ['topic/1', 'topic/2', 'topic/3', 'topic/4', 'topic/5']
    selected_topics = []
    def add_topic():
        selected_topic = topic_var.get()
        if len(selected_topics) < 5:
            if selected_topic in selected_topics:
                messagebox.showinfo("Alerta", f"El tópico '{selected_topic}' ya está en la lista.")
            elif any(topic == selected_topic for topic in selected_topics) or topic_already_exists(selected_topic):
                messagebox.showinfo("Alerta", f"El tópico '{selected_topic}' ya está en la lista.")
            else:
                selected_topics.append(selected_topic)
                update_listbox()
        else:
            messagebox.showinfo("Alerta", "Ya has seleccionado el máximo de tópicos permitidos.")
    def remove_topic():
        if selected_topic_listbox.curselection():
            index = selected_topic_listbox.curselection()[0]
            selected_topics.pop(index)
            update_listbox()
    def update_listbox():
        selected_topic_listbox.delete(0, tk.END)
        for topic in selected_topics:
            selected_topic_listbox.insert(tk.END, topic)

    topic_var = tk.StringVar(edit_window)
    topic_var.set("Seleccionar Tópico")
    topic_dropdown = tk.OptionMenu(edit_window, topic_var, *topics)
    topic_dropdown.pack()
    add_topic_button = tk.Button(edit_window, text="Agregar Tópico", command=add_topic)
    add_topic_button.pack()
    remove_topic_button = tk.Button(edit_window, text="Eliminar Tópico", command=remove_topic)
    remove_topic_button.pack()
    selected_topic_listbox = tk.Listbox(edit_window, selectmode=tk.MULTIPLE)
    selected_topic_listbox.pack()

    def on_select(event):
        widget = event.widget
        selected = widget.curselection()
        selected_topics.clear()
        for index in selected:
            selected_topics.append(widget.get(index))
        update_listbox()

    selected_topic_listbox.bind("<<ListboxSelect>>", on_select)
        
    def save_changes():
        new_name = entry_name.get()
        new_topics = selected_topics
    
    # Obtener los valores actuales en el elemento seleccionado
        current_values = tree.item(selected_item)['values']
    
    # Crear una lista con los valores actuales de la fila
        updated_values = list(current_values)
        updated_values[2] = new_name
    # Modificar solo la columna de tópicos
        updated_values[4] = ', '.join(new_topics)
    
        tree.item(selected_item, values=updated_values)  # Actualizar solo la fila del Treeview
        #2323
        for topic in new_topics:
            if topic not in topic_list:
                topic_list.append(topic)
        reconnect_and_subscribe()
        update_table_data()
        save_table_data_to_json()
        edit_window.destroy()  # Cerrar la ventana de edición después de guardar los cambios


    save_button = tk.Button(
        edit_window,
        text="Guardar cambios",
        command=save_changes
    )
    save_button.pack()


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

primer_click = True
def abrir_programa(topic):
    global primer_click
    
    if not primer_click:
        # Cargar los datos desde el archivo JSON
        try:
            with open("table_data.json", "r") as file:
                table_data = json.load(file)
                cargar_datos_en_tabla(table_data)
                # ...
        except FileNotFoundError:
            print("Archivo JSON no encontrado.")
        
        # Reconnect and subscribe
        reconnect_and_subscribe()  # Esta función debe reconectar al broker y suscribirse a los tópicos nuevamente
        
        # Lógica para abrir el subprograma (reemplaza esto con tu lógica real)
        if topic == 'topic/1':
            subprocess.Popen(["python", "main.py"])
        elif topic == 'topic/2':
            subprocess.Popen(["python", "main1.py"])
        elif topic == 'topic/3':
            subprocess.Popen(["python", "main.py"])
        elif topic == 'topic/4':
            subprocess.Popen(["python", "main.py"])
        
        root.destroy()
    else:
        primer_click = False

def cargar_datos_en_tabla(table_data):
    for item in table_data:
        # Suponiendo que 'tree' es tu objeto Treeview y 'item' es un diccionario con los datos
        tree.insert("", "end", values=(
            item["ID"],
            item["Hora y Fecha"],
            item["Nombre"],
            item["Estado de Alarma"],
            item["Tópicos"],
            item["IP ESP32"],
            item["Conexión ESP32"]
        ))
        print("Datos insertados:", item)


def on_tree_click(event):
    item = tree.item(tree.focus())
    topic = item['values'][4]  # Supongamos que el topic está en la quinta columna
    print(topic)
    abrir_programa(topic)


#prueba
table_data = load_table_data_from_json()  # Cargar los datos del archivo JSON

# Insertar datos en el Treeview
cargar_datos_en_tabla(table_data)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(side="left", fill="y")

tree_scroll = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree_scroll.pack(side="right", fill="y")

tree.configure(yscrollcommand=tree_scroll.set)

tree.bind("<ButtonRelease-1>", on_tree_click)

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


# ------------------------
## Iniciar el hilo para la función de ping
ping_thread = threading.Thread(target=check_connection, args=("192.168.3.38",))
ping_thread.start()

client = connect_mqtt()
subscribe(client)


#root.mainloop()

if __name__ == "__main__":
    #main()
    while(1):
        client.loop_start()
        root.mainloop()

        client.loop_stop()