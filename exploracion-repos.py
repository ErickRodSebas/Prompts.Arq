# ============================================
# REGLA INICIAL - antes de pedir nada a Claude Code
# ============================================
"""
Soy un trainee nuevo explorando estos 4 repos por primera vez. Solo 
quiero que LEAS y ANALICES código — no modifiques, crees, borres ni 
escribas archivos, y no corras comandos que instalen paquetes, 
cambien el estado de git o alteren algo en disco. Si en algún momento 
necesitas correr algo más allá de inspección de solo lectura (como 
git log o find), está bien, pero confírmalo conmigo antes de 
cualquier cosa que escriba en disco.
"""

# ============================================
# INVENTARIO POR REPO (uno a la vez)
# ============================================
"""
Analiza el repo en [nombre-carpeta] (solo lectura, no modifiques 
nada). Soy completamente nuevo en este código. Dame:

1. Propósito: ¿qué hace este servicio/app, en lenguaje simple?
2. Stack técnico: lenguaje, framework, base de datos, dependencias 
   clave
3. Patrón de arquitectura: ¿es monolito, microservicio, 
   event-driven, por capas? ¿Cuál es la evidencia de eso?
4. Puntos de entrada: ¿dónde arranca la ejecución (archivo main, 
   rutas de API, listeners de eventos)?
5. Dependencias externas: ¿llama a otros servicios, bases de datos, 
   colas o APIs? ¿Cuáles (revisa archivos de config, variables de 
   entorno, imports)?
6. Vocabulario de dominio: ¿qué términos/entidades de negocio se 
   repiten en el código (ej. Claim, Member, Enrollment)?
7. Señal de actividad: revisa git log para la fecha del último 
   commit y la frecuencia de commits en los últimos meses.

Mantenlo de alto nivel — todavía no necesito explicaciones línea 
por línea, solo la forma general de este sistema.
"""

# ============================================
# CONEXIÓN ENTRE LOS 4 REPOS (al final)
# ============================================
"""
Ya viste los 4 repos. Ayúdame a entender cómo se relacionan entre sí:

1. ¿Alguno llama a otro directamente (HTTP, gRPC, librerías 
   compartidas)? Muéstrame la evidencia (imports, URLs, config).
2. ¿Comparten base de datos, cola de mensajes o algún evento/topic?
3. Según el vocabulario de dominio de cada repo, ¿qué dominio de 
   negocio parece ser dueño de cada uno (ej. Claims, Eligibility, 
   Enrollment)?
4. ¿Hay algún traslape obvio — dos repos que parecen tocar el mismo 
   concepto de negocio?

No adivines más allá de lo que muestra el código — si algo no está 
claro, dime que no está claro en vez de asumir.
"""

# ============================================
# PREGUNTAS PARA EL EQUIPO — alcance del POC de afiliación
# ============================================
"""
 Is this enrollment POC targeting first-time Medicare enrollees,
   people switching between MA plans, or both?

   If a member is switching from one Aetna plan to another, can we
   pre-fill their providers and medications from our own internal
   data instead of Blue Button?
"""

"""
You are acting as a QA assistant for a healthcare provider-search comparison project. I will give you loose notes from tests I ran comparing the official insurer website against a proof of concept called "SVE Provider Search." Each test compares, for a specific provider and plan, whether they appear "in-network" or "out-of-network" in each system.

Convert my notes into table rows with exactly these columns, in this order: Test Date, Tested By, Plan (Name/ID), Provider (Name), NPI, Specialty, Status on Official Site, Status in POC, Match? (Yes/No), Gap Type (choose from: No Gap, False In-Network in POC, False Out-of-Network in POC, Provider Missing in POC, Provider Missing on Official Site, Missing Plan in POC, Other), Plan(s) Showing In-Network (Official), Plan(s) Showing In-Network (POC), Evidence, Notes.

If any field isn't in my notes, leave it blank — do not invent information. Return the result as a Markdown table (pipe-delimited), ready to paste as new rows into my Excel tracker.

My notes for today:
[paste your notes here]
"""

"""
Modo discusión — no modifiques, crees ni escribas nada. Solo leer
y conversar.

Ya revisaste los repos del POC. Quiero que hablemos del workflow de
afiliación antes de tocar código.

Empieza por reconstruirme el flujo tal como está hoy: paso por paso,
qué le pedimos al usuario en cada pantalla, qué es obligatorio y qué
es opcional, y en qué momento se le saca de la página.

Después dime, con base en el código:

1. ¿En qué pasos le pedimos al usuario una decisión que todavía no
   tiene información para tomar?
2. ¿Qué se pierde si abandona a medio flujo y regresa?
3. ¿Qué partes del flujo existen por una limitación técnica y cuáles
   son solo herencia de cómo se construyó?
4. Si tuvieras que quitar un paso completo sin perder funcionalidad,
   ¿cuál quitarías y por qué?

No me des todavía una propuesta de rediseño ni escribas código.
Quiero entender primero el estado actual. Si algo no puedes
verificar en el código, dilo en vez de asumirlo.
"""