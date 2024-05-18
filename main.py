def calcular_nivel(vitorias, derrotas):
    saldo = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo, nivel

# Entrada de dados
vitorias = int(input("Digite o número de vitórias: "))
derrotas = int(input("Digite o número de derrotas: "))

# Chamar a função e obter o resultado
saldoVitorias, nivel = calcular_nivel(vitorias, derrotas)

# Exibir mensagem
print(f"O Herói tem de saldo de {saldoVitorias} está no nível de {nivel}")
