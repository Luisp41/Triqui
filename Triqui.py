def triqui(tablero, simbolo):
    combinaciones_ganadoras = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    tablero = [" "] + tablero
    for combinacion in combinaciones_ganadoras:
        a, b, c = combinacion
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] != " ":
            return True
    return False
tablero = [
    ["X", "X", "O"],
    [" ", "X", "O"],
    [" ", "O", "X"]
]
tablero_planificado = [celda for fila in tablero for celda in fila]
print(triqui(tablero_planificado))
