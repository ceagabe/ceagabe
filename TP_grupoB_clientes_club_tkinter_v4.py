 
    #***** GRUPO B ************
    # Maria Silvia Ariño
	# Sofia Gabriela Bravo
	# Ariadna Prinsich
	# Laura Arias 
	# Ariel M. Torres 
	# Gabriel J. M. Benedetti
    #**************************
from os import system
system("cls")

import tkinter as tk
from tkinter import ttk
import sqlite3

clientes = []
deportes = []

def decorar():
    print("-"* 50)

def imprimir(cliente):
        print("-" *50)
        print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
        print(f"DNI: {cliente['dni']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Edad: {cliente['edad']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Deporte: {cliente['deporte']}")
        print(f"Fecha de alta: {cliente['fecha']}")
        print(f"Certificado médico: {cliente['certificado']}")
        print("-" *50)

def agregar_cliente(): 
        nombre = nombre1.get()
        apellido = apellido1.get()
        dni =int(dni1.get())
        telefono =int(telefono1.get())
        edad=int(edad1.get())
        direccion =direccion1.get()
        deporte = deporte1.get()
        fecha = fecha1.get()
        certificado = certificado1.get()

        cliente = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "telefono": telefono,
            "edad": edad,
            "direccion": direccion,
            "deporte": deporte,
            "fecha": fecha,
            "certificado": certificado,
            "activo": True
        }

        clientes.append(cliente)

        nombre1.delete(0, tk.END)
        apellido1.delete(0, tk.END)
        dni1.delete(0, tk.END)
        telefono1.delete(0, tk.END)
        edad1.delete(0, tk.END)
        direccion1.delete(0, tk.END)
        deporte1.delete(0, tk.END)
        fecha1.delete(0, tk.END)
        certificado1.delete(0, tk.END)
         
        print("Cliente agregado: ") 
        imprimir(cliente)
        
        #Base de Datos para los socios
        conexion= sqlite3.connect("BD_clientes.db")
        cursor= conexion.cursor()  #puntero a la base de datos
        cursor.execute("CREATE TABLE IF NOT EXISTs clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50),apellido VARCHAR(50), dni INTEGER, telefono INTEGER, edad INTEGER,direccion VARCHAR(20),deporte VARCHAR(20),ingreso VARCHAR(20),certificado VARCHAR(20))")
        cursor.execute("insert into clientes (nombre, apellido, dni, telefono, edad, direccion, deporte, ingreso, certificado ) values (?,?,?,?,?,?,?,?,?)",(nombre, apellido, dni, telefono, edad, direccion, deporte,fecha, certificado ))
        cursor.execute("select nombre, apellido, dni,telefono, edad, direccion, ingreso,certificado from clientes" )

        clientes.append(cliente)
 
        conexion.commit()
        conexion.close()
        
def borrar_cliente():
    dni =int(dni1.get())
    for cliente in clientes:
        if cliente["dni"] == dni:
            print("Cliente a borrar: ")
            imprimir(cliente)  
            clientes.remove(cliente)
            print("Borrar Cliente", "Cliente eliminado correctamente.")
            conexion= sqlite3.connect("BD_clientes.db")
            cursor= conexion.cursor()  #puntero a la base de datos  
            cursor.execute("delete from clientes where dni= ?",(dni,))  #Borra en la Base de Datos
            conexion.commit()
            conexion.close()
        
            return
                   
       
        
    print("Borrar Cliente", "No se encontró un cliente con ese DNI.")

def listar_clientes():
    for cliente in clientes:
       print("Lista de Clientes: ")
       imprimir(cliente)    


def listar_clientes_activos():
    for cliente in clientes:
        if cliente["activo"]:
            decorar()
            print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
            print(f"DNI: {cliente['dni']}")
            print(f"Edad: {cliente['edad']}")
            print(f"Deporte: {cliente['deporte']}")
            print(f"Fecha de alta: {cliente['fecha']}")
            print(f"Certificado médico: {cliente['certificado']}")
            decorar()
            
def listar_deportes():
    deportes = {}   #utilizo un dicc para guardar cantidad y deportes
    for cliente in clientes:
        deporte = cliente["deporte"]
        if deporte in deportes:
            deportes[deporte] += 1
        else:
            deportes[deporte] = 1
    for deporte, cantidad in deportes.items():
        decorar()
        print(f"{deporte}: {cantidad} clientes")
        decorar() 
        

def consultar_cliente():
    dni =int(dni1.get())
    for cliente in clientes:
        if cliente["dni"]==dni:
            print(f"Consulta de Cliente: {dni}")
            imprimir(cliente)
        return    
    print("No se encontro el cliente")
    return

def modificar_deporte():  #mofifique despues de la entrega  (falta el boton...)
    dni =int(dni1.get())
    for cliente in clientes:
        if cliente["dni"]==dni:
            imprimir(cliente)
            cliente["deporte1"] = deporte1.get() 
            cliente["deporte"]= ""
            cliente["deporte"]=cliente["deporte"] + cliente["deporte1"] 
            print(f"Deporte: {cliente['deporte']}")
            decorar()
            return
        else: 
            print("Debe ingresar DNI") 
        
    print("No se encontro el cliente")
    return

def modificar_cliente():  #mofifique despues de la entrega
    dni =int(dni1.get())
    for cliente in clientes:
        if cliente["dni"]==dni:
            imprimir(cliente)
            cliente={}

            nombre = nombre1.get()
            apellido = apellido1.get()
            dni =int(dni1.get())
            telefono =int(telefono1.get())
            edad=int(edad1.get())
            direccion =direccion1.get()
            deporte = deporte1.get()
            fecha = fecha1.get()
            certificado = certificado1.get()

            cliente = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "telefono": telefono,
            "edad": edad,
            "direccion": direccion,
            "deporte": deporte,
            "fecha": fecha,
            "certificado": certificado,
            "activo": True
            }

            clientes.replace(cliente)
            return
        else: 
            print("Debe ingresar DNI") 
        
    print("No se encontro el cliente")
    return

def cantidad_clientes():
    cantidad = 0
    for cliente in clientes:
       cantidad= cantidad + 1 
    decorar()        
    print(f"Cantidad de clientes: {cantidad} ")
    decorar()
    return

def cliente_mas_deportes():
    cliente_mas_deportes=clientes[0]
    for cliente in clientes:
        if len(cliente["deporte"]) >= len(cliente_mas_deportes["deporte"]):
         cliente_mas_deportes=cliente
        else:
         cliente
        print("Cliente con mas deportes: ")
        #imprimir(cliente)
        imprimir(cliente_mas_deportes)
    return

def listar_clientes_certificado():
    for cliente in clientes:
        if cliente["certificado"]== "si":
          print("Lista de clientes con certificado")
          decorar()
          print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
          decorar()
        else:
          print("Lista de clientes sin certificado")
          decorar()
          print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
          decorar()
    return        


ventana=tk.Tk()

ventana.title("Ingresar los siguientes datos :D")
ventana.config(bg="light green", width=400, height=600, relief="groove", bd=10)
titulo = tk.Label(ventana, text="Bienvenidos al Club Codo a Codo! Ingresar Socio: ", bg="white", fg="black", font=("TimesNewRoman", 10, "bold", "italic"))
titulo.place(x=30, y=10)

#Entradas
nombre = tk.Label(ventana, text="Nombre: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
nombre.place(x=60, y=40)
nombre1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
nombre1.place(x=200, y=40)
apellido = tk.Label(ventana, text="Apellido: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
apellido.place(x=60, y=60)
apellido1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
apellido1.place(x=200, y=60)
dni = tk.Label(ventana, text="DNI: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
dni.place(x=60, y=80)
dni1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
dni1.place(x=200, y=80)
telefono = tk.Label(ventana, text="Telefono: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
telefono.place(x=60, y=100)
telefono1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
telefono1.place(x=200, y=100)
edad = tk.Label(ventana, text="Edad: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
edad.place(x=60, y=120)
edad1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
edad1.place(x=200, y=120)
direccion = tk.Label(ventana, text="Direccion: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
direccion.place(x=60, y=140)
direccion1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
direccion1.place(x=200, y=140)
deportes = tk.Label(ventana, text="Deportes: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
deportes.place(x=60, y=160)
deporte1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
deporte1.place(x=200, y=160)
fecha = tk.Label(ventana, text="Fecha de alta: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
fecha.place(x=60, y=180)
fecha1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
fecha1.place(x=200, y=180)
certificado = tk.Label(ventana, text="Certificado médico: ", bg="AntiqueWhite2", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
certificado.place(x=60, y=200)
certificado1 = tk.Entry(ventana, bg="white", fg="black", font=("TimesNewRoman", 8))
certificado1.place(x=200, y=200)


# cuadro.get() # Obtiene el texto del cuadro de texto lo necesitamos en el boton
#Botones para las opciones!
boton = ttk.Button( text="Agregar Cliente", command=agregar_cliente)  #uso la funcion ttk
boton.place(x=20, y=240)
boton = tk.Button(ventana, text="Borrar Cliente (DNI)", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=borrar_cliente)
boton.place(x=40, y=270)
boton = tk.Button(ventana, text="Listar Clientes", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=listar_clientes)
boton.place(x=60, y=300)
boton = tk.Button(ventana, text="Listar Clientes Activos", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=listar_clientes_activos)
boton.place(x=80, y=330)
boton = tk.Button(ventana, text="Listar deportes", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=listar_deportes)
boton.place(x=100, y=360)
boton = tk.Button(ventana, text="Consultar cliente (DNI)", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=consultar_cliente)
boton.place(x=120, y=390)
boton = tk.Button(ventana, text="Modificar cliente (DNI)", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=modificar_cliente)
boton.place(x=140, y=420)
boton = tk.Button(ventana, text="Cantidad de clientes ", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=cantidad_clientes)
boton.place(x=160, y=450)
boton = tk.Button(ventana, text="Cliente con mas deportes ", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=cliente_mas_deportes)
boton.place(x=180, y=480)
boton = tk.Button(ventana, text="Clientes con/sin certificado ", fg="black", font=("TimesNewRoman", 8, "bold", "italic"), command=listar_clientes_certificado)
boton.place(x=200, y=510)

titulo = tk.Label(ventana, text="Copyright © 2023, Grupo B", bg="white", fg="black", font=("TimesNewRoman", 8, "bold", "italic"))
titulo.place(x=20, y=550)

ventana.mainloop()


      