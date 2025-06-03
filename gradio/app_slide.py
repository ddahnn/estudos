import  gradio as gr
import numpy as np
from PIL import Image
import io
import base64


def criar_slide(titulo, texto, imagem, corde_fundo,  cor_do_texto):
    estilo = (
        f"background color:{corde_fundo};"
        f"color: {cor_do_texto};"
        "padding: 20px;"
        "text-align: center;"
    )

    #converte a imagem para base64 se estiver presente
    imagem_html =""
    if imagem is not None:
        buffered = io.BytesIO()
        Image.fromarray(imagem).save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        imagem_html = (
            f"<img src='data:image/png;base64,{img_str}' "
            f"<style='max-width: 100%; height: auto;'/>"
        )

        slide_html = f"""
        <div style="{estilo}">
            <h1>{titulo}</h1>
            <p>{texto}</p>
            {imagem_html}"""
    return slide_html #type: ignore

iface = gr.Interface (
fn=criar_slide,
    inputs=[
        gr.Textbox(label="Digite o Título"),
        gr.Textbox(label="digite o Texto"),
        gr.Image(type="numpy", label="Imagem"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.ColorPicker(label="Cor do Texto"),
    ],
    outputs=gr.HTML(label="Slide HTML"),
    title="Gerador de Slide",
    description="Crie um slide HTML com título, texto, imagem e cores personalizadas.",

)
iface.launch()