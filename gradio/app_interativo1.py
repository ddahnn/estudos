import gradio as gr


def copnverter_Temperatura(temperatura, escala):
    if escala == 'Celsius':
        return  (temperatura* 9/5 ) +32
    else:
        return (temperatura - 32) * 5/9

iface=gr.Interface(
    fn=copnverter_Temperatura,
    inputs=[
        gr.Number(label ="Temperatura", precision=2),
        gr.Radio(
            choices=["Celsius", "Fahrenheit"],
            label="Escala"
        ),
    ],
    outputs=gr.Number(label="Resultado"),
    title="Conversor de Temperatura",
    description="Converta temperaturas entre Celsius e Fahrenheit.",
    
)

iface.launch()