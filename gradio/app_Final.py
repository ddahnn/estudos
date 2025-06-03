import gradio as gr
import string
from collections import Counter  # Faltava importar isso


def copnverter_Temperatura(temperatura, escala):
    if escala == 'Celsius':
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9


def analizar_texto(texto):
    texto_Limpo = texto.translate(str.maketrans('', '', string.punctuation))
    palavras = texto_Limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto_Limpo)

    frequencia = Counter(palavras)
    frequencia_html = "<br>".join([f"{palavra}: {contagem}" for palavra, contagem in frequencia.items()])
    return num_palavras, num_caracteres, frequencia_html


def criarRelatorio(temperatura, escala, condicao, texto, relatorio_texto):  # agora com 5 argumentos
    temperatura_convertida = copnverter_Temperatura(temperatura, escala)
    numero_palavras, numero_caracteres, frequencia_html = analizar_texto(texto)

    relatorio = (f"**Relatorio de Clima**\n\n"
                 f"Temperatura: {temperatura_convertida:.2f} "
                 f"{'F' if escala == 'Celsius' else 'C'}\n"
                 f"Condicao: {condicao}\n\n"
                 f"Numero de palavras: {numero_palavras}\n"
                 f"Numero de caracteres: {numero_caracteres}\n"
                 f"Frequencia de palavras:\n{frequencia_html}\n")
    return relatorio


iface = gr.Interface(
    fn=criarRelatorio,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(choices=["Celsius", "Fahrenheit"], label="Escala"),
        gr.Dropdown(
            choices=["Ensolarado", "Chuvoso", "Nublado", "Nevando"],
            label="Condição do clima"),
        gr.Textbox(label="Texto"),
        gr.Textbox(label="Relatorio", lines=4, placeholder="Descreva o Dia")
    ],
    outputs=gr.Markdown(label="Relatório de Clima"),
    title="Relatório de clima",
    description="Crie um relatório de clima com base na temperatura, condição e texto descritivo.",
)

iface.launch()
