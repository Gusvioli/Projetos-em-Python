"""Jogo criado de Blackjack em python"""
from random import randint


class Blackjack(object):

    def __init__(self):
        pass

    def nome_jogo(self):
        print("\033[31mJOGO BlACKJACK\033[m")

    def baralho(self):
        self.dic_b = {"2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9, "10♥": 10, "A♥": 0, "J♥": 10, "Q♥": 10,
                      "K♥": 10, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "A♣": 0, "J♣": 10,
                      "Q♣": 10, "K♣": 10, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "8♠": 8, "9♠": 9, "10♠": 10, "A♠": 0,
                      "J♠": 10, "Q♠": 10, "K♠": 10, "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "8♦": 8, "9♦": 9, "10♦": 10,
                      "A♦": 0, "J♦": 10, "Q♦": 10, "K♦": 10}

        return self.dic_b

    def menu_opcoes(self):
        self.opcoes = {">> Sair": 0, ">> Recusar": 1, ">> Carta": 2, ">> Dobrar": 3, ">> Dividir": 4, ">> Min.": 5, ">> Max.": 6,
                       ">> Apostar": 7, ">> Seguro": 8}

        return self.opcoes

    def resultado(self, val, opcoes):
        self.dic_b = val
        self.li_B = list(self.dic_b)
        self.dic_b_novo_crouper_menu = {}
        self.dic_b_novo_crouper = {}
        self.dic_b_novo_jogador = {}
        self.dic_b_novo_jogador_aposta = {}
        self.dic_b_novo_crouper_soma = []
        self.dic_b_novo_jogador_soma = []
        self.loop_msg = []
        self._up_reaposta_entrada_jogador_li = [0]
        self._up_reaposta_entrada_crouper_li = [0]
        self.cartera_jogador = [5000]
        self.quem_ganhou = [3]
        self.dic_b_novo_li_jogador_A = ["A♠", "A♦", "A♥", "A♣"]
        self.msg_divisao = []

        while True:

            # Gerar cartas do Crouper com 1 baralho
            x = 0
            while x <= 1:
                while True:
                    self.ranint = randint(0, 51)
                    self.indice_crouper = self.li_B[self.ranint]
                    self.valor_crouper = self.dic_b[self.indice_crouper]
                    if self.indice_crouper in self.dic_b_novo_crouper:
                        continue
                    else:
                        self.ind_val_format = {"{}".format(
                            self.indice_crouper): self.valor_crouper}
                        self.dic_b_novo_crouper.update(self.ind_val_format)
                        break
                x = x + 1

            # Gerar cartas do Jogador com 1 baralho
            x = 0
            while x <= 1:
                while True:
                    self.ranint = randint(0, 51)
                    self.indice_jogador = self.li_B[self.ranint]
                    self.valor_jogador = self.dic_b[self.indice_jogador]
                    if self.indice_jogador in self.dic_b_novo_jogador:
                        continue
                    else:
                        self.ind_val_format = {"{}".format(
                            self.indice_jogador): self.valor_jogador}
                        self.dic_b_novo_jogador.update(self.ind_val_format)
                        break
                x = x + 1

            self._up_aposta = opcoes
            self._up_aposta_lista = list(self._up_aposta)
            self.lista_valor_aposta = [3, 5, 10, 20, 50, 100]
            # ">> Sair":0 ">> Rcusar":1 ">> Carta":2 ">> Dobrar":3 ">> Dividir":4 ">> Min.":5 ">> Max.":6 ">> Apostar":7

            self.dic_b_novo_crouper_menu.update(self._up_aposta)

            print("Faça sua aposta: ")
            print("\033[36mSua Carteira inicial:\033[m ${}".format(
                self.cartera_jogador[0]))
            self._up_aposta_entrada_jogador_ = \
                input("\033[34m{}\033[m(1)\n\033[34m{}\033[m(2)\n\033[34m{}\033[m(3, 5, 10, 20, 50 ou 100)\n".format(
                    self._up_aposta_lista[5],
                    self._up_aposta_lista[6],
                    self._up_aposta_lista[7]))

            if int(self._up_aposta_entrada_jogador_) == 1:
                self._up_aposta_entrada_jogador_in = {
                    "{}".format("Aposta"): min(self.lista_valor_aposta)}
                self.dic_b_novo_jogador_aposta.update(
                    self._up_aposta_entrada_jogador_in)
                break
            elif int(self._up_aposta_entrada_jogador_) == 2:
                self._up_aposta_entrada_jogador_in = {
                    "{}".format("Aposta"): max(self.lista_valor_aposta)}
                self.dic_b_novo_jogador_aposta.update(
                    self._up_aposta_entrada_jogador_in)
                break
            else:
                if int(self._up_aposta_entrada_jogador_) in self.lista_valor_aposta:
                    self._up_aposta_entrada_jogador_in = {
                        "{}".format("Aposta"): self._up_aposta_entrada_jogador_}
                    self.dic_b_novo_jogador_aposta.update(
                        self._up_aposta_entrada_jogador_in)
                    break
                else:
                    print(
                        "\033[31mO valor digitado não é uma aposta válida.\033[m")
                    continue
        if self._up_aposta_entrada_jogador_ == "1":
            self.cartera_jogador.append(
                self.cartera_jogador[0] - min(self.lista_valor_aposta))

        elif self._up_aposta_entrada_jogador_ == "2":
            self.cartera_jogador.append(
                self.cartera_jogador[0] - max(self.lista_valor_aposta))

        else:
            self.cartera_jogador.append(
                self.cartera_jogador[0]-int(self._up_aposta_entrada_jogador_))

        self.dic_b_novo_li_crouper = list(self.dic_b_novo_crouper.items())
        self.dic_b_novo_li_jogador = list(self.dic_b_novo_jogador.items())
        self.dic_b_novo_li_jogador_aposta = list(
            self.dic_b_novo_jogador_aposta.items())

        # Verificação da carta do baralho Ás e seus valores para o crouper
        if self.dic_b_novo_li_crouper[0][0] in self.dic_b_novo_li_jogador_A:
            if self.dic_b_novo_li_crouper[0][1] + self.dic_b_novo_li_crouper[1][1] >= 21:
                self.dic_b_novo_crouper[self.dic_b_novo_li_crouper[0][0]] = 1
            else:
                self.dic_b_novo_crouper[self.dic_b_novo_li_crouper[0][0]] = 11

        if self.dic_b_novo_li_crouper[1][0] in self.dic_b_novo_li_jogador_A:
            if self.dic_b_novo_li_crouper[0][1] + self.dic_b_novo_li_crouper[1][1] >= 21:
                self.dic_b_novo_crouper[self.dic_b_novo_li_crouper[1][0]] = 1
            else:
                self.dic_b_novo_crouper[self.dic_b_novo_li_crouper[1][0]] = 11

        self.dic_b_novo_li_crouper = list(self.dic_b_novo_crouper.items())
        self.dic_b_novo_crouper_soma.append(
            self.dic_b_novo_li_crouper[0][1] + self.dic_b_novo_li_crouper[1][1])

        # Verificação da carta do baralho Ás e seus valores para o jogador
        if self.dic_b_novo_li_jogador[0][0] in self.dic_b_novo_li_jogador_A:
            if self.dic_b_novo_li_jogador[0][1] + self.dic_b_novo_li_jogador[1][1] >= 21:
                self.dic_b_novo_jogador[self.dic_b_novo_li_jogador[0][0]] = 1
            else:
                self.dic_b_novo_jogador[self.dic_b_novo_li_jogador[0][0]] = 11

        if self.dic_b_novo_li_jogador[1][0] in self.dic_b_novo_li_jogador_A:
            if self.dic_b_novo_li_jogador[0][1] + self.dic_b_novo_li_jogador[1][1] >= 21:
                self.dic_b_novo_jogador[self.dic_b_novo_li_jogador[1][0]] = 1
            else:
                self.dic_b_novo_jogador[self.dic_b_novo_li_jogador[1][0]] = 11

        self.dic_b_novo_li_jogador = list(self.dic_b_novo_jogador.items())
        self.dic_b_novo_jogador_soma.append(
            self.dic_b_novo_li_jogador[0][1] + self.dic_b_novo_li_jogador[1][1])

        self.loop_stop = [1]
        zz = 1
        while True:
            # Conta qtas vz o loop aconteceu
            self.loop_msg.append(zz)
            zz = zz + 1

            if self.loop_stop[0] == 1:

                print("---------------------------------------------------------")
                # Exibição da msg no jogo do crouper

                if self._up_reaposta_entrada_jogador_li[0] == 1:
                    if self.dic_b_novo_crouper_soma[0] < 21:
                        self.ranint = randint(0, 51)
                        self.indice_crouper = self.li_B[self.ranint]
                        self.valor_crouper = self.dic_b[self.indice_crouper]
                        self.ind_val_format = {"{}".format(
                            self.indice_crouper): self.valor_crouper}
                        self.ind_val_format_li = list(self.ind_val_format)
                        self.dic_b_novo_crouper_soma[0] = self.dic_b_novo_crouper_soma[0] + \
                            self.valor_crouper
                        self.dic_b_novo_li_crouper.append(
                            self.ind_val_format_li)

                print("\033[33mCartas do Crouper:\033[m")
                if self._up_reaposta_entrada_jogador_li[0] == 0 or self._up_reaposta_entrada_jogador_li[0] >= 2:
                    print("Carta 1: {0}".format(
                        self.dic_b_novo_li_crouper[0][0]))
                    print("Carta 2: **")
                    print("\033[1mSoma: {}\033[m".format(
                        self.dic_b_novo_li_crouper[0][1]))
                else:
                    yy = 0
                    for y in self.dic_b_novo_li_crouper:
                        if y in self.dic_b_novo_li_crouper:
                            print("Carta {0}: {1}".format(yy + 1, y[0]))

                        yy += 1

                    if self.dic_b_novo_crouper_soma[0] > 21:
                        print("\033[1mSoma: {}\033[m \033[31mESTOROU\033[m!".format(
                            self.dic_b_novo_crouper_soma[0]))
                        self.quem_ganhou[0] = 1
                        self.loop_stop[0] = 0

                    elif self.dic_b_novo_crouper_soma[0] == 21:
                        print("\033[1mSoma: {}\033[m \033[33mBLACKJACK!!\033[m!".format(
                            self.dic_b_novo_crouper_soma[0]))
                        self.quem_ganhou[0] = 0
                    else:
                        print("\033[1mSoma: {}\033[m ".format(
                            self.dic_b_novo_crouper_soma[0]))

                # Espaço de separação entre as msgs
                print("")

                # Exibição da msg no jogo do Jogador
                print("\033[36mCarteira:\033[m ${}".format(
                    self.cartera_jogador[len(self.cartera_jogador)-1]))
                print("\033[33mSuas cartas:\033[m")
                print("Aposta: ${0}".format(
                    self.dic_b_novo_jogador_aposta["Aposta"]))

                if self._up_reaposta_entrada_jogador_li[0] != 4:
                    xx = 0
                    for x in self.dic_b_novo_li_jogador:
                        if x in self.dic_b_novo_li_jogador:
                            print("Carta {0}: {1}".format(xx+1, x[0]))

                        xx += 1
                else:

                    xxx = 0
                    while xxx <= 1:
                        self.ranint = randint(0, 51)
                        self.indice_jogador = self.li_B[self.ranint]
                        self.valor_jogador = self.dic_b[self.indice_jogador]
                        self.ind_val_format = {"{}".format(
                            self.indice_jogador): self.valor_jogador}
                        self.dic_b_novo_jogador.update(self.ind_val_format)
                        xxx = xxx + 1

                    self.dic_b_novo_li_jogador = list(
                        self.dic_b_novo_jogador.items())

                    print("")
                    print("Divisão 1: ")
                    xx = 0
                    for x in self.dic_b_novo_li_jogador:
                        if x in self.dic_b_novo_li_jogador:
                            if xx % 2 == 0:
                                print("Carta {0}: {1}".format(xx+1, x[0]))

                        xx += 1
                    self.soma_divisao1 = self.dic_b_novo_li_jogador[0][1] + \
                        self.dic_b_novo_li_jogador[2][1]
                    print("\033[1mSoma: {}\033[m".format(self.soma_divisao1))
                    print("")
                    print("Divisão 2: ")
                    xx = 0
                    for x in self.dic_b_novo_li_jogador:
                        if x in self.dic_b_novo_li_jogador:
                            if xx % 2 != 0:
                                print("Carta {0}: {1}".format(xx+1, x[0]))

                        xx += 1
                    self.soma_divisao2 = self.dic_b_novo_li_jogador[1][1] + \
                        self.dic_b_novo_li_jogador[3][1]
                    print("\033[1mSoma: {}\033[m".format(self.soma_divisao2))
                    print("")

                if self.dic_b_novo_jogador_soma[0] > 21:
                    print("\033[1mSoma: {}\033[m \033[31mESTOROU\033[m!".format(
                        self.dic_b_novo_jogador_soma[0]))
                    self.quem_ganhou[0] = 0
                    self.loop_stop[0] = 0

                elif self.dic_b_novo_jogador_soma[0] == 21:
                    print("\033[1mSoma: {}/21\033[m \033[33mBLACKJACK!!\033[m!".format(
                        self.dic_b_novo_crouper_soma[0]))
                    self.quem_ganhou[0] = 1
                else:
                    if self._up_reaposta_entrada_jogador_li[0] != 4:
                        print("\033[1mSoma: {}\033[m".format(
                            self.dic_b_novo_jogador_soma[0]))
                    else:
                        pass

                if self._up_reaposta_entrada_jogador_li[0] == 1:
                    if self.dic_b_novo_crouper_soma[0] > self.dic_b_novo_jogador_soma[0] \
                            and self.dic_b_novo_crouper_soma[0] < 21:
                        self.quem_ganhou[0] = 0

                    if self.dic_b_novo_jogador_soma[0] > self.dic_b_novo_crouper_soma[0] \
                            and self.dic_b_novo_jogador_soma[0] < 21:
                        self.quem_ganhou[0] = 1

                print("")
                if self.quem_ganhou[0] == 0:
                    print("\033[35mCROUPER GANHOU!!\033[m!")
                    self.cartera_jogador.append(self.cartera_jogador[len(
                        self.cartera_jogador)-1]+int(self.dic_b_novo_li_jogador_aposta[0][1]))
                    self.soma_resu_aposta = self.cartera_jogador[1]
                    print("\033[36mSua Carteira atualizada é:\033[m ${}".format(
                        self.soma_resu_aposta))
                    break

                if self.quem_ganhou[0] == 1:
                    print("\033[35mVOCÊ GANHOU!!\033[m!")
                    self.cartera_jogador.append(self.cartera_jogador[len(
                        self.cartera_jogador)-1]+int(self.dic_b_novo_li_jogador_aposta[0][1]))
                    self.soma_resu_aposta = self.dic_b_novo_jogador_aposta["Aposta"] + \
                        self.cartera_jogador[1]
                    print("\033[36mSua Carteira atualizada é:\033[m ${}".format(
                        self.soma_resu_aposta))
                    break

                print("")

                if self.dic_b_novo_li_jogador.__len__() == 4:
                    yyy = 0
                    while yyy <= 1:
                        if yyy == 0:
                            print("Divisão 1: ")
                        else:
                            print("Duvisão 2: ")
                        if self.dic_b_novo_li_crouper[0][0] in self.dic_b_novo_li_jogador_A \
                                and self.dic_b_novo_li_jogador[0][1] % 2 == 0 \
                                and self.dic_b_novo_li_jogador[1][1] % 2 == 0:
                            if self.loop_msg.__len__() == 1:
                                self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                           "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                           "\033[34m{4}\033[m(4)\n\033[34m{5}\033[m(5)\n".format(
                                                                               self._up_aposta_lista[1], self._up_aposta_lista[
                                                                                   2], self.dic_b_novo_jogador_aposta["Aposta"],
                                                                               self._up_aposta_lista[3], self._up_aposta_lista[4], self._up_aposta_lista[8]))
                            else:
                                self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                           "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                           "\033[34m{4}\033[m(4)\n".format(
                                                                               self._up_aposta_lista[1], self._up_aposta_lista[
                                                                                   2], self.dic_b_novo_jogador_aposta["Aposta"],
                                                                               self._up_aposta_lista[3], self._up_aposta_lista[8]))

                        elif self.dic_b_novo_li_jogador[0][1] % 2 == 0 and self.dic_b_novo_li_jogador[1][1] % 2 == 0:

                            if self.loop_msg.__len__() == 1:
                                self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                           "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                           "\033[34m{4}\033[m(4)\n".format(
                                                                               self._up_aposta_lista[1], self._up_aposta_lista[
                                                                                   2], self.dic_b_novo_jogador_aposta["Aposta"],
                                                                               self._up_aposta_lista[3], self._up_aposta_lista[4]))
                            else:
                                self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                           "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n".format(
                                                                               self._up_aposta_lista[1], self._up_aposta_lista[
                                                                                   2], self.dic_b_novo_jogador_aposta["Aposta"],
                                                                               self._up_aposta_lista[3]))

                        elif self.dic_b_novo_li_crouper[0][0] in self.dic_b_novo_li_jogador_A:

                            if self.loop_msg.__len__() == 1:
                                self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                           "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                           "\033[34m{4}\033[m(2)\n".format(
                                                                               self._up_aposta_lista[1], self._up_aposta_lista[
                                                                                   2], self.dic_b_novo_jogador_aposta["Aposta"],
                                                                               self._up_aposta_lista[3], self._up_aposta_lista[8]))

                        else:
                            self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n""\033[34m{1}\033[m(2)\n"
                                                                       "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n".format(
                                                                           self._up_aposta_lista[1], self._up_aposta_lista[
                                                                               2], self.dic_b_novo_jogador_aposta["Aposta"],
                                                                           self._up_aposta_lista[3]))
                        yyy = yyy + 1

                        self.msg_divisao.append(
                            self._up_reaposta_entrada_jogador_)

                else:
                    if self.dic_b_novo_li_crouper[0][0] in self.dic_b_novo_li_jogador_A \
                            and self.dic_b_novo_li_jogador[0][1] % 2 == 0 \
                            and self.dic_b_novo_li_jogador[1][1] % 2 == 0:
                        if self.loop_msg.__len__() == 1:
                            self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                       "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                       "\033[34m{4}\033[m(4)\n\033[34m{5}\033[m(5)\n".format(
                                                                           self._up_aposta_lista[1], self._up_aposta_lista[2],
                                                                           self.dic_b_novo_jogador_aposta["Aposta"],
                                                                           self._up_aposta_lista[3], self._up_aposta_lista[4], self._up_aposta_lista[8]))
                        else:
                            self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                       "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                       "\033[34m{4}\033[m(4)\n".format(
                                                                           self._up_aposta_lista[1], self._up_aposta_lista[2],
                                                                           self.dic_b_novo_jogador_aposta["Aposta"],
                                                                           self._up_aposta_lista[3], self._up_aposta_lista[8]))

                    elif self.dic_b_novo_li_jogador[0][1] % 2 == 0 and self.dic_b_novo_li_jogador[1][1] % 2 == 0:

                        if self.loop_msg.__len__() == 1:
                            self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                       "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                       "\033[34m{4}\033[m(4)\n".format(
                                                                           self._up_aposta_lista[1], self._up_aposta_lista[2],
                                                                           self.dic_b_novo_jogador_aposta["Aposta"],
                                                                           self._up_aposta_lista[3], self._up_aposta_lista[4]))
                        else:
                            self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                       "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n".format(
                                                                           self._up_aposta_lista[1], self._up_aposta_lista[2],
                                                                           self.dic_b_novo_jogador_aposta["Aposta"],
                                                                           self._up_aposta_lista[3]))

                    elif self.dic_b_novo_li_crouper[0][0] in self.dic_b_novo_li_jogador_A:

                        if self.loop_msg.__len__() == 1:
                            self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n\033[34m{1}\033[m(2)\n"
                                                                       "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n"
                                                                       "\033[34m{4}\033[m(2)\n".format(
                                                                           self._up_aposta_lista[1], self._up_aposta_lista[2],
                                                                           self.dic_b_novo_jogador_aposta["Aposta"],
                                                                           self._up_aposta_lista[3], self._up_aposta_lista[8]))

                    else:
                        self._up_reaposta_entrada_jogador_ = input("\033[34m{0}\033[m(1)\n""\033[34m{1}\033[m(2)\n"
                                                                   "\033[34m{3}\033[m \033[31m${2} x2\033[m(3)\n".format(
                                                                       self._up_aposta_lista[1], self._up_aposta_lista[2],
                                                                       self.dic_b_novo_jogador_aposta["Aposta"],
                                                                       self._up_aposta_lista[3]))

                self._up_reaposta_entrada_jogador_li[0] = int(
                    self._up_reaposta_entrada_jogador_)
                if self._up_reaposta_entrada_jogador_li[0] == 3:
                    self.multipli = {"{}".format(
                        "Aposta"): self.dic_b_novo_jogador_aposta["Aposta"]*2}
                    self.dic_b_novo_jogador_aposta.update(self.multipli)

                    self.ranint = randint(0, 51)
                    self.indice_jogador = self.li_B[self.ranint]
                    self.valor_jogador = self.dic_b[self.indice_jogador]
                    self.ind_val_format = {"{}".format(
                        self.indice_jogador): self.valor_jogador}
                    self.ind_val_format_li = list(self.ind_val_format)
                    self.dic_b_novo_jogador_soma[0] = self.dic_b_novo_jogador_soma[0] + \
                        self.valor_jogador
                    self.dic_b_novo_li_jogador.append(self.ind_val_format_li)

                if self._up_reaposta_entrada_jogador_li[0] == 2:

                    self.ranint = randint(0, 51)
                    self.indice_jogador = self.li_B[self.ranint]
                    self.valor_jogador = self.dic_b[self.indice_jogador]
                    self.ind_val_format = {"{}".format(
                        self.indice_jogador): self.valor_jogador}
                    self.ind_val_format_li = list(self.ind_val_format)
                    self.dic_b_novo_jogador_soma[0] = self.dic_b_novo_jogador_soma[0] + \
                        self.valor_jogador
                    self.dic_b_novo_li_jogador.append(self.ind_val_format_li)


Blackjack().nome_jogo()
menu_opcoes = Blackjack().menu_opcoes()
baralho_f = Blackjack().baralho()
Blackjack().resultado(baralho_f, menu_opcoes)
