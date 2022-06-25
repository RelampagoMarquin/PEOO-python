def aumentar(valor, taxa):
    valor += (valor * taxa)/100
    return valor

def descontar(valor, taxa):
    valor -= (valor * taxa)/100
    return valor
