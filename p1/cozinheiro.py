# -*- coding: utf-8 -*-
import time

SUL   = 0
OESTE = 1
NORTE = 2
LESTE = 3

class Posicao(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Posicao):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

class Tamanho(object):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura  = altura

class Item(object):
    def __init__(self, nome, posicao):
        self.nome    = nome
        self.posicao = posicao

class Sala(object):
    def __init__(self, nome, tamanho = Tamanho(10, 10)):
        self.nome         = nome
        self.tamanho      = tamanho
        self.itens        = []
        self.posicaoAtual = Posicao(0, 0)
        
    def adicionarItem(self, item):
        self.itens.append(item)
        
    def entrar(self, posicao):
        print "Você está no(a)", self.nome
        self.posicaoAtual = posicao
        
class Porta(Item):
    def __init__(self, nome, posicao, salaDestino, posicaoDestino):
        super(Item, self).__init__()
        self.nome           = nome
        self.posicao        = posicao
        self.posicaoDestino = posicaoDestino
        self.salaDestino    = salaDestino
        self.posicaoDestino = posicaoDestino
        
class Jogador(object):
    def __init__(self, posicao, sala):
        self.sala = sala
        self.sala.entrar(posicao)
        self.orientacao       = SUL
        self.armarioAberto    = False
        self.pegouSal         = False
        self.pegouPrato       = False
        self.pegouPanela      = False
        self.geladeiraAberta  = False
        self.pegouOvo         = False
        self.panelaNoFogao    = False
        self.quebrouOvoPanela = False
        self.colocouSal       = False
        self.fogaoLigado      = False
        self.tempoCozimento   = 10
        self.ovoPronto        = False
        self.ovoNoPrato       = False
        self.pratoNaMesa      = False
    
    def oQueEstaVendo(self):
        print "----------------------------------------------------------------"
        print "Estou vendo:"
        qtdItens = 0
        for item in self.sala.itens:
            if item.posicao == self.sala.posicaoAtual:
                qtdItens += 1
                print item.nome, "[VOCÊ AQUI]"
            else:
                if (self.orientacao == SUL):
                    if item.posicao.y > self.sala.posicaoAtual.y :
                        qtdItens += 1
                        if item.posicao.x == self.sala.posicaoAtual.x :
                            print item.nome, "[NA SUA FRENTE", (item.posicao.y - self.sala.posicaoAtual.y), "passos]"
                        elif item.posicao.x > self.sala.posicaoAtual.x :
                            print item.nome, "[NA SUA ESQUERDA", (item.posicao.x - self.sala.posicaoAtual.x), "passos e NA SUA FRENTE", (item.posicao.y - self.sala.posicaoAtual.y), "passos]"
                        else:
                            print item.nome, "[NA SUA DIREITA", (self.sala.posicaoAtual.x - item.posicao.x), "passos e NA SUA FRENTE", (item.posicao.y - self.sala.posicaoAtual.y), "passos]"
                elif (self.orientacao == OESTE):
                    if item.posicao.x < self.sala.posicaoAtual.x :
                        qtdItens += 1
                        if item.posicao.y == self.sala.posicaoAtual.y :
                            print item.nome, "[NA SUA FRENTE", (self.sala.posicaoAtual.x - item.posicao.x), "passos]"
                        elif item.posicao.y > self.sala.posicaoAtual.y :
                            print item.nome, "[NA SUA ESQUERDA", (item.posicao.y - self.sala.posicaoAtual.y), "passos e NA SUA FRENTE", (self.sala.posicaoAtual.x - item.posicao.x), "passos]"
                        else:
                            print item.nome, "[NA SUA DIREITA]", (self.sala.posicaoAtual.y - item.posicao.y), "passos e NA SUA FRENTE", (self.sala.posicaoAtual.x - item.posicao.x), "passos]"
                elif (self.orientacao == NORTE):
                    if item.posicao.y < self.sala.posicaoAtual.y :
                        qtdItens += 1
                        if item.posicao.x == self.sala.posicaoAtual.x :
                            print item.nome, "[NA SUA FRENTE", (self.sala.posicaoAtual.y - item.posicao.y), "passos]"
                        elif item.posicao.x < self.sala.posicaoAtual.x :
                            print item.nome, "[NA SUA ESQUERDA", (self.sala.posicaoAtual.x - item.posicao.x), "passos e NA SUA FRENTE", (self.sala.posicaoAtual.y - item.posicao.y), "passos]"
                        else:
                            print item.nome, "[NA SUA DIREITA", (item.posicao.x - self.sala.posicaoAtual.x), "passos e NA SUA FRENTE", (self.sala.posicaoAtual.y - item.posicao.y), "passos]"
                else:
                    if item.posicao.x > self.sala.posicaoAtual.x :
                        qtdItens += 1
                        if item.posicao.y == self.sala.posicaoAtual.y :
                            print item.nome, "[NA SUA FRENTE", (item.posicao.x - self.sala.posicaoAtual.x), "passos]"
                        elif item.posicao.y < self.sala.posicaoAtual.y :
                            print item.nome, "[NA SUA ESQUERDA", (self.sala.posicaoAtual.y - item.posicao.y), "passos e NA SUA FRENTE", (item.posicao.x - self.sala.posicaoAtual.x), "passos]"
                        else:
                            print item.nome, "[NA SUA DIREITA", (item.posicao.y - self.sala.posicaoAtual.y), "passos e NA SUA FRENTE", (item.posicao.x - self.sala.posicaoAtual.x), "passos]"
        if qtdItens == 0:
            print "PAREDE"
                
    def virarParaEsquerda(self):
        self.orientacao = (self.orientacao - 1) % 4
    
    def virarParaDireita(self):
        self.orientacao = (self.orientacao + 1) % 4
        
    def andar(self):
        if (self.orientacao == SUL):
            self.sala.posicaoAtual.y += 1
            if (self.sala.posicaoAtual.y > self.sala.tamanho.altura):
                print "Você bateu em uma parede !"
                self.sala.posicaoAtual.y -= 1
        elif (self.orientacao == OESTE):
            self.sala.posicaoAtual.x -= 1
            if (self.sala.posicaoAtual.x < 0):
                print "Você bateu em uma parede !"
                self.sala.posicaoAtual.x += 1
        elif (self.orientacao == NORTE):
            self.sala.posicaoAtual.y -= 1
            if (self.sala.posicaoAtual.y < 0):
                print "Você bateu em uma parede !"
                self.sala.posicaoAtual.y += 1
        else:
            self.sala.posicaoAtual.x += 1
            if (self.sala.posicaoAtual.x > self.sala.tamanho.largura):
                print "Você bateu em uma parede !"
                self.sala.posicaoAtual.x -= 1
            
    def abrirPorta(self):
        for item in self.sala.itens:
            if item.posicao == self.sala.posicaoAtual and isinstance(item, Porta):
                print "Abrindo a porta ..."
                self.sala = item.salaDestino
                self.sala.entrar(item.posicaoDestino)
                return
        print "Você não está na frente de nenhuma porta"
    
    # Retorna o item que o jogador está encostando ou None caso não esteja encostando em nada
    def __getItem(self):
        for item in self.sala.itens:
            if item.posicao == self.sala.posicaoAtual:
                return item
        return None
        
    def abrirArmario(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Armário'):
                if (not self.armarioAberto):
                    self.armarioAberto = True
                    print "Abriu o armário"
                else:
                    print "O armário já está aberto !"
            else:
                print "Você não está na frente do armário"
        else:
            print "Você não está na cozinha !"

    def fecharArmario(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Armário'):
                if (self.armarioAberto):
                    self.armarioAberto = False
                    print "Fechou o armário"
                else:
                    print "O armário já está fechado !"
            else:
                print "Você não está na frente do armário"
        else:
            print "Você não está na cozinha !"
        
    def pegarPanela(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Armário'):
                if (self.armarioAberto):
                    if (self.pegouSal):
                        print "Você guardou o sal !"
                        self.pegouSal = False
                    if (self.pegouPrato):
                        print "Você guardou o prato !"
                        self.pegouPrato = False
                    if (self.pegouOvo):
                        print "Você derrubou o ovo no chão, pegue outro ovo !"
                        self.pegouOvo = False
                    print "Pegou a panela"
                    self.pegouPanela = True
                else:
                    print "O armário está fechado !"
            else:
                print "Para pegar a panela, você deve estar de frente ao armário !"
        else:
            print "Você não está na cozinha !"
        
    def pegarSal(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Armário'):
                if (self.armarioAberto):
                    if (self.pegouPanela):
                        print "Você guardou a panela !"
                        self.pegouPanela = False
                    if (self.pegouPrato):
                        print "Você guardou o prato !"
                        self.pegouPrato = False
                    if (self.pegouOvo):
                        print "Você derrubou o ovo no chão, pegue outro ovo !"
                        self.pegouOvo = False
                    print "Pegou o sal"
                    self.pegouSal = True
                else:
                    print "O armário está fechado !"
            else:
                print "Para pegar o sal, você deve estar de frente ao armário !"
        else:
            print "Você não está na cozinha !"
        
    def pegarPrato(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Armário'):
                if (self.armarioAberto):
                    if (self.pegouSal):
                        print "Você guardou o sal !"
                        self.pegouSal = False
                    if (self.pegouPanela):
                        print "Você guardou a panela !"
                        self.pegouPanela = False
                    if (self.pegouOvo):
                        print "Você derrubou o ovo no chão, pegue outro ovo !"
                        self.pegouOvo = False
                    print "Pegou o prato"
                    self.pegouPrato = True
                else:
                    print "O armário está fechado !"
            else:
                print "Para pegar o sal, você deve estar de frente ao armário !"
        else:
            print "Você não está na cozinha !"
        
    def abrirGeladeira(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Geladeira'):
                self.geladeiraAberta = True
                print "Abriu a geladeira"
            else:
                print "Você não está na frente da geladeira"
        else:
            print "Você não está na cozinha !"
            
    def fecharGeladeira(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Geladeira'):
                if (self.geladeiraAberta):
                    self.geladeiraAberta = False
                    print "Fechou a geladeira"
                else:
                    print "A geladeira já está fechada !"
            else:
                print "Você não está na frente da geladeira"
        else:
            print "Você não está na cozinha !"
        
    def pegarOvo(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Geladeira'):
                if (self.geladeiraAberta):
                    if (self.pegouSal):
                        print "Você derrubou o sal no chão, pegue mais sal !"
                        self.pegouSal = False
                    if (self.pegouPanela):
                        print "Você derrubou a panela no chão, pegue outra panela !"
                        self.pegouPanela = False
                    if (self.pegouPrato):
                        print "Você derrubou o prato no chão, pegue outro prato !"
                        self.pegouPrato = False
                    print "Pegou o ovo"
                    self.pegouOvo = True
                else:
                    print "A geladeira está fechada !"
            else:
                print "Você não está na frente da geladeira"
        else:
            print "Você não está na cozinha !"
        
    def colocarPanelaNoFogao(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Fogão'):
                if (self.pegouPanela):
                    if (self.panelaNoFogao):
                        print "Já tem uma panela no fogão !"
                    else:
                        print "Panela colocada no fogão"
                        self.pegouPanela   = False
                        self.panelaNoFogao = True
                else:
                    print "Você não pegou a panela !"
            else:
                print "Você não está na frente do fogão"
        else:
            print "Você não está na cozinha !"
    
    def quebrarOvoDentroDaPanela(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Fogão'):
                if (self.panelaNoFogao):
                    if (self.pegouOvo):
                        if (self.quebrouOvoPanela):
                            print "Já tem um ovo dentro da panela"
                        else:
                            print "Quebrou o ovo dentro da panela"
                            self.quebrouOvoPanela = True
                            self.tempoCozimento   = 10
                        self.pegouOvo = False
                    else:
                        print "Você não pegou o ovo !"
                else:
                    print "A panela não está no fogão"
            else:
                print "Você não está na frente do fogão"
        else:
            print "Você não está na cozinha !"

    def ligarFogao(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Fogão'):
                if (self.fogaoLigado):
                    print "O fogão já está ligado"
                else:
                    print "Fogão ligado"
                    self.fogaoLigado = True
                    if (self.quebrouOvoPanela):
                        self.tempoCozimento = 10
            else:
                print "Você não está na frente do fogão"
        else:
            print "Você não está na cozinha !"
            
    def desligarFogao(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Fogão'):
                if (not self.fogaoLigado):
                    print "O fogão já está desligado"
                else:
                    print "Fogão desligado"
                    self.fogaoLigado    = False
                    self.tempoCozimento = 10
            else:
                print "Você não está na frente do fogão"
        else:
            print "Você não está na cozinha !"
    
    def colocarSal(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Fogão'):
                if (self.panelaNoFogao):
                    if (self.pegouSal):
                        if (self.colocouSal):
                            print "Você já colocou sal !"
                            self.pegouSal = False
                        else:
                            if (self.quebrouOvoPanela):
                                print "Sal colocado sobre o ovo !"
                                self.colocouSal = True
                                self.pegouSal   = False
                            else:
                                print "Não tem um ovo na panela ! Coloque o ovo primeiro."
                    else:
                        print "Você não pegou o sal !"
                else:
                    print "A panela não está no fogão"
            else:
                print "Você não está na frente do fogão"
        else:
            print "Você não está na cozinha !"
    
    def jaEstaPronto(self):
        if (self.quebrouOvoPanela and self.tempoCozimento > 0 and self.fogaoLigado):
            self.tempoCozimento -= 1
            time.sleep(1)
        if self.tempoCozimento == 0:
            self.ovoPronto = True
        
        return self.ovoPronto
        
    def colocarOvoNoPrato(self):
        if (self.sala.nome == 'Cozinha'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Fogão'):
                if (self.panelaNoFogao):
                    if (self.quebrouOvoPanela):
                        if (self.ovoPronto):
                            print "Ovo colocado dentro do prato !"
                            self.ovoNoPrato = True
                        else:
                            print "O ovo ainda não está pronto !"
                    else:
                        print "Você ainda não quebrou o ovo dentro da panela !"
                else:
                    print "A panela não está no fogão"
            else:
                print "Você não está na frente do fogão"
        else:
            print "Você não está na cozinha !"
            
    def colocarPratoNaMesa(self):
        if (self.sala.nome == 'Sala de Jantar'):
            item = self.__getItem()
            if (item is not None and item.nome == 'Mesa'):
                if (self.ovoNoPrato):
                    print "Prato colocado sobre a mesa."
                    self.pratoNaMesa = True
                else:
                    print "Você não está segurando o prato com o ovo pronto dentro !"
            else:
                print "Você não está na frente da mesa !"
        else:
            print "Você não está na sala de jantar !"
            
    def exibirResumo(self):
        infracoes = 0
        
        if self.armarioAberto: 
            print "Você deixou o armário aberto !"
            infracoes += 1
        if self.geladeiraAberta:
            print "Você deixou a geladeira aberta !"
            infracoes += 1
        if not self.panelaNoFogao:
            print "Você não colocou a panela no fogão !"
            infracoes += 1
        if not self.quebrouOvoPanela:
            print "Você não quebrou o ovo dentro da panela !"
            infracoes += 1
        if not self.colocouSal:
            print "Você não colocou sal no ovo !"
            infracoes += 1
        if self.fogaoLigado:
            print "O fogão está ligado !"
            infracoes += 1
        if not self.ovoPronto:
            print "O ovo não ficou pronto !"
            infracoes += 1
        if not self.ovoNoPrato:
            print "Você não colocou o ovo no prato !"
            infracoes += 1
        if not self.pratoNaMesa:
            print "Você não colocou o ovo pronto sobre a mesa !"
            infracoes += 1
        
        print "----------------------------------------------------------------"
        print "Você cometeu", infracoes, "infrações !"
        
        if infracoes == 0:
            print "Parabéns, você conseguiu !!!"

salaJantar = Sala("Sala de Jantar")
cozinha    = Sala("Cozinha")

salaJantar.adicionarItem(Item("Mesa", Posicao(5, 0)))
salaJantar.adicionarItem(Porta("Porta da Cozinha", Posicao(5, 10), cozinha, Posicao(5, 0)))

cozinha.adicionarItem(Item("Armário",   Posicao(10, 5)))
cozinha.adicionarItem(Item("Geladeira", Posicao(5, 10)))
cozinha.adicionarItem(Item("Fogão",     Posicao(0, 5)))
cozinha.adicionarItem(Porta("Porta da Sala de Jantar", Posicao(5, 0), salaJantar, Posicao(5, 10)))

cozinheiro = Jogador(Posicao(5, 5), salaJantar)