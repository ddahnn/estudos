import gradio as gr
import math


def fatorial(num):
    if  num <0:
        return "Fatorrial ,não definido para numero negativos"
    return math.factorial(num)

iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="text",
    title="Cauculadora de Fatorial",
    description="Insira um número para obter o fatorial"
)

iface.launch