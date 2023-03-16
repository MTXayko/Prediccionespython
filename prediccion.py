#1
def number_of_food_groups():            #Se define una funcion
    return 5                            #Se retorna 5
print(number_of_food_groups())          #Se imprime la funcion

"""
Se imprimira: 5
"""
#2
def number_of_military_branches():      #Se define una funcion    
    return 5      #Se retorna 5                                                                       
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())  #Se imprime la suma de las dos funciones (una funcion no existe)
"""
Se imprimira: Error, ya que la funcion (number_of_days_in_a_week_silicon_or_triangle_sides) no fue definida anteriormente
"""

#3
def number_of_books_on_hold():      #Se define una funcion
    return 5                        #Se retorna 5
    return 10                       #Se retorna 10
    print(number_of_books_on_hold())    #Se imprime la funcion
"""
Se imprimira: 15, (Se imprimia 5)
"""

#4
def number_of_fingers():            #Se define una funcion
    return 5                        #Se retorna 5
    print(10)                           #Se imprime 10
print(number_of_fingers())          #Se imprime la funcion
"""
Se imprimira: 10
"""

#5
def number_of_great_lakes():        #Se define una funcion
    print(5)                        #Se imprimen 5
x = number_of_great_lakes()         #Se asigna que x es igual a la funcion definada
print(x)                            #Se imprime x
"""
Se imprimira: 5, 5  (Se imprimia 5, None)
"""

#6
def add(b,c):                       #Se define la funcion con un elementos
    print(b+c)                      #Se imprime la suma de los elementos
    print(add(1,2) + add(2,3))      #Se imprime la suma de dos elementos
"""
Saldra Error, ya que los elementos que se sumaran, no estaban definidos anteriormente, y tampoco se definio (b,c),(b+c)
"""

#7
def concatenate(b,c):               #Se define la funcion con elementos
    return str(b)+str(c)            #Se retorna la suma de los variables b y c
print(concatenate(2,5))         #Se imprime la funcion junto a los elementos
"""
Se imprimira: 25 
"""

#8
def number_of_oceans_or_fingers_or_continents():        #Se define la funcion
    b = 100                                             #Se define que b es igual a 100
    print(b)                                            #Se imprime b
    if b < 10:                                          #Se define que b es menor que 10
        return 5                                        #Se retorna 5
    else:                                               #Se define else
        return 10                                       #Se retorna 10
    return 7                                            #Se retorna 7
print(number_of_oceans_or_fingers_or_continents())      #Se imprime la funcion
"""
Se imprimira: 100, 5  (Se imprimia 100, 10)
"""

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):                            #Se define la funcion
    if b<c:                                                                             #Se define que b es menor que c
        return 7                                                                        #Se retornan 7
    else:                                                                               #Se define else
        return 14                                                                       #Se retornan 14
    return 3                                                                            #Se retornan 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))                          #Se imprime la funcion y elementos
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))                          #Se imprime la funcion y elementos
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))    #Se imprime la suma de funciones con elementos
"""
Se imprimira: 7 , 14 , 21
"""

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
