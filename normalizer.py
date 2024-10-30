import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Abrir o arquivo CSV e ler o conteúdo
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []
        
        # Converter cada linha do CSV em um dicionário e adicionar à lista
        for row in csv_reader:
            # Converter strings de listas para listas reais
            if 'platforms' in row:
                row['platforms'] = eval(row['platforms'])
            if 'genres' in row:
                row['genres'] = eval(row['genres'])
            if 'price' in row:
                row['price'] = float(row['price'])
            if 'rating' in row:
                row['rating'] = float(row['rating'])
            if 'votes' in row:
                row['votes'] = int(row['votes'])
                
            # Adicionar o dicionário à lista
            data.append(row)
    
    # Salvar a lista de dicionários no arquivo JSON
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Exemplo de uso:
csv_to_json('games.csv', 'games.json')