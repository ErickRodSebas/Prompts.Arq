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

Context:
This is the same "Plan Recommendation" POC wizard I just added a step
indicator to (item 7, already merged and pushed). Current tabs are:
1. "Select Your Provider" (Provider Search)
2. "Drug Coverage"
3. "Recommended Plans" (formerly "Plans")

Now I'm picking up item 4: adding a new pharmacy step as a new tab, before
the "Recommended Plans" tab.

Task — Add pharmacy step (new tab — "Your Pharmacy"):
- Add a new tab called "Your Pharmacy" positioned after the drug coverage
  tab and before the "Recommended Plans" tab.
- Simple ZIP-based pharmacy search (single ZIP input, no radius/adjacent
  ZIP logic — out of scope for this POC).
- Selecting a pharmacy can be mocked/simulated — no real pharmacy API
  integration needed.
- Make sure the step indicator picks up this new tab automatically (it was
  built to read tab count/labels dynamically — verify this instead of
  hardcoding).

Constraints:
- Follow the same design system/styling as the other tabs.
- Do not modify the other three tabs' logic — only add the new pharmacy tab
  and wire it into the wizard's navigation.
- Small, frequent commits, pushed as we finish each verified piece.

Before writing code, show me which files you'll touch and confirm the step
indicator update happens automatically.
Additional constraint:
Before making changes, run git pull to make sure you're working against the
latest version of App.tsx. If Tab 2 (Drug Coverage) or Tab 3 (Recommended
Plans) code looks like it's mid-change or inconsistent, stop and tell me
instead of guessing intent. When wiring the new tab into App.tsx, make the
smallest possible insertion (add to the tabs array/list and routing) —
don't reformat, refactor, or reorder anything else in that file.

Before making any changes, investigate and report back (don't implement
yet):

1. Find the removed <nav> block in this session's commit history and show
   me the exact original code for the contract/PBP badge — what component
   it used, what data/props it read, and under what condition it rendered
   (always visible, or conditional on something).

2. Look at the current StepIndicator step-button markup/styling and tell
   me whether there's reasonable room to render that badge inline without
   breaking the step indicator's layout, or if it would need a design
   adjustment (e.g. smaller badge, different position).

Once you report these findings, I'll tell you how to proceed. do it in a consise way.

Based on your investigation: restore the contract/PBP badge as a compact
pill element in the StepIndicator, following your own "smallest viable
option" recommendation.

Implementation:
- Add a small pill/badge (reuse the old .tabHint visual style — small,
  monospace, reduced font-size/padding — as you suggested) positioned
  below the label, only on the "Select Your Drugs" / Drug Coverage step.
- Content: {selectedPlan.contract}-{selectedPlan.pbp}, exactly as before.
- Condition: only render when selectedPlan is truthy (same as the original
  logic) — hidden until a plan is picked, shown after.
- Read selectedPlan from the same state in App.tsx (set by
  handlePlanSelect) — pass it down to StepIndicator as a prop if it isn't
  already available there.
- Make sure it doesn't push the 4-step layout wider or cause wrapping on
  narrow screens, per the constraint you already flagged.

Scope:
- Only touch what's needed to add this one badge to this one step. Don't
  change anything else in StepIndicator, App.tsx navigation, or the other
  three tabs.
- Show me the diff before committing. Run npm run build to confirm nothing
  breaks, then commit with a clear message and push on its own, following
  our usual small-commit pattern.

  After implementing and verifying the badge fix (build clean, diff shown),
do NOT push yet. Instead, give me a short summary (3-4 lines max, plain
language, no code) describing exactly what changed, that I can paste into
our team chat to ask for a quick go-ahead before I push.
"""

