import random


def noEsRepe(n, B):

    norepe = True
    for g in range(4):
        for v in range(4):
            if n == B[g][v]:

                norepe = False

    return norepe

class Puzzle:
    movimientos = 0
    xVacio = -1
    yVacio =-1
    Resultado = [[1,2,3,4],[5,6,7,8],[9, 10,11,12],[13,14,15,0]]

    #Contructor que genera la matriz sin numeros repetidos
    def __init__(self):
        self.M = []
        #Se crea la matriz vacia que sera el tablero
        for i in range(4):
            self.M.append([None]*4)
        #Se introducen los valores aleatorios usando la funcion auxiliar anterior
        fila = len(self.M)
        columna = len(self.M[0])
       # j = 0
        #while j <= fila*columna:
          #  j += 1
        for f in range(fila):
            for c in range(columna):
                print('[',f,'][',c,']')
                x = random.randint(0, 15)
                while  not noEsRepe(x, self.M):
                    x = random.randint(0, 15)
                self.M[f][c] = x
        #guardamos la coordenada del hueco vacio
        for f in range(fila):
            for c in range(columna):
                if self.M[f][c] == 0:
                    self.xVacio = f
                    self.yVacio = c
                    print(self.xVacio,self.yVacio)
    def resueltoPuzzle(self):
        result = True
        f = 0
        c = 0
        while result:
            if self.M[f][c]==self.Resultado[f][c]:
                print('Esta bien :)')
                print('Has realizado un total de',self.movimientos,'movimientos')
            else:
                print('No esta bien :(')
                print('Has realizado un total de', self.movimientos, 'movimientos')
                result = False
        f +=1
        c +=1


    def movimientoValido(self,coorX,coorY):
        valido = True;
        if (coorX==self.xVacio+1 and coorY == self.yVacio)or(coorX==self.xVacio and coorY == self.yVacio+1)or(coorX==self.xVacio-1 and coorY == self.yVacio)or(coorX==self.xVacio and coorY == self.yVacio-1):
            print('El movimiento es valido')
        elif coorX==self.xVacio and coorY == self.yVacio:
            print('El movimiento no es valido, es el hueco vacio')
            valido = False
        else:
            print('El movimiento no es valido')
            valido = False
        return valido


    #get para el tablero y para el numero de movimientos
    def devolverTablero(self):
        return self.M
    def devolverMovimientos(self):
        return self.movimientos
    def toString(self):
        res = self.M
        return res