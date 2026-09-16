
def mi_capitalize(cadena1: str) -> str:
    '''
    ###FEN###
    sintaxis:cadena.capitalize()
    parametros: No
    ¿Que hace?: pone la primer letra en mayusculas
    La  cadena es inmutable
    ¿Que devuelve?: 1 de tipo -> str
    '''
    from  icecream import ic
    ic.disable()
    ic()
    
    cadena2 = cadena1.capitalize()
    
    ic(cadena1)
    ic(cadena2)
    return cadena2

def main():
    CADENA1 = 'cg5'

    CADENA2 = mi_capitalize(cadena1=CADENA1)

    print('cadena: ', CADENA1, ' cadena2: ', CADENA2)
    print(f'cadena2 es del tipo : {type(CADENA2)}')

if __name__ == "__main__":
    main()
