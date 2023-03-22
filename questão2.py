valor_1 = 0
valor_2 = 1
valor_3 = 0

numero_para_consulta = int(input('Digite um número para consultar se faz parte da sequência de Fibonacci: '))

while numero_para_consulta > valor_3:
    valor_3 = valor_1 + valor_2
    valor_1 = valor_2
    valor_2 = valor_3

if numero_para_consulta == 0 or numero_para_consulta == 1:
    print('O número faz parte da sequência de Fibonacci.')
elif numero_para_consulta == valor_3:
    print('O número faz parte da sequência de Fibonacci.')
else:
    print('O número não faz parte da sequência de Fibonacci.')
