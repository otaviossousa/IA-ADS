"""Múltiplos de Três e Cinco: Escreva um programa que imprime os números de 1 a 100, mas para múltiplos de três
imprima "Fizz" em vez do número e para os múltiplos de cinco imprima "Buzz". Para números que são múltiplos de ambos
três e cinco, imprima "FizzBuzz"."""


def fizz_buzz():
    x: int = 1
    while x <= 100:
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)
        x += 1


# fizz_buzz()


"""Conversor de Notas: Dada uma nota numérica, converta-a em conceitos A, B, C, D, E ou F, seguindo a tabela de 
conversão tradicional (90 para cima é A, 80 a 89 é B, etc.). Inclua uma verificação para entrada inválida (notas 
abaixo de 0 ou acima de 100)."""


def conversor_notas():
    nota = 0
    while True:
        nota = float(input('Digite uma nota entre 0 e 100: '))
        if 0 <= nota <= 100:  # nota >= 0 and nota <= 100
            break
    if nota > 90:
        print('A')
    elif nota > 80:
        print('B')
    elif nota > 70:
        print('C')
    elif nota > 60:
        print('D')
    elif nota > 50:
        print('E')
    else:
        print('F')


# conversor_notas()

"""###Encontrar Elementos Comuns: Dadas duas listas de números, escreva um programa que encontre e imprima os elementos 
comuns às duas listas, sem repeti-los, utilizando estruturas de controle para a comparação.

# Defina duas listas de números.
# Percorra cada elemento da primeira lista. (use o for)
# Verifique se o elemento está presente na segunda lista. (use in)
# Se estiver, verifique se o elemento ainda não foi adicionado à lista de elementos comuns. (use in)
# Se não estiver, adicione-o à lista de elementos comuns.
"""

"""###Detector de Palíndromo: Escreva uma função que verifica se uma dada string é um palíndromo (palavras que lêem 
o mesmo de trás para frente), ignorando espaços e maiúsculas/minúsculas, considere que a string não terá acentos ou 
outros caracteres especiais. 

**Dicas** 
- Remover espaços e converter todas as letras para minúsculas. 
- Remover espaços (pode usar o `replace(" ", "")`) 
- Converter para minúsculo (`lower()`) 
- Comparar a string original com sua versão invertida (use slicing) 
- Se forem iguais, a string é um palíndromo; caso contrário, não é."""

"""### Quadrados Perfeitos: Utilize uma list comprehension para criar uma lista dos primeiros 10 quadrados perfeitos 
(1, 4, 9, ...) que são divisíveis por um dado número n. **Dica** - Quadrados perfeitos: `n ** 2` - list comprehension 
`[<var> for <var> in <iterable> if <expr>] `"""

"""### Interseção de Listas: Utilize list comprehensions para criar uma lista que seja a interseção de dois outros 
conjuntos (listas) de números, sem usar sets. **Dicas** - Use o comando `in`"""

"""### Diferença de Listas: Dadas duas listas de números, utilize uma list comprehension para criar uma lista que 
contenha todos os elementos da primeira lista que não estão na segunda. 

**Dicas** 
- `set` serve para criar um conjunto, que é uma coleção não ordenada e sem elementos duplicados. Possui as seguintes 
operações: 
- A operação de união (|) combina dois conjuntos, retornando um novo conjunto contendo todos os elementos presentes em 
ambos os conjuntos, sem duplicatas. 
- A operação de interseção (&) retorna um novo conjunto contendo apenas os elementos que estão presentes em ambos os 
conjuntos originais. 
- A operação de diferença (-) retorna um novo conjunto contendo os elementos que estão presentes no primeiro conjunto, 
mas não no segundo. 
- A operação de diferença simétrica (^) retorna um novo conjunto contendo os elementos que estão presentes em apenas um 
dos conjuntos, mas não em ambos."""

"""### Conversão de Temperaturas: Escreva uma list comprehension que converta uma lista de temperaturas em Celsius para 
Fahrenheit. Fórmula: F = C * 9/5 + 32.
"""

"""### Filtrar Palavras: Dada uma lista de palavras, use uma list comprehension para criar uma lista com apenas as 
palavras que têm mais de 4 caracteres e menos de 8 caracteres.
"""

"""### Função Recursiva de Fibonacci: Escreva uma função recursiva que retorne o n-ésimo número de Fibonacci. 

- A sequência de Fibonacci é uma série de números onde cada número é a soma dos dois números anteriores. Ela começa com 
os números 0 e 1, e os números subsequentes são calculados somando os dois números anteriores. Aqui estão os 
primeiros números da sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..."""

"""### Validação de Senha: Escreva uma função que receba uma senha (string) e retorne True se a senha for forte. 
Uma senha forte deve ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um número.
"""

"""### Agregação de Lista: Escreva uma função que receba uma lista de números e retorne um dicionário com as chaves 
'max', 'min', 'average' e 'sum' correspondendo aos valores máximo, mínimo, média e soma da lista, respectivamente.
"""

"""### MDC (Máximo Divisor Comum): Implemente uma função que calcule o Máximo Divisor Comum entre dois números usando 
o algoritmo de Euclides.
"""

"""### Rotacionar Lista: Escreva uma função que rotacione os elementos de uma lista à direita n vezes. 
Por exemplo, para a lista [1, 2, 3, 4, 5] e n = 2, o resultado seria [4, 5, 1, 2, 3].
"""

"""### Contagem de Palavras: Dada uma longa string de texto, escreva uma função que retorne um dicionário onde as chaves
 são palavras únicas e os valores são o número de vezes que cada palavra aparece no texto."""

"""### Inverter Dicionário: Escreva uma função que receba um dicionário e retorne um novo dicionário onde os valores do 
original se tornam as chaves e as chaves se tornam os valores.
"""

"""### Agrupamento por Tamanho de Palavra: Dada uma lista de palavras, escreva uma função que retorne um dicionário onde
 as chaves são os tamanhos das palavras e os valores são listas de palavras desse tamanho."""

"""### Mesclagem de Dicionários: Escreva uma função que combine dois dicionários. Se uma chave estiver presente em ambos
, adicione os valores. Considere que os valores são numéricos."""

"""### Manipulação de Data e Hora: Utilize o módulo datetime para escrever uma função que retorne a diferença em dias 
entre duas datas passadas como strings.
"""

"""### Expressões Regulares: Utilize o módulo re para escrever uma função que valide endereços de email. 
Um endereço é válido se seguir o formato nome@dominio.com."""

"""### Criação de Números Aleatórios: Utilize o módulo random para escrever uma função que gere uma lista de n números 
aleatórios entre dois valores, ambos inclusivos.
"""

"""### Execução de Comandos do Sistema: Utilize o módulo os para escrever um script que liste todos os arquivos 
e diretórios no diretório atual."""

"""### Classe Conta Bancária: Crie uma classe ContaBancaria que encapsule o nome do titular e o saldo. Utilize métodos 
para depositar, sacar e verificar o saldo, garantindo que o saldo não possa ser diretamente modificado fora dos métodos 
e que saques não possam deixar o saldo negativo.
"""

"""### Classe Carro com Encapsulamento: Implemente uma classe Carro que encapsule atributos como marca, modelo e 
quilometragem. Adicione métodos para retornar a marca e o modelo, aumentar a quilometragem e retornar a quilometragem 
atual. Use o decorador @property para tornar a quilometragem uma propriedade "apenas leitura".
"""

"""### Sistema de Avaliação de Alunos: Crie uma classe Aluno que encapsule o nome do aluno, notas e a média das notas. 
Utilize métodos para adicionar notas e calcular a média. A lista de notas não deve ser acessível fora dos métodos da 
classe.
"""

"""### Gerenciador de Tarefas: Implemente uma classe Tarefa que encapsule detalhes como titulo, descricao e concluida. 
Adicione métodos para marcar uma tarefa como concluída e verificar se está concluída, usando o princípio do 
encapsulamento para proteger o estado da tarefa."""