import con

def create_bussines(nombre_empresa):
    try:
        data = con.conexion.cursor()
        data.execute(f" create database {nombre_empresa};")
        print (f"base de datos creada con el nombre {nombre_empresa}")
        data.execute(f"use {nombre_empresa};")
        data.execute(f"CREATE table {nombre_empresa} (id_empresa int primary key auto_increment, nombre varchar (100), rnc varchar (50), provincia varchar (100), direccion varchar (300), telefono varchar (50), correo varchar (50), encargado varchar (100), logo varchar (200), fecha_registro timestamp);")
        data.execute(f"CREATE table users (id_user int primary key auto_increment, nombre varchar (100), password varchar (50), rol varchar (30));")
        print ("Tablas de registro de la empresa creada")
    except:
        print ("Error")


def registrar(nombre, rnc, direccion, telefono, correo, encargado):
    try:
        data = con.conexion.cursor()
        data.execute(f"use {nombre}")
        data.execute(f"INSERT INTO `{nombre}` (`id_empresa`, `nombre`, `rnc`,`provincia`, `direccion`, `telefono`, `correo`, `encargado`) VALUES (NULL, '{nombre}', '{rnc}', '{provincia}', '{direccion}', '{telefono}', '{correo}', '{encargado}');")
        con.conexion.commit()
        print('registo de la empresa')
    except ():
        print("no funciono la insert")


def create_user(db, nombre, password):
    try:
        data = con.conexion.cursor()
        data.execute(f"use {db}")
        data.execute(f"INSERT INTO `users` (`id_user`, `nombre`, `password`, `rol`) VALUES (NULL, '{nombre}', '{password}', 'administrador');")
        con.conexion.commit()
    except ():
        print("no funciono la insert")

print (create_bussines('SoftFlesh'))
print(registrar('SoftFlesh','RDF22222152','Santo Domingo', 'Calle SAntiago Rodriguez', '809-536-4833', 'Freddypimpns@gmail.com', 'Freddy Pimpns'))
print(create_user('SoftFlesh','Freddy','Freddy0770'))
