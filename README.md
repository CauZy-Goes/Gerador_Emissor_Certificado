# 🏆 Gerador e Emissor de Certificados

## 📝 Descrição
Este projeto automatiza a geração e o envio de certificados para participantes de palestras, utilizando um arquivo CSV contendo nomes e emails. O software gera certificados personalizados em formato PDF e os envia automaticamente por email.

## 🚀 Tecnologias Utilizadas
- Python 3.x
- FPDF (para geração de PDFs)
- Pandas (para manipulação de dados CSV)
- smtplib e email.mime (para envio de emails)

## 📂 Estrutura do Projeto
```
|
|-- services/
|   |-- gerador_certificado.py  # Gera certificados em PDF
|   |-- emissor_certificado.py  # Envia certificados por email
|
|-- app.py  # Executa o fluxo completo
|-- dados.csv  # Planilha contendo os nomes e emails dos participantes
|-- Template.png  # Template do certificado
|-- certificados/  # Pasta onde serão salvos os certificados gerados
|-- README.md  # Documentação do projeto
|-- Requirementes.txt # Dependencias instaladas no venv
```

## ⚙️ Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/gerador-certificados.git
   cd gerador-certificados
   ```

2. **Crie o Ambiente Virtual Python:**
   ```bash
   python -m venv nome_do_ambiente
   ```

3. **Ative o Ambiente Virtual Python:**
   ```bash
   nome_do_ambiente/Scripts/Activate
   ```
   
4. **Instale as dependências necessárias:**
   ```bash
   pip install -r requirements.txt multiplos
   ```

5. **Configure o arquivo `app.py`**
   - Substitua `seu endereço de email` pelo seu email.
   - Gere uma senha de app para seu email (caso use Gmail) e substitua `sua senha de app do seu gmail`.
   - Atualize o caminho correto para `dados.csv` se necessário.
   
6. **Prepare a planilha de dados (`dados.csv`)**
   - Certifique-se de que ela contém as colunas `nomecompleto` e `email`.

7. **Configure com service gerador_certificado com base em seu template de certificado (gerador_certificado.py)**
   - Passe a localição em pixels que o nome dos participantes devem ser inseridos, você pode saber dessa informação utilizando o biblioteca cv2 do python

## ▶️ Como Usar

### 1. Gerar um certificado pelo nome
```python
import services.gerador_certificado as gc
gc.gerarCertificadoPeloNome("Nome do Participante")
```
O certificado será salvo na pasta `certificados/`.

### 2. Gerar e enviar certificado por email para um participante
```python
import app

gerar_emitir_certificado_email_nome(
      email_remetente,
      senha,
      assunto,
      mensagem,
      nome_destinatario,
      email_destinatario
      )
```

### 3. Gerar e enviar certificados para todos os participantes do CSV
```python
import app

app.gerar_emitir_certificado_emails_csv(
    "dados.csv", "seu_email@gmail.com", "sua_senha", "Assunto", "Mensagem"
)
```

## ⚠️ Observações Importantes
- O template do certificado deve estar na raiz do projeto com o nome `Template.png`.
- O envio de emails está configurado para Gmail. Caso use outro provedor, ajuste `smtp_server` e `smtp_port` em `emissor_certificado.py`.
- Para evitar problemas de login no envio de emails, configure a autenticação de dois fatores e gere uma senha de app no Gmail.

Feito por Cauã Farias 🚀

