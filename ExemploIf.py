#Demonstração do uso de if/elif/else...

print("Digite a sua idade")
idade = int(input())

if idade <18:
    print("Você não é maior idade!")
    print("Não poderá realizar a operação! ")
elif idade >=65:
    print("Você já está pronto para se aposentar? ")
    print("Poderemos oferecer suporte técnico. ")
else:
    print("Você é maior de idade")
    print("Portanto,poderá realizar a operação ")
print("Obrigado por optar pelos  nossos serviços!  ")