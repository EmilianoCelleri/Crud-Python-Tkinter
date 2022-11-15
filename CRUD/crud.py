from tkinter import *
from tkinter import messagebox
from asyncio.windows_events import NULL
import sqlite3 as sq3

'''
================
PARTE FUNCIONAL
================
'''
# MENU
# ---------------- BBDD ------------------
#Conectar con la BBDD
def conectar():
  global con
  global cur
  con = sq3.connect('mi_db.db')
  cur = con.cursor()
  messagebox.showinfo("STATUS", "Conectado a la BBDD OK")
#Salir
def salir():
  resp = messagebox.askquestion("CONFIRME", "Desea salir de la aplicacion?")
  if resp == 'yes':
    #con.close()
    raiz.destroy()

#Limpiar formulario

def limpiar():
  legajo.set("")
  alumno.set("")
  email.set("")
  calificacion.set("")
  escuela.set("Seleccione")
  localidad.set("")
  provincia.set("")
  legajo_input.config(state="normal")

#------------------ Acerca de...
#Licencia
def mostrar_licencia():
  msg = '''
    Sistema CRUD en Python
    Copyright (C) 2022 - Celleri Emiliano
    Email: emiliano.celleri@gmail.com\n=======================================
    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public 
    License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any 
    later version.
    This program is distributed in the hope that it will be 
    useful, but WITHOUT ANY WARRANTY; without even the 
    implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE.  See the GNU General Public License 
    for more details.
    You should have received a copy of the GNU General Public 
    License along with this program.  
  '''

  messagebox.showinfo("Licencia", msg)


def mostrar_acercade():
  messagebox.showinfo("Acerca de...", "Creado por Celleri, Emiliano Julian\n para Codo a Codo \n Noviembre 2022 \n Email: emiliano.celleri@gmail.com")


#------------------ FUNCIONES CRUD


#CREAR
def crear():
  id_escuela = int(buscar_escuelas(True)[0])
  datos = id_escuela, legajo.get(), alumno.get(), calificacion.get(), email.get()
  cur.execute("INSERT INTO alumnos (id_escuela,legajo,nombre, nota, email) VALUES (?,?,?,?,?)", datos)
  con.commit()
  messagebox.showinfo("STATUS", "Registro Agregado")
  limpiar()

#BUSCAR
def buscar_legajo():

  query_buscar ='''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota, alumnos.email,
  escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos INNER JOIN escuelas
  ON alumnos.id_escuela = escuelas._id WHERE alumnos.legajo= 
  '''
  cur.execute(query_buscar + legajo.get())
  resultado = cur.fetchall()

  if resultado == []:
    messagebox.showerror('ERROR', 'Ese numero de legajo no existe')
    legajo.set('')
  else:
    for campo in resultado:
      legajo.set(campo[0])
      alumno.set(campo[1])
      calificacion.set(campo[2])
      email.set(campo[3])
      escuela.set(campo[4])
      localidad.set(campo[5])
      provincia.set(campo[6])
      legajo_input.config(state='disabled')


#ACTUALIZAR
def actualizar():
  id_escuela = int(buscar_escuelas(True)[0])
  datos = id_escuela, alumno.get(), calificacion.get(), email.get()
  cur.execute("UPDATE alumnos SET id_escuela=?, nombre=?, nota=?, email=? WHERE legajo="+legajo.get(), datos)
  con.commit()
  messagebox.showinfo("STATUS", "Registro actualizado")
  limpiar()

#BORRAR
def borrar():
  resp = messagebox.askquestion("BORRAR?", "Desea eliminar el registro?")
  if resp == 'yes':
    cur.execute("DELETE FROM alumnos WHERE legajo="+legajo.get())
    con.commit()
    messagebox.showinfo("STATUS", "El registro fue eliminado")
    limpiar()




#------------------ FUNCIONES GENERALES

def buscar_escuelas(actualiza):
  con = sq3.connect('mi_db.db')
  cur = con.cursor()
  if actualiza:
    cur.execute('SELECT _id, localidad, provincia FROM escuelas WHERE nombre = ?', (escuela.get(),))
  else:
    cur.execute('SELECT nombre FROM escuelas')
  
  resultado = cur.fetchall()
  retorno = []
  for e in resultado:
    if actualiza:
      localidad.set(e[1])
      provincia.set(e[2])

    esc=e[0]
    retorno.append(esc)
  con.close()
  return retorno


#Listado alumnos
def listar():
  
  class Table():
    
    def __init__(self, raiz2):
      nombre_cols = ['Legajo', 'Alumno', 'Calificacion', 'Email', 'Escuela', 'Localidad', 'Provincia']
      for i in range (cant_cols):
        self.e = Entry(frameppal)
        self.e.config(bg='black', fg='white')
        self.e.grid(row=0, column=i)
        self.e.insert(END, nombre_cols[i])

      for fila in range(cant_filas):
        for col in range(cant_cols):
          self.e = Entry(frameppal)
          self.e.grid(row=fila+1, column=col)
          self.e.insert(END, resultado[fila][col])
          self.e.config(state='readonly')

  
  #Estructura ventana
  raiz2 = Tk()
  raiz2.title('Listado de alumnos')
  frameppal = Frame(raiz2)
  frameppal.pack(fill='both')
  framecerrar = Frame(raiz2)
  framecerrar.pack(fill='both')
  boton_cerrar = Button(framecerrar, text='Cerrar', command=raiz2.destroy)
  boton_cerrar.config(bg=color_fondo_boton, fg=color_texto_boton)
  boton_cerrar.pack(fill='both')

  #Obtener los datos de listar

  con = sq3.connect('mi_db.db')
  cur = con.cursor()

  query1 = '''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota, alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id'''
  cur.execute(query1)
  resultado= cur.fetchall()
  cant_filas = len(resultado) # Cantidad de registros para saber cuantas filas
  cant_cols = len(resultado[0]) #cantidad de columnas

  tabla = Table(frameppal)
  #Cierre conexion y mantener abierta la ventana
  con.close()
  raiz2.mainloop()

buscar_escuelas(False)


'''
================
INTERFAZ GRAFICA
================
'''


#Espaciados

esp_h = 10
esp_v = 10

#Frame botones

color_fondo_framebotones = 'plum'
color_fondo_boton = 'black'
color_texto_boton = color_fondo_framebotones

#Frame campos

color_fondo_framecampos = 'slate blue'
color_letra_framecampos = 'black'



#RAIZ
raiz = Tk()
raiz.title('Python CRUD')

#MENU

barramenu = Menu(raiz)
raiz.config(menu=barramenu)

#Boton 1

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label = 'Conectar', command=conectar)
bbddmenu.add_command(label='Listado de alumnos', command=listar)
bbddmenu.add_command(label = 'Salir', command=salir)

#Boton 2: Limpiar formulario

limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label='Limpiar el formulario', command=limpiar)

#Boton 3: Licencia y acerca de

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia', command=mostrar_licencia)
ayudamenu.add_command(label='Acerca de...', command=mostrar_acercade)

#Frame campos

framecampos = Frame(raiz)
framecampos.config(bg=color_fondo_framecampos)
framecampos.pack(fill='both')

legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

#Campos entry

legajo_input = Entry(framecampos, textvariable=legajo, width=35)
legajo_input.grid(row=0, column=1, padx=10,pady=10)

alumno_input = Entry(framecampos, textvariable=alumno,width=35)
alumno_input.grid(row=1, column=1, padx=10,pady=10)

email_input = Entry(framecampos, textvariable=email, width=35)
email_input.grid(row=2, column=1, padx=10,pady=10)

calificacion_input = Entry(framecampos, textvariable=calificacion, width=35)
calificacion_input.grid(row=3, column=1, padx=10,pady=10)

lista_escuelas = buscar_escuelas(False)
escuela.set('Seleccione')
escuela_option = OptionMenu(framecampos, escuela, *lista_escuelas)
escuela_option.grid(row=4, column=1, padx=10,pady=10, sticky=W+E)
#escuela_input = Entry(framecampos, textvariable=escuela)
#escuela_input.grid(row=4, column=1, padx=10,pady=10)

localidad_input = Entry(framecampos, textvariable=localidad, width=35)
localidad_input.grid(row=5, column=1, padx=10,pady=10)
localidad_input.config(state='readonly')

provincia_input = Entry(framecampos, textvariable=provincia, width=35)
provincia_input.grid(row=6, column=1, padx=10,pady=10)
provincia_input.config(state='readonly')

#Labels

'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''

#Funcion para configurar los labels

def config_label(mi_label, fila):
    espaciado_labels = {'column':0, 'sticky': 'e', 'padx': esp_h, 'pady': esp_v}
    color_labels = {'bg': color_fondo_framecampos, 'fg': color_letra_framecampos}
    mi_label.grid(row=fila, **espaciado_labels)
    mi_label.config(**color_labels)




legajo_label = Label(framecampos, text='Legajo:')
config_label(legajo_label,0)
#legajo_label.grid(row=0,column=0,sticky='e', padx=10, pady=10)

alumno_label = Label(framecampos, text='Alumno:')
config_label(alumno_label,1)
#alumno_label.grid(row=1,column=0,sticky='e', padx=10, pady=10)

email_label = Label(framecampos, text='Email:')
config_label(email_label,2)
#email_label.grid(row=2,column=0,sticky='e', padx=10, pady=10)

calificacion_label = Label(framecampos, text='Calificacion:')
config_label(calificacion_label,3)
#calificacion_label.grid(row=3,column=0,sticky='e', padx=10, pady=10)

escuela_label = Label(framecampos, text='Escuela:')
config_label(escuela_label,4)
#escuela_label.grid(row=4,column=0,sticky='e', padx=10, pady=10)

localidad_label = Label(framecampos, text='Localidad:')
config_label(localidad_label,5)
#localidad_label.grid(row=5,column=0,sticky='e', padx=10, pady=10)

provincia_label = Label(framecampos, text='Provincia:')
config_label(provincia_label,6)
#provincia_label.grid(row=6,column=0,sticky='e', padx=10, pady=10)

#Botonera CRUD

framebotones = Frame(raiz)
framebotones.config(bg=color_fondo_framebotones)
framebotones.pack(fill='both')

boton_crear = Button(framebotones, text='Crear', command=crear)
boton_crear.grid(row=0, column=0,padx=10,pady=10, ipadx=7)
boton_crear.config(bg=color_fondo_boton,fg=color_texto_boton)

boton_leer = Button(framebotones, text='Leer', command=buscar_legajo)
boton_leer.grid(row=0, column=1,padx=10,pady=10, ipadx=7)
boton_leer.config(bg=color_fondo_boton,fg=color_texto_boton)


boton_actualizar = Button(framebotones, text='Actualizar', command=actualizar)
boton_actualizar.grid(row=0, column=2,padx=10,pady=10, ipadx=7)
boton_actualizar.config(bg=color_fondo_boton,fg=color_texto_boton)

boton_borrar = Button(framebotones, text='Borrar', command=borrar)
boton_borrar.grid(row=0, column=3,padx=10,pady=10, ipadx=7)
boton_borrar.config(bg=color_fondo_boton,fg=color_texto_boton)


#Frame pie

framecopy = Frame(raiz)
framecopy.config(bg='black')
framecopy.pack(fill='both')

copylabel = Label(framecopy, text='(2022) por Celleri Emiliano para CaC - Big Data')
copylabel.pack(fill='both')
#copylabel.grid(padx=10, pady=10)
copylabel.config(bg='black', fg='white')
'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''




barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Limpiar', menu=limpiarmenu)
barramenu.add_cascade(label='Acerca de...', menu=ayudamenu)






raiz.mainloop()