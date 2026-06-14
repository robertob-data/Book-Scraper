import requests
from bs4 import BeautifulSoup
import time
import random

livros_prontos = []

estrelas_dict = {'One' : 1, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5}


def requisiçao(url):

    meus_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    
#tenta capturar o html
    try:
        resposta = requests.get(url,headers=meus_headers, timeout=10)
        time.sleep(random.randint(2,5))

        if resposta.status_code == 200:
            return resposta.text
        else:
            return None
        
    except Exception as e:

        print(f'[SISTEMA] - ERRO falha na requisiçao do site erro{e}')
        return None

def sopa(html):

## Organiza, limpa e estrutura os dados em uma lista
    html_limpo = BeautifulSoup(html, 'html.parser')
    estante = html_limpo.find_all('article', class_='product_pod')
    for i, livro in enumerate(estante):

        #Nome do livro
        tag_h3 = livro.find('h3')
        nome = tag_h3.find('a')
        titulo = nome['title']
        
        #preço do livro
        preco_sujo = livro.find('p', class_='price_color')
        preco_limpo = preco_sujo.get_text(strip=True)
        preco = float(preco_limpo.replace('Â£', '').replace('£', ''))
        
        #Avaliaçao
        # Converte a classe CSS de avaliação para um valor numérico
        tag_estrelas = livro.find('p', 'star-rating')
        estrela = tag_estrelas['class']
        if estrela[1] in estrelas_dict:
            avaliaçao = estrelas_dict[estrela[1]]

        modelo = {
            'Titulo' : titulo,
            'Preço' : preco,
            'Moeda' : '£',
            'Avaliacao': '⭐' * avaliaçao
        }
        
        print(f'[SISTEMA] livro {titulo} DE ÍNDICE {i+1} Coletado com Sucesso')
        time.sleep(0.03)

        livros_prontos.append(modelo)

    return livros_prontos

def scraper_de_livros(total_paginas):    
    livros_prontos.clear()

    #loop principal para atualizar a URL a cada volta
    for i in range(total_paginas):
        url_dinamica = f'https://books.toscrape.com/catalogue/page-{i+1}.html'
        html_sujo = requisiçao(url_dinamica)

        if html_sujo is not None:
            sopa(html_sujo)
            time.sleep(0.5)
            print(f'[SISTEMA] PAGINA {i+1} COLETADA')
        else:
            print(f'[SISTEMA] - AVISO: Pág {i+1} ignorada por falha na rede.')
        time.sleep(0.7)
        
    return livros_prontos

