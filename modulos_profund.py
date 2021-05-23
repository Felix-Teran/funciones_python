from ejemplos_clase import numero_pi
import random
from collections import Counter

def imprimir_nombre(nombre, apellido):
    """Imprime nombre completo"""
    print("Nombre: {} {} \n".format(nombre, apellido))
    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)


def promedio(numeros):
    """Esta función calcula el promedio de una lista, en caso
       de no poseer ningún elemento, arroja una alarma al user"""
    # Alumno:
    # 1) calcule el promedio
    
    if len(numeros) == 0:
        print("\33[93mLa lista se encuentra vacía, no posee elementos\33[0m")
        numeros = []
        new_list = int(input("Ingrese un número y crearemos una lista aleatoaria\n"))
        for i in range(new_list):
            new_elements = random.randrange(new_list)
            numeros.append(new_elements)
        print("La nueva lista es:", numeros)
        numeros_cantidad = len(numeros)
        numeros_sumatoria = sum(numeros)
        promedio = numeros_sumatoria / numeros_cantidad
        return promedio

    elif len(numeros) > 0:
        print("La lista es:", numeros)
        numeros_cantidad = len(numeros)
        numeros_sumatoria = sum(numeros)
        promedio = numeros_sumatoria / numeros_cantidad

    # 2) use "return" para retornar ese valor
        return promedio
    # Cuando termine de implementar está función borrar "pass"


def ordenar(numeros):
    if len(numeros) == 0:
        print("\33[93mLa lista se encuentra vacía, no posee elementos\33[0m")
        numeros = []
        new_list = int(input("Ingrese un número y crearemos una lista aleatoaria\n"))
        for i in range(new_list):
            new_elements = random.randrange(new_list)
            numeros.append(new_elements)
        print("La nueva lista es:", numeros)
        numeros.sort(reverse=True)
        return numeros

    elif len(numeros) > 0:
        numeros.sort(reverse=True)
        return numeros

def contar(dado_list, num):
    for i in num:
        if i not in dado_list:
            print(f"El número {i} no aparece en su lista de dados tirados")
        elif i in dado_list:
            print(f"El número {i} aparece x{dado_list.count(i)} en su lista de dados tirados") 

def examinar(dado_list, dado_list_max, repetidos):
    dados_guardados = []
    for dado in dado_list:
        if dado == dado_list_max:
            dados_guardados.append(dado)
            generala = len(repetidos) + len(dados_guardados)
            if generala == 5:
                break
    return dados_guardados

