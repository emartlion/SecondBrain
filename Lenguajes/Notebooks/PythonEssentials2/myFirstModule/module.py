#!/usr/bin/env python3 

print("Module.py - Un ejemplo de un módulo de Python")

__counter = 0

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for elem in the_list:
        the_sum += elem
    return the_sum

def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for elem in the_list:
        prod *= elem
    return prod


if __name__ == "__main__":
    print("Prefiero ser un módulo, pero puedo hacer unas pruebas para ti.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)