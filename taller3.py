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