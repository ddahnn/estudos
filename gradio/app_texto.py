import gradio as gr


def reverter_Texto(texto):
    texto_reveso = texto[::-1]
    return texto_reveso, len(texto_reveso)

iface = gr.Interface(
    fn=reverter_Texto,
    inputs="text",
    outputs=["text", "number"],
    title='Reversor de Texto',
    description="Insira um texto para revertê-lo e contar os caracteres"
)

iface.launch()