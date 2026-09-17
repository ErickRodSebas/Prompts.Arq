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

Context:
This is a "Plan Recommendation" POC with a multi-step wizard (tabs 1 through 4).
The component runs embedded inside a Salesforce Experience Cloud site.
I'm working on ticket #7: "Step indicator + UX copy pass", on the
iteration-playground-collab branch.

My teammates are actively working in parallel on:
- Item 1: renaming Tab 1 to "Select Your Provider" + lazy-load logic
- Item 2: ZIP search logic
- Item 3: redesigning Tab 2 as "Your Medications" (drug list)

Task 1 — Step Indicator (wizard progress bar):
- Add a visual progress indicator showing steps 1→2→3→4, highlighting the
  current step (e.g. "Step 1 of 4").
- It must update dynamically as the user moves forward/backward between
  steps.
- Follow the existing design system/styling already used in the project.
- Add clear accessibility labels (aria-label) for each step in the
  indicator itself.

Task 2 — UX Copy Pass (SCOPE LIMITED):
- Do NOT rename or touch the headings/labels for Tab 1, Tab 2, or Tab 3 —
  those are already being renamed by teammates in items 1-3. Leave their
  copy exactly as-is, even if it looks unfinished or inconsistent right now.
- Only review and improve the heading/label for Tab 4 ("Recommended Plans"),
  since no one else is currently working on it.
- Update accessibility attributes (alt/aria-label) only for the step
  indicator and Tab 4 — not for Tabs 1-3.

Task 3 — "Simulate" button:
- Verify the "Simulate" button displays and works correctly when the
  component is embedded inside Experience Cloud. If something in Experience
  Cloud's wrapper/CSS/context is hiding or breaking it, flag it before
  applying any fix.

Constraints:
- Do not modify business logic, data handling, or navigation flow for any
  tab.
- Do not refactor or restructure Tab 1, Tab 2, or Tab 3 components at all —
  treat their files as read-only unless the step indicator needs to hook
  into their navigation state (in which case, make the smallest possible
  change and point it out to me explicitly).
- Make small, frequent commits (one per logical change) so I can push often
  and avoid merge conflicts with the team.

Before writing any code, show me which files you plan to touch and a short
summary of the plan.

I have an uncommitted change to react-app/package-lock.json and an
untracked package-lock.json at the repo root. Neither is related to my
ticket #7 work (step indicator + copy pass) — they likely appeared from an
npm install run during your own verification steps.

Please:
1. Discard/restore the modified react-app/package-lock.json (revert it to
   its committed state).
2. Delete the untracked package-lock.json at the repo root.
3. Run git status to confirm the working tree is clean and confirm the 2
   commits from this session are still intact and ready to push.
4. Run git pull to bring in any changes from teammates.
5. If the pull is clean (no conflicts), run git push to publish my 2
   commits to origin/iteration-playground-collab.
6. If there's a merge conflict, STOP and show me exactly which files and
   lines conflict — do not resolve it automatically without me reviewing it
   first.

   Update the step indicator's step-1 label to "Select Your Provider" to match
Purab's rename — keep it in sync with whatever the tab button actually
says, since showing two different names for the same step would confuse
users. Commit this separately with a clear message (e.g. "fix: sync step
indicator label with Tab 1 rename").
"""

