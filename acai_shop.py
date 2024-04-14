print('Bem-Vindo')

print('============Cardápio=============')
print('Tamanho | Cupuaçu (CP) | Açaí (AC)')
print('   P    |   R$ 10,00   | R$ 12,00')
print('   M    |   R$ 15,00   | R$ 17,00')
print('   G    |   R$ 19,00   | R$ 21,00\n')

#variavel que acumula os preços
acumulador = 0

while True:
    sabor = input('Entre com o sabor desejado (CP/AC):  ').upper()
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor inválido. Tente novamente')
        continue #se o usuário digitar a opção que não é valida volta para o while.

    tamanho = input('Entre com o tamanho desejado (P/M/G):  ').upper()
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente')
        continue  # se o usuário digitar a opção que não é valida volta para o while.



    #Cupuaçu
    if sabor == 'CP' and tamanho == 'P':
        acumulador = acumulador + 10
        print('Você pediu Cupuaçu no tamanho P, preço: R$10.00')

    elif sabor == 'CP' and tamanho == 'M':
        acumulador = acumulador + 15
        print('Você pediu Cupuaçu no tamanho P, preço: R$15.00')

    elif sabor == 'CP' and tamanho == 'G':
        acumulador = acumulador + 19
        print('Você pediu Cupuaçu no tamanho P, preço: R${19.00}')

    #Açaí
    elif sabor == 'AC' and tamanho == 'P':
        acumulador = acumulador + 12
        print('Você pediu Açaí no tamanho P, preço: R$12.00')

    elif sabor == 'AC' and tamanho == 'M':
        acumulador = acumulador + 17
        print('Você pediu Açaí no tamanho P, preço: R$17.00')

    elif sabor == 'AC' and tamanho == 'G':
        acumulador = acumulador + 21
        print('Você pediu Açaí no tamanho P, preço: R$21.00')

    carrinho = input('\nDeseja mais algo (S/N)?\n').upper()

    if carrinho == 'S':
        continue

    else:
        print('O valor total a ser pago é de R${:.2f}'.format(acumulador))
        break