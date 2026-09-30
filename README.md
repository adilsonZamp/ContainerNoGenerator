# Calculadora de Dígito Verificador de Contêineres 
É um programa simples em Python que pega um input, valida se ele tem o formato correto e calcula o último dígito (verificador) de acordo com a norma internacional ISO 6346.

Segundo a norma, a quarta letra deve ser U, J ou Z para identificar unidades para frete geral (U), equipamento destacável relacionado ao contêiner (J) e reboques que transportam os contêineres (Z).

Atualmente o sistema opera totalmente no terminal pegando o input, validando e exibindo mensagens de acordo com os erros encontrados, calculando o dígito se o input tiver pelo menos 4 letras e 6 números.

## Como o cálculo funciona
1. Cada letra tem um valor, ex.: A = 10, B = 12, C = 13, e assim vai. A lógica aqui é que cada letra em ordem alfabética recebe um valor numérico começando em 10 e adicionando um a mais, múltiplos de 11 são desconsiderados ex.: K = 21, L = 23 ← pula 22, M = 24
2. Após converter as letras temos 10 números, os quais serão multiplicados por 2^i, inicialmente i vale 0 e a cada posição a direita é adicionado +1
3. Depois de obter o resultado da multiplicação somamos todos os 10 valores
4. Então pegamos o resto da divisão do total por 11 (soma % 11)
5. O resto obtido é o dígito verificador. Se o resto for 10, o dígito é considerado 0

## Próximos passos
Em breve pretendo implementar uma função para gerar números aleatórios e válidos, também estou pensando em criar uma interface simples para treinar o uso do tkinter e fazer uma versão executável por comando no terminal
