import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def emitir_certificado_via_email(remetente,senha,destinatario, path_certificado, assunto, mensagem):
    # Configurações do servido de email     
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Criação da mensagem
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    # Corpo do texto
    msg.attach(MIMEText(mensagem,"plain"))

    # Anexando o arquivo PDF
    try:
        with open(path_certificado, "rb") as anexo:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(anexo.read())

        # Codifica o arquivo em base64
        encoders.encode_base64(part)

        # Define o cabeçalho do anexo
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {path_certificado.split('\\')[-1]}",  # Extrai o nome do arquivo do caminho
        )

        # Adiciona o anexo à mensagem
        msg.attach(part)

    except Exception as e:
        print(f"Erro ao anexar o arquivo: {e}")
        return

    # Inicializa a variável server como None
    server = None
    
    try:
        # Conecta ao server SMTP
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(remetente,senha)

        # Envia o email
        server.sendmail(remetente,destinatario,msg.as_string())
        print(f"o email {destinatario} foi enviado com sucesso !")
    except Exception as e :
        print(f"erro a enviar o email: {e}" )
    finally:
        if server:  # Verifica se a variável server foi definida
            server.quit()


