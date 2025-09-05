import gradio as gr
import time
import requests
from requests.auth import HTTPBasicAuth
import json


def send_message():
    try:
        print("get_memory INIT")
        url = "https://bot.api.woztell.com/sendResponses?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJBUEkiLCJhcHAiOiI2NTgwMmVjMWE4NTlkNmFkM2ZhNTI0ZWUiLCJhY2wiOlsiYXBpOmFkbWluIl0sImp0aSI6Ijg1MzA1OTMxLWM2ZjAtNTI5ZC04NzhlLWM1YTljMDk1NTc1NyIsImlzcyI6IjY1ODAyZWE1YTg1OWQ2MzVhZmE1MjRlYyIsImlhdCI6MTczMDIxMDExODkwNX0.vY76M2JG0w656MXWfT8_cOTPV-HtGd02GatWjRUnT6s"
        headers = {"Content-Type": "application/json"}
        data = {
            "channelId": "65802ee9a859d69a9fa524f3",
            "recipientId": "56990029260",
            "response": [
                {
                    "type": "TEMPLATE",
                    "integrationId": "67483c872295e123d121365a",
                    "wabaId": "183047921562037",
                    "namespace": "f6092c43_f3c1_483a_8506_29caeeddc420",
                    "components": [
                        {
                            "type": "button",
                            "sub_type": "quick_reply",
                            "index": "0",
                            "parameters": [
                                {"type": "payload", "payload": "confirmar_recepcion"}
                            ],
                        },
                        {
                            "type": "button",
                            "sub_type": "quick_reply",
                            "index": "1",
                            "parameters": [
                                {"type": "payload", "payload": "revisar_detalles"}
                            ],
                        },
                    ],
                    "elementName": "aviso_ataque_america_movil_2",
                    "languageCode": "es",
                    "languagePolicy": "deterministic",
                    "content": [
                        {
                            "type": "HEADER",
                            "format": "TEXT",
                            "text": "Atención: posible amenaza detectada",
                        },
                        {
                            "type": "BODY",
                            "text": "*⚠️ *Este mensaje es exclusivo para el área de seguridad\n\nNuestros sistemas han identificado una* actividad inusual *en la red de* America's Mobile*\n\n*Por favor, accede al flujo técnico de revisión para actuar de forma inmediata.*",
                        },
                        {"type": "FOOTER", "text": "Selecciona una opción"},
                        {
                            "type": "BUTTONS",
                            "buttons": [
                                {"type": "QUICK_REPLY", "text": "Confirmar recepción"},
                                {"type": "QUICK_REPLY", "text": "Revisar detalles"},
                            ],
                        },
                    ],
                }
            ],
        }
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(data),
            auth=HTTPBasicAuth(
                "ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"
            ),
        )
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        tool_response = api_response.get("success")
        print(tool_response)
        return "Memoria Guardada"

    except Exception as e:
        print("Error al guardar la memoria", e)
        return None


# Función fake que simula el streaming del agente de IA.
def fake_ask_agent(mensaje_usuario):
    pasos = [
        {
            "reasoning": "2025-06-10T12:00:00Z | Orchestrator         | 🔄  Inicio ciclo de escaneo #1 (target subnets: 10.1.0.0/16, 172.16.1.0/24)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:01Z | NetScan-Agent        | 🔍  Escaneando puerto 5060 UDP en core-sip-01",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:02Z | NetScan-Agent        | 🛜  Escaneo HTTP a portal-auth-1.americanmobile.net",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:03Z | DB-Sink-Agent        | 💾  Logs de escaneo persistidos en cluster InfluxDB",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:04Z | AMX-Eval-Agent       | 🆗  Métricas de escaneo dentro del SLA 99%",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:05Z | Learner-Agent        | 🤖  Model updated w/ 1.2k new benign patterns",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:06Z | Orchestrator         | ⏳  Esperando resultados de detección de anomalías",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:07Z | Anomaly-Detect       | 🧠  Analizando 500 eventos recientes...",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:08Z | Anomaly-Detect       | ✅  No anomalías detectadas en este batch",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:09Z | NetScan-Agent        | 📈  Tasa de paquetes anómalos 0.1%",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:10Z | AMX-Eval-Agent       | 📊  Health-check completado",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:11Z | Orchestrator         | 🔄  Inicio ciclo de escaneo #2 (target subnets: 10.2.0.0/16, 172.16.2.0/24)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:12Z | NetScan-Agent        | 🔍  Escaneando puerto 5060 UDP en core-sip-02",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:13Z | NetScan-Agent        | 🛜  Escaneo HTTP a portal-auth-2.americanmobile.net",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:14Z | DB-Sink-Agent        | 💾  Logs de escaneo persistidos en cluster InfluxDB",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:15Z | AMX-Eval-Agent       | 🆗  Métricas de escaneo dentro del SLA 99%",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:16Z | Learner-Agent        | 🤖  Model updated w/ 1.2k new benign patterns",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:17Z | Orchestrator         | ⏳  Esperando resultados de detección de anomalías",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:18Z | Anomaly-Detect       | 🧠  Analizando 500 eventos recientes...",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:19Z | Anomaly-Detect       | ✅  No anomalías detectadas en este batch",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:20Z | NetScan-Agent        | 📈  Tasa de paquetes anómalos 0.2%",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:21Z | AMX-Eval-Agent       | 📊  Health-check completado",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:31Z | Orchestrator         | 🔄  Inicio ciclo de escaneo #3 (target subnets: 10.3.0.0/16, 172.16.2.0/24)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:32Z | NetScan-Agent        | 🔍  Escaneando puerto 5060 UDP en core-sip-03",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:33Z | NetScan-Agent        | 🛜  Escaneo HTTP a portal-auth-3.americanmobile.net",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:34Z | DB-Sink-Agent        | 💾  Logs de escaneo persistidos en cluster InfluxDB",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:35Z | AMX-Eval-Agent       | 🆗  Métricas de escaneo dentro del SLA 99%",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:36Z | Learner-Agent        | 🤖  Model updated w/ 1.2k new benign patterns",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:37Z | Orchestrator         | ⏳  Esperando resultados de detección de anomalías",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:38Z | Anomaly-Detect       | 🧠  Analizando 500 eventos recientes...",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:39Z | Anomaly-Detect       | ✅  No anomalías detectadas en este batch",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:40Z | NetScan-Agent        | 📈  Tasa de paquetes anómalos 0.1%",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:00:41Z | AMX-Eval-Agent       | 📊  Health-check completado",
            "sleep": 1,
        },
        # ← ciclos 3-5 análogos (mantengo el mismo patrón)
        {
            "reasoning": "2025-06-10T12:01:00Z | NetScan-Agent        | 🔍  Escaneando puerto 443 TCP en web-core-03",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:01Z | NetScan-Agent        | 📶  Tráfico HTTPS esperado desde IP 10.45.22.88 → web-core-03",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:02Z | DB-Sink-Agent        | 💾  Registro de actividad normal guardado (id:NORM-2213)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:03Z | Anomaly-Detect       | ✅  Patrón sin anomalías: tráfico consistente con baseline",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:04Z | Orchestrator         | 🟢  Estado de red saludable, sin alertas generadas",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:05Z | AMX-Eval-Agent       | 📈  SLA operación normal = 35 s (objetivo ≤ 60 s)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:06Z | Learner-Agent        | 📚  Reforzando perfil de tráfico habitual para web-core-03",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:07Z | NotifierChat-Agent   | 📨  Informe de rutina enviado al canal #net-health",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:11Z | NetScan-Agent        | 🔍  Escaneando puerto 22 TCP en mgmt-core-07",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:12Z | NetScan-Agent        | ⚡  Tráfico SIP inusual detectado desde IP 201.175.14.22 → core-sip-07",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:13Z | DB-Sink-Agent        | 💾  Evento anómalo guardado (id:ANOM-5942)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:14Z | Anomaly-Detect       | 🚨  Severidad preliminar = HIGH, patrón ≈ fuerza bruta SIP",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:15Z | Orchestrator         | 📣  Posible ataque detectado; solicitando validación humana",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:16Z | NotifierChat-Agent   | 🚨  Incidente AMX-20250610-01 publicado en canal #sec-ops",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:16Z | NotifierWA-Agent     | ⚠️  *Alerta crítica* posible ataque SIP fuerza bruta en core-sip-07. Necesita validación.",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:17Z | Human-Validator      | 👤  Revisor humano asignado (Maria.Duarte)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:19Z | Human-Validator      | 🔎  Validando logs ANOM-5942, confirmando correlación 4 eventos CRIT en 2 min",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:20Z | Human-Validator      | ✅  Confirmado: ataque en curso",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:21Z | NotifierWA-Agent     | 📲  Mensaje urgente enviado por WhatsApp al C-Level de Seguridad: 🚨 Alerta crítica en red SIP core-sip-07. IP atacante: 201.175.14.22. Acción requerida.",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:21Z | Orchestrator         | 🛑  Bloqueando IP 201.175.14.22 via firewall API",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:22Z | NetScan-Agent        | 🔒  Regla FW aplicada correctamente",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:23Z | DB-Sink-Agent        | 💾  Evento bloqueo registrado",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:24Z | AMX-Eval-Agent       | 📈  SLA respuesta incidente = 47 s (objetivo ≤ 60 s)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:25Z | Learner-Agent        | 📚  Reinforcement learning applied: attack signature added",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:26Z | Orchestrator         | 📤  Informe final incidente AMX-20250610-01 archivado",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:27Z | NotifierChat-Agent   | 📢  Incidente AMX-20250610-01 marcado como RESUELTO en #sec-ops",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:01:28Z | AMX-Eval-Agent       | 🆗  Métricas post-incident 100%",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:10Z | NetScan-Agent        | 🔍  Escaneando puertos 161/162 UDP en snmp-core-02",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:11Z | NetScan-Agent        | 🔁  Tráfico SNMP de monitoreo recibido desde IP 192.168.5.10",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:12Z | DB-Sink-Agent        | 💾  Entrada de monitoreo archivada (id:NORM-2245)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:13Z | Anomaly-Detect       | 💤  Sin eventos relevantes detectados",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:14Z | Orchestrator         | 📘  Ciclo de monitoreo finalizado sin incidentes",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:15Z | AMX-Eval-Agent       | 📈  SLA verificación = 42 s (objetivo ≤ 60 s)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:16Z | Learner-Agent        | 📚  No se detectaron patrones nuevos, sin cambios al modelo",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:02:17Z | NotifierChat-Agent   | ✅  Estado OK reportado en canal #sec-ops",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:00Z | NetScan-Agent        | 🔍  Escaneando puerto 5060 UDP en core-sip-03",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:01Z | NetScan-Agent        | 📡  Tráfico SIP dentro de parámetros esperados desde IP 10.33.12.45",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:02Z | DB-Sink-Agent        | 💾  Evento normal archivado (id:NORM-2291)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:03Z | Anomaly-Detect       | 🔎  Resultado: sin anomalías detectadas",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:04Z | Orchestrator         | 🔔  Activando validación humana rutinaria por auditoría interna",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:05Z | Human-Validator      | 👤  Revisor humano asignado (Ana.Ruiz)",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:06Z | Human-Validator      | 🧐  Revisión manual de logs NORM-2291: sin hallazgos críticos",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:07Z | Human-Validator      | ✅  Validación completada: tráfico legítimo",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:08Z | Orchestrator         | 🟢  Finalizando ciclo sin alertas",
            "sleep": 1,
        },
        {
            "reasoning": "2025-06-10T12:03:09Z | NotifierChat-Agent   | 📄  Revisión cumplimiento NORM-2291 documentada en #sec-ops",
            "sleep": 1,
        },
        # ← ciclos de escaneo 6-7 reanudan operación normal y cierran la lista.
    ]

    fin = 'Ataque detectado. Aqui tiene el <a href="https://linkhubai-my.sharepoint.com/:w:/g/personal/angel_pozo_linkhub_ai/EXBsDH5hvvpNu7p7zmtLmTEB7x2qwdizdZPPGBEa39jNQQ?e=XpUiIz">reporte</a>'
    razonamiento = "2025-06-10T12:02:23Z | Orchestrator     | 🏁 Monitoreo Completado"

    for paso in pasos:
        yield {"razonamiento": paso["reasoning"], "respuesta": None}
        time.sleep(paso["sleep"])

    send_message()
    yield {"razonamiento": razonamiento, "respuesta": fin}


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
                    gr.Markdown("## Razonamiento")
                    panel_razonamiento = gr.HTML(label="Log de razonamiento")
            send_btn.click(
                fn=conversacion_en_stream,
                inputs=[user_input, state_historial, razonamiento_state],
                outputs=[chatbot, panel_razonamiento, razonamiento_state],
                queue=True,
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
