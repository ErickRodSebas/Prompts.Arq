# ============================================
# REGLA INICIAL - antes de pedir nada a Claude Code
# ============================================
"""
Soy trainee explorando estos repos por primera vez. Solo quiero 
que LEAS y ANALICES código — no modifiques, crees, borres ni 
escribas archivos...
"""

# ============================================
# INVENTARIO POR REPO
# ============================================
"""
Analiza el repo en [nombre-carpeta] (solo lectura, no modifiques 
nada). Soy nuevo en este código. Dame:

1. Propósito: ¿qué hace este servicio/app, en lenguaje simple?
2. Stack técnico: lenguaje, framework, base de datos, dependencias clave
3. Patrón de arquitectura: ¿monolito, microservicio, event-driven, 
   por capas? ¿Cuál es la evidencia?
4. Puntos de entrada: ¿dónde arranca la ejecución (archivo main, 
   rutas de API, listeners de eventos)?
5. Dependencias externas: ¿llama a otros servicios, bases de datos, 
   colas o APIs? ¿Cuáles (revisa configs, variables de entorno, imports)?
6. Vocabulario de dominio: ¿qué términos de negocio se repiten en 
   el código (ej. Claim, Member, Enrollment)?
7. Actividad: revisa git log — última fecha de commit y frecuencia 
   en los últimos meses.

Mantenlo de alto nivel, no necesito explicación línea por línea todavía.
"""

# ============================================
# Conexión entre los 4 repos (al final)
# ============================================
"""
Ya viste los 4 repos. Ayúdame a entender cómo se relacionan:

1. ¿Alguno llama a otro directamente (HTTP, gRPC, librerías 
   compartidas)? Muéstrame la evidencia (imports, URLs, config).
2. ¿Comparten base de datos, cola de mensajes o eventos?
3. Según el vocabulario de dominio de cada uno, ¿qué dominio de 
   negocio parece dueño de cada repo (ej. Claims, Eligibility, 
   Enrollment)?
4. ¿Hay algún traslape obvio entre dos repos sobre el mismo concepto?

No adivines más allá de lo que muestra el código — si algo no 
está claro, dime que no está claro en vez de asumir.
"""