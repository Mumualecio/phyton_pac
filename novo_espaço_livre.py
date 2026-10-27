nome=str(input("Digite o nome da pessoa "))
idade=int(input("Digite a idade da pessoa  "))

if idade<12:
    print(f"A pessoa cuja o nome é {nome} é conciderado(a) uma criança por ter {idade} anos de idade")

elif idade>=12 and idade<18:
    print(f"A pessoa cuja o nome é {nome} é conciderado(a) um(a) adolescente por ter {idade} anos de idade")

elif idade>=18:
    print(f"A pessoa cuja o nome é {nome} é conciderado(a) um(a) adulto(a) por ter {idade} anos de idade")






