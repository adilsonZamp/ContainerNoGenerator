i = 0

numero = ""
valido = True
mensagens = ""
listaValor = {
    "A":10, "B":12, "C":13, "D":14, "E":15, "F":16, "G":17, "H":18, "I":19, "J":20, "K":21, "L":23, "M":24, "N":25, "O":26, "P":27, "Q":28, "R":29, "S":30, "T":31, "U":32, "V":34, "W":35, "X":36, "Y":37, "Z":38
}

# adicionar função para gerar aleatorio
# gerar interface e comando no terminal

print("Insira o número do container (sem verificador): ")
print("Formato ABCD567890 ")
numero = str(input()).upper().strip()

# colocar as 4 letras como maiusculas e retirar espaços a mais (opcional)

# valida tamanho
if len(numero) != 10:
    mensagens = "Número fora do formato"
    valido = False

if not valido:
    print(mensagens)
    exit()
# valida estrutura (sem simbolos, 4 letras e 6 números)

# verifica se os 4 primeiros caracteres sao letras [ok]

for i in range(4):
    if numero[i] < 'A' or numero[i] > 'Z':
        valido = False
        mensagens += "Os 4 primeiros caracteres devem ser letras!\n"
        break
# verifica se o resto sao numeros
for i in range(4, 10):
    if numero[i] < '0' or numero[i] > '9':
        valido = False
        mensagens += "Os 6 últimos caracteres devem ser números!\n"
        break

print(numero, valido)
print("Mensagens: ", mensagens)

num = "A"
print(listaValor.__getitem__(num))
# calcular o verificador
# cada letra tem um valor (listaValor)
# Cada um dos 10 primeiros caracteres (letras convertidas e números de série) é multiplicado por 2^i, onde i varia de 0 a 9 (da esquerda para a direita). 
# soma tudo os 10 valores
# divide o resultado por 11 e pega o resto da divisão
# O resto obtido é o dígito verificador. Se o resto for 10, o dígito é considerado 0 (ou o valor ajustado conforme a norma).
