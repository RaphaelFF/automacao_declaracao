from docx import Document

nome_arquivo = './teste.docx'  # Nome do arquivo Word
texto_antigo = '{nome}'  # Texto que deve ser substituído
texto_novo = 'Raphael Fernanades Franca com o cpf ta ta'  # Novo texto para substituir

documento = Document(nome_arquivo) #abrindo o arquivo
paragrafo = documento.paragraphs[0]  # Assumindo que o texto está no primeiro parágrafo

# Substitui o texto antigo pelo novo em todo o parágrafo

paragrafo.text = paragrafo.text.replace(texto_antigo, texto_novo)

# Salva o documento modificado
documento.save('nome_arquivo.docx')
