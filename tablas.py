# • Diseña un algoritmo que permita mostrar las
# tablas de multiplicar del 1 al 10


print('Tablas de multiplicar')
for x in range(10):
    print(f'Tabla del {x}')
    for y in range(10):
        resultado=x*y
        print(f'{x} * {y} es {resultado}')