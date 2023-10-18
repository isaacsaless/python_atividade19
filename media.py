# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print("Calculadora de média")

nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))

if (nota1+nota2)/2 < 5:
    print(f"Sua nota foi de {(nota1+nota2)/2:.1f}, por conta disso você foi REPROVADO.")
elif (nota1+nota2)/2 > 5 and (nota1+nota2)/2 <6.9:
    print(f"Sua nota foi de {(nota1+nota2)/2:.1f}, como a média é 7 você ficou de RECUPERAÇÃO.")
else: 
    print(f"Sua nota foi de {(nota1+nota2)/2:.1f}, por conta disso você foi APROVADO.")