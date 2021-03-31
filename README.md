### Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)

### Centro de Informática (CIn) (http://www.cin.ufpe.br)

### Graduando em Sistemas de Informação

### IF969 - Algoritmos e Estrutura de Dados

### Autor: Vinícius Luiz da Silva França (vlsf2)

### Email: vlsf2@cin.ufpe.br

### Data: 2020-09-06

### Copyright(c) 2020 Vinícius Luiz da Silva França



#### BST Workout para Python

> Uma árvore de busca binária (BST) é uma árvore binária em que o valor de cada nó é maior do que os valores de cada nó à sua esquerda, e menor ou igual aos valores de cada nó à sua direita.
>
> Neste exercício iremos praticar as operações sobre BSTs vistas em aula.

> **Input Specification**
>
> A entrada inicia com uma linha contendo um inteiro
>
> > N
>
> correspondente à quantidade inicial de nós de uma BST T.
>
> Segue-se uma linha com N inteiros separados por espaços,
>
> > P[0] P[1] ... P[N-1]
>
> correspondentes aos valores dos nós de T enumerados em pré-ordem.
>
> Em seguida, temos várias operações numa das formas a seguir:
>
> - SCH k : procura o valor k em T
> - INS k : insere o valor k em T
> - DEL k : remove o valor k de T
>
> A entrada termina com uma linha
>
> > END

> **Output Specification** 
>
> Inicialmente, deve ser impressa uma linha com um inteiro
>
> > Hinit
>
> correposndente à altura inicial da árvore T com os N elementos em pré-ordem dados na entrada.
>
> Em seguida, para cada operação deve-se imprimir o seguinte.
>
> - SCH k : imprime a profundidade do primeiro nó encontrado (nó menos profundo) com valor k. Caso tal nó não exista, imprime -1.
> - INS k : imprime a profundidade da folha com valor k inserida.
> - DEL k : imprime a profundidade do nó removido com valor k, se houver. Caso contrário imprime -1. Esse valor é o mesmo valor que seria impresso por SCH k antes da remoção.
>
> Ao final, deve-se imprimir uma linha
>
> > Hfinal
>
> correspondente à altura final da árvore T, após todas as operações.

>  **Sample Input #1**

> 100  
> 570 250 0 220 60 40 10 20 30 50 200 80 70 170 150 140 110 100 90 120 130 160 190 180 210 230 240 280 260 270 310 300 290 450 380 360 350 320 330 340 370 390 420 400 410 440 430 470 460 520 490 480 500 510 550 530 540 560 940 760 630 590 580 610 600 620 650 640 700 690 670 660 680 720 710 730 740 750 860 840 770 780 790 830 800 820 810 850 870 890 880 930 900 910 920 980 970 950 960 990  
> SCH 1008  
> SCH 280  
> SCH 100  
> SCH 1006  
> SCH 200  
> SCH 490  
> SCH 210  
> SCH 480  
> SCH 700  
> SCH 930  
> SCH 940  
> SCH 1001  
> SCH 1002  
> SCH 1005  
> SCH 790  
> SCH 1004  
> SCH 990  
> SCH 820  
> SCH 1008  
> SCH 880  
> SCH 120  
> SCH 1003  
> SCH 1000  
> SCH 880  
> SCH 70  
> SCH 200  
> SCH 220  
> SCH 340  
> SCH 800  
> SCH 170  
> SCH 120  
> SCH 620  
> SCH 1005  
> SCH 750  
> SCH 1008  
> SCH 390  
> SCH 1001  
> SCH 220  
> SCH 1006  
> SCH 560  
> SCH 350  
> SCH 1005  
> SCH 1000  
> SCH 830  
> SCH 800  
> SCH 1001  
> SCH 1000  
> SCH 1002  
> SCH 1007  
> SCH 210  
> SCH 270  
> SCH 1004  
> SCH 410  
> SCH 1001  
> SCH 1004  
> SCH 500  
> SCH 1005  
> SCH 540  
> SCH 300  
> SCH 150  
> SCH 1003  
> SCH 1009  
> SCH 1002  
> SCH 530  
> SCH 1006  
> SCH 170  
> SCH 840  
> SCH 1008  
> SCH 1007  
> SCH 680  
> SCH 1003  
> SCH 1009  
> SCH 860  
> SCH 20  
> SCH 470  
> SCH 1004  
> SCH 600  
> SCH 1000  
> SCH 530  
> SCH 1003  
> SCH 1000  
> SCH 1005   
> SCH 1005  
> SCH 930   
> SCH 1007  
> SCH 390  
> SCH 460  
> SCH 610  
> SCH 1000  
> SCH 1006  
> SCH 1007  
> SCH 1003  
> SCH 410  
> SCH 390  
> SCH 1008   
> SCH 870  
> SCH 1001  
> SCH 1007  
> SCH 1001  
> SCH 1006  
> END  

> **Sample Output #1**

>  13  
>  -1  
>  2  
>  11  
>  -1  
>  5  
>  7  
>  6  
>  8  
>  5  
>  6  
>  1  
>  -1  
>  -1  
>  -1  
>  7   
>  -1  
>  3  
>  10  
>  -1  
>  6  
>  11  
>  -1  
>  -1  
>  6  
>  7  
>  5  
>  3  
>  10  
>  9  
>  7  
>  11  
>  6  
>  -1  
>  9  
>  -1  
>  6  
>  -1  
>  3  
>  -1  
>  8  
>  7  
>  -1  
>  -1  
>  8  
>  9  
>  -1  
>  -1  
>  -1  
>  -1  
>  6  
>  4  
>  -1  
>  9   
>  -1   
>  -1  
>  8  
>  -1  
>  9  
>  4  
>  8  
>  -1  
>  -1  
>  -1  
>  8  
>  -1  
>  7   
>  4  
>  -1  
>  -1  
>  8  
>  -1  
>  -1  
>  3  
>  7  
>  5  
>  -1  
>  6  
>  -1  
>  8  
>  -1  
>  -1   
>  -1  
>  -1   
>  6  
>  -1  
>  6  
>  6  
>  5  
>  -1  
>  -1  
>  -1  
>  -1  
>  9  
>  6  
>  -1  
>  4  
>  -1  
>  -1  
>  -1  
>  -1  
>  13   

