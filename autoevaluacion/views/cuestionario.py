# views/cuestionario.py
# Pantalla del cuestionario — una competencia a la vez

import flet as ft
from data import COMPETENCIAS, PREGUNTAS, ESCALA


def vista_cuestionario(page: ft.Page, respuestas: dict, ir_a_resultados, ir_a_instrucciones):
    """
    Muestra las preguntas de una competencia a la vez.
    Navega entre competencias con Siguiente / Atrás.
    Al terminar la última competencia llama a ir_a_resultados().

    respuestas: dict compartido { competencia: [p1, p2, p3] }
    """

    # Estado mutable del índice actual (lista de 1 elemento para que las
    # closures internas puedan modificarlo sin 'nonlocal')
    indice = [0]

    # RadioGroups de la competencia visible
    grupos_radio: list[ft.RadioGroup] = []

    def competencia_actual():
        return COMPETENCIAS[indice[0]]

    def preguntas_actuales():
        return PREGUNTAS[competencia_actual()]

    # ── Controles del encabezado ───────────────────────────────────────────────
    titulo_comp = ft.Text(
        "",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_900,
        text_align=ft.TextAlign.CENTER,
    )
    progreso_texto = ft.Text("", size=13, color=ft.Colors.BLUE_GREY_600)
    barra_progreso = ft.ProgressBar(
        width=460, color=ft.Colors.BLUE_700, bgcolor=ft.Colors.BLUE_100
    )

    # ── Columna dinámica de preguntas ──────────────────────────────────────────
    columna_preguntas = ft.Column(spacing=20, scroll=ft.ScrollMode.AUTO)

    # ── Mensaje de validación ──────────────────────────────────────────────────
    mensaje_error = ft.Text("", color=ft.Colors.RED_600, size=13)

    # ── Botones de navegación ──────────────────────────────────────────────────
    btn_atras = ft.OutlinedButton(
        content="Atrás",
        icon=ft.Icons.ARROW_BACK,
        on_click=lambda _: navegar(-1),
    )
    btn_siguiente = ft.Button(
        content="Siguiente",
        icon=ft.Icons.ARROW_FORWARD,
        on_click=lambda _: navegar(1),
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            padding=ft.Padding.symmetric(horizontal=28, vertical=12),
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )

    # ── Helpers ────────────────────────────────────────────────────────────────
    def construir_preguntas():
        """Reconstruye la lista de preguntas para la competencia actual."""
        comp = competencia_actual()
        preguntas = preguntas_actuales()
        previas = respuestas.get(comp, [None] * len(preguntas))

        grupos_radio.clear()
        columna_preguntas.controls.clear()

        for idx_p, pregunta in enumerate(preguntas):
            grupo = ft.RadioGroup(
                value=str(previas[idx_p]) if previas[idx_p] is not None else None,
                content=ft.Column(
                    controls=[
                        ft.Radio(value=str(v), label=f"{v} — {etiq}")
                        for v, etiq in ESCALA.items()
                    ],
                    spacing=4,
                ),
            )
            grupos_radio.append(grupo)

            columna_preguntas.controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                f"{idx_p + 1}. {pregunta}",
                                size=14,
                                color=ft.Colors.BLUE_GREY_900,
                            ),
                            grupo,
                        ],
                        spacing=8,
                    ),
                    bgcolor=ft.Colors.WHITE,
                    border=ft.Border.all(1, ft.Colors.BLUE_100),
                    border_radius=10,
                    padding=ft.Padding.all(16),
                )
            )

    def actualizar_encabezado():
        idx = indice[0]
        total = len(COMPETENCIAS)
        titulo_comp.value = f"Competencia {idx + 1} de {total}: {competencia_actual()}"
        progreso_texto.value = f"Progreso: {idx + 1} / {total}"
        barra_progreso.value = (idx + 1) / total
        es_ultimo = idx == total - 1
        btn_siguiente.content = "Ver resultados" if es_ultimo else "Siguiente"
        btn_siguiente.icon = ft.Icons.ASSESSMENT if es_ultimo else ft.Icons.ARROW_FORWARD
        btn_atras.visible = idx > 0

    def guardar_respuestas_actuales() -> bool:
        """Persiste las respuestas del bloque actual. Retorna False si falta alguna."""
        comp = competencia_actual()
        vals = []
        for g in grupos_radio:
            if g.value is None:
                return False
            vals.append(int(g.value))
        respuestas[comp] = vals
        return True

    def navegar(direccion: int):
        mensaje_error.value = ""

        if direccion == 1 and not guardar_respuestas_actuales():
            mensaje_error.value = "Por favor responde todas las preguntas antes de continuar."
            page.update()
            return

        if direccion == -1 and indice[0] == 0:
            ir_a_instrucciones()
            return

        nuevo = indice[0] + direccion
        if nuevo >= len(COMPETENCIAS):
            ir_a_resultados()
            return

        indice[0] = nuevo
        construir_preguntas()
        actualizar_encabezado()
        page.update()

    # ── Estado inicial ─────────────────────────────────────────────────────────
    construir_preguntas()
    actualizar_encabezado()

    return ft.Column(
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            titulo_comp,
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[progreso_texto]),
            ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[barra_progreso]),
            ft.Divider(height=12, color=ft.Colors.TRANSPARENT),
            ft.Container(content=columna_preguntas, width=500),
            ft.Divider(height=8, color=ft.Colors.TRANSPARENT),
            mensaje_error,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=16,
                controls=[btn_atras, btn_siguiente],
            ),
            ft.Divider(height=16, color=ft.Colors.TRANSPARENT),
        ],
    )
