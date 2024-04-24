'''
Interpolação básica de strings
s == string
d, i == int
f == float
x, X == Hexadecimal (ABCDEFG0123456789)
'''

nome = 'Matheus'
preco= 1000.3123123
variavel= '%s, o preço é R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15,15))