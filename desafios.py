 #001
def desafio001():
  print('olá mundo!')

#002
def desafio002():
  nome = input("digite seu nome:")
  print('seja bem vindo', nome)

#003
def desafio003():
  n1 = int(input('digite um numero: '))
  n2 = int(input('digite outro numero: '))
  print( f'a soma entre eles é {n1+n2}')

#004
def desafio004():
 algo = input('escreva algo: ')
 print('seu tipo é', type(algo))
 print('pertence ao grupo alphabetico:', algo.isalpha())
 print('pertence ao grupo numerico:', algo.isnumeric())
 print('pertence ao grupo alphanumerico:', algo.isalnum())
 print('estar em letras minusculas:',algo.islower())
 print('estar em letras maisculas:', algo.isupper())

#005
def desafio005():
 x = int(input('digite um numero:'))
 antecessor = x-1
 sucessor = x+1
 print('analisando o valor {}, seu antecessor é {}, seu sucessor é {}'.format(x, antecessor, sucessor))


#006
def desafio006():
  n = int(input('digite um numero:'))
  d = 2*n
  t = 3*n
  rq = n**(1/2)
  print('analisando {}, seu dobro é {}, seu tlipo é {}, sua raiz quadrada é {}'.format(n, d, t, rq))

#007
def desafio007():
  n = float(input('nota 1 do aluno:'))
  n1 = float(input('nota 2 do aluno:'))
  ma = (n+n1)/2
  print('a media entre {}, e {} é: {:.2}'.format(n, n1, ma))

#008
def desafio008():
 metros = float(input('digite uma medida em metros:'))
 mm = 1000 * metros
 cm = 100 * metros
 dm = 10 * metros
 km = metros / 1000
 hm = metros / 100
 dam = metros / 10
 print('o valor em metros {} corresponde a: \n milimetro: {} mm \n centimetro: {} cm \n decimetro: {} dm \n quilometro: {} km \n hectometro: {} hm \n decametro: {} dam'.format(metros,mm, cm, dm, km, hm, dam))

#009
def desafio009():
 y = int(input('digite um numero para ver sua tabuada:'))
 n1 = 1 * y
 n2 = 2 * y
 n3 = 3 * y
 n4 = 4 * y
 n5 = 5 * y
 n6 = 6 * y
 n7 = 7 * y
 n8 = 8 * y
 n9 = 9 * y
 n10 = 10 * y
 print('-' * 15)
 print(' {} X 1 = {}\n {} X 2 = {}\n {} X 3 = {}\n {} X 4 = {}\n {} X 5 = {}\n {} X 6 = {}\n {} X 7 ={}\n {} X 8 = {}\n {} X 9 = {}\n {} X 10 = {}'.format(y, n1, y, n2, y, n3, y, n4, y, n5, y, n6, y, n7, y, n8, y, n9, y, n10, y))
 print('-'*15)

#010
def desafio010():
  dinheiro = float(input('quanto de dinheiro voçe tem? R$'))
  dolar = dinheiro / 5.30
  print('com R${} voçe pode ter ${:.3} '.format(dinheiro, dolar))

#011
def desafio011():
  l = float(input('largura da parede:'))
  h = float(input('altura da parede:'))
  a = l * h
  t = a / 2
  print('sua parede tem dimensao de {} X {} e sua area é de {} m² precisara de {} litros de tinta para pintar a parede por completo.'.format(l, h, a, t ))

#012
def desafio012():
  valor = float(input('qual é o preço do produto? R$'))
  des = valor - (valor * 5 / 100)
  print('o produto que custava R${} com o desconto de 5% fica por R${}'.format(valor,des))

#013
def desafio013():
  salario = float(input('qual o salario do funcionario? R$'))
  alm = salario + (salario * 15 / 100)
  print(f'um funcionario que ganhava R${salario:.2f}, com um almento de 15% em seu salario passa a ganhar R${alm:.2f}')

#014
def desafio014():
 t = float(input('informe temperatura de onde voçe estar em C°:'))
 c = (t * 9 / 5) + 32
 print('{}C° equivale a {}°F '.format(t, c))

#015
def desafio015():
  dias = float(input('quantos dias alugado?'))
  km = float(input('quantos km rodados?'))
  total = (60 * dias) + (0.15 * km)
  print('o total que deve se pagar é: R${}'.format(total))

#016
from math import trunc
def desafio016():
  valor = float(input('digite um valor:'))
  print(f'o valor digitado foi {valor} e sua porçao inteira é {trunc(valor)}')

#017
from math import hypot
def desafio017():
  cao = float(input('qual o comprimento do cateto oposto:'))
  caa = float(input('qual o comprimento do cateto adjacente:'))
  print(f'a hipotenusa vai valer: {hypot(cao, caa):.2f}')

#018
from math import sin, cos, tan, radians
def desafio018():
  sct = float(input('digite um angulo:'))
  print(f'o angulo de {sct} tem o SENO de:{sin(radians(sct)):.2f}')
  print(f'o angulo de {sct} tem o COSSENO de {cos(radians(sct)):.2f}')
  print(f'o angulo de {sct} tem a TANGENTE de {tan(radians(sct)):.2f}')

#019
from random import choice
def desafio019():
  a1 = input('primeiro aluno:')
  a2 = input('segundo aluno:')
  a3 = input('terceiro aluno:')
  a4 = input('quarto aluno:')
  alunos = [a1, a2, a3, a4]
  print(f'o aluno escolhido foi: {choice(alunos)}')

#020
from random import shuffle
def desafio020():
  a1 = input('primeiro aluno:')
  a2 = input('segundo aluno:')
  a3 = input('terceiro aluno:')
  a4 = input('quarto aluno:')
  alunos = [a1, a2, a3, a4]
  shuffle(alunos)
  print('a ordem será:')
  print(alunos)

'''
#021
import pygame
def desafio021():
  pygame.init()
  pygame.mixer.music.load('desafios.mp3')
  pygame.mixer.music.play()
  pygame.event.wait()
 '''

#022
def desafio022():
  nome = input('digite seu nome completo:')
  print(f'seu nome em maiusculo fica: {nome.upper()}')
  print(f'seu nome em minusculo fica: {nome.lower()}')
  print(f'seu nome ao todo tem {len(nome)} letras')
  nomee = nome.split()
  print(f'seu primeiro nome tem {len(nomee[0])}')

#023
def desafio023():
  num = int(input('digite um numero:'))
  u = num // 1 % 10
  d = num // 10 % 10
  c = num // 100 % 10
  m = num // 1000 % 10
  print(f'unidade: {u}')
  print(f'dezena: {d}')
  print(f'centena: {c}')
  print(f'milhar: {m}')

#024
def desafio024():
  cidade = input('em que cidade voçe mora?').strip()
  print(cidade[:5].upper() == 'SANTO')

#025
def desafio025():
  nome = str(input('qual o seu nome completo:')).strip()
  print(f'seu nome tem silva? {"silva" in nome.lower()}')

#026
def desafio026():
  frase = input('escreva uma frase:').upper().strip()
  print(f'a letra A aparece {frase.count("A")}')
  print(f'a letra A apareceu pela primeira vem em {frase.find("A")}')
  print(f'a letra A apareceu pela ultima vez em {frase.rfind("A")}')

#027
def desafio027():
  nome =  input('escreva seu nome:').strip()
  n = nome.split()
  print(f'seu primeiro nome é:{n[0]}')
  print(f'seu ultimo nome é: {n[len(n)-1]}')

#028
def desafio028():
  from random import randint
  computador = randint(0, 5)
  print('=-='*15)
  print('vou pensar em um numero entre 0 e 5. tente adivinhar')
  print('=-='*15)
  diga = int(input('em qual eu pensei?'))
  if diga == computador:
    print(f'PARABENS voçe ganhou! eu realmente pensei no {diga}')
  else:
    print(f'Eu ganhei! pensei no numero {computador} e nao no {diga}')

#029
def desafio029():
  velocidade = float(input('qual a velocidade que voçe estar nesse momento?'))
  multa = 7 * (velocidade-30)
  if velocidade > 30:
    print(f'reduza a velocidade o maximo nessa via é 30km/h, se continuar pagara uma multa de R${multa}')
  else:
    print('estar na velocidade certa indicada pela via')

#030
def desafio030():
  n = int(input('digite um numero:'))
  par = n % 2
  if par == 0:
    print(f'o numero que voçe escolheu é PAR')
  else:
    print('o numero que voçe escolheu é IMPAR')

#031
def desafio031():
   distancia = int(input(' qual a distancia da sua viagem?'))
   
   l = 0.50*distancia
   p = 0.45*distancia
   
   if distancia <= 200:
     print(f'sua viagem de {distancia}KM/h custara R${l}')
   else:
     print(f'sua viagem de {distancia}KM/h custara R${p}')
     
#032
def desafio032():
  from datetime import date
  ano =  int(input('qual ano quer analisar? coloque 0 se quiser analizar o ano atual:'))
  if ano == 0:
    ano = date.today().year

  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano que voçe escolheu ele é BISSEXTO')
  else:
    print('o ano que voçe escolheu ele NÃO É BISSEXTO')
    
#033
def desafio033():
  v1 = int(input('primeiro valor:'))
  v2 = int(input('segundo valor:'))
  v3 = int(input('terceiro valor:'))
 
  if v1 < v2 and v1 < v3:
    print(f'o menor valor foi {v1}')
  if v2 < v3 and v2 < v1:
    print(f'o menor valor foi {v2}')
  if v3 < v1 and v3 < v2:
    print(f'o menor valor foi {v3}')
  
  if v1 > v2 and v1 > v3:
    print(f'o maior valor foi {v1}')
  if v2 > v3 and v2 > v1:
    print(f'o maior valor foi {v2}')
  if v3 > v1 and v3 > v2:
    print(f'o maior valor foi {v3}')
  
#034
def desafio034():
  salario = int(input('qual o valor do seu salario? R$'))
  if salario <= 1250:
   print(f'o valor do seu salario é R${salario} voçe recebeu um almento de 15% e receberá R${salario + (salario * 15 / 100)}')
  else:
    print(f'o valor do seu salario é R${salario} voçe recebeu um almento de 10% e receberá R${salario + (salario * 10 / 100)}')
#035
def desafio035():
  print('=-='*15)
  print('ANALISADOR DE TRIANGULOS')
  print('=-='*15)
  p1 = float(input('primeiro seguimento:'))
  p2 = float(input('segundo seguimento:'))
  p3 = float(input('terceiro seguimento:'))
  if (p2 - p3) < p1 < p2 + p3 and (p1 - p3) < p2 < p1 + p3 and (p1 - p2) < p3 < p1 + p2:
    print('essas medidas podem formar um trialgulo!')
  else:
    print('ops! essas medidas nao formam um triangulo')