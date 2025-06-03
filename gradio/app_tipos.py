import gradio as gr

def processar_dados(texto, numero, image, lista_texto, cor, opcoes):
    texto_reverso = texto[::-1]
    dobro_numero = numero*2
    mensagem_imagem = "Imagem recebida" if image else "Nenhuma imagem recebida"
    lista_processada = [[item] for item in lista_texto.splitlines()] if lista_texto else []

    return (
        texto_reverso,
        mensagem_imagem,
        dobro_numero,
        lista_processada,
        f"Cor selecionada {cor}",
        opcoes
    )

iface = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(placeholder="Digite um texto aqui", label='texto'),
        gr.Slider(minimum=0 , maximum=100, label="numero", value=0),
        gr.Image( type='pil', label="Imagem"),
        gr.Textbox(label="Lista de itens", lines=4, placeholder= 'item1\niten2'),
        gr.ColorPicker(label="Cor"),
        gr.CheckboxGroup(label="Opções", choices=["Opção 1", "Opção 2", "Opção 3"])
    ],
    outputs=[
        gr.Textbox(label="Texto Reverso"),
        gr.Textbox(label="Mensagem Imagem"),
        gr.Number(label="Dobro do Número"),
        gr.Dataframe(label="Lista Processada", headers=["Item"]),
        gr.Textbox(label="Cor Selecionada"),
        gr.CheckboxGroup(label="Opções Selecionadas")
    ],
    title="Processador de Dados",
    description="Insira os dados para processá-los"
)


iface.launch()