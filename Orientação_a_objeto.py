class ColetorDeNumeros:
    def __init__(self):
        self.numeros = []

    def coletar(self):
        while True:
            try:
                entrada = int(input("Digite um número (ou -1 para sair): "))
                if entrada == -1:
                    print("Encerrando...")
                    break
                if 0 <= entrada <= 100:
                    self.numeros.append(entrada)
                else:
                    print("Apenas números de 0 a 100 são aceitos.")
            except ValueError:
                print("Digite apenas números.")

    def calcular_soma(self):
        soma = 0
        for n in self.numeros:
            soma += n
        return soma

    def exibir_resultados(self):
        print(f"Soma dos números válidos: {self.calcular_soma()}")
        print(f"Números coletados: {self.numeros}")


# --- Programa principal ---
coletor = ColetorDeNumeros()
coletor.coletar()
coletor.exibir_resultados()