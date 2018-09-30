from tkinter import *
import os

j_cal = Tk()


def lb():
    lb_inicial = Label(j_cal, font=("Verdana", 36), anchor="e", width="11", height="2", text="", bg="#838a80")
    lb_inicial.place(x=7, y=33)
    return lb_inicial


def li_(valor):
    lis = []
    lis_0 = lis.append(valor)
    return lis_0


def acao_inicial_del():
    pass


def acao_inicial():
    lb()
    o = open("hist_a_i.txt", "r")
    lb_in = o.read()
    ler = lb_in
    o.close()
    if len(lb_in) <= 10:
        lb()["text"] = ler
    else:
        Label(lb(), text=ler, font=("Verdana", 20), anchor="e", width="19", height="2", bg="#838a80").place(x=3, y=33)


def trava_acao_ini():
    ooss = open("hist_a_i.txt", "a")
    ooss.write("")
    ooss.close()
    oss = open("hist_a_i.txt", "r")
    o_so = oss.read()
    oss.close()
    if len(o_so) == 19:
        return True
    else:
        return False


def formatar_pontos(em):
    em


def acao_0():
    if trava_acao_ini() == False:
        zero = open("hist_a_i.txt", "r")
        ze = zero.read()
        zero.close()
        if ze != "0":
            te = btn_0["text"]
            o = open("hist_a_i.txt", "a")
            o.write(te)
            o.close()
            acao_inicial()


def acao_1():
    if trava_acao_ini() == False:
        te = btn_1["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_2():
    if trava_acao_ini() == False:
        te = btn_2["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_3():
    if trava_acao_ini() == False:
        te = btn_3["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_4():
    if trava_acao_ini() == False:
        te = btn_4["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_5():
    if trava_acao_ini() == False:
        te = btn_5["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_6():
    if trava_acao_ini() == False:
        te = btn_6["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_7():
    if trava_acao_ini() == False:
        te = btn_7["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_8():
    if trava_acao_ini() == False:
        te = btn_8["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_9():
    if trava_acao_ini() == False:
        te = btn_9["text"]
        o = open("hist_a_i.txt", "a")
        o.write(te)
        o.close()
        acao_inicial()


def acao_mais():
    if trava_acao_ini() == False:
        if os.path.isfile('hist_a_i.txt'):
            o = open("hist_a_i.txt", "r")
            re = o.read()
            o.close()
            te = btn_mais["text"]
            if re[::-1][0] != te:
                o = open("hist_a_i.txt", "a")
                o.write(te)
                o.close()
                acao_inicial()


def acao_menos():
    if trava_acao_ini() == False:
        if os.path.isfile('hist_a_i.txt'):
            o = open("hist_a_i.txt", "r")
            re = o.read()
            o.close()
            te = btn_menos["text"]
            if re[::-1][0] != te:
                o = open("hist_a_i.txt", "a")
                o.write(te)
                o.close()
                acao_inicial()


def acao_vezes():
    if trava_acao_ini() == False:
        if os.path.isfile('hist_a_i.txt'):
            o = open("hist_a_i.txt", "r")
            re = o.read()
            o.close()
            te = btn_vezes["text"]
            if re[::-1][0] != te:
                o = open("hist_a_i.txt", "a")
                o.write(te)
                o.close()
                acao_inicial()


def acao_divisao():
    if trava_acao_ini() == False:
        if os.path.isfile('hist_a_i.txt'):
            o = open("hist_a_i.txt", "r")
            re = o.read()
            o.close()
            te = btn_divisao["text"]
            if re[::-1][0] != te:
                o = open("hist_a_i.txt", "a")
                o.write(te)
                o.close()
                acao_inicial()


def acao_p_cento():
    # if os.path.isfile('hist_a_i.txt'):
    pass


def acao_raiz():
    # if os.path.isfile('hist_a_i.txt'):
    pass


def acao_virgula():
    if trava_acao_ini() == False:
        if os.path.isfile('hist_a_i.txt'):
            o = open("hist_a_i.txt", "r")
            re = o.read()
            o.close()
            te = btn_virgula["text"]
            if re[::-1][0] != te:
                o = open("hist_a_i.txt", "a")
                o.write(te)
                o.close()
                acao_inicial()


def acao_C():
    if os.path.isfile('hist_a_i.txt'):
        os.remove("hist_a_i.txt")
        c = open("hist_a_i.txt", "a")
        c.write("")
        c.close()
        lb()["text"] = "0"


def acao_voltar_espaco():
    if os.path.isfile('hist_a_i.txt'):
        o = open("hist_a_i.txt", "r")
        ler = o.read()
        o.close()
        li_ler = list(ler)
        tam_li_ler = len(li_ler) - 1
        li_ler.pop(tam_li_ler)
        list_li_ler = list(li_ler)
        t = ""
        for tx in list_li_ler:
            t = t + tx
        os.remove("hist_a_i.txt")

        o = open("hist_a_i.txt", "a")
        o.write(t)
        o.close()

        o = open("hist_a_i.txt", "r")
        to = o.read()
        o.close()

        if len(to) <= 10:
            lb()["text"] = to
        else:
            Label(lb(), text=ler, font=("Verdana", 20), anchor="e", width="19", height="2", bg="#838a80").place(x=3,
                                                                                                                y=33)


def historico():
    o = open("hist_a_i.txt", "r")
    ler = o.read()
    o.close()
    te = btn_igual["text"]
    ler_in_ = ler[::-1]
    if ler_in_[0] != "x" and ler_in_[0] != "/" and ler_in_[0] != "+" and ler_in_[0] != "-":
        o = open("historico.txt", "a")
        ler_te = "{}{}".format(ler, te)
        o.write(ler_te)
        o.close()
        acao_inicial()
    else:
        lb()["text"] = "0"


def acao_igual():
    if os.path.isfile('hist_a_i.txt'):
        historico()

        o = open("hist_a_i.txt", "r")
        ler = o.read()
        o.close()

        li_ler_rep_0 = ler.replace("x", "*")
        com_li = li_ler_rep_0.replace(",", ".")
        len_ler = len(ler)

        ler_ig = com_li[::-1]

        if ler_ig[0] != "*" or ler_ig[0] != "+" or ler_ig[0] != "/" or ler_ig[0] != "-":
            if com_li == "0/0" or com_li == "0.0/0.0" or com_li == "0.0/0" or com_li == "0/0.0":
                lb()["text"] = "Indefinido"
            elif ler_ig[0:2] == "0/":
                lb()["text"] = "Indivisivel"
            else:
                if len_ler > 10:
                    eval_ = eval(com_li)
                    eval_t = str(eval_)
                    com_li_r = eval_t.replace(".", ",")
                    com_li_0_len_0 = com_li_r[::-1]
                    com_li_0_len = com_li_0_len_0[0:2]
                    if com_li_0_len == "0,":
                        com_li_r_f = com_li_0_len_0.replace(com_li_0_len, "")
                        com_li_r_f = com_li_r_f[::-1]
                        Label(lb(), text=com_li_r_f, font=("Verdana", 20), anchor="e", width="19", height="2",
                              bg="#838a80").place(x=3, y=33)

                        te_lb = com_li_r_f
                        o = open("historico.txt", "a")
                        ler_te = "\n{}\n".format(te_lb)
                        o.write(ler_te)
                        o.close()
                    else:
                        Label(lb(), text=com_li_r, font=("Verdana", 20), anchor="e", width="19", height="2",
                              bg="#838a80").place(x=3, y=33)

                        te_lb = com_li_r
                        o = open("historico.txt", "a")
                        ler_te = "\n{}\n".format(te_lb)
                        o.write(ler_te)
                        o.close()
                elif len_ler <= 10:
                    eval_ = eval(com_li)
                    eval_t = str(eval_)
                    com_li_r = eval_t.replace(".", ",")
                    com_li_0_len_0 = com_li_r[::-1]
                    com_li_0_len = com_li_0_len_0[0:2]
                    if com_li_0_len == "0,":
                        com_li_r_f = com_li_0_len_0.replace(com_li_0_len, "")
                        com_li_r_f = com_li_r_f[::-1]
                        lb()["text"] = com_li_r_f
                        te_lb = com_li_r_f
                        o = open("historico.txt", "a")
                        ler_te = "\n{}\n".format(te_lb)
                        o.write(ler_te)
                        o.close()

                    else:
                        lb()["text"] = com_li_r
                        te_lb = com_li_r
                        o = open("historico.txt", "a")
                        ler_te = "\n{}\n".format(te_lb)
                        o.write(ler_te)
                        o.close()

        Label(lb(), font=("Verdana", 14), anchor="ne", width="27", height="1", text="{}= ".format(ler),
              bg="#838a80").grid()


btn_hist = Button(font=("Verdana", 10), width="8", text="Histórico")
btn_hist["bg"] = "#dbe8d4"
btn_hist["bd"] = 1
btn_hist.place(x=10, y=2)

btn_raiz = Button(font=("Verdana", 22), width="4", text="√", command=acao_raiz)
btn_raiz["bg"] = "#dbe8d4"
btn_raiz["bd"] = 1
btn_raiz.place(x=10, y=430)

btn_0 = Button(font=("Verdana", 22), width="4", text="0", command=acao_0)
btn_0["bg"] = "#afd19c"
btn_0["bd"] = 1
btn_0.place(x=93, y=430)

btn_virgula = Button(font=("Verdana", 22), width="4", text=",", command=acao_virgula)
btn_virgula["bg"] = "#dbe8d4"
btn_virgula["bd"] = 1
btn_virgula.place(x=176, y=430)

btn_igual = Button(font=("Verdana", 22), width="4", text="=", command=acao_igual)
btn_igual["bg"] = "#dbe8d4"
btn_igual["bd"] = 1
btn_igual.place(x=259, y=430)

btn_1 = Button(font=("Verdana", 22), width="4", text="1", command=acao_1)
btn_1["bg"] = "#afd19c"
btn_1["bd"] = 1
btn_1.place(x=10, y=365)

btn_2 = Button(font=("Verdana", 22), width="4", text="2", command=acao_2)
btn_2["bg"] = "#afd19c"
btn_2["bd"] = 1
btn_2.place(x=93, y=365)

btn_3 = Button(font=("Verdana", 22), width="4", text="3", command=acao_3)
btn_3["bg"] = "#afd19c"
btn_3["bd"] = 1
btn_3.place(x=176, y=365)

btn_mais = Button(font=("Verdana", 22), width="4", text="+", command=acao_mais)
btn_mais["bg"] = "#dbe8d4"
btn_mais["bd"] = 1
btn_mais.place(x=259, y=365)

btn_4 = Button(font=("Verdana", 22), width="4", text="4", command=acao_4)
btn_4["bg"] = "#afd19c"
btn_4["bd"] = 1
btn_4.place(x=10, y=300)

btn_5 = Button(font=("Verdana", 22), width="4", text="5", command=acao_5)
btn_5["bg"] = "#afd19c"
btn_5["bd"] = 1
btn_5.place(x=93, y=300)

btn_6 = Button(font=("Verdana", 22), width="4", text="6", command=acao_6)
btn_6["bg"] = "#afd19c"
btn_6["bd"] = 1
btn_6.place(x=176, y=300)

btn_menos = Button(font=("Verdana", 22), width="4", text="-", command=acao_menos)
btn_menos["bg"] = "#dbe8d4"
btn_menos["bd"] = 1
btn_menos.place(x=259, y=300)

btn_7 = Button(font=("Verdana", 22), width="4", text="7", command=acao_7)
btn_7["bg"] = "#afd19c"
btn_7["bd"] = 1
btn_7.place(x=10, y=235)

btn_8 = Button(font=("Verdana", 22), width="4", text="8", command=acao_8)
btn_8["bg"] = "#afd19c"
btn_8["bd"] = 1
btn_8.place(x=93, y=235)

btn_9 = Button(font=("Verdana", 22), width="4", text="9", command=acao_9)
btn_9["bg"] = "#afd19c"
btn_9["bd"] = 1
btn_9.place(x=176, y=235)

btn_vezes = Button(font=("Verdana", 22), width="4", text="x", command=acao_vezes)
btn_vezes["bg"] = "#dbe8d4"
btn_vezes["bd"] = 1
btn_vezes.place(x=259, y=235)

btn_p_cento = Button(font=("Verdana", 22), width="4", text="%", command=acao_p_cento)
btn_p_cento["bg"] = "#dbe8d4"
btn_p_cento["bd"] = 1
btn_p_cento.place(x=10, y=170)

btn_C = Button(font=("Verdana", 22), width="4", text="C", command=acao_C)
btn_C["bg"] = "#dbe8d4"
btn_C["bd"] = 1
btn_C.place(x=93, y=170)

btn_voltar_espaco = Button(font=("Verdana", 22), width="4", text="←", command=acao_voltar_espaco)
btn_voltar_espaco["bg"] = "#dbe8d4"
btn_voltar_espaco["bd"] = 1
btn_voltar_espaco.place(x=176, y=170)

btn_divisao = Button(font=("Verdana", 22), width="4", text="/", command=acao_divisao)
btn_divisao["bg"] = "#dbe8d4"
btn_divisao["bd"] = 1
btn_divisao.place(x=259, y=170)

j_cal.geometry("350x500+400+200")
j_cal["bg"] = "#eaf1e7"
j_cal.title("Clube do alfabeto - Calculadora")
j_cal.iconbitmap("imgs/iconcalc.ico")
j_cal.maxsize(width=350, height=500)
j_cal.minsize(width=350, height=500)
j_cal.mainloop()


def ler_grava_exclue():
    co = open("hist_a_i.txt")
    tex = ""
    for linha in co:
        linha = linha + "\n"
        tex = tex + linha
    co.close()
    co2 = open("historico.txt", "a")
    co2.write(tex)
    co2.close()

    os.remove("hist_a_i.txt")
    os.remove("historico.txt")

    co3 = open("historico.txt", "a")
    co3.write("")
    co3.close()


ler_grava_exclue()
