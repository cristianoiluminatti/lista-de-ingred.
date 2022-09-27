
import os


AGREGAR = 1
INSERTAR= 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

def imprimir_menu ():
    os.system('cls')
    print(f'''            Frutas
{AGREGAR}) Agregar
{INSERTAR}) Insertar
{MOSTRAR}) Mostrar
{BUSCAR}) Buscar 
{ELIMINAR}) Elimminar
{ORDENAR}) Ordenar
{LIMPIAR}) Limpiar lista
{SALIR}) Salir''')

def agregar_registro():
    print('                agregar')
    nombre = input('nombre:  ')
    frutas.append (nombre)
    print ('Registro agregado con exito')

def insertar_registro():
    print('                   insertar')
    nombre = input('Nombre: ')
    pos = int(input('posicion:  '))
    frutas.insert(pos,nombre)
    print ('Registro insertado en la posicion indicada') 

def mostrar_registro():
    print('                       mostrar')
    if len (frutas) > 0:
        for fruta in frutas:
            print(fruta)
    else:
        print('No se han agregado frutas a la lista seleccionada')

def buscar_registro():
    print('                    buscar')
    if len(lista) > 0:
        nombre = input('nombre a buscar')
        if nombre in frutas:
            cantidad = frutas.count(nombre)
            inicio = 0
            for i in range(cantidad):
                pos = frutas.index(nombre,inicio)
                print(f'{nombre} se encuentra en la posicion {pos+1}')
            inicio = pos + 1
        else:
            print(f'{nombre}no ha sido registrado ela mierdilista esta')    
    
    else:
        print: ('No se han agregado frutas en la lista de mierda esta')    

def eliminar_registro():
    print('                          registro')       
    if  len(frutas) > 0:
        for i in range (len(frutas)):
            print(f'{i+1}.{frutas[i]}')
        print('0. cancelar')
        pos = int(input(f'posicion a eliminar (1  - {len(frutas)})'))
        if 0 < pos <= len(frutas):
            frutas.pop(pos - 1)
        else:
            print ('No se elimminara ningin registro')

    else:
        print('No se han agregado frutas de la lista chimgona pue')

def ordenar_registro():
    print('                        ordenar')
    if len(frutas) >  0:
         frutas.sort()
         print('Registros ordenados alfabeticamente')
    else:
        print('No se han agregado frutas a la lista')

def limpiar_registro():
    print('                    limpiar')
    frutas.clear()
    print('Los registros han sido borrados')

def main():
    continuar = true
    while continuar:

        imprimir_menu()

        opc = int(input('Selecciona una opcion'))
        os.system(' cls')
        if opc == AGREGAR:
            agregar_registro()
        elif opc == INSERTAR:
            insertar_registro()
        elif opc == MOSTRAR: 
            mostrar_registro()
        elif opc == ELIMINAR:
            eliminar_registro()
        elif opc == ORDENAR:
            ordenar_registro()
        elif opc == LIMPIAR:
            limpiar_registro()
        elif opc == SALIR:
            print('\U0001F600'  'NOS VEMOS')
            continuar = False
        else:
            print('opcion no valida carnal')
        input('presiona enter para continuar...')

if ___name__ == '__main__':
    main()


