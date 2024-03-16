from functools import reduce


def calcula_saldo(lancamentos) -> float:
    valores = map(
        lambda l: l[0] if l[1] == "C" else -l[0], lancamentos
    )  # mapear valores: pos crédito e neg débito
    saldo = reduce(
        lambda acumulador, valor: acumulador + valor, valores, 0
    )  # reduce saldo final, 0 como acumulador

    return saldo


if __name__ == "__main__":
    lancamentos = [(200, "D"), (300, "C"), (100, "C")]  # exemplo
    saldo = calcula_saldo(lancamentos)
    print(saldo)
