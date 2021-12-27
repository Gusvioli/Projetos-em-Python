from tkinter import *

ini_tk = Tk()

acao_q = []
acao_q.append("*")
acao_q.append("**")

dic_acao_q = {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
empate_acao_q = []
ini_acao_q = ["1"]

def btn_ini_0():
    ini_acao_q.pop()
    ini_acao_q.insert(0,"1")

    btn_ini["text"] = "Reiniciar"
    btn_ini["width"] = ("7")

    empate_acao_q.clear()

    btn_1["command"] = btn_0_1
    btn_2["command"] = btn_0_2
    btn_3["command"] = btn_0_3
    btn_4["command"] = btn_0_4
    btn_5["command"] = btn_0_5
    btn_6["command"] = btn_0_6
    btn_7["command"] = btn_0_7
    btn_8["command"] = btn_0_8
    btn_9["command"] = btn_0_9

    dic_acao_q[1] = ""
    dic_acao_q[2] = ""
    dic_acao_q[3] = ""
    dic_acao_q[4] = ""
    dic_acao_q[5] = ""
    dic_acao_q[6] = ""
    dic_acao_q[7] = ""
    dic_acao_q[8] = ""
    dic_acao_q[9] = ""

    acao_q.clear()
    acao_q.append("*")
    acao_q.append("**")

    lab_x_o["text"] = "Jogador X inicia o jogo"
    lab_x_o["fg"] = "#ffffff"

    btn_1["bg"] = "#ffffff"
    btn_2["bg"] = "#ffffff"
    btn_3["bg"] = "#ffffff"
    btn_4["bg"] = "#ffffff"
    btn_5["bg"] = "#ffffff"
    btn_6["bg"] = "#ffffff"
    btn_7["bg"] = "#ffffff"
    btn_8["bg"] = "#ffffff"
    btn_9["bg"] = "#ffffff"

    btn_1["text"] = ""
    btn_2["text"] = ""
    btn_3["text"] = ""
    btn_4["text"] = ""
    btn_5["text"] = ""
    btn_6["text"] = ""
    btn_7["text"] = ""
    btn_8["text"] = ""
    btn_9["text"] = ""

lab_ = Label(ini_tk, font=("Verdana", 18), anchor="e", width="22", height="2", text="", bg="#000000", fg="#ffffff")
lab_.place(x=4, y=2)

lab_x_o = Label(lab_, font=("Verdana", 17), anchor="s", width="23", height="2", text="", bg="#000000", fg="#ffffff")
lab_x_o.tk_focusFollowsMouse()
lab_x_o.grid(column=1, row=1, padx=2)

def acao(val, btn):

    to_int = len(acao_q)
    if to_int % 2 != 0:
        acao_q.append("O")
        dic_acao_q[val] = "O"
    else:
        acao_q.append("X")
        dic_acao_q[val] = "X"

    for x in range(1, len(acao_q)):
        if x % 2 != 0:
            lab_x_o["text"] = "Sua vez jogador X"
            btn["text"] = "O"
        else:
            lab_x_o["text"] = "Sua vez jogador O"
            btn["text"] = "X"

def vencedor():
    if dic_acao_q[1] == "X" and dic_acao_q[2] == "X" and dic_acao_q[3] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_1["bg"] = "green"
        btn_2["bg"] = "green"
        btn_3["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[1] == "O" and dic_acao_q[2] == "O" and dic_acao_q[3] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_1["bg"] = "green"
        btn_2["bg"] = "green"
        btn_3["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[4] == "X" and dic_acao_q[5] == "X" and dic_acao_q[6] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_4["bg"] = "green"
        btn_5["bg"] = "green"
        btn_6["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[4] == "O" and dic_acao_q[5] == "O" and dic_acao_q[6] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_4["bg"] = "green"
        btn_5["bg"] = "green"
        btn_6["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[7] == "X" and dic_acao_q[8] == "X" and dic_acao_q[9] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_7["bg"] = "green"
        btn_8["bg"] = "green"
        btn_9["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[7] == "O" and dic_acao_q[8] == "O" and dic_acao_q[9] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_7["bg"] = "green"
        btn_8["bg"] = "green"
        btn_9["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[1] == "X" and dic_acao_q[4] == "X" and dic_acao_q[7] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_1["bg"] = "green"
        btn_4["bg"] = "green"
        btn_7["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[1] == "O" and dic_acao_q[4] == "O" and dic_acao_q[7] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_1["bg"] = "green"
        btn_4["bg"] = "green"
        btn_7["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[2] == "X" and dic_acao_q[5] == "X" and dic_acao_q[8] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_2["bg"] = "green"
        btn_5["bg"] = "green"
        btn_8["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[2] == "O" and dic_acao_q[5] == "O" and dic_acao_q[8] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_2["bg"] = "green"
        btn_5["bg"] = "green"
        btn_8["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[3] == "X" and dic_acao_q[6] == "X" and dic_acao_q[9] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_3["bg"] = "green"
        btn_6["bg"] = "green"
        btn_9["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[3] == "O" and dic_acao_q[6] == "O" and dic_acao_q[9] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_3["bg"] = "green"
        btn_6["bg"] = "green"
        btn_9["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[1] == "X" and dic_acao_q[5] == "X" and dic_acao_q[9] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_1["bg"] = "green"
        btn_5["bg"] = "green"
        btn_9["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[1] == "O" and dic_acao_q[5] == "O" and dic_acao_q[9] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_1["bg"] = "green"
        btn_5["bg"] = "green"
        btn_9["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[3] == "X" and dic_acao_q[5] == "X" and dic_acao_q[7] == "X":
        lab_x_o["text"] = "Parabéns jogador X"
        lab_x_o["fg"] = "green"
        btn_3["bg"] = "green"
        btn_5["bg"] = "green"
        btn_7["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    elif dic_acao_q[3] == "O" and dic_acao_q[5] == "O" and dic_acao_q[7] == "O":
        lab_x_o["text"] = "Parabéns jogador O"
        lab_x_o["fg"] = "green"
        btn_3["bg"] = "green"
        btn_5["bg"] = "green"
        btn_7["bg"] = "green"
        btn_1["command"] = ""
        btn_2["command"] = ""
        btn_3["command"] = ""
        btn_4["command"] = ""
        btn_5["command"] = ""
        btn_6["command"] = ""
        btn_7["command"] = ""
        btn_8["command"] = ""
        btn_9["command"] = ""

    else:
        empate_acao_q.append("0")
        if len(empate_acao_q) == 9:
            lab_x_o["text"] = "O jogo empatou!!!!"
            btn_1["bg"] = "yellow"
            btn_2["bg"] = "yellow"
            btn_3["bg"] = "yellow"
            btn_4["bg"] = "yellow"
            btn_5["bg"] = "yellow"
            btn_6["bg"] = "yellow"
            btn_7["bg"] = "yellow"
            btn_8["bg"] = "yellow"
            btn_9["bg"] = "yellow"
            btn_1["command"] = ""
            btn_2["command"] = ""
            btn_3["command"] = ""
            btn_4["command"] = ""
            btn_5["command"] = ""
            btn_6["command"] = ""
            btn_7["command"] = ""
            btn_8["command"] = ""
            btn_9["command"] = ""

def btn_0_1():
    acao(1, btn_1)
    vencedor()
    btn_1["command"] = ""

def btn_0_2():
    acao(2, btn_2)
    vencedor()
    btn_2["command"] = ""

def btn_0_3():
    acao(3, btn_3)
    vencedor()
    btn_3["command"] = ""

def btn_0_4():
    acao(4, btn_4)
    vencedor()
    btn_4["command"] = ""

def btn_0_5():
    acao(5, btn_5)
    vencedor()
    btn_5["command"] = ""

def btn_0_6():
    acao(6, btn_6)
    vencedor()
    btn_6["command"] = ""

def btn_0_7():
    acao(7, btn_7)
    vencedor()
    btn_7["command"] = ""

def btn_0_8():
    acao(8, btn_8)
    vencedor()
    btn_8["command"] = ""

def btn_0_9():
    acao(9, btn_9)
    vencedor()
    btn_9["command"] = ""

btn_ini = Button(lab_, font=("Verdana", 10), width="6", text="Iniciar", command=btn_ini_0)
btn_ini.place(x=1, y=1)

btn_1 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_1.place(x=4, y=75)
btn_2 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_2.place(x=124, y=75)
btn_3 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_3.place(x=244, y=75)
btn_4 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_4.place(x=4, y=175)
btn_5 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_5.place(x=124, y=175)
btn_6 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_6.place(x=244, y=175)
btn_7 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_7.place(x=4, y=275)
btn_8 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_8.place(x=124, y=275)
btn_9 = Button(font=("Verdana", 20), width="5", height="2", text="", command="")
btn_9.place(x=244, y=275)

ini_tk.geometry("324x310")
ini_tk["bg"] = "#1b1e19"
ini_tk.title("Jogo da velha")
ini_tk.maxsize(width=344, height=370)
ini_tk.minsize(width=344, height=370)
ini_tk.mainloop()

