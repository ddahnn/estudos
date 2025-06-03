import gradio as gr
def customizar_texto(texto, cor, tamanho, corGundo, estilo  ):
    estilo =(
        f"color: {cor};"
        f"font-size: {tamanho}px;"
        f"background-color: {corGundo};"
        f"font-family: {estilo}"
    )
    return f"<p style='{estilo}'>{texto}</p>"


iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="Texto"),
        gr.ColorPicker(label="Cor do Texto"),
        gr.Slider(minimum=10, maximum=100, label="Tamanho do Texto"),
        gr.ColorPicker(label="Cor de Fundo"),
        gr.Dropdown(
            choices=["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana"],
            label="Estilo da Fonte",
        ),
    ],
    outputs=gr.HTML(label="Texto Personalizado"),
    title="Personalizador de Texto",
    description="Customize seu texto com cor, tamanho, cor de fundo e estilo da fonte.",
)

iface.launch()