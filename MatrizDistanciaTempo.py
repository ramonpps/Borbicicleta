import requests
import csv

estacoes = {
    "Praca Arariboia": (-22.895631838467075, -43.124899960635375),
    "Estacao das Barcas Charitas": (-22.932304595900444, -43.09928328774055),
    "UFF - Campus Valonguinho": (-22.896405514258564, -43.12563537779726),
    "Praia de Icarai": (-22.907545758498568, -43.11204286551062),
    "Terminal Rodoviario Joao Goulart": (-22.890036515681363, -43.12588182378228),
    "Praia de Sao Francisco": (-22.91811262505584, -43.09448110941094),
    "Museu de Arte Contemporanea (MAC)": (-22.90733073016797, -43.126150379425006),
    "Santa Rosa": (-22.898919136366207, -43.09838055462202),
    "UFF - Campus Praia Vermelha": (-22.903761658709644, -43.130206268244464),
    "UFF - Campus Gragoata": (-22.89918236796127, -43.13071039109646),
}

velocidade_media = 20
dados = []

for origem_nome, origem_coords in estacoes.items():
    for destino_nome, destino_coords in estacoes.items():
        if origem_nome != destino_nome:
            origem_str = f"{origem_coords[1]},{origem_coords[0]}"
            destino_str = f"{destino_coords[1]},{destino_coords[0]}"
            
            url = f"http://router.project-osrm.org/route/v1/cycling/{origem_str};{destino_str}?overview=false"
            
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
