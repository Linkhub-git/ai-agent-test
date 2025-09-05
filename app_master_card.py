import gradio as gr
import time


# Función fake que simula el streaming del agente de IA.
def fake_ask_agent(mensaje_usuario, index):
    pasos = [
        {
            "reasoning": "<b>⧉ TraceID 0001 – 00 : 00</b><br><b>Task:</b> Comprender petición inicial.<br><b>Action:</b> NLP.parse(user_utterance)<br><b>Result:</b> Intención = “Plan de llamada de ventas”, Entidad = “Mastercard Gold”, Región = “México”.<br><b>Evaluator:</b> Adherencia a políticas 100 %. Sin alucinación detectada.",
            "sleep": 1,
        },
        {
            "reasoning": "<b>⧉ TraceID 0002 – 00 : 01</b><br><b>Task:</b> Buscar mejores prácticas de venta consultiva.<br><b>Action:</b> KB.search('sales_frameworks', tags=['financial_services','Latam'])<br><b>Result:</b> Modelo SPIN, AIDA, y “3 Actos”.<br><b>Evaluator:</b> Relevancia 98 %. Sin alucinación detectada.",
            "sleep": 1,
        },
        {
            "reasoning": "<b>⧉ TraceID 0004 – 00 : 04</b><br><b>Task:</b> Enriquecer con datos de cliente.<br><b>Action:</b><br>1. CRM.get_profile('prospect_id_44551') <b>→ gasta 12 000 USD/mes, viajes = 34 al año.</b><br>2. ERP.get_product('MC_GOLD_LATAM') <b>→ beneficios y coberturas actualizadas.</b><br>3. LEGACY_RISK.query('prospect_id_44551') <b>→ sin morosidad.</b><br><br><b>Evaluator: Datos fidedignos 99 %. Sin alucinación detectada.</b>",
            "sleep": 1,
        },
        {
            "reasoning": "<b>⧉ TraceID 0011 – 00 : 26</b><br><b>Task:</b> Comparativa con Visa Platinum.<br><b>Action:</b><br>1. WEB.search('Visa Platinum travel insurance duration 2025')<br>2. WEB.search('Mastercard Global Service replacement cost')<br><br><b>Result: Visa = 90 días; reposición ≈ 175 USD + envío.</b><br><b>Evaluator AI: Corrobora con fuentes oficiales (visa.com, mastercard.com). Confianza 96 %. Sin alucinación detectada.</b>",
            "sleep": 1,
        },
        {
            "reasoning": "<b>⧉ TraceID 0013 – 00 : 32</b><br><b>Task:</b> Resumen final y motivación.<br><b>Action:</b> draft_closing_tips(listen_ratio=0.7)<br><b>Evaluator:</b> Coaching breve, motivador. Sin alucinación detectada.",
            "sleep": 1,
        },
    ]

    if index == 0:
        print("Index")
        pasos = pasos[:2]
        fin = "¡Claro, Laura! Para una venta consultiva efectiva, pensemos la llamada en tres actos:<br><br><b>1. Explorar – haz preguntas abiertas sobre su estilo de vida y hábitos de pago.</b><br><b>2. Conectar valor – empareja sus necesidades con beneficios tangibles (seguros, asistencias, programa de recompensas).</b><br><b>3. Cerrar con claridad – resume acuerdos y solicita confirmación.</b><br><br>Para empezar, ¿qué sabes ya del prospecto?"
        razonamiento = "<b>⧉ TraceID 0003 – 00 : 02<b><br><b>Task:<b> Proponer estructura de llamada.<br><b>Reasoning:<b> SPIN es útil pero 3 Actos más simple para demo.<br><b>Action:<b> draft_reply(structure_3_acts)<br><b>PolicyCheck:<b> Contenido no sensible ni regulado. Sin alucinación detectada."
    elif index == 1:
        print("Inicio")
        pasos = [pasos[2]]
        fin = "Perfecto. Entonces destacaremos:<br><br><b>- Seguro de viajes por hasta 150 000 USD incluido.</b><br><b>- Asistencia global 24/7; reposición de tarjeta en 48 h donde esté.</b><br><b>- Mastercard Travel Rewards: cashback en hoteles y restaurantes premium.</b><br><b>- Protección de compras por un año - ideal para su volumen de gasto.</b><br><br><b>Tip: formula preguntas como “En tus viajes, ¿qué respaldo valoras más cuando surge un imprevisto?” Esto hará que él mismo identifique la relevancia del beneficio.</b>"
        razonamiento = "<b>⧉ TraceID 0005 – 00 : 05</b><br><b>Task:</b> Transformar datos en beneficio-cliente.<br><b>Action:</b> map_features_to_needs(travel_security_high)<br><b>Result:</b> Seguro viajes, reposición exprés, cashback travel.<br><b>PolicyCheck:</b> Cumple marketing guidelines. <b>Sin alucinación detectada.</b><br>"
    elif index == 2:
        print("Inicio")
        pasos = []
        fin = "Propongo algo así:<br><br><i>“Juan, sé que viajas constantemente y tu tiempo vale oro. ¿Qué tan valioso sería contar con un equipo que adelanta tus reembolsos médicos en el extranjero y te envía una tarjeta nueva antes de que termine tu agenda de la semana?”</i><br><br>-- Pausa aquí para escuchar su reacción y luego enlaza con el seguro y la reposición exprés."
        razonamiento = "<b>⧉ TraceID 0006 – 00 : 09</b><br><b>Task:</b> Generar gancho de apertura.<br><b>Action:</b> copywriting.generate_hook(benefit='seguridad', duration=20s)<br><b>Evaluator:</b> Tono profesional y empático. Sin alucinación detectada."
    elif index == 3:
        print("Inicio")
        pasos = []
        fin = "Estrategia “Costo vs. Retorno”:<br><br><b>1. Cuantifica: “Con tu gasto promedio, recuperas el fee en 3 meses solo vía cashback.”</b><br><b>2. Ancla emocional: compara el fee con un gasto cotidiano (“menos que una noche de hotel ejecutivo”).</b><br><b>3. Prueba social: menciona un caso real de cliente similar que ahorró 1 200 USD en un año.</b><br><b>4. Cierre en positivo: pide confirmación: “¿Te hace sentido invertir 180 USD para proteger 150 000 USD cada vez que vuelas?”"
        razonamiento = "<b>⧉ TraceID 0007 – 00 : 12</b><br><b>Task:</b> Preparar manejo de objeción fee anual.<br><b>Action:</b><br>- INTRANET.sales_playbooks('annual_fee_handling')<br>- ERP.benefit_roi('MC_GOLD', spend=12000) <b>→ payback = 3 meses.</b><br><br><b>Evaluator: Datos sólidos 97 %. Sin alucinación detectada.</b>"
    elif index == 4:
        print("Inicio")
        pasos = []
        fin = "Sí: <b>bono de 25 000 puntos</b> al gastar 1 000 USD los primeros 60 días, equivalente a dos noches en hotel 4★. Además, fee cero el primer año si activa débito automático de servicios."
        razonamiento = "<b>⧉ TraceID 0008 – 00 : 17</b><br><b>Task:</b> Verificar promociones vigentes.<br><b>Action:</b> ERP.promos.get_active(campaign='Gold_Q3_25')<br><b>Result:</b> 25 000 puntos + fee cero con débito automático.<br><b>PolicyCheck:</b> Oferta aprobada por Marketing (valid hasta 30-sep-2025). <b>Sin alucinación detectada.</b>"
    elif index == 5:
        print("Inicio")
        pasos = []
        fin = "Correcto. Añade una pregunta de cierre suave: <i>“¿Quieres que coordine el envío de tu solicitud hoy mismo para que aproveches la promo?”</i>"
        razonamiento = "<b>⧉ TraceID 0009 – 00 : 18</b><br><b>Task:</b> Confirmar claridad legal de promoción.<br><b>Action:</b> LEGAL.validate_marketing_claim(promo_id='G25P')<br><b>Result:</b> OK, wording permitido.<br><b>Evaluator:</b> Adherencia 100 %. <b>Sin alucinación detectada.</b>"
    elif index == 6:
        print("Inicio")
        pasos = []
        fin = "Señales verbales:<br><b>- Cambia de “si” a “cuando” (“Cuando reciba la tarjeta…”).</b><br><b>- Pregunta por tiempos específicos de entrega.</b><br><br>Señales paraverbales (en videollamada):<br><b>- Asiento con la cabeza, sonrisa espontánea. Cuando detectes dos señales consecutivas, lanza el cierre.</b>"
        razonamiento = "<b>⧉ TraceID 0010 – 00 : 23</b><br><b>Task:</b> Detectar señales de compra.<br><b>Action:</b> GPT-SalesCoach.retrieve('buy_signals_soft')<br><b>Evaluator:</b> Lista concisa – cumple coaching brief. Sin alucinación detectada."
    elif index == 7:
        print("Inicio")
        pasos = [pasos[3]]
        fin = "<b>1. Amplitud de coberturas: Mastercard extiende a 365 días de viajes; Visa normalmente 90.</b><br><b>2. Mastercard Global Service™: reposición gratis en 2 días hábiles globalmente; con Visa el costo puede ser 175 USD.</b><br><b>3. Asistencias en carretera incluidas, útiles en Latam donde la infraestructura es desigual.</b><br><b>4. Mastercard Priceless Cities con experiencias exclusivas en CDMX, Bogotá y São Paulo.<br><br>Refuerza que lo “premium” no es solo el plástico sino el ecosistema.</b>"
        razonamiento = "<b>⧉ TraceID 0012 – 00 : 28</b><br><b>Task:</b> Ensamblar diferenciadores competitivos.<br><b>Action:</b> compose_reply(list_diffs, tone='assertive')<br><b>PolicyCheck:</b> Sin comparaciones denigrantes; factual. Sin alucinación detectada."
    else:
        print("Fin")
        pasos = [pasos[4]]
        fin = "¡Éxitos mañana! Recuerda: escucha el 70 % del tiempo, habla el 30 %. Después cuéntame cómo fue."
        razonamiento = "<b>⧉ TraceID END – 00 : 34</b><br><b>Overall QA (Agente Evaluador)</b><br><b>- Cobertura de objetivos: 100 % (técnicas de venta, manejo de objeciones, valor Mastercard).</b><br><b>- Adherencia a políticas de marca y compliance: 99 %.</b><br><b>- Detected hallucination risk: 0 %.</b><br><b>Sin alucinación detectada.</b>"

    for paso in pasos:
        yield {"razonamiento": paso["reasoning"], "respuesta": None, "index": index}
        time.sleep(paso["sleep"])

    index += 1
    yield {"razonamiento": razonamiento, "respuesta": fin, "index": index}


# Función de streaming para la conversación.
def conversacion_en_stream(mensaje_usuario, historial, razonamiento_acumulado, index):
    historial.append((mensaje_usuario, "Pensando..."))
    yield historial, razonamiento_acumulado, razonamiento_acumulado, index  # <-- agrega index aquí

    print("INICIAMOS INDEX")
    print(index)

    for chunk in fake_ask_agent(mensaje_usuario, index):
        print("FOR CHUNK")
        index = chunk["index"]
        print(index)
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
            print("INCREMENTAMOS INDEX 1")
            print(index)

            yield historial, html_razonamiento, razonamiento_acumulado, index
        else:
            print("INCREMENTAMOS INDEX 2")
            print(index)
            historial[-1] = (mensaje_usuario, chunk["respuesta"])
            yield historial, html_razonamiento, razonamiento_acumulado, index


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
            index_state = gr.State(0)
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
            print("PULSAMOS BOTON")
            index = 0
            send_btn.click(
                fn=conversacion_en_stream,
                inputs=[user_input, state_historial, razonamiento_state, index_state],
                outputs=[chatbot, panel_razonamiento, razonamiento_state, index_state],
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
