import persistencia
from scraper import scraper_de_livros
import time

print('[SISTEMA] INICIANDO ROBO...')
time.sleep(1)

#Interface via terminal
while True:
    try:
        qtd = int(input('[SISTEMA] Quantas paginas do site [Toscrape.com] voce gostaria de baixar ? 1/50 : '))
        if qtd > 0 and qtd <= 50:
            break
        else:
            print('[SISTEMA] DIGITE UM NUMERO ENTRE 1 E 50')
    except Exception as e:
        print('[SISTEMA] POR FAVOR DIGITE APENAS NUMEROS')

print('[SISTEMA] INICIANDO BUSCA...')

livros = scraper_de_livros(qtd)

print(f'[SISTEMA] {qtd} PAGINAS COLETADAS COM SUCESSO')
time.sleep(1)
print('[SISTEMA] SALVANDO ARQUIVOS LOCALMENTE...')
time.sleep(1)

persistencia.salvar_dados(livros)

print('=' * 50)
print('COLETA FINALIZADA COM SUCESSO')
print(f'PÁGINAS COLETADAS: {qtd}')
print(f'LIVROS COLETADOS: {len(livros)}')
print('ARQUIVO GERADO: Livros.json')
print('=' * 50)

