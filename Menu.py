
import math
import random


# Funções para ler números
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite um número válido!")


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido!")


# 1 - Nome e Sobrenome
def nome_sobrenome():
    print("\n=== NOME E SOBRENOME ===")

    nome_completo = input("Digite seu nome completo: ").strip()
    partes = nome_completo.split()

    if len(partes) < 2:
        print("Digite pelo menos um nome e um sobrenome!")
    else:
        nome = partes[0]
        sobrenome = " ".join(partes[1:])

        print("\nNome com sobrenome invertido:")
        print(sobrenome, nome)


# 2 - Calculadora
def calculadora():
    print("\n=== CALCULADORA ===")

    numero1 = ler_numero("Digite o primeiro número: ")
    numero2 = ler_numero("Digite o segundo número: ")

    op = input("Digite a operação (+, -, *, /, ^): ")

    if op == "+":
        resultado = numero1 + numero2
        print("Resultado:", resultado)

    elif op == "-":
        resultado = numero1 - numero2
        print("Resultado:", resultado)

    elif op == "*":
        resultado = numero1 * numero2
        print("Resultado:", resultado)

    elif op == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado:", resultado)
        else:
            print("Erro! Não é possível dividir por zero.")

    elif op == "^":
        resultado = numero1 ** numero2
        print("Resultado:", resultado)

    else:
        print("Operação inválida!")


# 3 - Média
def media():
    print("\n=== MÉDIA ===")

    nota1 = ler_numero("Digite a nota 1: ")
    nota2 = ler_numero("Digite a nota 2: ")
    nota3 = ler_numero("Digite a nota 3: ")
    nota4 = ler_numero("Digite a nota 4: ")

    resultado = (nota1 + nota2 + nota3 + nota4) / 4

    print("\nMédia:", resultado)

    if resultado < 5:
        print("Menção: I - Insuficiente")

    elif resultado < 7:
        print("Menção: R - Regular")

    elif resultado < 9:
        print("Menção: B - Bom")

    else:
        print("Menção: MB - Muito Bom")


# 4 - Hipotenusa
def hipotenusa():
    print("\n=== HIPOTENUSA ===")

    cateto1 = ler_numero("Digite o valor do primeiro cateto: ")
    cateto2 = ler_numero("Digite o valor do segundo cateto: ")

    if cateto1 > 0 and cateto2 > 0:
        resultado = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
        print("\nA hipotenusa é:", resultado)
    else:
        print("Os catetos devem ser maiores que zero!")


# 5 - Triângulo
def triangulo():
    print("\n=== TRIÂNGULO ===")

    lado1 = ler_numero("Digite o primeiro lado: ")
    lado2 = ler_numero("Digite o segundo lado: ")
    lado3 = ler_numero("Digite o terceiro lado: ")

    if (lado1 > 0 and lado2 > 0 and lado3 > 0
            and lado1 < lado2 + lado3
            and lado2 < lado1 + lado3
            and lado3 < lado1 + lado2):

        if lado1 == lado2 and lado2 == lado3:
            print("\nTriângulo Equilátero")

        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("\nTriângulo Isósceles")

        else:
            print("\nTriângulo Escaleno")

    else:
        print("\nNão é possível formar um triângulo!")


# 6 - Equação do 2º Grau
def equacao_segundo_grau():
    print("\n=== EQUAÇÃO DO 2º GRAU ===")

    a = ler_numero("Digite o valor de A: ")
    b = ler_numero("Digite o valor de B: ")
    c = ler_numero("Digite o valor de C: ")

    if a == 0:
        print("O valor de A deve ser diferente de zero!")
        return

    delta = b ** 2 - 4 * a * c

    print("\nDelta:", delta)

    if delta < 0:
        print("Não existem raízes reais, pois o Delta é negativo.")

    elif delta == 0:
        x = -b / (2 * a)
        print("Existe apenas uma raiz real:")
        print("X =", x)

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print("X1 =", x1)
        print("X2 =", x2)


# 7 - Tabuada
def tabuada():
    print("\n=== TABUADA ===")

    numero = ler_numero("Digite o número da tabuada: ")
    inicio = ler_inteiro("Começar de quanto? ")
    fim = ler_inteiro("Terminar em quanto? ")

    if inicio <= fim:
        print("\nTabuada de", numero)

        for multiplicador in range(inicio, fim + 1):
            resultado = numero * multiplicador
            print(numero, "x", multiplicador, "=", resultado)

    else:
        print("O início deve ser menor ou igual ao final!")


# 8 - Jogo da Adivinhação
def jogo_adivinhacao():
    print("\n=== JOGO DA ADIVINHAÇÃO ===")

    numero_secreto = random.randint(0, 100)
    tentativas = 0

    print("Tente adivinhar o número de 0 a 100!")

    while True:
        palpite = ler_inteiro("Digite seu palpite: ")

        if palpite < 0 or palpite > 100:
            print("Digite um número entre 0 e 100!")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("O número secreto é MAIOR!")

        elif palpite > numero_secreto:
            print("O número secreto é MENOR!")

        else:
            print("\nPARABÉNS! Você acertou!")
            print("O número secreto era:", numero_secreto)
            print("Total de tentativas:", tentativas)
            break


# MENU PRINCIPAL
opcao = 0

while opcao != 9:

    print("\n========== MENU PRINCIPAL ==========")
    print("1. Nome e Sobrenome")
    print("2. Calculadora")
    print("3. Média")
    print("4. Hipotenusa")
    print("5. Triângulo")
    print("6. Equação do 2º Grau")
    print("7. Tabuada")
    print("8. Joguinho da Adivinhação")
    print("9. Sair")
    print("====================================")

    opcao = ler_inteiro("Digite a opção desejada: ")

    if opcao == 1:
        nome_sobrenome()

    elif opcao == 2:
        calculadora()

    elif opcao == 3:
        media()

    elif opcao == 4:
        hipotenusa()

    elif opcao == 5:
        triangulo()

    elif opcao == 6:
        equacao_segundo_grau()

    elif opcao == 7:
        tabuada()

    elif opcao == 8:
        jogo_adivinhacao()

    elif opcao == 9:
        print("\nSaindo do programa... Até logo!")

    else:
        print("\nOpção inválida! Tente novamente.")
