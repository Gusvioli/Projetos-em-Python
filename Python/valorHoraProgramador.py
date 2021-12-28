def calculoValorHora(salario, horaMes):
    calculo = salario / horaMes
    print("Seu valor hora é de {}/hora".format(int(calculo)))

sal = int(input("Qual o seu sálario?"))
hmes = int(input("Quantas horas vocÊ trabalha por mês?"))
calculoValorHora(sal,hmes)