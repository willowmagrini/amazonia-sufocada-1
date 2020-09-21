'''
Esse script lê os dados e imagens salvos
por process_tweet_variables.py e process_tweet_images.py
e salva arquivos JSON com os fios que serão publicados por tweet.py
'''

from datetime import datetime
import json
import os


###############
### Helpers ###
###############

def read_variables(time):
    '''
    Lê o arquivo JSON com as variáveis
    salvas para o período de tempo desejado
    e retorna como um dicionário do Python.

    Parâmetros:
​
    > time: O intervalo de tempo desejado. Pode ser
    '24h' ou '7d'.
    '''

    with open(f"../output/jsons/alerts/{time}.json") as f:
        data = json.load(f)

    return data


##########################
### Funções principais ###
##########################

def build_thread_most_fire_indigenous_land(data):
    '''
    Acessa as variáveis criadas por find_values
    para montar a thread diária sobre terras indígenas
    que será publicada no Twitter.
    
    O fio é estruturado em um array do objetos com um campo
    para o texto e um para o caminho de uma eventual foto.
    '''

    # Cria timestamps para garantir unicidade

    # Cria correspondências curtas para as variáveis,
    # tornando o texto do fio mais fácil de acompanhar.



    # Campos usados para evitar repetição exagerada
    day = datetime.now().strftime("%d/%m/%Y")
    total_geral = data["total_focos_amazonia_legal_2020"]
    total_fogo = data["terras_indigenas"]["total_focos_24h"]


    # Números

    a = data["terras_indigenas"]["areas_com_fogo_24h"]

    b = data["terras_indigenas"]["areas_mais_fogo_24h"]["1"]["nome"]
    c = data["terras_indigenas"]["areas_mais_fogo_24h"]["1"]["n_focos"]
    d = data["terras_indigenas"]["areas_mais_fogo_24h"]["1"]["porcentagem"]
    e = data["terras_indigenas"]["areas_mais_fogo_24h"]["1"]["dias_consecutivos"]

    f = data["terras_indigenas"]["areas_mais_fogo_24h"]["2"]["nome"]
    g = data["terras_indigenas"]["areas_mais_fogo_24h"]["2"]["n_focos"]
    h = data["terras_indigenas"]["areas_mais_fogo_24h"]["2"]["porcentagem"]

    i = data["terras_indigenas"]["areas_mais_fogo_24h"]["3"]["nome"]
    j = data["terras_indigenas"]["areas_mais_fogo_24h"]["3"]["n_focos"]
    k = data["terras_indigenas"]["areas_mais_fogo_24h"]["3"]["porcentagem"]

    
    tweets = [ ]
    
    # Abertura
    tweet = {
        "text": (f"Olá! Hoje, dia {day}, o robô do InfoAmazonia detectou {a} terras indígenas da Amazônia Legal com fogo ativo nas últimas 24h. Veja mais informações no fio 👇"),
        "img": None
    }
    tweets.append(tweet)
    
    # Chamada para imagem retirada da API do Mapbox.
    tweet = {
        "text": (f"Este mapa mostra todos os focos de calor em terras indígenas no dia {day}. Cada ponto representa uma área de 375 metros quadrados em que há atividade de fogo. As áreas escuras são os {a} territórios onde foram registados focos."),
        "img": "../output/imgs/tweets/ti_24h_todos_os_focos.jpg"
    }
    tweets.append(tweet)
    
    # Destaca a terra indígena com mais focos de fogo nas últimas 24h.
    tweet = { "text": f"A situação mais crítica acontece na Terra Indígena {b}, cujos {c} focos de calor representam {d}% do total rgistrado em terras indígenas nas últimas 24h. Além disso, lá existem áreas com fogo há {e} dias consecutivos. Veja no mapa.",
         "img": "../output/imgs/tweets/ti_24h_local_mais_focos.jpg"
    }
    tweets.append(tweet)
    
    
    tweet =  { 
                "text": (f"Ela, porém, não é a única que sofre. As outras duas terras com mais fogo no último dia foram estas:\n\n"
					f"- {f}: {h}% do total, com {g} focos\n"
					f"- {i}: {k}% do total, com {j} focos\n"),
                "img": None
            }
    tweets.append(tweet)
    
    
    tweet = { "text": f"Atenção para a metodologia! A análise usa dados do satélite SUOMI-NPP, da NASA, que não é o mesmo que o INPE usa como referência. Cada um dos {total_fogo} focos mostrados representa uma área de 375 m² com brilho e calor compatíveis com atividade de fogo.",
         "img": None
    }
    tweets.append(tweet)
    

    tweet = { "text": f"Você pode ver detalhes sobre a situação da Amazônia Legal na página do Amazônia Sufocada, no site do InfoAmazonia, e navegar pelo mapa interativo com todos os {total_geral} focos de calor registrados na região em 2020. \n\nhttps://infoamazonia.org/",
         "img": None
    }
    tweets.append(tweet)
    

    # Não podemos aceitar nenhum tuíte com mais de 280 toques
    tweets_over_280_chars = [len(tweet["text"]) >= 280 for tweet in tweets]
    #print(tweets_over_280_chars)
    assert not any(tweets_over_280_chars), "tuítes acima do limite de caracteres detectados"

    return tweets



def build_thread_most_fire_conservation_units(data):
    '''
    Acessa as variáveis criadas por find_values
    para montar a thread diária sobre unidades de conservação
    que será publicada no Twitter.
    
    O fio é estruturado em um array do objetos com um campo
    para o texto e um para o caminho de uma eventual foto.
    '''

    # Campos usados para evitar repetição exagerada
    day = datetime.now().strftime("%d/%m/%Y")
    total_geral = data["total_focos_amazonia_legal_2020"]
    total_fogo = data["unidades_de_conservacao"]["total_focos_24h"]

    # Cria correspondências curtas para as variáveis,
    # tornando o texto do fio mais fácil de acompanhar.

    a = data["unidades_de_conservacao"]["areas_com_fogo_24h"]

    b = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["1"]["nome"]
    c = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["1"]["n_focos"]
    d = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["1"]["porcentagem"]
    e = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["1"]["dias_consecutivos"]

    f = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["2"]["nome"]
    g = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["2"]["n_focos"]
    h = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["2"]["porcentagem"]

    i = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["3"]["nome"]
    j = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["3"]["n_focos"]
    k = data["unidades_de_conservacao"]["areas_mais_fogo_24h"]["3"]["porcentagem"]

    
    tweets = [ ]
    
    # Abertura
    tweet = {
        "text": (f"Oi! O InfoAmazonia consultou imagens de satélite e descobriu que há {a} áreas de proteção na Amazônia Legal com focos de fogo registrados no último dia, {day}. Mais detalhes no fio 👇"),
        "img": None
    }
    tweets.append(tweet)
    
    # Chamada para imagem retirada da API do Mapbox.
    tweet = {
        "text": (f"No mapa abaixo, as áreas mais escuras são unidades de conservação com focos de fogo no dia {day}. Cada ponto representa 375 metros quadrados em que o satélite detectou atividade de fogo."),
        "img": "../output/imgs/tweets/uc_24h_todos_os_focos.jpg"
        
    } 
    tweets.append(tweet)
    
    # Destaca a terra indígena com mais focos de fogo nas últimas 24h.
    tweet = { "text": f"Nas últimas 24h, a maior quantidade de focos aconteceu no local {b}, que teve {c} pontos de fogo ({d}% do total). Essa reserva está queimando há {d} dias. Veja no mapa:",

         "img": "../output/imgs/tweets/uc_24h_local_mais_focos.jpg"

    }
    tweets.append(tweet)
    
    
    tweet =  { 
                "text": (f"As outras duas unidades de conservação com mais fogo no últimos dia foram estas:\n\n"
                    f"- {f}: {h}% do total, com {g} focos\n"
                    f"- {i}: {k}% do total, com {j} focos\n"),

                "img": None
              
            }
    tweets.append(tweet)
    
    
    tweet = { "text": f"Atenção para a metodologia! A análise usa dados do satélite SUOMI-NPP, da NASA, que não é o mesmo que o INPE usa como referência. Cada um dos {total_fogo} focos mostrados representa uma área de 375 m² em que o satélite encontrou brilho e calor compatíveis com atividade de fogo.",
         "img": None
    }
    tweets.append(tweet)
    

    tweet = { "text": f"Você pode ver mais detalhes sobre a situação da Amazônia Legal na página especial Amazônia Sufocada, no site do InfoAmazonia, e navegar pelo mapa interativo com todos os {total_geral} focos de calor registrados na região em 2020. \n\nhttps://infoamazonia.org/",
         "img": None
    }
    tweets.append(tweet)


    # Não podemos aceitar nenhum tuíte com mais de 280 toques
    tweets_over_280_chars = [len(tweet["text"]) >= 280 for tweet in tweets]
    #print(tweets_over_280_chars)
    assert not any(tweets_over_280_chars), "tuítes acima do limite de caracteres detectados"
    
    return tweets

################
### Execução ###
################

def main():

	# Lê os dados das variáveis de 24h
	data_24h = read_variables("24h")

	# Verifica se o diretório de tweets de fato existe
	directory = "../output/jsons/tweets/"
	if not os.path.exists(directory):
		os.makedirs(directory)

	# Terras indígenas, 24h
	with open("../output/jsons/tweets/tis_24h.json", "w+") as f:
		content = build_thread_most_fire_indigenous_land(data_24h)
		json.dump(content, f, indent=2)

	# Unidades de conservação, 24h
	with open("../output/jsons/tweets/ucs_24h.json", "w+") as f:
		content = build_thread_most_fire_conservation_units(data_24h)
		json.dump(content, f, indent=2)

if __name__ == "__main__":
	main()