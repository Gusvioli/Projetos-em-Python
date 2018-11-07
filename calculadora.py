from tkinter import *
from math import floor,sqrt

j_cal = Tk()

def lb():
    lb_inicial = Label(j_cal, font=("Verdana", 36), anchor="e", width="11", height="2", text="", bg="#838a80")
    lb_inicial.place(x=7, y=33)
    return lb_inicial

lb()["text"] = "0"
li_val = []
li_val.append("0")
li_val_virg = []
li_0 = []
li_op = []

historico_dic = []

def acao_li_val_virg():
    li_val_virg.clear()

def acao_inicial_del():
    pass

def acao_inicial():
    pass

def trava_acao():
    if len(li_val) == 27:
        return True
    else:
        return False

def formatar_pontos(txt):
    def li_to_str(li):

        tx = ""
        for x in li:
            tx = tx + x
        tx = tx.replace(",",".")

        if tx.find("x"):
            tx = tx.replace("x", "*")
            return tx
        elif tx.find(","):
            tx = tx.replace(",", ".")
            return tx
        else:
            return tx


    def inverter(li_in):
        return li_in[::-1]

    def to_list(x):
        return list(x)

    def separar_vergula(txt):
        tx = txt.split(".")
        return tx

    def juntar_vergula(in_txt, in_txt2):
        i_t = "{},{}".format(in_txt, in_txt2)
        return i_t

    l_t_s_val = li_to_str(li_val)
    resulta_eval = eval(l_t_s_val)
    resulta_str = str(resulta_eval)

    if type(eval(li_to_str(resulta_str))) == int:

        resulta = str(resulta_str)
        li = inverter(to_list(resulta))
        tam_txt_div_3 = floor(len(li_to_str(resulta)) / 3)
    elif type(eval(li_to_str(resulta_str))) == float:

        resulta = str(resulta_str)
        resulta = separar_vergula(resulta)
        li = inverter(to_list(resulta[0]))
        tam_txt_div_3 = floor(len(li_to_str(resulta[0])) / 3)

    elif type(eval(li_to_str(resulta_str))) == tuple:

        resulta = str(resulta_str)
        resulta = separar_vergula(resulta)
        li = inverter(to_list(resulta[0]))
        tam_txt_div_3 = floor(len(li_to_str(resulta[0])) / 3)


    if tam_txt_div_3 == 1:
        li.insert(3, ".")
    elif tam_txt_div_3 == 2:
        li.insert(3, ".")
        li.insert(7, ".")
    elif tam_txt_div_3 == 3:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
    elif tam_txt_div_3 == 4:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
        li.insert(15, ".")
    elif tam_txt_div_3 == 5:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
        li.insert(15, ".")
        li.insert(19, ".")
    elif tam_txt_div_3 == 6:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
        li.insert(15, ".")
        li.insert(19, ".")
        li.insert(23, ".")
    elif tam_txt_div_3 == 7:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
        li.insert(15, ".")
        li.insert(19, ".")
        li.insert(23, ".")
        li.insert(27, ".")
    elif tam_txt_div_3 == 8:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
        li.insert(15, ".")
        li.insert(19, ".")
        li.insert(23, ".")
        li.insert(27, ".")
        li.insert(31, ".")
    elif tam_txt_div_3 == 9:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
        li.insert(15, ".")
        li.insert(19, ".")
        li.insert(23, ".")
        li.insert(27, ".")
        li.insert(31, ".")
        li.insert(35, ".")
    elif tam_txt_div_3 == 10:
        li.insert(3, ".")
        li.insert(7, ".")
        li.insert(11, ".")
        li.insert(15, ".")
        li.insert(19, ".")
        li.insert(23, ".")
        li.insert(27, ".")
        li.insert(31, ".")
        li.insert(35, ".")
        li.insert(39, ".")

    if li[(len(li)-1)] == ".":
        li.pop()

    li = inverter(li_to_str(li))

    if type(eval(li_to_str(resulta_str))) == int:
        return li
    elif type(eval(li_to_str(resulta_str))) == float:
        return juntar_vergula(li, resulta[1])
    elif type(eval(li_to_str(resulta_str))) == tuple:
        return juntar_vergula(li, resulta[1])

def formatar_tam(txt):
    if len(txt) <= 10:
        lb()["text"] = txt
    elif len(txt) <= 19 and len(txt) > 10:
        Label(lb(), text=txt, font=("Verdana", 20), anchor="e", width="19",
              height="2", bg="#838a80").place(x=3, y=27)
    elif len(txt) > 19 and len(txt) <= 27:
        Label(lb(), text=txt, font=("Verdana", 14), anchor="e", width="27",
              height="2", bg="#838a80").place(x=3, y=34)
    else:
        Label(lb(), text="Limite para cálculo alcançado", font=("Verdana", 14), anchor="e", width="27",
              height="2", bg="#838a80").place(x=3, y=34)

def co_list_str_tam(li_v):
    t = ""
    for i in li_v:
        t = t + i
    return formatar_tam(t)

def list_str(li_v):
    t = ""
    for i in li_v:
        t = t + i
    return t

def acao_0():
    if trava_acao() == False:
        if list_str(li_val) == "0,":
            li_val.clear()
        if li_val[0] == "0" and li_val[1] == ",":
            li_val.append(btn_0["text"])
            li_val_virg.append(btn_0["text"])
            co_list_str_tam(li_val)
        elif li_val[0] != "0":
            li_val.append(btn_0["text"])
            li_val_virg.append(btn_0["text"])
            co_list_str_tam(li_val)
        if li_val[(len(li_val) - 1)] == "+" \
                and li_val[(len(li_val) - 1)] == "-" \
                and li_val[(len(li_val) - 1)] == "/" \
                and li_val[(len(li_val) - 1)] == "x" \
                and li_val[(len(li_val) - 1)] == "," \
                and li_val[(len(li_val) - 1)] == "%" \
                and li_val[(len(li_val) - 1)] == "√":
            li_val.append(btn_0["text"])
            li_val_virg.append(btn_0["text"])
            co_list_str_tam(li_val)

def acao_1():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_1["text"])
        li_val_virg.append(btn_1["text"])
        co_list_str_tam(li_val)

def acao_2():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_2["text"])
        li_val_virg.append(btn_2["text"])
        co_list_str_tam(li_val)

def acao_3():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_3["text"])
        li_val_virg.append(btn_3["text"])
        co_list_str_tam(li_val)

def acao_4():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_4["text"])
        li_val_virg.append(btn_4["text"])
        co_list_str_tam(li_val)

def acao_5():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_5["text"])
        li_val_virg.append(btn_5["text"])
        co_list_str_tam(li_val)

def acao_6():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_6["text"])
        li_val_virg.append(btn_6["text"])
        co_list_str_tam(li_val)

def acao_7():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_7["text"])
        li_val_virg.append(btn_7["text"])
        co_list_str_tam(li_val)

def acao_8():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_8["text"])
        li_val_virg.append(btn_8["text"])
        co_list_str_tam(li_val)

def acao_9():
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()
        li_val.append(btn_9["text"])
        li_val_virg.append(btn_9["text"])
        co_list_str_tam(li_val)

def acao_mais():
    acao_li_val_virg()
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()

        if len(li_val) == 0:
            li_val.append("0")
            li_val.append("+")

        if li_val[(len(li_val) - 1)] != "+" \
                and li_val[(len(li_val) - 1)] != "-" \
                and li_val[(len(li_val) - 1)] != "/" \
                and li_val[(len(li_val) - 1)] != "x" \
                and li_val[(len(li_val) - 1)] != "," \
                and li_val[(len(li_val) - 1)] != "%" \
                and li_val[(len(li_val) - 1)] != "√":
            li_val.append(btn_mais["text"])
            li_op.append(btn_mais["text"])
        co_list_str_tam(li_val)
    li_op.clear()

def acao_menos():
    acao_li_val_virg()
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()

        if len(li_val) == 0:
            li_val.append("0")
            li_val.append("-")

        if li_val[(len(li_val) - 1)] != "+" \
                and li_val[(len(li_val) - 1)] != "-" \
                and li_val[(len(li_val) - 1)] != "/" \
                and li_val[(len(li_val) - 1)] != "x" \
                and li_val[(len(li_val) - 1)] != "," \
                and li_val[(len(li_val) - 1)] != "%" \
                and li_val[(len(li_val) - 1)] != "√":
            li_val.append(btn_menos["text"])
            co_list_str_tam(li_val)
            li_op.append(btn_menos["text"])
    li_op.clear()

def acao_vezes():
    acao_li_val_virg()
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()

        if len(li_val) == 0:
            li_val.append("0")
            li_val.append("x")

        if li_val[(len(li_val) - 1)] != "+" \
                and li_val[(len(li_val) - 1)] != "-" \
                and li_val[(len(li_val) - 1)] != "/" \
                and li_val[(len(li_val) - 1)] != "x" \
                and li_val[(len(li_val) - 1)] != "," \
                and li_val[(len(li_val) - 1)] != "%" \
                and li_val[(len(li_val) - 1)] != "√":
            li_val.append(btn_vezes["text"])
            co_list_str_tam(li_val)
            li_op.append(btn_vezes["text"])
    li_op.clear()

def acao_divisao():
    acao_li_val_virg()
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()

        if len(li_val) == 0:
            li_val.append("0")
            li_val.append("/")

        if li_val[(len(li_val) - 1)] != "+" \
                and li_val[(len(li_val) - 1)] != "-" \
                and li_val[(len(li_val) - 1)] != "/" \
                and li_val[(len(li_val) - 1)] != "x" \
                and li_val[(len(li_val) - 1)] != "," \
                and li_val[(len(li_val) - 1)] != "%" \
                and li_val[(len(li_val) - 1)] != "√":
            li_val.append(btn_divisao["text"])
            co_list_str_tam(li_val)
            li_op.append(btn_divisao["text"])
    li_op.clear()

def acao_p_cento():
    acao_li_val_virg()
    if trava_acao() == False:
        lis_str = list_str(li_val)
        btn_ra_li = lis_str


        if list_str(li_val) == "0":
            li_val.clear()

        if len(li_val) == 0:
            li_val.append("0")
            #li_val.append("/")

        if btn_p_cento["text"] == "%":
            if li_val.count("%") == 0:
                btn_ra = list_str(li_val)
                btn_ra = btn_ra.replace(",", ".")
                if li_val.count("x") == 1:
                    btn_ra = btn_ra.split("x")
                    btn_ra_0 = eval(btn_ra[0])
                    btn_ra_1 = eval(btn_ra[1])
                    btn_ra = btn_ra_1/100*btn_ra_0*btn_ra_0
                if li_val.count("/") == 1:
                    btn_ra = btn_ra.split("/")
                    btn_ra_0 = eval(btn_ra[0])
                    btn_ra_1 = eval(btn_ra[1])
                    btn_ra = btn_ra_1/100*btn_ra_0/btn_ra_0
                if li_val.count("+") == 1:
                    btn_ra = btn_ra.split("+")
                    btn_ra_0 = eval(btn_ra[0])
                    btn_ra_1 = eval(btn_ra[1])
                    btn_ra = btn_ra_1/100*btn_ra_0+btn_ra_0
                if li_val.count("-") == 1:
                    btn_ra = btn_ra.split("-")
                    btn_ra_0 = eval(btn_ra[0])
                    btn_ra_1 = eval(btn_ra[1])
                    btn_ra = btn_ra_0-(btn_ra_1/100*btn_ra_0)


                btn_ra = str(btn_ra)
                btn_ra = btn_ra.replace(".",",")
                if btn_ra[::-1][0] == "0" and btn_ra[::-1][1] == ",":
                    btn_ra = btn_ra.replace(",0","")
                else:
                    btn_ra = btn_ra

            li_val.clear()
            for xx in btn_ra:
                li_val.append(xx)
                li_val_virg.append(xx)

                co_list_str_tam(formatar_pontos(li_val))
            Label(lb(), font=("Verdana", 12), anchor="ne", width="32", height="1", text="{}%= ".format(list_str(list_str(btn_ra_li))),
                  bg="#838a80", fg="#565b54").grid()
            
        historico_dic.append(("{}%={}".format(list_str(btn_ra_li), btn_ra)))
def acao_raiz():
    acao_li_val_virg()
    if trava_acao() == False:
        if list_str(li_val) == "0":
            li_val.clear()

        if len(li_val) == 0:
            li_val.append("0")
            #li_val.append("/")

        if btn_raiz["text"] == "√":

            btn_ra = list_str(li_val)
            btn_ra = btn_ra.replace(",", ".")
            btn_ra = eval(btn_ra)
            btn_ra = sqrt(btn_ra)
            btn_ra = str(btn_ra)
            if btn_ra[(len(btn_ra) - 1)] == "0" and btn_ra[(len(btn_ra) - 2)] == ".":
                btn_ra = btn_ra.replace(".0","")

        if li_val[(len(li_val) - 1)] != "+" \
                and li_val[(len(li_val) - 1)] != "-" \
                and li_val[(len(li_val) - 1)] != "/" \
                and li_val[(len(li_val) - 1)] != "x" \
                and li_val[(len(li_val) - 1)] != "," \
                and li_val[(len(li_val) - 1)] != "%" \
                and li_val[(len(li_val) - 1)] != "√":
            btn_ra = btn_ra.replace(".",",")
            co_list_str_tam(btn_ra)
        Label(lb(), font=("Verdana", 12), anchor="ne", width="32", height="1", text="√({})= ".format(list_str(li_val)),
              bg="#838a80", fg="#565b54").grid()

        historico_dic.append(("√({})={}".format(list_str(li_val), btn_ra)))

        li_val.clear()
        for xx in btn_ra:
            li_val.append(xx)
            li_val_virg.append(xx)

def acao_virgula():
    if trava_acao() == False:
        if li_val[(len(li_val) - 1)] != "+" \
                and li_val[(len(li_val) - 1)] != "-" \
                and li_val[(len(li_val) - 1)] != "/" \
                and li_val[(len(li_val) - 1)] != "x" \
                and li_val[(len(li_val) - 1)] != "," \
                and li_val[(len(li_val) - 1)] != "%" \
                and li_val[(len(li_val) - 1)] != "√" \
                and li_val_virg.count(",") < 1:
            li_val.append("{}".format(","))
            li_val_virg.append("{}".format(","))
            co_list_str_tam(li_val)

def acao_C():
    acao_li_val_virg()
    li_val.clear()
    li_0.clear()
    lb()["text"] = "0"
    li_val.append("0")
    li_op.clear()

def acao_voltar_espaco():
    if trava_acao() == False:
        if li_val[(len(li_val) - 1)] != "+" \
                and li_val[(len(li_val) - 1)] != "-" \
                and li_val[(len(li_val) - 1)] != "/" \
                and li_val[(len(li_val) - 1)] != "x" \
                and li_val[(len(li_val) - 1)] != "%" \
                and li_val[(len(li_val) - 1)] != "√":
            if len(li_val) >= 1:
                li_val.pop()
            if len(li_val_virg) >= 1:
                li_val_virg.pop()
            if len(li_val) == 0:
                li_val.append("0")
                li_val_virg.append("0")
            co_list_str_tam(li_val)
def acao_igual():

    if li_op.count("1") == 0:
        if li_val[(len(li_val) - 1)] == "+" \
                or li_val[(len(li_val) - 1)] == "-" \
                or li_val[(len(li_val) - 1)] == "x":

            li_val.append("{}".format("0"))
            li_val_virg.append("{}".format("0"))

        elif li_val[(len(li_val) - 1)] == "/":

            li_val.append("{}".format("1"))
            li_val_virg.append("{}".format("1"))

        co_list_str_tam(formatar_pontos(li_val))


        Label(lb(), font=("Verdana", 12), anchor="ne", width="32", height="1", text="{}= ".format(list_str(li_val)),
              bg="#838a80", fg="#565b54").grid()

        list_str_li_v = list_str(li_val).replace("x","*")
        ccc = list_str_li_v.replace(",",".")
        cccc = ccc.replace(".0","")
        list_str_t = eval(cccc)
        li_val.clear()
        str_to = str(list_str_t)

        historico_dic.append(("{}=".format(cccc),str_to))

        if str_to.count(".0"):
            str_to.replace(".0", "")

        for ttsx in str_to:
            if ttsx == ".":
                li_val.append(ttsx.replace(".",","))
                li_val_virg.append(ttsx.replace(".",","))
            else:
                li_val.append(ttsx)
                li_val_virg.append(ttsx)
        li_op.append("1")
        print(li_val)
def historico():

    if len(historico_dic) > 0:
        lab_hist_in = Label(j_cal, font=("Verdana", 16), anchor="nw", width="28", height="20", text="", bg="#838a80")
        lab_hist_in.grid()
    elif len(historico_dic) == 0:
        lab_hist_in = Label(j_cal, font=("Verdana", 16), anchor="nw", width="28", height="20", text="Sem histórico", bg="#838a80")
        lab_hist_in.grid()


    def historico_in():
        lab_hist_in.destroy()

    btn_hist_in = Button(lab_hist_in, font=("Verdana", 10), width="2", text="X", command=historico_in)
    btn_hist_in["bg"] = "#838a80"
    btn_hist_in["bd"] = 0
    btn_hist_in.tk_setPalette("#8e928c")
    btn_hist_in.tk_focusFollowsMouse()
    btn_hist_in.place(x=318, y=1)
    yx = 40
    historico_dics = historico_dic[::-1]
    for h_dic in historico_dics[0:10]:
        t = ""
        for xx in h_dic:
            t = t +xx
        h_dics = t
        h_dics = h_dics.split("=")
        h_dics = h_dics[0]+"=\n"+h_dics[1]
        btn_hist_in_l = Button(lab_hist_in, font=("Verdana", 10), width="41", height="2", anchor="w", text=h_dics)
        btn_hist_in_l["bg"] = "#8e928c"
        btn_hist_in_l["bd"] = 0
        btn_hist_in_l.place(x=5, y=yx)
        yx += 45




btn_hist = Button(font=("Verdana", 10), width="8", text="Histórico", command=historico)
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
j_cal.maxsize(width=350, height=500)
j_cal.minsize(width=350, height=500)
j_cal.mainloop()
