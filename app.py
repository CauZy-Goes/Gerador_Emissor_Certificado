import services.gerador_certificado as gc
import services.emissor_certificado as ec
import pandas as pd

email_remetente = "seu endereço de email"
senha = "sua senha de app do seu gmail"
assunto = "titulo do email"
mensagem =  "Aqui o corpo da mensagem"
path_planilha = "dados.csv" #caminho da planilha que estam o dados dos clientes

def gerar_emitir_certificado_email_nome(email_remetente, senha, assunto, mensagem, nome_destinatario, email_destinatario):
    # Gera o certificado pelo nome
    gc.gerarCertificadoPeloNome(nome_destinatario)
    path_certificado = (f"certificados\\Certificado_{nome_destinatario}.pdf")

    # Envia certificado pelo email
    ec.emitir_certificado_via_email(
        email_remetente,
        senha,
        email_destinatario,
        path_certificado,
        assunto,
        mensagem
    )
        

# gerar_emitir_certificado_email_nome(email_remetente, senha, assunto, mensagem, nome_destinatario, email_destinatario)

def gerar_emitir_certificado_emails_csv(path_planilha, email_remetente, senha, assunto, mensagem):
    # Pegar os dados da planilha csv
    dados = pd.read_csv(path_planilha)

    # Itera sobre as linhas do DataFrame
    for index, row in dados.iterrows():
        # Gera o certificado pelo nome
        nome = row["nomecompleto"]
        gc.gerarCertificadoPeloNome(nome)

        # Pega o caminho do certificado gerado
        path_certificado = (f"certificados\\Certificado_{nome}.pdf")

        # Enviai o email para o email 
        email_destinatario = row["email"]
        ec.emitir_certificado_via_email(
            email_remetente,
            senha,
            email_destinatario,
            path_certificado,
            assunto,
            mensagem
        )

gerar_emitir_certificado_emails_csv(path_planilha, email_remetente, senha, assunto, mensagem)