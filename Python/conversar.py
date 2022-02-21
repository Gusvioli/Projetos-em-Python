import os
from PySimpleGUI import PySimpleGUI as sg
import socket

sg.theme("Reddit")
lay = [
    [sg.Text("IP:         "), sg.Input(key='seuip', size=(16, 1)),
     sg.Text('Porta: '), sg.Input(key='outroip', size=(16, 1))],
    [sg.Text('Servidor:'), sg.Checkbox(
        'Servidor', default=False, key='servidor'), sg.Button('Conectar', key='conectar')],
    [sg.Text('Msg:      '), sg.Input(key='msgs', size=(70, 2))],
    [sg.Text('Megs:    '), sg.Output(size=(70, 20))],
    [sg.Button('Enviar', key='enviar')]
]
janela = sg.Window('Conversar', lay)
while True:

    eventos, valores = janela.read()
    if eventos == "conectar":
        pass
    if eventos == 'enviar':
        if valores['seuip'] != '':
            print(valores['seuip'])
        if valores['outroip'] != '':
            print(valores['outroip'])
        if valores['msgs'] != '':
            print(valores['msgs'])

    if eventos == sg.WINDOW_CLOSED:
        break
