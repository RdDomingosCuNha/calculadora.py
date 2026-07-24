n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))
print()
print('\nEscolha uma operação:')
print('1 - somar')
print('2 - subtrair')
print('3 - multiplicar')
print('4 - dividir')
opcao = input('\nescolha uma operação:')
if opcao == '1':
    resultado = n1 + n2
    print('Resulltado', resultado)
elif opcao == '2':
    resultado = n1 - n2
    print('Resultado', resultado)
elif opcao == '3':
    resultado = n1 * n2
    print('Resultado', resultado)
elif opcao == '4':
    resultado = n1 / n1
    print('Resultado', resultado)
else:
    print('opcao invalida!')
