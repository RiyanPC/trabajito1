# main.py
# Punto de entrada y navegación entre pantallas

import flet as ft
from views.inicio import vista_inicio
from views.instrucciones import vista_instrucciones
from views.cuestionario import vista_cuestionario
from views.resultados import vista_resultados


def main(page: ft.Page):
    # ── Configuración general de la página ────────────────────────────────────
    page.title = "Autoevaluación de Competencias — SENATI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.Padding.symmetric(horizontal=20, vertical=10)
    page.scroll = ft.ScrollMode.AUTO
    page.window.width = 600
    page.window.min_width = 360
    page.fonts = {}

    # ── Estado compartido de respuestas ──────────────────────────────────────
    respuestas: dict = {}

    # ── Contenedor principal (una sola vista activa a la vez) ─────────────────
    contenido = ft.Column(expand=True)

    def cambiar_vista(nueva_vista):
        contenido.controls.clear()
        contenido.controls.append(nueva_vista)
        page.update()

    # ── Funciones de navegación ───────────────────────────────────────────────
    def ir_a_inicio():
        cambiar_vista(
            vista_inicio(page, ir_a_instrucciones)
        )

    def ir_a_instrucciones():
        cambiar_vista(
            vista_instrucciones(page, ir_a_cuestionario, ir_a_inicio)
        )

    def ir_a_cuestionario():
        cambiar_vista(
            vista_cuestionario(page, respuestas, ir_a_resultados, ir_a_instrucciones)
        )

    def ir_a_resultados():
        cambiar_vista(
            vista_resultados(page, respuestas, reiniciar)
        )

    def reiniciar():
        respuestas.clear()
        ir_a_inicio()

    # ── Arrancar en la pantalla de inicio ─────────────────────────────────────
    page.add(contenido)
    ir_a_inicio()


ft.run(main, assets_dir="assets")
