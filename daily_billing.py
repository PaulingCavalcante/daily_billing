import json

dados = {
    "faturamento_diario": [0, 1500.0, 2344.23, 0, 4324.56, 0, 1254.98, 0, 0, 2444.44, 500.0, 0, 6000.0, 0, 0, 1000.0, 0, 4200.0, 0, 1230.0]
}

faturamento = [valor for valor in dados['faturamento_diario'] if valor != 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_media = len([dia for dia in faturamento if dia > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")