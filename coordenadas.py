from atan2 import*
#encoding: UTF-8
#Autor: Blanca Flor Caldern Vzquez
#Actividad 1:Tarea_02
#Mis datos  
x= int(input("dame valor x"))
y= int(input("dame valor y"))
radio=(y**2+x**2)**(1/2)
angulo= atan2(y/x)
print (angulo,radio)