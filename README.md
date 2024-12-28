# HexCode - Gerador de Códigos Hexadecimais

Este é um script em Python que gera códigos hexadecimais aleatórios de 4 dígitos. Além disso, permite pesquisar códigos gerados anteriormente, associando-os a nomes e descrições.

## Requisitos

- Python 3.x
- PyInstaller (para criar o executável)
- Windows (ou outro sistema operacional com suporte para Python)

## Como Usar

### 1. Criar o Executável

Para gerar o executável do script, siga os passos abaixo:

1. Abra o **Prompt de Comando** ou **PowerShell**.
2. Navegue até o diretório onde o arquivo `hexcode.py` está localizado.
3. Execute o seguinte comando para criar o executável:

   ```bash
   pyinstaller --onefile --name=hexcode .\hexcode.py
   ```

   Isso criará um executável chamado `hexcode.exe` na pasta `dist`.

### 2. Adicionar o Executável ao PATH

Para tornar o executável acessível de qualquer lugar no sistema, adicione-o ao `PATH`:

1. Crie a pasta `C:\hexcode` (ou qualquer diretório de sua escolha).
2. Copie o arquivo `hexcode.exe` para essa pasta.
3. Abra o **Prompt de Comando** como Administrador e execute o seguinte comando para adicionar o caminho ao `PATH` do sistema:

   ```bash
   setx PATH "%PATH%;C:\hexcode"
   ```

   Agora, você pode executar o `hexcode` de qualquer lugar no sistema.

### 3. Usando o Programa

Após configurar o executável no `PATH`, basta abrir o **Prompt de Comando** ou **PowerShell** e digitar `hexcode` para rodar o programa.

Você verá as seguintes opções:

1. **Gerar novo código**: Cria um novo código hexadecimal aleatório e o salva.
2. **Pesquisar código**: Permite buscar um código já gerado, exibindo seu nome (se houver) e descrição.

### 4. Personalizando

Você pode personalizar o código gerado e os dados associados (nome e descrição) editando o script `hexcode.py`.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
