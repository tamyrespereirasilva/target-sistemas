"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: • O menor valor de faturamento ocorrido em um dia do mês; • O maior valor de faturamento ocorrido em um dia do mês; • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE: a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

def main():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "OUTROS": 19849.53
    }

    soma = sum(map(lambda x: float(x), faturamento.values()))

    for uf, valor in faturamento.items():
        porcentual = (valor / soma) * 100
        print(f"{uf} – {porcentual:3.2f}%")


if __name__ == "__main__":
    main()