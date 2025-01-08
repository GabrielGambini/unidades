def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

while True:

    temperatura = float(input("Digite a temperatura (Se deseja sair, tecle 0): "))

    if temperatura == 0:
        print ("Obrigado por usar o programa!")
        break

    unidade = input("Escolha (C para Celsius, K para Kelvin) : "). upper()

    if unidade == 'C':
        fahrenheit = celsius_para_fahrenheit (temperatura)
        print(f"{temperatura}℃ é igual a {fahrenheit : . 2f}ºF")
        continue

    elif unidade == 'K':
        fahrenheit = kelvin_para_fahrenheit(temperatura)
        print (f"{temperatura}ºK é igual a {fahrenheit: . 2f}ºF")
        continue

    else:
        print("Digite um valor válido!")

