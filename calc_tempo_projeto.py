"""Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C.
No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
Se algum valor for negativo, mostre uma mensagem informando o erro."""

A = int(input("Informe os dias para a atividade A: "))
B = int(input("Informe os dias para a atividade B: "))
C = int(input("Informe os dias para a atividade C: "))

if A < 0 or B < 0 or C < 0:
    print("Erro: os dias nao podem ser negativos.")
else:
    print("Os dias restantes para as respectivas atividades são: {A}, {B}, {C}")
