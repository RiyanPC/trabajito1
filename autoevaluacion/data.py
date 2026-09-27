# data.py
# Competencias, preguntas y recomendaciones para la autoevaluación

COMPETENCIAS = [
    "Aprendizaje autónomo",
    "Trabajo en equipo",
    "Comunicación efectiva",
    "Resolución de problemas",
    "Responsabilidad y puntualidad",
    "Pensamiento crítico",
    "Adaptabilidad",
]

# 3 preguntas por competencia (21 en total)
# Escala de respuesta: 1=Nunca, 2=A veces, 3=Casi siempre, 4=Siempre
PREGUNTAS = {
    "Aprendizaje autónomo": [
        "Busco información adicional por mi cuenta para entender mejor los temas.",
        "Organizo mi tiempo de estudio sin esperar que otros me lo indiquen.",
        "Reviso mis errores y aprendo de ellos sin necesidad de que me lo pidan.",
    ],
    "Trabajo en equipo": [
        "Colaboro activamente con mis compañeros para alcanzar los objetivos del equipo.",
        "Escucho y respeto las ideas de los demás miembros del grupo.",
        "Asumo responsabilidades dentro del equipo sin evadirlas.",
    ],
    "Comunicación efectiva": [
        "Expreso mis ideas de forma clara y ordenada, tanto de forma oral como escrita.",
        "Pregunto cuando no entiendo algo en lugar de quedarme con dudas.",
        "Adapto mi forma de comunicarme según la situación o el interlocutor.",
    ],
    "Resolución de problemas": [
        "Cuando encuentro un problema, analizo las posibles causas antes de actuar.",
        "Propongo soluciones concretas frente a los desafíos que se presentan.",
        "Evalúo los resultados de mis decisiones para mejorar en el futuro.",
    ],
    "Responsabilidad y puntualidad": [
        "Entrego mis trabajos y tareas en los plazos establecidos.",
        "Cumplo con mis compromisos y obligaciones sin necesidad de recordatorios.",
        "Llego a tiempo a mis clases, prácticas y actividades programadas.",
    ],
    "Pensamiento crítico": [
        "Cuestiono la información que recibo y busco verificarla antes de aceptarla.",
        "Analizo los pros y contras antes de tomar una decisión importante.",
        "Reconozco cuando me equivoco y busco argumentos para sustentar mis opiniones.",
    ],
    "Adaptabilidad": [
        "Me adapto con facilidad a los cambios en las actividades o en el entorno de trabajo.",
        "Mantengo una actitud positiva frente a situaciones nuevas o inesperadas.",
        "Aprendo rápidamente cuando tengo que usar herramientas o métodos nuevos.",
    ],
}

ESCALA = {
    1: "Nunca",
    2: "A veces",
    3: "Casi siempre",
    4: "Siempre",
}

# Niveles según puntaje promedio por competencia (1.0 – 4.0)
NIVELES = [
    (1.0, 1.9, "Inicial",      "Necesitas desarrollar esta competencia con mayor dedicación."),
    (2.0, 2.9, "En proceso",   "Vas por buen camino, pero aún hay aspectos importantes por reforzar."),
    (3.0, 3.4, "Satisfactorio","Tienes un buen nivel. Sigue practicando para consolidarlo."),
    (3.5, 4.0, "Destacado",    "¡Excelente! Esta es una de tus fortalezas."),
]

# Recomendaciones específicas por competencia y nivel
RECOMENDACIONES = {
    "Aprendizaje autónomo": {
        "Inicial":       "Reserva 30 minutos diarios para repasar el tema del día y anota tus dudas.",
        "En proceso":    "Usa técnicas de estudio como mapas mentales o el método Pomodoro.",
        "Satisfactorio": "Explora fuentes adicionales (videos, artículos) para profundizar los temas.",
        "Destacado":     "Comparte lo que aprendes con tus compañeros; enseñar refuerza el aprendizaje.",
    },
    "Trabajo en equipo": {
        "Inicial":       "Practica escuchar sin interrumpir y luego da tu opinión de forma respetuosa.",
        "En proceso":    "Ofrécete a coordinar actividades grupales para desarrollar tu rol en el equipo.",
        "Satisfactorio": "Identifica los puntos fuertes de cada compañero y apóyate en ellos.",
        "Destacado":     "Actúa como mediador cuando surjan diferencias dentro del grupo.",
    },
    "Comunicación efectiva": {
        "Inicial":       "Practica explicar en voz alta lo que aprendiste cada día, aunque sea solo.",
        "En proceso":    "Antes de exponer, organiza tus ideas en un esquema o lista de puntos clave.",
        "Satisfactorio": "Solicita retroalimentación sobre tu comunicación a docentes o compañeros.",
        "Destacado":     "Considera participar en debates o exposiciones para seguir puliendo tu estilo.",
    },
    "Resolución de problemas": {
        "Inicial":       "Ante un problema, escríbelo en papel y anota al menos dos posibles soluciones.",
        "En proceso":    "Usa la técnica de los '5 porqués' para identificar la causa raíz de los problemas.",
        "Satisfactorio": "Revisa los resultados de tus decisiones pasadas y anota qué mejorarías.",
        "Destacado":     "Comparte tu proceso de resolución con otros; puede servirles de guía.",
    },
    "Responsabilidad y puntualidad": {
        "Inicial":       "Usa una agenda o aplicación de recordatorios para registrar tus compromisos.",
        "En proceso":    "Planifica tus tareas con un día de anticipación para evitar imprevistos.",
        "Satisfactorio": "Mantén el hábito y reflexiona sobre el impacto positivo que genera en tu entorno.",
        "Destacado":     "Tu ejemplo motiva a los demás. Ayuda a un compañero a organizar mejor su tiempo.",
    },
    "Pensamiento crítico": {
        "Inicial":       "Antes de aceptar una información, pregúntate: ¿de dónde viene? ¿es confiable?",
        "En proceso":    "Ejercita el análisis comparando dos fuentes distintas sobre el mismo tema.",
        "Satisfactorio": "Participa en discusiones argumentadas para afinar tu capacidad de razonamiento.",
        "Destacado":     "Plantea preguntas desafiantes en clase para estimular el pensamiento en el grupo.",
    },
    "Adaptabilidad": {
        "Inicial":       "Intenta salir de tu zona de confort realizando una tarea de forma diferente cada semana.",
        "En proceso":    "Reflexiona sobre cambios pasados que hayas superado y qué te ayudó a lograrlo.",
        "Satisfactorio": "Practica la resiliencia identificando oportunidades dentro de los cambios.",
        "Destacado":     "Sirve de apoyo a compañeros que tienen dificultades para adaptarse a los cambios.",
    },
}
