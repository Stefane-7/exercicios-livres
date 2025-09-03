cores = ("vermelho", "verde", "azul", "verde")
cores_01 = list(cores)
cores_01.append("amarelo")
cores_01 = tuple(list(dict.fromkeys(cores_01)))

print(cores_01)