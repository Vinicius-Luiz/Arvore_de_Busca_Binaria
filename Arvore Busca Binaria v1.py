def main():
    class No:
        def __init__(self, chave = None, esquerda = None, direita = None, pai = None):
            self.chave    = chave
            self.esquerda = esquerda
            self.direita  = direita
            self.pai      = pai

        def __int__(self):
            return int(self.chave)
        def __int__(self):
            return int(self.esquerda)
        def __int__(self):
            return int(self.direita)

    class ArvBinaria(No):
        def __init__(self):
            self.raiz      = None
            self.altura    = []
            self.keyTemp = None

        def __int__(self):
            return self.raiz

        def alturaArvore(self):
            return max(self.altura)+1

        def inserir(self, novaChave):
            if self.raiz is None:
                novo_No = No(novaChave)
                self.raiz = novo_No
                return novaChave
            else:
                novo_No = No(novaChave)
                p = self._inserir(novo_No, self.raiz)
                return p
            
        def _inserir(self, novaChave, raizTemp, profundidade = 0):
            if raizTemp.chave <= novaChave.chave:
                if raizTemp.direita is None:#V
                    raizTemp.direita = novaChave
                    novaChave.pai = raizTemp
                    profundidade +=1
                    self.altura.append(profundidade)
                    return profundidade
                else:
                    profundidade += 1
                    return self._inserir(novaChave, raizTemp.direita, profundidade)

            elif raizTemp.chave > novaChave.chave:
                if raizTemp.esquerda is None:
                    raizTemp.esquerda = novaChave
                    novaChave.pai = raizTemp
                    profundidade +=1
                    self.altura.append(profundidade)
                    return profundidade
                else:
                    profundidade += 1
                    return self._inserir(novaChave, raizTemp.esquerda, profundidade)            

        def buscar(self, chaveTemp):
            if self.raiz is None:
                return -1
            else:
                raizTemp = self.raiz
                c = self._buscar(chaveTemp, raizTemp)
                return c
                
                
        def _buscar(self, chaveTemp, raizTemp, profundidade = 0, encontrou = False):
            if raizTemp is None:
                return -1
            elif raizTemp.chave < chaveTemp:
                profundidade+=1
                return self._buscar(chaveTemp, raizTemp.direita, profundidade, encontrou)
            elif raizTemp.chave > chaveTemp:
                profundidade += 1
                return self._buscar(chaveTemp, raizTemp.esquerda, profundidade, encontrou)
            else:
                encontrou = True
                self.keyTemp = raizTemp
                return profundidade       

        def remover(self):
            chaveTemp = self.keyTemp
            if chaveTemp.esquerda is None:
                self.transplantar(chaveTemp, chaveTemp.direita)
            elif chaveTemp.direita is None:
                self.transplantar(chaveTemp, chaveTemp.esquerda)
            else:
                raizTemp = self.sucessor(chaveTemp)
                if raizTemp.pai is not chaveTemp:
                    self.transplantar(raizTemp, raizTemp.direita)
                    raizTemp.direita = chaveTemp.direita
                    raizTemp.direita.pai = raizTemp
                self.transplantar(chaveTemp, raizTemp)
                raizTemp.esquerda = chaveTemp.esquerda
                if raizTemp.esquerda is not None:
                    raizTemp.esquerda.pai = raizTemp

        def transplantar(self, chaveTemp, raizTemp):
            if chaveTemp.pai is None:
                self.raiz = raizTemp
            elif chaveTemp == chaveTemp.pai.esquerda:
                chaveTemp.pai.esquerda = raizTemp
            else:
                chaveTemp.pai.direita = raizTemp

            if raizTemp is not None:
                raizTemp.pai = chaveTemp.pai

        def sucessor(self, raizTemp, naDireita = False):
            if not naDireita:
                naDireita = True
                raizTemp = raizTemp.direita
                
            if raizTemp.esquerda is None:
                return raizTemp
            else:
                return self.sucessor(raizTemp.esquerda, naDireita)
                    
    def entrada():
        keys = input()
        keys += ' '
        return keys

    def ins_arvore_entrada():
        lista = []
        word  =  ''
        for c in keys:
            if c != ' ':
                word += c
            else:
                lista.append(word)
                word = ''
        for x in range(int(qtd)):
            v.inserir(int(lista[x]))
        print(v.alturaArvore())
        return
        
    v = ArvBinaria()        
    qtd   = input()
    keys = entrada()
    ins_arvore_entrada()


    ops = ['SCH ','INS ', 'DEL ']
    programa = True
    while programa:
        try:
            op = input()
            if ops[0] in op:
                op = int(op[4:])
                print(v.buscar(op))
            elif ops[1] in op:
                op = int(op[4:])
                print(v.inserir(op))
            elif ops[2] in op:
                op = int(op[4:])
                encontrou = v.buscar(op)
                print(encontrou)
                if encontrou != -1:
                    v.remover()
            
        except EOFError:
            print(v.alturaArvore())
            programa = False

if __name__ == '__main__':
    main()

