//por Leonardo Ferreira Trevisani de Oliveira :3
using System;

class Program
{
    static void Main(string[] args)
    {
        // Gerador de números aleatórios para o Caso 8
        Random random = new Random();

        int opcao = 0;
        string resp = "N";

        // Variáveis do programa
        double numero1, numero2, finalResult;
        char op;
        double valorA, valorB, valorC, delta, x1, x2;
        double cat1, cat2, hip;
        double num1, num2, num3, num4, media;
        double lado1, lado2, lado3;
        int multiplicador, contador, numeroSecreto, palpite, tentativas;
        double resultadoTabuada;

        do
        {
            Console.Clear(); // Limpa a tela a cada retorno ao menu
            Console.WriteLine("=== MENU PRINCIPAL ===");
            Console.WriteLine("1) Cálculos (5 operações diretas)");
            Console.WriteLine("2) Calculadora (escolha a operação)");
            Console.WriteLine("3) Média");
            Console.WriteLine("4) Hipotenusa");
            Console.WriteLine("5) Triângulo");
            Console.WriteLine("6) Equação do 2º grau");
            Console.WriteLine("7) Tabuada");
            Console.WriteLine("8) Números Aleatórios");
            Console.WriteLine("9) Sair");
            Console.WriteLine("======================");

            Console.Write("\nEscolha uma opção: ");
            int.TryParse(Console.ReadLine(), out opcao);

            Console.Clear();

            switch (opcao)
            {
                case 1: // 1 - Cálculos
                    do
                    {
                        Console.Clear();
                        Console.WriteLine("=== PROGRAMA CÁLCULOS ===");
                        Console.Write("Digite o primeiro número: ");
                        numero1 = double.Parse(Console.ReadLine());
                        Console.Write("Digite o segundo número: ");
                        numero2 = double.Parse(Console.ReadLine());

                        Console.WriteLine($"\nSoma: {numero1 + numero2}");
                        Console.WriteLine($"Subtração: {numero1 - numero2}");
                        Console.WriteLine($"Multiplicação: {numero1 * numero2}");

                        if (numero2 != 0.0)
                        {
                            Console.WriteLine($"Divisão: {numero1 / numero2}");
                        }
                        else
                        {
                            Console.WriteLine("Divisão: Erro (divisão por zero)");
                        }

                        Console.WriteLine($"Potência: {Math.Pow(numero1, numero2)}");

                        Console.Write("\nDeseja continuar no programa 1? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 2: // 2 - Calculadora
                    do
                    {
                        Console.Clear();
                        Console.WriteLine("=== PROGRAMA CALCULADORA ===");
                        Console.Write("Digite o primeiro número: ");
                        numero1 = double.Parse(Console.ReadLine());
                        Console.Write("Digite o segundo número: ");
                        numero2 = double.Parse(Console.ReadLine());
                        Console.Write("Digite uma operação (+, -, *, /, ^): ");
                        op = Console.ReadLine()[0];

                        if (op == '+')
                        {
                            finalResult = numero1 + numero2;
                            Console.WriteLine($"Resultado: {finalResult}");
                        }
                        else if (op == '-')
                        {
                            finalResult = numero1 - numero2;
                            Console.WriteLine($"Resultado: {finalResult}");
                        }
                        else if (op == '*')
                        {
                            finalResult = numero1 * numero2;
                            Console.WriteLine($"Resultado: {finalResult}");
                        }
                        else if (op == '/')
                        {
                            if (numero2 != 0.0)
                            {
                                finalResult = numero1 / numero2;
                                Console.WriteLine($"Resultado: {finalResult}");
                            }
                            else
                            {
                                Console.WriteLine("Erro: divisão por zero é impossível!");
                            }
                        }
                        else if (op == '^')
                        {
                            finalResult = Math.Pow(numero1, numero2);
                            Console.WriteLine($"Resultado: {finalResult}");
                        }
                        else
                        {
                            Console.WriteLine("Operação inválida!");
                        }

                        Console.Write("\nDeseja continuar no programa 2? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 3: // 3 - Média
                    do
                    {
                        Console.Clear();
                        Console.WriteLine("=== PROGRAMA MÉDIA ===");
                        Console.Write("Digite a nota 1: ");
                        num1 = double.Parse(Console.ReadLine());
                        Console.Write("Digite a nota 2: ");
                        num2 = double.Parse(Console.ReadLine());
                        Console.Write("Digite a nota 3: ");
                        num3 = double.Parse(Console.ReadLine());
                        Console.Write("Digite a nota 4: ");
                        num4 = double.Parse(Console.ReadLine());

                        media = (num1 + num2 + num3 + num4) / 4;

                        Console.WriteLine($"\nA média é: {media:F2}");

                        if (media < 5)
                        {
                            Console.WriteLine("Menção: I - Insuficiente (reprovado)");
                        }
                        else if (media >= 5 && media < 7)
                        {
                            Console.WriteLine("Menção: R - Regular (aprovado)");
                        }
                        else if (media >= 7 && media < 9)
                        {
                            Console.WriteLine("Menção: B - Bom (aprovado)");
                        }
                        else
                        {
                            Console.WriteLine("Menção: MB - Muito Bom (aprovado com louvor!)");
                        }

                        Console.Write("\nDeseja continuar no programa 3? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 4: // 4 - Hipotenusa
                    do
                    {
                        Console.Clear();
                        Console.WriteLine("=== PROGRAMA HIPOTENUSA ===");
                        Console.Write("Digite o valor do Cateto 1: ");
                        cat1 = double.Parse(Console.ReadLine());
                        Console.Write("Digite o valor do Cateto 2: ");
                        cat2 = double.Parse(Console.ReadLine());

                        hip = Math.Sqrt((cat1 * cat1) + (cat2 * cat2));
                        Console.WriteLine($"\nA hipotenusa é: {hip:F2}");

                        Console.Write("\nDeseja continuar no programa 4? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 5: // 5 - Triângulo
                    do
                    {
                        Console.Clear();
                        Console.WriteLine("=== PROGRAMA TRIÂNGULO ===");
                        Console.Write("Digite o primeiro lado: ");
                        lado1 = double.Parse(Console.ReadLine());
                        Console.Write("Digite o segundo lado: ");
                        lado2 = double.Parse(Console.ReadLine());
                        Console.Write("Digite o terceiro lado: ");
                        lado3 = double.Parse(Console.ReadLine());

                        if (lado1 < lado2 + lado3 && lado2 < lado1 + lado3 && lado3 < lado1 + lado2)
                        {
                            if (lado1 == lado2 && lado2 == lado3)
                            {
                                Console.WriteLine("\nTriângulo Equilátero");
                            }
                            else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3)
                            {
                                Console.WriteLine("\nTriângulo Isósceles");
                            }
                            else
                            {
                                Console.WriteLine("\nTriângulo Escaleno");
                            }
                        }
                        else
                        {
                            Console.WriteLine("\nNão é triângulo!!!");
                        }

                        Console.Write("\nDeseja continuar no programa 5? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 6: // 6 - Equação do 2º grau
                    do
                    {
                        Console.Clear();
                        Console.WriteLine("=== PROGRAMA EQUAÇÃO 2º GRAU ===");
                        Console.Write("Digite o valor de A: ");
                        valorA = double.Parse(Console.ReadLine());
                        Console.Write("Digite o valor de B: ");
                        valorB = double.Parse(Console.ReadLine());
                        Console.Write("Digite o valor de C: ");
                        valorC = double.Parse(Console.ReadLine());

                        delta = (valorB * valorB) - (4 * valorA * valorC);

                        Console.WriteLine($"\nDelta: {delta}");

                        if (delta < 0.0)
                        {
                            Console.WriteLine("Resultado não é real, pois o Delta é negativo!");
                        }
                        else
                        {
                            x1 = (-valorB + Math.Sqrt(delta)) / (2 * valorA);
                            x2 = (-valorB - Math.Sqrt(delta)) / (2 * valorA);

                            Console.WriteLine($"X1 é igual a: {x1:F2}");
                            Console.WriteLine($"X2 é igual a: {x2:F2}");
                        }

                        Console.Write("\nDeseja continuar no programa 6? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 7: // 7 - Tabuada
                    do
                    {
                        Console.Clear();
                        Console.WriteLine("=== PROGRAMA TABUADA ===");
                        Console.Write("Digite o número que deseja ver a tabuada: ");
                        numero1 = double.Parse(Console.ReadLine());
                        Console.Write("Digite até qual multiplicador você deseja: ");
                        contador = int.Parse(Console.ReadLine());
                        Console.WriteLine($"\nTabuada de {numero1}:");

                        for (multiplicador = 1; multiplicador <= contador; multiplicador++)
                        {
                            resultadoTabuada = numero1 * multiplicador;
                            Console.WriteLine($"{numero1} x {multiplicador} = {resultadoTabuada}");
                        }

                        Console.Write("\nDeseja continuar no programa 7? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 8: // 8 - Número Aleatório
                    do
                    {
                        numeroSecreto = random.Next(1, 250); // Gera um número entre 1 e 249
                        Console.Clear();
                        tentativas = 0;
                        palpite = 0;

                        Console.WriteLine("=======================================");
                        Console.WriteLine(" BEM-VINDO AO JOGO DE ADIVINHAÇÃO! ");
                        Console.WriteLine("=======================================");
                        Console.WriteLine("Tente adivinhar o número de 1 a 249.\n");

                        while (palpite != numeroSecreto)
                        {
                            Console.Write("Digite o seu palpite: ");
                            palpite = int.Parse(Console.ReadLine());
                            tentativas++;

                            if (palpite < numeroSecreto)
                            {
                                Console.WriteLine("O número secreto é MAIOR!\n");
                            }
                            else if (palpite > numeroSecreto)
                            {
                                Console.WriteLine("O número secreto é MENOR!\n");
                            }
                        }

                        Console.WriteLine("---------------------------------------");
                        Console.WriteLine($"PARABÉNS! Você acertou o número {numeroSecreto}");
                        Console.WriteLine($"Total de tentativas: {tentativas}");
                        Console.WriteLine("---------------------------------------");

                        Console.Write("\nDeseja continuar no programa 8? (S/N): ");
                        resp = Console.ReadLine();

                    } while (resp.Equals("S", StringComparison.OrdinalIgnoreCase));
                    break;

                case 9: // 9 - Sair
                    Console.WriteLine("Saindo do programa... Até logo!");
                    break;

                default:
                    Console.Write("Opção inválida! Digite qualquer tecla e aperte Enter para voltar ao menu: ");
                    Console.ReadLine();
                    break;
            }

        } while (opcao != 9);
    }
}
