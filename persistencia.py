import json
import time
def salvar_dados(dados):
    with open('Livros.json', 'w', encoding='utf-8') as arquive:
        try:
            json.dump(dados, arquive, indent=4, ensure_ascii=False)
            print('[SISTEMA] ARQUIVOS SALVOS!!!')
            time.sleep(1)
        except Exception as e:
            print(f'[SISTEMA] ERRO AO SALVAR ARQUIVO...{e}')
            time.sleep(1)