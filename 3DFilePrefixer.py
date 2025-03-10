import os
import re
import sys

def listar_arquivos(diretorio):
    # Lista apenas arquivos .stl e .obj no diretório atual (sem subpastas)
    arquivos = [f for f in os.listdir(diretorio) if f.lower().endswith(('.stl', '.obj')) and os.path.isfile(os.path.join(diretorio, f))]
    return arquivos

def renomear_arquivos(diretorio, numero):
    arquivos = listar_arquivos(diretorio)
    padrao = re.compile(r'^\d+x\s')  # Regex para verificar se o arquivo já tem um número e 'x'

    if not arquivos:
        print("Nenhum arquivo STL ou OBJ encontrado na pasta.")
        return

    for arquivo in arquivos:
        # Pula se o arquivo já tiver um número e 'x' no nome
        if padrao.match(arquivo):
            print(f"Pulado: {arquivo} (já tem um número e prefixo 'x')")
            continue
        
        # Renomeia o arquivo
        novo_nome = f"{numero}x {arquivo}"
        caminho_antigo = os.path.join(diretorio, arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {arquivo} -> {novo_nome}")
    
    print("\nTodos os arquivos STL e OBJ foram processados com sucesso!")

def main():
    # Obtém o caminho da pasta onde o .exe está localizado
    if getattr(sys, 'frozen', False):
        # Se estiver rodando como .exe (empacotado com PyInstaller)
        diretorio = os.path.dirname(sys.executable)
    else:
        # Se estiver rodando como script Python
        diretorio = os.path.dirname(os.path.abspath(__file__))
    
    # Pede ao usuário o número a ser adicionado
    while True:
        try:
            numero = int(input("Digite o número a ser adicionado (ex: 1, 2, 3): ").strip())
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    # Confirma a ação com o usuário
    confirmacao = input(f"\nTem certeza que deseja renomear todos os arquivos STL e OBJ em '{diretorio}' com o prefixo '{numero}x '? (sim/não): ").strip().lower()
    
    if confirmacao == 'sim':
        renomear_arquivos(diretorio, numero)
    else:
        print("Operação cancelada.")
    
    # Aguarda o usuário pressionar qualquer tecla para sair
    input("\nPressione qualquer tecla para sair...")

if __name__ == "__main__":
    main()