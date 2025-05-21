import json

def carregar_ativos():
    try:
        with open('ativos.json', 'r', encoding='utf-8') as arquivo:
            ativos = json.load(arquivo)
        return ativos
    except FileNotFoundError:
        print("Arquivo de ativos não encontrado.")
        return {}
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")
        return {}

def buscar_ativo(ativos):
    id_ativo = input("\nDigite o ID do ativo (Ex.: HE001, HU032, SW001, FT005): ").strip().upper()

    if id_ativo in ativos:
        dados = ativos[id_ativo]

        print("\nInformações do Ativo:")
        print(f"ID: {id_ativo}")
        print(f"Descrição: {dados.get('descrição', 'Não informado')}")
        print(f"Categoria: {dados.get('categoria', 'Não informado')}")

        if 'valor de compra' in dados:
            print(f"Valor de Compra: R$ {dados['valor de compra']:.2f}")
        if 'valor de venda' in dados:
            print(f"Valor de Venda: R$ {dados['valor de venda']:.2f}")
        if 'quantidade' in dados:
            print(f"Quantidade: {dados['quantidade']}")
        if 'nota_fiscal' in dados:
            print(f"Número da Nota Fiscal: {dados['nota_fiscal']}")
        if 'localização' in dados:
            print(f"Localização: {dados['localização']}")
        if 'responsável' in dados:
            print(f"Responsável: {dados['responsável']}")
        print(f"Status: {dados.get('status', 'Não informado')}")
    else:
        print("Ativo não encontrado.")

ativos = carregar_ativos()

while True:
    buscar_ativo(ativos)

    continuar = input("\nDeseja buscar outro ativo? (S/N): ").strip().lower()
    if continuar != 's':
        print("\nPrograma encerrado.")
        break
