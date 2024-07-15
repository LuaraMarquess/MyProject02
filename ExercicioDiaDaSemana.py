print("Digite o dia da semana: ")
print("Digite o número referente ao estado da moeda:  ")
print("Segunda-feira")
print("Terça-Feira")
print("Quarta-feira")
print("Quinta-feira")
print("Sexta-feira")
print("Sábado")
print("Domingo")
estado = input()

match estado:
    case "Segunda-feira":
        print("Você poderá assistir um filme")
    case "Terça feira":
        print("Você poderá fazer uma caminhada")
    case "Quarta-feira":
        print("Você poderá viajar")
    case "Quinta-feira":
        print("Você poderá assistir aula")
    case "Sexta-feira":
        print("você poderá sair")
    case "Sábado":
        print("Final de semana começou pode descansar")
    case "Domingo":
        print("Descanso")
    case _:
        print("Operação INVÁLIDA")
