from tkinter import *
from math import floor

j_cal = Tk()

def lb():
    lb_inicial = Label(j_cal, font=("Verdana", 36), anchor="e", width="11", height="2", text="", bg="#838a80")
    lb_inicial.place(x=7, y=33)
    return lb_inicial

lb()["text"] = "0"
li_val = []
li_val.append("0")

li_0 = []

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
        if li_val[0] == "0,":
            li_val.clear()
        if li_val[0] != btn_0["text"]:
            li_val.append(btn_0["text"])
            co_list_str_tam(li_val)

def acao_1():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_1["text"])
        co_list_str_tam(li_val)


def acao_2():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_2["text"])
        co_list_str_tam(li_val)

def acao_3():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_3["text"])
        co_list_str_tam(li_val)

def acao_4():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_4["text"])
        co_list_str_tam(li_val)

def acao_5():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_5["text"])
        co_list_str_tam(li_val)

def acao_6():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_6["text"])
        co_list_str_tam(li_val)

def acao_7():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_7["text"])
        co_list_str_tam(li_val)

def acao_8():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_8["text"])
        co_list_str_tam(li_val)

def acao_9():
    if trava_acao() == False:
        if li_val[0] == "0":
            li_val.clear()
        li_val.append(btn_9["text"])
        co_list_str_tam(li_val)

def acao_mais():
    if trava_acao() == False:
        if li_val[0] == "0":
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
        co_list_str_tam(li_val)

def acao_menos():
    if trava_acao() == False:
        if li_val[0] == "0":
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

def acao_vezes():
    if trava_acao() == False:
        if li_val[0] == "0":
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

def acao_divisao():
    if trava_acao() == False:
        if li_val[0] == "0":
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

def acao_p_cento():
    if trava_acao() == False:
        if li_val[0] == "0":
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
            li_val.append(btn_p_cento["text"])
            co_list_str_tam(li_val)

def acao_raiz():
    if trava_acao() == False:
        if li_val[0] == "0":
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
            li_val.append(btn_raiz["text"])
            co_list_str_tam(li_val)

def acao_virgula():
    if trava_acao() == False:
        if li_val[0] == "0" or li_val[0] == "0,":
            li_val.clear()
            li_val.append("0{}".format(btn_virgula["text"]))
            co_list_str_tam(li_val)
        else:
            if li_val[(len(li_val) - 1)] != "+" \
                    and li_val[(len(li_val) - 1)] != "-" \
                    and li_val[(len(li_val) - 1)] != "/" \
                    and li_val[(len(li_val) - 1)] != "x" \
                    and li_val[(len(li_val) - 1)] != "," \
                    and li_val[(len(li_val) - 1)] != "%" \
                    and li_val[(len(li_val) - 1)] != "√":
                if li_val.count(",") < 1:
                    li_val.append("{}".format(","))
                co_list_str_tam(li_val)
def acao_C():
    li_val.clear()
    li_0.clear()
    lb()["text"] = "0"
    li_val.append("0")

def acao_voltar_espaco():
    if trava_acao() == False:
        if len(li_val) >= 1:
            li_val.pop()
        if len(li_val) == 0:
            li_val.append("0")
        co_list_str_tam(li_val)

def historico():
    pass

def acao_igual():

    co_list_str_tam(formatar_pontos(li_val))

    Label(lb(), font=("Verdana", 14), anchor="ne", width="27", height="1", text="{}= ".format(list_str(li_val)),
          bg="#838a80", fg="#565b54").grid()

    list_str_li_v = list_str(li_val).replace("x","*")

    ccc = list_str_li_v.replace(",",".")

    list_str_t = eval(ccc)

    li_val.clear()

    list_str_t

    str_to = str(list_str_t)


    for ttsx in str_to:
        if ttsx == ".":
            li_val.append(ttsx.replace(".",","))
        else:
            li_val.append(ttsx)

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
