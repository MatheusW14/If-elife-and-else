"""Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas.
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento."""

despesas = float(input("Digite o total de despezas do mês(R$): "))

if despesas <= 3000.0:
    print("Orçamento dentro do limite.")
else:
    print("Atenção, você ultrapassou o limirte do orçamento.")
