# scoring.py
# Lógica de cálculo de puntajes y niveles por competencia

from data import COMPETENCIAS, PREGUNTAS, NIVELES, RECOMENDACIONES


def calcular_resultados(respuestas: dict) -> list[dict]:
    """
    Recibe un dict con la estructura:
        { "Competencia": [puntaje_p1, puntaje_p2, puntaje_p3], ... }

    Retorna una lista de dicts ordenada por competencia:
        [
            {
                "competencia": str,
                "promedio": float,
                "nivel": str,
                "descripcion_nivel": str,
                "recomendacion": str,
            },
            ...
        ]
    """
    resultados = []

    for competencia in COMPETENCIAS:
        puntajes = respuestas.get(competencia, [])

        if not puntajes or len(puntajes) != len(PREGUNTAS[competencia]):
            # Si faltan respuestas, promedio 0
            promedio = 0.0
        else:
            promedio = sum(puntajes) / len(puntajes)

        nivel, descripcion = _obtener_nivel(promedio)
        recomendacion = RECOMENDACIONES.get(competencia, {}).get(nivel, "")

        resultados.append(
            {
                "competencia": competencia,
                "promedio": round(promedio, 2),
                "nivel": nivel,
                "descripcion_nivel": descripcion,
                "recomendacion": recomendacion,
            }
        )

    return resultados


def calcular_puntaje_general(resultados: list[dict]) -> dict:
    """
    Calcula el promedio general a partir de los resultados por competencia.
    Retorna un dict con promedio_general, nivel_general y descripcion_general.
    """
    if not resultados:
        return {"promedio_general": 0.0, "nivel_general": "-", "descripcion_general": ""}

    promedio_general = sum(r["promedio"] for r in resultados) / len(resultados)
    nivel, descripcion = _obtener_nivel(promedio_general)

    return {
        "promedio_general": round(promedio_general, 2),
        "nivel_general": nivel,
        "descripcion_general": descripcion,
    }


def _obtener_nivel(promedio: float) -> tuple[str, str]:
    """Devuelve (nivel, descripcion) según el promedio."""
    from data import NIVELES

    for minimo, maximo, nivel, descripcion in NIVELES:
        if minimo <= promedio <= maximo:
            return nivel, descripcion

    # Promedio 0 (sin respuestas)
    return "Sin evaluar", "No se registraron respuestas para esta competencia."
