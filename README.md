### Descrição do Projeto
Este projeto contém soluções para uma série de problemas de programação e lógica, implementadas em Python. As soluções abordam tópicos como verificação na sequência de Fibonacci, contagem de letras em strings, cálculos de soma em loops, análise de sequências numéricas e um desafio prático envolvendo interruptores e lâmpadas.

## Problemas e Soluções
# 1. Verificação de Número na Sequência de Fibonacci
Objetivo: Verificar se um número pertence à sequência de Fibonacci.

[Fibonacci](https://github.com/EllenCassia/Teste-Tecnico-Estagio--Ribeirao-Preto/blob/main/fibonacci.py)

# 2. Contagem da Letra 'a' em uma String
Objetivo: Verificar a existência e contar a quantidade de vezes que a letra 'a' aparece em uma string.

Código:
def contar_letra_a(texto):
    contagem = texto.lower().count('a')
    return contagem
    
texto = input("Digite uma string para contar a letra 'a': ")
contagem = contar_letra_a(texto)
print(f"A letra 'a' aparece {contagem} vez(es) na string.")
Resposta: O código conta e exibe a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) aparece na string fornecida.

# 3. Resultado do Código Fornecido
   
Código:
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
R: O valor final da variável SOMA é 78. O código soma os números de 2 a 11 (inclusive).

# 4. Completação de Sequências Numéricas
a) 1, 3, 5, 7, 9
b) 2, 4, 8, 16, 32, 64, 128
c) 0, 1, 4, 9, 16, 25, 36, 49
d) 4, 16, 36, 64, 100
e) 1, 1, 2, 3, 5, 8, 13
f) 2, 10, 12, 16, 17, 18, 19, 20

# 5. Identificação de Interruptores e Lâmpadas
Desafio: Descobrir qual interruptor controla qual lâmpada usando duas idas até as salas das lâmpadas.

Solução:

Ligue o primeiro interruptor e deixe-o ligado por 10 minutos.
Desligue o primeiro interruptor e ligue o segundo.
Vá até as salas das lâmpadas:
A lâmpada acesa é controlada pelo segundo interruptor.
A lâmpada quente e apagada é controlada pelo primeiro interruptor.
A lâmpada fria e apagada é controlada pelo terceiro interruptor.
