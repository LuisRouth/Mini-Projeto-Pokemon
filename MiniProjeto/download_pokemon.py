import os
import requests
from bs4 import BeautifulSoup

url_base = 'https://pokemondb.net'
pagina_pokemon_atual = '/pokedex/bulbasaur'
os.makedirs('pokemon_images', exist_ok=True)

while pagina_pokemon_atual:
    
    url_completa = url_base + pagina_pokemon_atual
    print(f"Acessando: {url_completa}")
    resposta = requests.get(url_completa)
    sopa = BeautifulSoup(resposta.text, 'lxml')
    nome_pokemon = sopa.find('h1').text
    link_da_imagem = sopa.find('main').find('img')['src']

    print(f"Baixando imagem do {nome_pokemon}...")
    
    dados_da_imagem = requests.get(link_da_imagem).content
    nome_arquivo = f"{nome_pokemon.lower()}.jpg"
    caminho_salvar = os.path.join('pokemon_images', nome_arquivo)
    arquivo_imagem = open(caminho_salvar, 'wb')
    arquivo_imagem.write(dados_da_imagem)
    arquivo_imagem.close()
    botao_proximo = sopa.find('a', {'rel': 'next'})
    
    if botao_proximo:
        pagina_pokemon_atual = botao_proximo['href']
    else:
        pagina_pokemon_atual = None
    
print("Capturamos todos! Fim.")