# -*- coding: utf-8 -*-
 
# primer codigo de la clase 

import numpy as np 

 
x= "hello"
y= "wold"
 

print(x +' '+ y)

# se pueden sumar palabras con las formulas, y para agregar un 
#espacio ponemos + dos tildes separadas 

#python ya tiene las formulas como tal, el print es importante 
#ponerlo para que pueda ejecutarse al momento de correrlo

a=2
b=4
formula=((a**2)+(2*(a*b))+(b**2))
print (formula)

#temenos que escribir la formula = anotar la formula con las 
#operaciones aritmeticas 
#luego print y ponemos la formula para no tener que escribirla toda}
#otra vez.

x=36

print("el resultado es " + str(x))

#para cambiar una variable a texto ponemos str y entre parentesis 
#la variable que queremos que diga.


#EJERCICIO NUMERO 1  ESCRIBIR Y CORRER LAS FORMULAS

#formula area de una esfera
#primero definimos las variables, despues escribirmos la formula
#y con print entre parentesis escribirmos la formula para que 
#cuando lo corramos nos arroje el resultado.

r=2
PI=3.14 
formula= 4*PI*(r**2)

print(formula)

#formula general o chicharronera

a=float(input(1))
b=float(input(2))
c=float(input(3))

 
formula_1= -b+(((b**2)-(4*a*b))**0.5)/(2*a)
formula_2=-b-(((b**2)-(4*a*b))**0.5)/(2*a)

print(formula_1)
print (formula_2)

















