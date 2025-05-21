
# Procedimiento Operativo: Validación de Solicitudes de Carta de Garantía Bancaria

**Área responsable:** Cumplimiento (Agente KYC – Riesgo)  
**Objetivo:** Validar que el cliente, los firmantes y la documentación relacionada con la solicitud estén dentro del apetito de riesgo del banco y cumplan con los lineamientos de legitimidad y no sanción.  
**Resultado esperado:** Determinar si la solicitud cumple con los criterios de cumplimiento y emitir un veredicto: **Aprobado / Advertencia / Rechazado**.

---

## 1. Ingreso de Documentos

**Paso 1.1 – Recepción del Caso:**  
Recibirás una notificación con un nuevo caso a evaluar.  
La notificación incluirá:
- ID del caso (ej. `CF‑89421`)
- ID del cliente (ej. `CLI‑004576`)
- URLs de los documentos (ej. solicitud, poderes, etc.)
- Nombre del ejecutivo responsable

**Paso 1.2 – Descarga de Documentos:**  
Accede a los enlaces provistos y descarga los documentos adjuntos.  
- Asegúrate de guardar los archivos con nombres claros que permitan asociarlos al caso.

**Paso 1.3 – Digitalización y Hash:**  
Realiza un escaneo OCR a cada documento descargado para obtener su contenido digital y generar un hash único por archivo.  
- Este hash se usará para validar la integridad del documento más adelante.

---

## 2. Verificación de Autenticidad de Documentos

**Paso 2.1 – Validación de Firma:**  
Revisa si las firmas presentes en los documentos son válidas utilizando las herramientas o criterios establecidos por el área legal (firma digital o manuscrita, dependiendo del formato).

**Paso 2.2 – Detección de Manipulación:**  
Verifica que los documentos no hayan sido alterados:
- Compara los hashes generados con los esperados (si existen registros previos).
- Revisa los metadatos del archivo (fecha de creación, modificación, autor, etc.) para detectar cambios no justificados.

---

## 3. Verificación de Firmantes y Poderes

**Paso 3.1 – Comparación con Firmas Autorizadas:**  
Compara las firmas de los documentos con las muestras autorizadas registradas por el banco.
- Si la similitud es superior al 95%, continúa al siguiente paso.
- Si es inferior, marca el caso como **Fallido**

**Paso 3.2 – Validación de Vigencia del Poder:**  
Si la firma es válida, revisa que el poder legal del firmante esté vigente a la fecha actual.
- Si está vencido, marca el caso como **Fallido**.
- Si está vigente, continúa al paso siguiente.

---

## 4. Revisión de Listas de Sanción y PEP

**Paso 4.1 – Búsqueda en Listas:**  
Consulta listas oficiales (sanciones, OFAC, ONU, etc.) para verificar si el cliente, el beneficiario o los firmantes están incluidos.

**Paso 4.2 – Evaluación de Coincidencias:**  
Evalúa el nivel de coincidencia con los nombres encontrados en las listas y calcula el “match score”.

---

## 5. Evaluación de Riesgo

**Según el _match score_ obtenido en la etapa anterior:**
- Si el score es **menor o igual a 0.15**, se considera **Aprobado**.
- Si el score es **entre 0.15 y 0.40**, se considera **Advertencia**.
- Si el score es **mayor a 0.40**, se considera **Fallido**.