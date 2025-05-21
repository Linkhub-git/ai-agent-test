import gradio as gr
import time

# Función fake que simula el streaming del agente de IA.
def fake_ask_agent(mensaje_usuario):
    pasos = [
        {
            "reasoning": "2025-04-22T09:02:11Z | Intake-Agent        | 📧  Nuevo mail “Solicitud CF $2.5MM - Deudor: ACME S.A.” capturado (msg-id:<20250421.90123>)",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:12Z | Intake-Agent        | 🧠  Razonando … entidades:{monto:2.5M, moneda:PEN, vig:2026-06-30, ejecutivo:“JM.Salcedo”}",
            "sleep": 5
        },
        {
            "reasoning": "2025-04-22T09:02:12Z | Intake-Agent        | 🗄️  Vector-search confirma cliente existente (ID #CLI-004576)",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:13Z | Orchestrator        | 🔀  Caso CF-89421 creado; evento `new_intake` publicado → topic **cf.events**",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:15Z | KYC-Risk-Agent      | 🔍  Descargando poderes notariales (Hiperfirmas API)…",
            "sleep": 5
        },
        {
            "reasoning": "2025-04-22T09:02:18Z | KYC-Risk-Agent      | 🖼️  OCR y verificación de firma → MATCH = 98.6 %",
            "sleep": 3
        },
        {
            "reasoning": "2025-04-22T09:02:18Z | KYC-Risk-Agent      | 🌐  Listas sanciones consultadas (OFAC, ONU, EU) → NO_MATCH",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:19Z | KYC-Risk-Agent      | 📈  Score de cumplimiento = 0.07 (< 0.15) → OK",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:19Z | KYC-Risk-Agent      | ✅  Compliance aprobado - publicando `compliance.passed`",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:20Z | Orchestrator        | 📇  Recibido `compliance.passed`; despachando a Data-Entry-RPA",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:21Z | Data-Entry-RPA      | 🤖  Lanzando robot UiPath “IBS-CF-Create”",
            "sleep": 5
        },
        {
            "reasoning": "2025-04-22T09:02:23Z | Data-Entry-RPA      | ⌨️  Login IBS - usuario:bot_cf, MFA token OK",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:28Z | Data-Entry-RPA      | 🗄️  Registro operación preliminar (IBS ticket #056781)",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:30Z | Data-Entry-RPA      | 🔄  Insertando datos en SP Desembolsos - opID:SP-CF-21894",
            "sleep": 5
        },
        {
            "reasoning": "2025-04-22T09:02:33Z | Data-Entry-RPA      | 💾  Guardado correcto - 3 s",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:34Z | Data-Entry-RPA      | 📤  Evento `dataentry.completed` emitido",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:34Z | Validator-Agent     | 📝  Checklist dinámico (14 ítems) generado",
            "sleep": 2
        },
        {
            "reasoning": "2025-04-22T09:02:35Z | Validator-Agent     | ✅  Ítem(1) Carta solicitud → OK",
            "sleep": 3
        },
        {
            "reasoning": "2025-04-22T09:02:35Z | Validator-Agent     | ✅  Ítem(2) Contrato marco → OK",
            "sleep": 3
        },
        {
            "reasoning": "2025-04-22T09:02:36Z | Validator-Agent     | ⚠️  Ítem(3) Garantía mobiliaria → PENDIENTE",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:36Z | Validator-Agent     | 📬  Solicitando documento faltante al ejecutivo “JM.Salcedo”",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:02:37Z | Orchestrator        | ⏳  Waiting-state “await_docs” iniciado (SLA = 30 min)",
            "sleep": 10
        },
        {
            "reasoning": "2025-04-22T09:05:04Z | Intake-Agent        | 📧  Mail adjunto recibido - “Garantía mobi.pdf” (signature verified)",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:05Z | Intake-Agent        | 🧠  Clasificado como doc faltante, encaminando a Validator-Agent",
            "sleep": 3
        },
        {
            "reasoning": "2025-04-22T09:05:08Z | Validator-Agent     | ✅  Ítem(3) ahora OK",
            "sleep": 3
        },
        {
            "reasoning": "2025-04-22T09:05:08Z | Validator-Agent     | ✅  Checklist 14/14 cumplido",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:09Z | Validator-Agent     | 📈  KPI “linea_bienvertida”=TRUE, publicando `validation.green`",
            "sleep": 5
        },
        {
            "reasoning": "2025-04-22T09:05:09Z | Orchestrator        | 🚦  Recibido `validation.green`; enviando a Pre-Approval-Agent",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:10Z | Pre-Approval-Agent  | 🧮  Calculando exposición residual deudor…",
            "sleep": 5
        },
        {
            "reasoning": "2025-04-22T09:05:11Z | Pre-Approval-Agent  | 💡  LLM analysis: margen colateral ≥ requerido",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:12Z | Pre-Approval-Agent  | 📊  Score = 91/100 → RECOMENDACIÓN Pre-aprobar",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:12Z | Pre-Approval-Agent  | 📤  Evento `preapproval.ok` emitido",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:13Z | Orchestrator        | 📤  Enviando a Approval-Hub (firmante: jefe_riesgos)",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:40Z | Approval-Hub        | 📲  Notificación móvil push enviada al Jefe-Riesgos (timeout = 15 min)",
            "sleep": 10
        },
        {
            "reasoning": "2025-04-22T09:05:42Z | Approval-Hub        | 👤  Firma digital capturada - fingerprint #A6F3",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:42Z | Approval-Hub        | ✅  Aprobación oficial - evento `approval.granted`",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:43Z | Orchestrator        | 🚀  Trigger a Generador-Valores",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:44Z | Generador-Valores   | 📝  Redactando Carta Fianza con plantilla “CF_STD_v4”",
            "sleep": 8
        },
        {
            "reasoning": "2025-04-22T09:05:45Z | Generador-Valores   | 🔏  Firma electrónica interna aplicada (hash:0x34ab…)",
            "sleep": 3
        },
        {
            "reasoning": "2025-04-22T09:05:45Z | Generador-Valores   | 🖨️  Documento PDF almacenado en repositorio S3 → key s3://cf/2025/04/CF-89421.pdf",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:46Z | Generador-Valores   | 📤  Evento `cf.generated`",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:46Z | Release-Delivery    | 📦  Inicio proceso de liberación - validando límites operativos",
            "sleep": 5
        },
        {
            "reasoning": "2025-04-22T09:05:48Z | Release-Delivery    | 🔐  Verificación 4-eyes passed",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:48Z | Release-Delivery    | 🚚  Courier asignado - provider: “GreenLog” tracking:#GN12345",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:05:49Z | Release-Delivery    | 📤  Evento `cf.dispatched` enviado",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:07:27Z | Auditor-360         | 📊  SLA parcial: 5 m 16 s; Cumple objetivo (≤ 30 m)",
            "sleep": 10
        },
        {
            "reasoning": "2025-04-22T09:20:02Z | Release-Delivery    | 🛰️  Tracking update courier: arrived at client site",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:24:55Z | Release-Delivery    | 📲  Beneficiario firmó en tablet (lat/long validated)",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:24:55Z | Release-Delivery    | ✅  Confirmación recepción cliente final",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:24:55Z | Release-Delivery    | 📤  Evento `cf.received` emitido",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:24:55Z | Orchestrator        | 🎉  Caso CF-89421 marcado como COMPLETED",
            "sleep": 1
        },
        {
            "reasoning": "2025-04-22T09:24:55Z | Auditor-360         | 🗄️  Flujo cerrado - SLA TOTAL: 22 m 44 s, tokens LLM: 17 392",
            "sleep": 1
        }
    ]
    
    for paso in pasos:
        yield {"razonamiento": paso['reasoning'], "respuesta": None}
        time.sleep(paso['sleep'])
    yield {"razonamiento": "2025-04-22T09:24:56Z | Self-Learning       | 🤖  Ingestando logs; detecta 1 doc faltante → recomienda “Smart-Form” obligatorio", "respuesta": f"Respuesta fija para '{mensaje_usuario}'"}

# Función de streaming para la conversación.
def conversacion_en_stream(mensaje_usuario, historial, razonamiento_acumulado):
    historial.append((mensaje_usuario, "Pensando..."))
    yield historial, razonamiento_acumulado, razonamiento_acumulado

    for chunk in fake_ask_agent(mensaje_usuario):
        razonamiento_acumulado += f"<p>{chunk['razonamiento']}</p>"
        scroll_script = """
        <script>
        var div = document.getElementById('log-div');
        if (div) { div.scrollTop = div.scrollHeight; }
        </script>
        """
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

# Funciones para leer los ficheros Markdown reales.
def show_policy():
    with open("policies/policy_1.md", "r", encoding="utf-8") as f:
        content = f.read()
    return content

def show_routine():
    with open("routines/routine_1.md", "r", encoding="utf-8") as f:
        content = f.read()
    return content

# Construcción de la interfaz con pestañas.
with gr.Blocks() as demo:
    with gr.Tabs():
        # Pestaña "Agente" para la conversación.
        with gr.Tab("Agente"):
            state_historial = gr.State([])
            razonamiento_state = gr.State("")
            with gr.Row():
                with gr.Column():
                    gr.Markdown("## Conversación")
                    # Se usa el Chatbot en modo "tuples".
                    chatbot = gr.Chatbot(label="Agente", type="tuples")
                    user_input = gr.Textbox(label="Tu mensaje")
                    send_btn = gr.Button("Enviar")
                with gr.Column():
                    gr.Markdown("## Razonamiento (auto-scroll)")
                    panel_razonamiento = gr.HTML(label="Log de razonamiento")
            send_btn.click(
                fn=conversacion_en_stream,
                inputs=[user_input, state_historial, razonamiento_state],
                outputs=[chatbot, panel_razonamiento, razonamiento_state],
                queue=True
            )
        # Pestaña "Documentos" para mostrar ficheros Markdown.
        with gr.Tab("Documentos"):
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Policy")
                    policy_md = gr.Markdown(value=show_policy())
                with gr.Column():
                    gr.Markdown("### Routine")
                    routine_md = gr.Markdown(value=show_routine())

demo.launch(share=True)
