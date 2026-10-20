"""Peça o nome do aluno e logo em seguida receba 3 ou mais notas, calcule a média e informe a situação do aluno:

Se media for menor que 5 aluno está reprovado
Se for de 5 e menor que 7 está em recuperação
igual maior que 7 aluno está aprovado"""

nome=str(input("Digite o nome do aluno "))
nota1=float(input("Digite a nota da média "))
nota2=float(input("Digite a nota da prova "))
nota3=float(input("Digite a note de comportamento "))

media=(nota1+nota2+nota3)/3



if media<5:
    print(f"O aluno {nome} foi reprovado com a nota {media}")

elif media>=5 and media<7:
    print(f"O aluno{nome} ficou de recuperação com a nota {media}")

elif media>=7:
    print(f"O aluno {nome} foi aprovado!!! Com a nota {media}")







