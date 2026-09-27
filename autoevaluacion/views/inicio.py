# views/inicio.py
# Pantalla de bienvenida

import flet as ft


def vista_inicio(page: ft.Page, ir_a_instrucciones):
    """Construye y retorna el contenido de la pantalla de inicio."""

    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        controls=[
            # Logo de SENATI
            ft.Image(
                src="assets/senati_logo.svg",
                width=280,
                height=82,
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Divider(height=18, color=ft.Colors.TRANSPARENT),
            ft.Text(
                "Autoevaluación de Competencias",
                size=26,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.BLUE_900,
            ),
            ft.Text(
                "Aprendizaje Dual",
                size=15,
                color=ft.Colors.BLUE_GREY_600,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Divider(height=24, color=ft.Colors.TRANSPARENT),
            ft.Text(
                "Esta herramienta te permitirá conocer tu nivel actual\n"
                "en las 7 competencias clave y recibir recomendaciones\n"
                "personalizadas para mejorar.",
                size=15,
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.BLUE_GREY_800,
            ),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Button(
                content="Comenzar",
                icon=ft.Icons.ARROW_FORWARD,
                on_click=lambda _: ir_a_instrucciones(),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.BLUE_700,
                    color=ft.Colors.WHITE,
                    padding=ft.Padding.symmetric(horizontal=40, vertical=16),
                    shape=ft.RoundedRectangleBorder(radius=8),
                ),
            ),
        ],
    )
