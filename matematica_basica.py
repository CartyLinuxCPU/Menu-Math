import time
from datetime import date

nome = '''

 ██████╗     █████╗     ██████╗     ████████╗    ██╗   ██╗            ██╗         ██╗    ███╗   ██╗    ██╗   ██╗    ██╗  ██╗    
██╔════╝    ██╔══██╗    ██╔══██╗    ╚══██╔══╝    ╚██╗ ██╔╝            ██║         ██║    ████╗  ██║    ██║   ██║    ╚██╗██╔╝    
██║         ███████║    ██████╔╝       ██║        ╚████╔╝             ██║         ██║    ██╔██╗ ██║    ██║   ██║     ╚███╔╝     
██║         ██╔══██║    ██╔══██╗       ██║         ╚██╔╝              ██║         ██║    ██║╚██╗██║    ██║   ██║     ██╔██╗     
╚██████╗    ██║  ██║    ██║  ██║       ██║          ██║               ███████╗    ██║    ██║ ╚████║    ╚██████╔╝    ██╔╝ ██╗    
 ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝       ╚═╝          ╚═╝               ╚══════╝    ╚═╝    ╚═╝  ╚═══╝     ╚═════╝     ╚═╝  ╚═╝    

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
                             
Powered by: Carty Linux

[Instagram]: [CartyLinuxCPU]
[GitHub]: [CartyLinuxCPU]
[Facebook]: [Linux Cpu]

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+'''
print(nome)
time.sleep(5)
print("\n=+=+=+=+=+=+ Menu da Matemática =+=+=+=+=+=+\n[1] = SOMA MATEMÁTICA\n[2] = MULTIPLICAÇÃO MATEMÁTICA\n[3] = DIVISÃO MATEMÁTICA\n[4] = SUBTRAÇÃO MATEMÁTICA\n ")

op = input("Escolha uma OPÇÃO para entrar e SAIR para fechar: >>> ")
if op == '1':
    time.sleep(3)
    print("Espere..\n")
    try:
        while True:
            time.sleep(3)
            data_atual = date.today()
            horario_em_texto = '0{}.0{}.{}'.format(data_atual.day, data_atual.month, data_atual.year)
            print("Essa aqui é a Data BR ", horario_em_texto)
            print("\n=+=+=+= Soma =+=+=+=\n")
            n = int(input("Escreva o primeiro Numero >>> "))
            n_2 = int(input("Escreva o segundo numero >>> "))
            soma = n + n_2
            if soma:
                print('O', n,  " mais ", n_2 ,"é igual a >>> ", soma )
            else:
                print("O", n ,"Nao somou com >>", n_2)

    except Exception as error:
        print("Exeção encerrada. ",  error)
else:
    print("Voce Saiu da soma adição..\n")

if op == '2':
    time.sleep(3)
    print("Espere..\n")
    try:
        while True:
            data_atual = date.today()
            horario_em_texto = '0{}.0{}.{}'.format(data_atual.day, data_atual.month, data_atual.year)
            print("Essa aqui é a data BR ", horario_em_texto)
            print("\n ======= Multiplicação ======= \n ")
            n1 = int(input("Escreva o Primeiro Numero Para Multiplicação >>> "))
            n2 = int(input("Escreva O Segundo Numero para Multiplicação >>>"))
            multiplicacao = n1 * n2
            if multiplicacao:
                print("O" ,n1, " vezes ", n2, "é igual = ", multiplicacao )
            else:
                print(n1 ,"Não Multiplicou com", n2, 'o valor é', multiplicacao)

    except Exception as error_2:
        print("Exeção fechada. ", error_2)

else:
    print("Voce Saiu da multiplicação..\n")


if op == '3':
    time.sleep(3)
    print("Espere..\n")
    try:
        while True:
            time.sleep(3)
            data_atual = date.today()
            horario_em_texto = '0{}.0{}.{}'.format(data_atual.day, data_atual.month, data_atual.year)
            print("Essa aqui é a Data BR ", horario_em_texto)
            print("")
            print("\n ======== Divisão ========\n ")
            numero_1 = float(int(input("Escreva o primeiro numero para divisão >>>")))
            numero_2 = float(int(input("Escreva o segundo numero para divisão >>> ")))
            divisao = numero_1 / numero_2
            if divisao:
                print("O", numero_1, "divido por", numero_2, " é igual a", divisao)
            else:
                print(numero_1 , "Não dividiu por", numero_2, 'O Resultado é ', divisao)

    except ZeroDivisionError as error_3:
        print("Não divide por zero..", error_3)

else:
    print("Voce Saiu da Divisão..\n ")


if op == '4':
    time.sleep(3)
    print("Espere..\n")
    try:
        while True:
            time.sleep(3)
            data = date.today()
            data_tudo = '0{}.0{}.{}'.format(data.day, data.month, data.year)
            print(data_tudo)
            nmr1 = float(int(input("Escreva um Numero >>> ")))
            nmr2 = float(int(input('Escreva o segundo numero >>> ')))
            subtracao = nmr1 - nmr2
            if subtracao:
                print('O' ,nmr1  , '  menos  ', nmr2 , ' é igual a =  ', subtracao)

            else:
                print(nmr1, "Não subtraiu com ", nmr2, 'Resultado é ', subtracao)

    except Exception as error_4:
        print("A execeção deu error", error_4)

else:
    print('VOCE SAIU PORQUE QUIS.')





