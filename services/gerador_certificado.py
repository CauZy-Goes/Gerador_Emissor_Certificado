from fpdf import FPDF
import pandas as pd
import os

# Garantir que a pasta de certificados existe
def verificarPastaCertificados():
    if not os.path.exists("certificados"):
        os.makedirs("certificados")

# Gerar certificado recenbendo o nome
def gerarCertificadoPeloNome(nome):
    # Verifica se a pasta de certificados existe, se não cria ela
    verificarPastaCertificados()

    # Configurando PDF
    pdf = FPDF(orientation='L', unit='pt', format=(1240,1754))
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=62)
    pdf.image("Template.png", x=0, y=0)
    pdf.set_text_color(0,0,0)

    # Adicionar o nome
    pdf.text(180, 540, nome)

    # Salvar o PDF com um nome de arquivo único
    pdf.output(f"certificados\\Certificado_{nome}.pdf")

# Gerar todos os certificados no arquivo.csv
def gerarTodosOsCertificados(pathDoArquivoCsv): 
    # Verifica se a pasta de certificados existe, se não cria ela
    verificarPastaCertificados()

    # Acessando o certificado
    dados = pd.read_csv(pathDoArquivoCsv)

    # Gerar todos os certificados
    for nome in dados['nomecompleto']:
        # Configurando PDF
        pdf = FPDF(orientation='L', unit='pt', format=(1240,1754))
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=62)
        pdf.image("Template.png", x=0, y=0)
        pdf.set_text_color(0,0,0)

        # Adicionar o nome
        pdf.text(180, 540, nome)

        # Salvar o PDF com um nome de arquivo único
        pdf.output(f"certificados\\Certificado_{nome}.pdf")