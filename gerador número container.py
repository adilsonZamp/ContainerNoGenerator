import random
import sys

letras = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
listaValor = {
    "A":10, "B":12, "C":13, "D":14, "E":15, "F":16, "G":17, "H":18, "I":19, "J":20, "K":21, "L":23, "M":24, "N":25, "O":26, "P":27, "Q":28, "R":29, "S":30, "T":31, "U":32, "V":34, "W":35, "X":36, "Y":37, "Z":38
}

escolha = None
numero = ""
valido = True
mensagens = ""

# gerar interface e comando no terminal

# adicionar função para gerar aleatorio
def geraDigito(numero):
    global valido, mensagens
    digitoVerificador = 0
    valorNumero = []
    soma = 0

    # tamanho obrigatório
    if len(numero) != 10:
        mensagens = "Número fora do formato"
        print(mensagens)
        exit()

    # valida estrutura (sem simbolos, primeiro 3 letras, quarta letra sendo U, J ou Z e depois 6 números)
    for i in range(4):
        if numero[i] < 'A' or numero[i] > 'Z':
            valido = False
            mensagens += "Os 4 primeiros caracteres devem ser letras!\n"
            break

    if numero[3] not in ["U", "J", "Z"]:
        mensagens += "A ISO 6346 determina que a quarta letra seja U, J ou Z\n"

    for i in range(4, 10):
        if numero[i] < '0' or numero[i] > '9':
            valido = False
            mensagens += "Os 6 últimos caracteres devem ser números!\n"
            break

    print("O número:", numero, "é", "válido" if valido else "inválido")

    if not valido or mensagens:
        print("Mensagens:\n"+mensagens)

    if valido:
        for i in range(10):
            if i < 4:
                valorNumero.append(listaValor[numero[i]])
            else:
                valorNumero.append(int(numero[i]))

        for i in range(10):
            valorNumero[i] = valorNumero[i] * (2 ** i)
            soma += valorNumero[i]
        
        digitoVerificador = soma % 11

        if digitoVerificador == 10:
            digitoVerificador = 0

        numero += str(digitoVerificador)

        return numero

if escolha is None:
    print("Digite 1 para digitar o número ou 2 para gerar aleatoriamente")
    escolha = input()

if int(escolha) == 1:
    print("Insira o número do container (sem verificador): ")
    print("Formato de Referência ABCD567890 ")
    numero = str(input()).upper().strip()

    numero = geraDigito(numero);

    print("Número do Conteiner:", numero)

    print()
elif int(escolha) == 2:
    print("Gerando Aleatório")
    for i in range(3):
        numero += random.choice(letras)
    numero += 'U'

    for i in range(6):
        numero += str(random.randint(0, 9))

    numero = geraDigito(numero)

    print("Número gerado aleatoriamente:", numero)
else: 
    print("Tente novamente...")
