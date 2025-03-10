# 3D File Prefixer

Este script Python renomeia arquivos .stl e .obj em um diretório, adicionando um número e um x antes do nome do arquivo. É útil para organizar arquivos de impressão 3D, como .stl e .obj, de forma rápida e eficiente.

---

## Funcionalidades
- Lista arquivos .stl e .obj no diretório onde o script ou executável está localizado.
- Adiciona um número e um x antes do nome do arquivo (ex: 1x arquivo.stl).
- Ignora arquivos que já possuem um número e x no nome.
- Inclui um menu interativo para inserir o número e confirmar a ação.
- Mantém a simplicidade e é fácil de usar.

---

## Arquivos no Repositório
- 3DFilePrefixer.py: O script Python.
- 3DFilePrefixer.exe: O arquivo executável (para usuários que não têm o Python instalado).

---

## Como Usar

### Rodando o Script Python (3DFilePrefixer.py)
Pré-requisitos:
- Certifique-se de ter o Python instalado. Você pode baixá-lo em python.org.

Passos:
1. Clone este repositório ou baixe o arquivo 3DFilePrefixer.py.
2. Coloque o script na pasta onde estão os arquivos .stl e .obj que deseja renomear.
3. Execute o script:
   - No terminal, navegue até a pasta do script e execute:
     python 3DFilePrefixer.py
4. Siga as instruções na tela:
   - Digite o número que deseja adicionar antes dos nomes dos arquivos.
   - Confirme a ação.

Saída:
- Os arquivos .stl e .obj serão renomeados com o prefixo especificado (ex: 1x arquivo.stl).
- O terminal exibirá uma mensagem de sucesso e aguardará você pressionar uma tecla antes de fechar.

---

### Rodando o Arquivo Executável (3DFilePrefixer.exe)
Pré-requisitos:
- Não é necessário instalar o Python. O arquivo .exe é um executável independente.

Passos:
1. Baixe o arquivo 3DFilePrefixer.exe deste repositório.
2. Coloque o executável na pasta onde estão os arquivos .stl e .obj que deseja renomear.
3. Dê um duplo clique no arquivo .exe para executá-lo.
4. Siga as instruções na tela:
   - Digite o número que deseja adicionar antes dos nomes dos arquivos.
   - Confirme a ação.

Saída:
- Os arquivos .stl e .obj serão renomeados com o prefixo especificado (ex: 1x arquivo.stl).
- O terminal exibirá uma mensagem de sucesso e aguardará você pressionar uma tecla antes de fechar.

---

## Exemplo de Uso

### Antes:
/pasta_do_programa
    3DFilePrefixer.exe
    arquivo1.stl
    arquivo2.obj
    arquivo3.txt

### Após Executar o Programa:
- O usuário insere o número 2.

### Resultado:
/pasta_do_programa
    3DFilePrefixer.exe
    2x arquivo1.stl
    2x arquivo2.obj
    arquivo3.txt

---

## Construindo o Executável (Opcional)
Se você quiser construir o arquivo .exe por conta própria ou depois de alguma mudança no .py:

1. Instale o PyInstaller:
   pip install pyinstaller

2. Navegue até o diretório do script:
   cd caminho\para\diretório

3. Construa o executável:
   pyinstaller --onefile 3DFilePrefixer.py

4. O arquivo .exe será gerado na pasta dist.

---

## Licença
Este projeto está licenciado sob a Licença MIT.

---

## Contribuindo
Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

## Suporte
Se você encontrar algum problema ou tiver dúvidas, abra uma issue no GitHub.
