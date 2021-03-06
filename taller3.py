# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:28:35 2021

@author: Lenovo
"""
#Actividad 1
def actividad1(aut):
    amarilla = 0
    rosa = 0
    roja = 0
    verde = 0
    azul = 0

    for auto in aut:
        if auto == 1 or auto == 2:
            amarilla += 1
        elif auto == 3 or auto == 4:
            rosa += 1
        elif auto == 5 or auto == 6:
            roja += 1
        elif auto == 7 or auto == 8:
            verde += 1
        elif auto == 9 or auto == 0:
            azul += 1

    return {
        "Num de autos amarillos": amarilla,
        "Num de autos rosas": rosa,
        "Num de autos rojos": roja,
        "Num de autos verdes": verde,
        "Num de autos azules": azul
    }

#Actividad 2
def actividad2(anim):
    edad_anim = []
    if anim.lower() == 'elefante':
        for i in range(20):
            elefante = int(input('Ingrese edad del elefante:'))
            edad_anim.append(elefante)
    if anim.lower() == 'jirafa':
        for i in range(15):
            jirafa = int(input('Ingrese edad de la jirafa:'))
            edad_anim.append(jirafa)
    if anim.lower() == 'chimpance':
        for i in range(40):
            chimpance = int(input('Ingrese edad del chimpance:'))
            edad_anim.append(chimpance)
    
    cat1 = cat2 = cat3 = 0
    for edad in edad_anim:
        if edad >= 0 and edad <= 1:
            cat1 += 1
        elif edad > 1 and edad < 3:
            cat2 += 1
        elif edad >= 3:
            cat3 += 1
    
    if anim.lower() == 'elefante':
        cat1 = (cat1 * 100) / 20 
        cat2 = (cat2 * 100) / 20
        cat3 = (cat3 * 100) / 20
        
    if anim.lower() == 'jirafa':
        cat1 = (cat1 * 100) / 15 
        cat2 = (cat2 * 100) / 15
        cat3 = (cat3 * 100) / 15
        
    if anim.lower() == 'chimpance':
        cat1 = (cat1 * 100) / 40
        cat2 = (cat2 * 100) / 40
        cat3 = (cat3 * 100) / 40


    return {
        "Animal": anim,
        "De 0 a 1 año": cat1,
        "Mas de 1 y menos de 3 años": cat2,
        "De 3 o más años": cat3
    }

#Actividad 3
def actividad3(hor_x_obr):
    for obr in hor_x_obr:
        if obr <= 40:
            print(f'Pago: {obr * 20}')
        elif obr > 40:
            print(f'Pago: {40 * 20 + ((obr - 40) * 25)} ')

#Actividad 4
def actividad4(edad_hombre, edad_mujer):
    acum_hombre = acum_mujer = tot = 0
    for edad in edad_hombre:
        acum_hombre += edad
        tot += edad
    for edad in edad_mujer:
        acum_mujer += edad
        tot += edad
    
    return {
        "Promedio de hombres": acum_hombre / len(edad_hombre),
        "Promedio de mujeres": acum_mujer / len(edad_mujer),
        "Promedio gral": tot / (len(edad_hombre) + len(edad_mujer))
    }

#Actividad 5
def actividad5(num):
    menor = num[len(num) - 1]
    for n in num:
        if n < menor:
            menor = n
    return menor

#Actividad 6
def actividad6():
    for i in range(5):
        ult_peso = int(input('Ingrese su peso último:'))
        prom_peso = 0
        for i in range(10):
            prom_peso += int(input(f'Ingrese peso de báscula {i}:'))

        prom_peso = prom_peso / 10

        if prom_peso > ult_peso:
            print(f'***subió*** {prom_peso - ult_peso}')
        else:
            print(f'***bajó*** {ult_peso - prom_peso}')

#Actividad 7
def actividad7(num_prod):

    tot = 0
    for _ in range(num_prod):
        prec = int(input('Ingrese precio de producto: '))
        cant = int(input('Cantidad producto: '))

        tot += prec * cant
    return tot

#Actividad 8
def actividad8(num_ent, valor):
    rango_edad1 = rango_edad2 = rango_edad3 = rango_edad4 = rango_edad5 = 0
    for i in range(num_ent):

        edad = int(input('Ingrese edad: '))
        if edad < 5:
            print('No puede entrar')
        if edad >= 5 and edad <= 14:
            rango_edad1 += valor * 0.35
        if edad >= 15 and edad <= 19:
            rango_edad2 += valor * 0.25
        if edad >= 20 and edad <= 45:
            rango_edad3 += valor * 0.1 
        if edad >= 46 and edad <= 65:
            rango_edad4 += valor * 0.25
        if edad > 65:
            rango_edad5 += valor * 0.35

    return {
        "Rango 1": rango_edad1,
        "Rango 2": rango_edad2,
        "Rango 3": rango_edad3,
        "Rango 4": rango_edad4,
        "Rango 5": rango_edad5,
        }

#Actividad 9
def actividad9():
    for i in range(1):
        vend = int(input(f'{i} Valor vendido: '))

        if vend <= 20000000:
            print(f'Total vendido: {vend}')
            print(f'Comisión: {vend * 0.1}')
        elif vend > 20000000 and vend < 40000000:
            print(f'Total vendido: {vend}')
            print(f'Comisión: {vend * 0.15}')
        elif vend >= 40000000 and vend < 80000000:
            print(f'Total vendido: {vend}')
            print(f'Comisión: {vend * 0.2}')
        elif vend >= 80000000 and vend < 160000000:
            print(f'Total vendido: {vend}')
            print(f'Comisión: {vend * 0.25}')
        elif vend > 160000000:
            print(f'Total vendido: {vend}')
            print(f'Comisión: {vend * 0.3}')

#Actividad 10
def actividad10():
    vot1 = vot2 = vot3 = 0
    for i in range(5):
        voto = int(input('Ingrese el numero del candidato (1, 2, 3): '))

        if voto == 1:
            vot1 += 1
        if voto == 2:
            vot2 += 1
        if voto == 3:
            vot3 += 1
        
    if vot1 > vot2 and vot1 > vot3:
        return f'Candidato 1 ganó... # de votos: {vot1}'
    elif vot3 > vot1 and vot3 > vot2:
        return f'Candidato 3 ganó... # de votos: {vot3}'
    elif vot2 > vot1 and vot2 > vot3:
        return f'Candidato 2 ganó... # de votos: {vot2}'
    elif vot1 == vot2 or vot1 == vot3 or vot2 == vot3:
        return f'**EMPATE**...con un total de votos de: 50000'