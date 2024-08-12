import requests
import csv

estacoes = {
    "Praca Arariboia": (-22.8973, -43.1246),
    "Estacao das Barcas Charitas": (-22.9262, -43.0972),
    "UFF - Campus Valonguinho": (-22.8949, -43.1266),
    "Praia de Icarai": (-22.9053, -43.1114),
    "Terminal Rodoviario Joao Goulart": (-22.8993, -43.1216),
    "Praia de Sao Francisco": (-22.9245, -43.0970),
    "Museu de Arte Contemporanea (MAC)": (-22.9056, -43.1352),
    "Santa Rosa": (-22.9092, -43.1108),
    "UFF - Campus Praia Vermelha": (-22.9307, -43.1669),
    "UFF - Campus Gragoata": (-22.8987, -43.1244),
}

velocidade_media = 20
dados = []

for origem_nome, origem_coords in estacoes.items():
    for destino_nome, destino_coords in estacoes.items():
        if origem_nome != destino_nome:
            origem_str = f"{origem_coords[1]},{origem_coords[0]}"
            destino_str = f"{destino_coords[1]},{destino_coords[0]}"
            
            url = f"http://router.project-osrm.org/route/v1/driving/{origem_str};{destino_str}?overview=false"
            
            response = requests.get(url)
            data = response.json()
            
            distancia = round(data['routes'][0]['distance'] / 1000, 2)
            tempo_viagem = round(distancia / velocidade_media, 2)

            dados.append([origem_nome, destino_nome, distancia, tempo_viagem])

with open('outputs\\distancia_tempo.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Origem', 'Destino', 'Distancia (km)', 'Tempo de Viagem (h)'])
    writer.writerows(dados)

print("O arquivo 'distancia_tempo.csv' foi criado com sucesso.")
