import gradio as gr
import string 
from collections import Counter

def analizar_texto(texto):
    texto_Limpo = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_Limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto_Limpo)
    
    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])
    return num_palavras, num_caracteres, frequencia_html

iface=gr.Interface(
    fn=analizar_texto,
    inputs=gr.Textbox(label="texto", placeholder='Digite seu texto', lines=10),
    
    outputs=[
        gr.Number(label="Número de Palavras"),
        gr.Number(label="Número de Caracteres"),
        gr.HTML(label="Frequência de Palavras")
    ],
    title="Analisador de Texto",
    description="Analise o texto inserido para obter o número de palavras, número de caracteres e a frequência de cada palavra.",
)

iface.launch()