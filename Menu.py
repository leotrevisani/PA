#Leozin passou aqui :3 <3
import os
import math
import random

# ---------- Funções auxiliares ----------

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ler_float(mensagem):
    """Lê um número decimal, repetindo até o usuário digitar algo válido."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido! Digite um número.")


def ler_int(mensagem):
    """Lê um número inteiro, repetindo até o usuário digitar algo válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")


def continuar(numero_programa):
    """Pergunta se o usuário quer continuar no programa atual."""
    resp = input(f"\nDeseja continuar no programa {numero_programa}? (S/N): ")
    return resp.strip().upper() == "S"


# ---------- 1 - Nome e Sobrenome ----------

def nome_sobrenome():
    while True:
        limpar_tela()
        print("=== NOME E SOBRENOME ===")

        nome_completo = input("Digite seu nome completo: ").strip()
        partes = nome_completo.split()

        if len(partes) < 2:
            print("Digite pelo menos um nome e um sobrenome!")
        else:
            nome = partes[0]
            sobrenome = " ".join(partes[1:])

            print("\nNome com sobrenome invertido:")
            print(sobrenome, nome)

        if not continuar(1):
            break


# ---------- 2 - Calculadora ----------

def calculadora():
    while True:
        limpar_tela()
        print("=== PROGRAMA CALCULADORA ===")

        numero1 = ler_float("Digite o primeiro número: ")
        numero2 = ler_float("Digite o segundo número: ")
        op = input("Digite uma operação (+, -, *, /, ^): ").strip()

        if op == "+":
            print(f"Resultado: {numero1 + numero2}")
        elif op == "-":
            print(f"Resultado: {numero1 - numero2}")
        elif op == "*":
            print(f"Resultado: {numero1 * numero2}")
        elif op == "/":
            if numero2 != 0:
                print(f"Resultado: {numero1 / numero2}")
            else:
                print("Erro: divisão por zero é impossível!")
        elif op == "^":
            try:
                print(f"Resultado: {math.pow(numero1, numero2)}")
            except (ValueError, OverflowError):
                print("Erro: não foi possível calcular essa potência!")
        else:
            print("Operação inválida!")

        if not continuar(2):
            break


# ---------- 3 - Média ----------

def media():
    while True:
        limpar_tela()
        print("=== PROGRAMA MÉDIA ===")

        notas = []
        for i in range(1, 5):
            notas.append(ler_float(f"Digite a nota {i}: "))

        media_final = sum(notas) / 4
        print(f"\nA média é: {media_final:.2f}")

        if media_final < 5:
            print("Menção: I - Insuficiente (reprovado)")
        elif media_final < 7:
            print("Menção: R - Regular (aprovado)")
        elif media_final < 9:
            print("Menção: B - Bom (aprovado)")
        else:
            print("Menção: MB - Muito Bom (aprovado com louvor!)")

        if not continuar(3):
            break


# ---------- 4 - Hipotenusa ----------

def hipotenusa():
    while True:
        limpar_tela()
        print("=== PROGRAMA HIPOTENUSA ===")

        cat1 = ler_float("Digite o valor do Cateto 1: ")
        cat2 = ler_float("Digite o valor do Cateto 2: ")

        hip = math.sqrt(cat1 ** 2 + cat2 ** 2)
        print(f"\nA hipotenusa é: {hip:.2f}")

        if not continuar(4):
            break


# ---------- 5 - Triângulo ----------

def triangulo():
    while True:
        limpar_tela()
        print("=== PROGRAMA TRIÂNGULO ===")

        lado1 = ler_float("Digite o primeiro lado: ")
        lado2 = ler_float("Digite o segundo lado: ")
        lado3 = ler_float("Digite o terceiro lado: ")

        if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
            if lado1 == lado2 == lado3:
                print("\nTriângulo Equilátero")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("\nTriângulo Isósceles")
            else:
                print("\nTriângulo Escaleno")
        else:
            print("\nNão é triângulo!!!")

        if not continuar(5):
            break


# ---------- 6 - Equação do 2º Grau ----------

def equacao_segundo_grau():
    while True:
        limpar_tela()
        print("=== PROGRAMA EQUAÇÃO 2º GRAU ===")

        a = ler_float("Digite o valor de A: ")
        b = ler_float("Digite o valor de B: ")
        c = ler_float("Digite o valor de C: ")

        if a == 0:
            print("\nA não pode ser zero (não seria equação do 2º grau)!")
        else:
            delta = b ** 2 - 4 * a * c
            print(f"\nDelta: {delta}")

            if delta < 0:
                print("Resultado não é real, pois o Delta é negativo!")
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)

                print(f"X1 é igual a: {x1:.2f}")
                print(f"X2 é igual a: {x2:.2f}")

        if not continuar(6):
            break


# ---------- 7 - Tabuada ----------

def tabuada():
    while True:
        limpar_tela()
        print("=== PROGRAMA TABUADA ===")

        numero = ler_float("Digite o número que deseja ver a tabuada: ")
        inicio = ler_int("Digite a partir de qual multiplicador: ")
        fim = ler_int("Digite até qual multiplicador: ")

        print(f"\nTabuada de {numero:g}:")
        for mult in range(inicio, fim + 1):
            print(f"{numero:g} x {mult} = {numero * mult:g}")

        if not continuar(7):
            break


# ---------- 8 - Joguinho da Adivinhação ----------

def jogo_adivinhacao():
    while True:
        limpar_tela()
        numero_secreto = random.randint(0, 249)
        tentativas = 0
        palpite = None

        print("=======================================")
        print("   BEM-VINDO AO JOGO DE ADIVINHAÇÃO!   ")
        print("=======================================")
        print("Tente adivinhar o número de 0 a 249.\n")

        while palpite != numero_secreto:
            palpite = ler_int("Digite o seu palpite: ")
            tentativas += 1

            if palpite < numero_secreto:
                print("O número secreto é MAIOR!\n")
            elif palpite > numero_secreto:
                print("O número secreto é MENOR!\n")

        print("---------------------------------------")
        print(f"PARABÉNS! Você acertou o número {numero_secreto}")
        print(f"Total de tentativas: {tentativas}")
        print("---------------------------------------")

        if not continuar(8):
            break


# ---------- Programa principal ----------

def main():
    opcao = 0

    while opcao != 9:
        limpar_tela()
        print("=== MENU PRINCIPAL ===")
        print("1) Nome e Sobrenome")
        print("2) Calculadora")
        print("3) Média")
        print("4) Hipotenusa")
        print("5) Triângulo")
        print("6) Equação do 2º Grau")
        print("7) Tabuada")
        print("8) Joguinho da Adivinhação")
        print("9) Sair")
        print("======================")

        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            opcao = 0

        limpar_tela()

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
            print("Saindo do programa... Até logo!")
        else:
            input("Opção inválida! Aperte Enter para voltar ao menu: ")


if __name__ == "__main__":
    main()
