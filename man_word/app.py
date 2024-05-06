from docx import Document

nome_arquivo = './teste.docx'  # Nome do arquivo Word
texto_antigo = 'teste'  # Texto que deve ser substituído
texto_novo = 'Raphael Fernanades Franca com '  # Novo texto para substituir

documento = Document(nome_arquivo) #abrindo o arquivo


#percorrendo o documento inteiro até achar a palavra para ser substituida
for paragrafo in documento.paragraphs:
    for linha in paragrafo.runs:
        if texto_antigo in linha.text:
            # Substituir o texto na linha
            linha.text = linha.text.replace(texto_antigo, texto_novo)
            # Marcar como encontrado (opcional)
            linha.font.bold = True
            documento.save('nome_arquivo.docx')
