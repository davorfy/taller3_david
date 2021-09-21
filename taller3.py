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
