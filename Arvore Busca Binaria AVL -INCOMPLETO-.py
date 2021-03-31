def main():
    class No:
        def __init__(self, chave = None, esquerda = None, direita = None, pai = None):
            self.chave    = chave
            self.esquerda = esquerda
            self.direita  = direita
            self.pai      = pai
            self.altEsq   = 0
            self.altDir   = 0

    class ArvBinaria(No):
        def __init__(self):
            self.raiz      = None
            self.altura    = []
            self.keyTemp   = None

        def __int__(self):
            return self.raiz

        def alturaArvore(self):
            return max(self.altura)

        def inserir(self, novaChave):
            if self.raiz is None:
                novo_No   = No(novaChave)
                self.raiz = novo_No
                return novaChave
            else:
                novo_No = No(novaChave)
                p       = self._inserir(novo_No, self.raiz)
                return p
            
        def _inserir(self, novaChave, raizTemp, profundidade = 0):
            if raizTemp.chave <= novaChave.chave:
                if raizTemp.direita is None:
                    raizTemp.direita = novaChave
                    novaChave.pai    = raizTemp
                    profundidade    += 1
                    self.altura.append(profundidade)
                    self.setAlturaNo(self.raiz)
                    return profundidade
                else:
                    profundidade    += 1
                    return self._inserir(novaChave, raizTemp.direita, profundidade)

            else:
                if raizTemp.esquerda is None:
                    raizTemp.esquerda = novaChave
                    novaChave.pai     = raizTemp
                    profundidade     += 1
                    self.altura.append(profundidade)
                    self.setAlturaNo(self.raiz)
                    return profundidade
                else:
                    profundidade     += 1
                    return self._inserir(novaChave, raizTemp.esquerda, profundidade)

        def setAlturaNo(self, raizTemp):
          if raizTemp != None:
              self.setAlturaNo(raizTemp.esquerda)
              self.setAlturaNo(raizTemp.direita)
              if raizTemp.esquerda is not None:
                  raizTemp.altEsq = (max(raizTemp.esquerda.altEsq, raizTemp.esquerda.altDir))+1
              if raizTemp.direita is not None:
                  raizTemp.altDir = (max(raizTemp.direita.altEsq, raizTemp.direita.altDir))+1

              if (raizTemp.altEsq - raizTemp.altDir) == -2 and (raizTemp.direita.altEsq-raizTemp.direita.altDir) == -1:
                  self.rotacaoRR(raizTemp)
              elif (raizTemp.altEsq - raizTemp.altDir) == -2 and (raizTemp.direita.altEsq-raizTemp.direita.altDir) == 1:
                  self.rotacaoRL(raizTemp)
              elif (raizTemp.altEsq - raizTemp.altDir) == 2 and (raizTemp.esquerda.altEsq-raizTemp.esquerda.altDir) == 1:
                  self.rotacaoLL(raizTemp)
              elif (raizTemp.altEsq - raizTemp.altDir) == 2 and (raizTemp.esquerda.altEsq-raizTemp.esquerda.altDir) == -1:
                  self.rotacaoLR(raizTemp)

        def buscar(self, chaveTemp):
            if self.raiz is None:
                return -1
            else:
                raizTemp = self.raiz
                no        = self._buscar(chaveTemp, raizTemp)
                return no        
                
        def _buscar(self, chaveTemp, raizTemp, profundidade = 0):
            if raizTemp is None:
                return -1
            elif raizTemp.chave < chaveTemp:
                profundidade += 1
                return self._buscar(chaveTemp, raizTemp.direita, profundidade)
            elif raizTemp.chave > chaveTemp:
                profundidade += 1
                return self._buscar(chaveTemp, raizTemp.esquerda, profundidade)
            else:
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
                    raizTemp.direita     = chaveTemp.direita
                    raizTemp.direita.pai = raizTemp
                self.transplantar(chaveTemp, raizTemp)
                raizTemp.esquerda = chaveTemp.esquerda
                if raizTemp.esquerda is not None:
                    raizTemp.esquerda.pai = raizTemp
            self.setAlturaNo(self.raiz)
        
        def rotacaoRR(self, raiz):
            # esq-dir -2 -1
            y = raiz
            x = y.direita
            y.direita = x.esquerda
            if y.direita is not None:
                y.direita.pai = y
            x.pai = y.pai
            y.pai = x
            if x.pai is None:
                self.raiz = x
            x.esquerda = y
            return self.setAlturaNo(self.raiz)

        def rotacaoLL(self, raiz):
            ## esq-dir +2 +1 
            y = raiz
            x = y.esquerda
            y.esquerda = x.direita
            if y.esquerda is not None:
                y.esquerda.pai = y
            x.pai = y.pai
            y.pai = x
            if x.pai is None:
                self.raiz = x
            x.direita = y
            return self.setAlturaNo(self.raiz)
        
        def rotacaoLR(self, raiz):
            ##2 esq-dir +2 -1 
            y = raiz
            z = y.esquerda
            x = z.direita
            x.pai = y.pai
            y.pai = x
            if x.pai is None:
                self.raiz = x
            y.esquerda = x.direita
            if x.direita is not None:
                y.esquerda.pai = y
            z.direita = x.esquerda
            if x.esquerda is not None:
                z.direita.pai = z
            x.esquerda = z
            x.direita = y
        
        def rotacaoRL(self, raiz):
            #-2 +1
            y = raiz
            z = y.direita
            x = z.esquerda
            x.pai = y.pai
            y.pai = x
            if x.pai is None:
                self.raiz = x
            z.esquerda = x.direita
            if z.esquerda is not None:
                z.esquerda.pai = z
            y.direita = x.esquerda
            if y.direita is not None:
                y.direita.pai = y
            x.esquerda = y
            x.direita  = z
            z.pai = x

        def transplantar(self, chaveTemp, raizTemp):
            if chaveTemp.pai is None:
                self.raiz = raizTemp
            elif chaveTemp == chaveTemp.pai.esquerda:
                chaveTemp.pai.esquerda = raizTemp
            else:
                chaveTemp.pai.direita  = raizTemp

            if raizTemp is not None:
                raizTemp.pai = chaveTemp.pai

        def sucessor(self, raizTemp, naDireita = False):
            if not naDireita:
                naDireita = True
                raizTemp  = raizTemp.direita
                
            if raizTemp.esquerda is None:
                return raizTemp
            else:
                return self.sucessor(raizTemp.esquerda, naDireita)

        def imprimir(self, no, esquerda = None, direita = None, pai = None):
            profundidade = self.buscar(no)
            if profundidade == -1:
                return 'Chave não encontrada'
            else:
                no = self.keyTemp
                chave = no.chave
                alturaEsquerda = no.altEsq
                alturaDireita  = no.altDir
                if no.esquerda is not None:
                    esquerda = no.esquerda.chave
                if no.direita is not None:
                    direita = no.direita.chave
                if no.pai is not None:
                    pai     = no.pai.chave
                return f'Chave: {chave}\nEsquerda: {esquerda}\nDireita: {direita}\nPai: {pai}\nAltura Esquerda: {alturaEsquerda}\nAltura Direita: {alturaDireita}\nProfundidade: {profundidade}\n'

        def em_ordem(self, raizTemp):
            raizTemp = self.raiz
            while raizTemp is not None:
                print(raizTemp.chave)
                self.em_ordem(raizTemp.esquerda)
                self.em_ordem(raizTemp.direita)
            
                    
    def entrada():
        keys = input()
        keys += ' '
        ins_arvore_entrada(keys)

    def ins_arvore_entrada(keys):
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
    qtd = input()
    entrada()
    
    ops = ['SCH ','INS ', 'DEL ', 'PRT ']
    programa = True
    while programa:
        op = input()
        if ops[0] in op:
            op = int(op[5:-1])
            print(v.buscar(op))
        elif ops[1] in op:
            op = int(op[5:-1])
            print(v.inserir(op))
        elif ops[2] in op:
            op = int(op[5:-1])
            encontrou = v.buscar(op)
            print(encontrou)
            if encontrou != -1:
                v.remover()
        elif ops[3] in op:
          op = int(op[5:-1])
          print(v.imprimir(op))
        else:
          programa = False


if __name__ == '__main__':
    main()
