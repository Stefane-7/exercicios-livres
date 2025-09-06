"""10. Crie um dicionário com cores e seus códigos hexadecimais. Use um loop while para
permitir que o usuário procure o código de uma cor repetidamente. O loop deve terminar
quando o usuário digitar "sair"."""


cores = {
    "preto": "#000000",
    "branco": "#FFFFFF",
    "vermelho": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF",
    "amarelo": "#FFFF00",
    "ciano": "#00FFFF",
    "magenta": "#FF00FF",
    "laranja": "#FFA500",
    "rosa": "#FFC0CB",
    "roxo": "#800080",
    "marrom": "#A52A2A",
    "cinza": "#808080",
    "turquesa": "#40E0D0",
    "dourado": "#FFD700"
}

# Dicionário invertido: código -> cor

while True:
    entrada = input("Digite o nome ou o código da cor (ou 'sair' para parar): ").strip()
    
    if entrada.lower() == "sair":
        print("Encerrando...")
        break
    
    # Se for um código (começa com #), procuramos no dicionário invertido
    if entrada.startswith("#"):
        cor = codigos_para_cores.get(entrada.upper())
        if cor:
            print(f"O código {entrada.upper()} corresponde à cor: {cor}")
        else:
            print(f"Nenhuma correspondência encontrada para o código: {entrada}")
    else:
        # Se for nome da cor, procuramos diretamente
        codigo = cores.get(entrada.lower())
        if codigo:
            print(f"A cor {entrada.lower()} corresponde ao código: {codigo}")
        else:
            print(f"Nenhuma correspondência encontrada para a cor: {entrada}")