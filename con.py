import pymysql

try:
    conexion = pymysql.connect("localhost","root","Freddy0770")
    print ("conexion exitosa")
except:
    print ("no logro conectar")




