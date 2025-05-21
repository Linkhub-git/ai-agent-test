import gradio as gr
import time

def llamar_api_agente(mensaje_usuario):
    # Igual que antes
    pasos = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
    ]
    for paso in pasos:
        yield {"razonamiento": paso, "respuesta": None}
        time.sleep(1)
    yield {"razonamiento": "Finalizado", "respuesta": f"Respuesta a '{mensaje_usuario}'"}

def conversacion_en_stream(mensaje_usuario, historial, razonamiento_acumulado):
    historial.append((mensaje_usuario, "Pensando..."))
    yield historial, razonamiento_acumulado, razonamiento_acumulado

    for chunk in llamar_api_agente(mensaje_usuario):
        razonamiento_acumulado += f"<p>{chunk['razonamiento']}</p>"
        # Componemos el HTML final para mostrar
        html_razonamiento = f"""
        <div id='log-div' style='height: 300px; overflow-y: auto; border: 1px solid #ccc; padding: 5px;'>
            {razonamiento_acumulado}
        </div>
        """
        if chunk["respuesta"] is None:
            yield historial, html_razonamiento, razonamiento_acumulado
        else:
            historial[-1] = (mensaje_usuario, chunk["respuesta"])
            yield historial, html_razonamiento, razonamiento_acumulado

with gr.Blocks() as demo:
    state_historial = gr.State([])
    razonamiento_state = gr.State("")

    with gr.Row():
        with gr.Column():
            gr.Markdown("## Conversación")
            chatbot = gr.Chatbot(label="Agente")
            user_input = gr.Textbox(label="Tu mensaje")
            send_btn = gr.Button("Enviar")

        with gr.Column():
            gr.Markdown("## Razonamiento")
            panel_razonamiento = gr.HTML(label="Log de razonamiento")

    send_btn.click(
        fn=conversacion_en_stream,
        inputs=[user_input, state_historial, razonamiento_state],
        outputs=[chatbot, panel_razonamiento, razonamiento_state]
    )

demo.launch()