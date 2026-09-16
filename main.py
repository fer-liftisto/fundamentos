
def mi_capitalize() -> str:
    '''
    ###FEN###
    sintaxis:cadena.capitalize()
    parametros: No
    ¿Que hace?: pone la primer letra en mayusculas
    La  cadena es inmutable
    ¿Que devuelve?: 1 de tipo -> str
    '''
    from  icecream import ic
    ic()
    CADENA1='cg5'
    CADENA2 = CADENA1.capitalize()
    print('cadena: ', CADENA1, ' cadena2: ', CADENA2)
    print(f'CADENA2 es del tipo : {type(CADENA2)}')
    ic(CADENA1)
    ic(CADENA2)
    return CADENA2





def main():
    mi_capitalize()


if __name__ == "__main__":
    main()
