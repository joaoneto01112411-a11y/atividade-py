# 1- Crie uma variavel mensagem e exiba uma mensagen na tela
# 2- Crie uma variavel numero e exiba esse numero na tela
# 3- Crie duas variaveis numéricas e faça as 4 operações matematicas com esses números> Faça tambem a exponenciação e o resto da divisão
# 4- CRie duas variaveis de texto e faça a concatenação dessas mensagens
# 5- Faça um programa que receba um texto e faça-o repetir 5 vezes
# 6- Crie uma variavel de texto em minúsculo e deixo-o com todas as letras maiúsculas
# 7- Crie um programa que receba um texto do usuario e exiba na tela 
# 8- CRie um programa que receba do usuario nome, idade, altura, cidade e  estado e exiba a seguinte frase na tela: "Olá, meu nome é ____, tenho ____ anos de idade. Moro na cidade de ______/__". Use printf
# 9- Crie um programa com uma variavel numero qualquerl. Depois, crie uma variavel chute pedindo para o usuario digitar um numero. Na sequencia, crie uma condição para saber se o chute é igual a variavel. Caso seja igual exiba uma mensagem "Voce acertou", se for diferente exiba a mensagem "voce errou"1


mensagem = 'Meu nome é Maria'
print(mensagem)

numero = 8
print(numero)

numero2 = 2
soma = numero + numero2
print(soma)

numero3 = 40
numero4 = 60
soma = numero3 + numero4
div = numero3 / numero4 
sub = numero3 - numero4
multi = numero3 * numero4
print(soma)
print(sub)
print(div)
print(multi)

expo = numero ** numero3
Resto_div = numero3 % numero
Div_interia = numero4 // numero
print(expo)
print(Resto_div)
print(Div_interia)


texto1 = "batata"
texto2 = "banana"
c = texto1 + " " + texto2
print(c)

texto = "aula"
repetição = texto * 5 
print(repetição)


texto5 = 'bom dia'
print(texto5.upper())

texto3 = input('Coloque sua mensagem')
print(texto3)

nome2 = input('Digite seu nome')
idade = int (input(' Digite sua idade'))
altura = float(input("Digite sua altura"))
cidade = input('Digite sua cidade')
estado = input('Digite seu estado')
print(nome2)
print(idade)
print(altura)
print(cidade)
print(estado)

print (f'meu nome é {nome2}, tenho {idade} anos de idade. Moro na cidade de {cidade} do estado do {estado}. minha altura é {altura}') 