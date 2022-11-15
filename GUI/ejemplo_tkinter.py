from tkinter import *


'''
================
INTERFAZ GRAFICA
================
'''

#RAIZ
raiz = Tk()
raiz.title('Python CRUD')

#MENU

barramenu = Menu(raiz)
raiz.config(menu=barramenu)

#Boton 1

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label = 'Conectar')
bbddmenu.add_command(label = 'Salir')

#Boton 2: Limpiar formulario

limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label='Limpiar el formulario')

#Boton 3: Licencia y acerca de

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de...')

#Frame campos

framecampos = Frame(raiz)
framecampos.pack()

legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

#Campos entry

legajo_input = Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=1, padx=10,pady=10)

alumno_input = Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=1, column=1, padx=10,pady=10)

email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=1, padx=10,pady=10)

calificacion_input = Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=3, column=1, padx=10,pady=10)

escuela_input = Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=4, column=1, padx=10,pady=10)

localidad_input = Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=5, column=1, padx=10,pady=10)

provincia_input = Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=6, column=1, padx=10,pady=10)

#Labels

'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''

legajo_label = Label(framecampos, text='Legajo:')
legajo_label.grid(row=0,column=0,sticky='e', padx=10, pady=10)

alumno_label = Label(framecampos, text='Alumno:')
alumno_label.grid(row=1,column=0,sticky='e', padx=10, pady=10)

email_label = Label(framecampos, text='Email:')
email_label.grid(row=2,column=0,sticky='e', padx=10, pady=10)

calificacion_label = Label(framecampos, text='Calificacion:')
calificacion_label.grid(row=3,column=0,sticky='e', padx=10, pady=10)

escuela_label = Label(framecampos, text='Escuela:')
escuela_label.grid(row=4,column=0,sticky='e', padx=10, pady=10)

localidad_label = Label(framecampos, text='Localidad:')
localidad_label.grid(row=5,column=0,sticky='e', padx=10, pady=10)

provincia_label = Label(framecampos, text='Provincia:')
provincia_label.grid(row=6,column=0,sticky='e', padx=10, pady=10)

#Botonera CRUD

framebotones = Frame(raiz)
framebotones.pack()

boton_crear = Button(framebotones, text='Crear')
boton_crear.grid(row=0, column=0,padx=10,pady=10)

boton_leer = Button(framebotones, text='Leer')
boton_leer.grid(row=0, column=1,padx=10,pady=10)

boton_actualizar = Button(framebotones, text='Actualizar')
boton_actualizar.grid(row=0, column=2,padx=10,pady=10)

boton_borrar = Button(framebotones, text='Borrar')
boton_borrar.grid(row=0, column=3,padx=10,pady=10)

#Frame pie

framecopy = Frame(raiz)
framecopy.pack()

copylabel = Label(framecopy, text='(2022) por Celleri, Emiliano para CaC')
copylabel.grid(padx=10, pady=10)

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
