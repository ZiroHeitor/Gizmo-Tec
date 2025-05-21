import json
import os

usuarios = {
    "Gabriel": "123456",
    "Laura": "amominhamãe",
    "Matheus": "h53fn!8L",
    "Sofia": "senha",
    "Bruno": "bruno123"
}

cadastros = set()
relatorios = []

escala_status = ["Presente", "Ausente", "Home Office", "Outro"]

def salvar_dados():
    dados = {
        "cadastros": list(cadastros),
        "relatorios": relatorios
    }
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
    if os.path.exists("dados.json"):
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            global cadastros, relatorios
            cadastros = set(dados.get("cadastros", []))
            relatorios = dados.get("relatorios", [])

def login():
    print("===== Login =====")
    while True:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"Bem-vindo(a), {usuario}!")
            cadastros.add(usuario)
            salvar_dados()
            return usuario
        else:
            print("Usuário ou senha inválidos. Tente novamente.\n")

def menu_principal(usuario):
    while True:
        print("\n===== Menu Principal =====")
        print("1. Editar Escala")
        print("2. Consulta/Lista de Cadastros")
        print("3. Envio de Relatório")
        print("4. Consultar Relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            editar_escala(usuario)
        elif opcao == "2":
            listar_cadastros()
        elif opcao == "3":
            enviar_relatorio(usuario)
        elif opcao == "4":
            consultar_relatorios()
        elif opcao == "5":
            print("Encerrando programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def editar_escala(usuario):
    print("\n===== Editar Escala =====")
    for i, status in enumerate(escala_status, start=1):
        print(f"{i}. {status}")
    escolha = input("Escolha o status: ")
    if escolha.isdigit() and 1 <= int(escolha) <= len(escala_status):
        print(f"Status de escala definido como: {escala_status[int(escolha) - 1]}")
    else:
        print("Opção inválida.")

def listar_cadastros():
    print("\n===== Lista de Cadastros =====")
    if cadastros:
        for nome in cadastros:
            print(f"- {nome}")
    else:
        print("Nenhum cadastro encontrado no sistema.")

def enviar_relatorio(usuario):
    print("\n===== Envio de Relatório =====")
    texto = input("Digite seu relatório: ")
    relatorios.append((usuario, texto))
    salvar_dados()
    print("Esse texto foi enviado para os superiores.")

def consultar_relatorios():
    print("\n===== Relatórios Enviados =====")
    if relatorios:
        for i, (autor, texto) in enumerate(relatorios, start=1):
            print(f"{i}. {autor} escreveu: {texto}")
    else:
        print("Nenhum relatório enviado ainda.")

carregar_dados()
usuario_logado = login()
menu_principal(usuario_logado)
salvar_dados()