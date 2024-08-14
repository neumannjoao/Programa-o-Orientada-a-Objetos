import csv

# Nome do arquivo CSV
filename = 'dados_programacao.csv'

# Lendo o arquivo CSV
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Ler o cabeçalho
    print(f"{header[0]:<10} {'CPU':>5} {'Memória':>10} {'Tempo':>5} {'Linhas':>5}")

    for row in reader:
        linguagem = row[0]
        cpu = float(row[1])
        memoria = float(row[2])
        tempo = int(row[3])
        linhas = int(row[4])

        print(f"{linguagem:<10} {cpu:>5.2f} {memoria:>10.2f} {tempo:>5} {linhas:>5}")
    
    soma_cpu = soma_memoria = soma_tempo = soma_linhas = 0
    contador = 0

    # Lendo o arquivo CSV
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ler o cabeçalho
    
        # Encontrar índices das colunas para métricas
        idx_cpu = header.index('cpu')
        idx_memoria = header.index('memória')
        idx_tempo = header.index('tempo')
        idx_linhas = header.index('linhas')
    
        for row in reader:
            # Somar os valores das métricas
            soma_cpu += float(row[idx_cpu])
            soma_memoria += float(row[idx_memoria])
            soma_tempo += float(row[idx_tempo])
            soma_linhas += int(row[idx_linhas])
            contador += 1

    # Calcular as médias
    media_cpu = soma_cpu / contador
    media_memoria = soma_memoria / contador
    media_tempo = soma_tempo / contador
    media_linhas = soma_linhas / contador

    # Exibir as médias com três casas decimais
    print("Média das Métricas:")
    print(f"CPU: {media_cpu:.3f}")
    print(f"Memória: {media_memoria:.3f}")
    print(f"Tempo: {media_tempo:.3f}")
    print(f"Linhas: {media_linhas:.3f}")