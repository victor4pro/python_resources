

def vat_format_dot(string3):
    """
    This function takes a string as input and formats it according to certain conditions.
    Input:
        77888999-4
    Output:
        77.888.999-4
    """
    if "-" in string3:
        parte1, parte2 = string3.split('-')
        if parte1:
            numero = int(parte1)
            if numero // 1000 == 0:
                return string3
            lista_de_partes = []
            while numero > 0:
                lista_de_partes.append(str(numero % 1000))
                numero //= 1000
            lista_de_partes.reverse()
            parte1_formateada = '.'.join(lista_de_partes)
            return f"{parte1_formateada}-{parte2}"
        else:
            return string3
    else:
        return string3


if __name__ == '__main__':
    # Example
    string1 = "86841749-4"
    string2 = vat_format_dot(string1)
    print(string2)
