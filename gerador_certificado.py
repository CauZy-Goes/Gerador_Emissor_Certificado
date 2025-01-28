from fpdf import FPDF
import pandas as pd
import os

# Garantir que a pasta de certificados existe
if not os.path.exists("certificados"):
    os.makedirs("certificados")

# Dados do certificado
dados = pd.read_csv("dados.csv")

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