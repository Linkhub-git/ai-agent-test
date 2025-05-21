import gradio as gr
import time
from agent_logic import ask_ai_agent
from utils import save_images_array_from_file, save_documents_array_from_file

def upload_file(files):
    print("upload_file START")
    images = []
    documents = []
    for file in files:
        print(f"Archivo subido: {file}")
        if ".jpg" in file or ".jpeg" in file or ".png" in file:
            images.append(file.replace("\\", "/"))
        elif ".pdf" in file or ".doc" in file or ".docx" in file or ".txt" in file or ".md" in file:
            documents.append(file.replace("\\", "/"))
            
    if len(images) > 0:
        save_images_array_from_file(images)
    if len(documents) > 0:
        save_documents_array_from_file(documents)
    print("upload_file END")
 
def conversacion_en_stream(mensaje_usuario, historial, razonamiento_acumulado):
    historial.append((mensaje_usuario, "Pensando..."))
    yield historial, razonamiento_acumulado, razonamiento_acumulado
 
    for chunk in ask_ai_agent(mensaje_usuario, "test"):
        razonamiento_acumulado += f"<p>{chunk['razonamiento']}</p>"
        # Incrustamos también un script para forzar el scroll al fondo
        scroll_script = """
        <script>
        var div = document.getElementById('log-div');
        if (div) {
            div.scrollTop = div.scrollHeight;
        }
        </script>
        """
        # Componemos el HTML final para mostrar
        html_razonamiento = f"""
        <div id='log-div' style='height: 800px; overflow-y: auto; border: 1px solid #ccc; padding: 5px;'>
            {razonamiento_acumulado}
        </div>
        {scroll_script}
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
            user_input = gr.Textbox(label="Tu mensaje",autoscroll=True)
            send_btn = gr.Button("Enviar")
            file_output = gr.File(height=100, label="Archivos adjuntos")
            upload_button = gr.UploadButton("Adjuntar archivos", file_types=["image", "text"], file_count="multiple")
 
        with gr.Column():
            gr.Markdown("## Razonamiento")
            panel_razonamiento = gr.HTML(label="Log de razonamiento")
 
    send_btn.click(
        fn=conversacion_en_stream,
        inputs=[user_input, state_historial, razonamiento_state],
        outputs=[chatbot, panel_razonamiento, razonamiento_state],
        queue=True
    )
    
    upload_button.upload(upload_file, upload_button, file_output)
 
demo.launch(share=True)
