# -*- coding: utf-8 -*-
from p1.cozinheiro import cozinheiro

cozinheiro.oQueEstaVendo()     # Porta da Cozinha [NA SUA FRENTE 5 passos]
cozinheiro.andar()             # Andar 5 passos para frente até a porta
cozinheiro.andar()
cozinheiro.andar()
cozinheiro.andar()
cozinheiro.andar()             # Chegou na porta
cozinheiro.abrirPorta()        # Abre a porta e entra na cozinha
cozinheiro.oQueEstaVendo()     # Armário [NA SUA ESQUERDA 5 passos e NA SUA FRENTE 5 passos]
cozinheiro.virarParaEsquerda() # Virar para a esquerda
for i in range(5):
    cozinheiro.andar()         # Andar 5 passos
cozinheiro.virarParaDireita()  # Virar para a direita
for i in range(5):
    cozinheiro.andar()         # Andar 5 passos até chegar no armário
cozinheiro.abrirArmario()
cozinheiro.pegarPanela()
cozinheiro.virarParaDireita()
cozinheiro.oQueEstaVendo()     # Fogão [NA SUA FRENTE 10 passos]
for i in range(10):
    cozinheiro.andar()         # Andar 10 passos para frente até o fogão
cozinheiro.colocarPanelaNoFogao()
cozinheiro.virarParaEsquerda()
cozinheiro.virarParaEsquerda()
for i in range(5):
    cozinheiro.andar()         # Andar 5 passos
cozinheiro.virarParaDireita()
cozinheiro.oQueEstaVendo()     # Geladeira [NA SUA FRENTE 5 passos]
for i in range(5):
    cozinheiro.andar()         # Andar 5 até a geladeira
cozinheiro.abrirGeladeira()
cozinheiro.pegarOvo()          # Pegou o ovo
cozinheiro.virarParaDireita()
cozinheiro.virarParaDireita()
for i in range(5):
    cozinheiro.andar()         # Andar 5 passos
cozinheiro.virarParaEsquerda()
for i in range(5):
    cozinheiro.andar()         # Andar 5 até o fogão
cozinheiro.quebrarOvoDentroDaPanela()
cozinheiro.virarParaDireita()
cozinheiro.virarParaDireita()
for i in range(10):
    cozinheiro.andar()         # Andar 10 até o armário
cozinheiro.pegarSal()
cozinheiro.virarParaDireita()
cozinheiro.virarParaDireita()
for i in range(10):
    cozinheiro.andar()         # Andar 10 até o fogão
cozinheiro.colocarSal()
cozinheiro.ligarFogao()

while not cozinheiro.jaEstaPronto():
    print "Esperando o ovo ficar pronto ..."
    
print "O ovo está pronto"

cozinheiro.colocarOvoNoPrato()
cozinheiro.virarParaDireita()
cozinheiro.virarParaDireita()

for i in range(5):
    cozinheiro.andar()

cozinheiro.virarParaEsquerda()

for i in range(5):
    cozinheiro.andar()
    
cozinheiro.abrirPorta()

for i in range(10):
    cozinheiro.andar()
    
cozinheiro.colocarPratoNaMesa() # Ovo servido com sucesso !

#Voltando agora para arrumar a bagunça 
cozinheiro.virarParaEsquerda()
cozinheiro.virarParaEsquerda()
for i in range(10):
    cozinheiro.andar()
cozinheiro.abrirPorta()
for i in range(10):
    cozinheiro.andar()
cozinheiro.fecharGeladeira() # Fechando a geladeira

cozinheiro.virarParaEsquerda()
for i in range(5):
    cozinheiro.andar()
cozinheiro.virarParaEsquerda()
for i in range(5):
    cozinheiro.andar()
cozinheiro.fecharArmario() # Fechando o armário

cozinheiro.virarParaEsquerda()
for i in range(10):
    cozinheiro.andar()
cozinheiro.desligarFogao() # Desligando o fogão

#Exibindo o resumo
cozinheiro.exibirResumo() # Será que eu consegui ?