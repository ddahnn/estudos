import gradio as gr

def soma(numero , numero2):
    return f"{numero+numero2}"

print(soma(9,98))

iface = gr.Interface(
    fn=soma,
    inputs=["number","number"],
    outputs="number",
    title="Cauculadora de soma",
    description='Insira dois numeros para obter a soma.',
    theme="default"
)

iface.launch()
