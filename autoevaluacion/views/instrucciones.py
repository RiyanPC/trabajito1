# views/instrucciones.py
# Pantalla de instrucciones

import flet as ft


def vista_instrucciones(page: ft.Page, ir_a_cuestionario, ir_a_inicio):
    """Construye y retorna el contenido de la pantalla de instrucciones."""

    pasos = [
        "Responde con honestidad cada una de las 21 preguntas.",
        "Usa la escala: 1 = Nunca  ·  2 = A veces  ·  3 = Casi siempre  ·  4 = Siempre.",
        "Selecciona una opción por cada pregunta antes de continuar.",
        "Al finalizar verás tus resultados y recomendaciones personalizadas.",
        "No hay respuestas correctas o incorrectas; el objetivo es conocerte mejor.",
    ]

    pasos_controls = [
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(str(i + 1), color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                    bgcolor=ft.Colors.BLUE_700,
                    border_radius=20,
                    width=30,
                    height=30,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Text(paso, size=14, expand=True, color=ft.Colors.BLUE_GREY_900),
            ],
            spacing=12,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        for i, paso in enumerate(pasos)
    ]

    return ft.Column(
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            ft.Icon(ft.Icons.INFO_OUTLINE, size=50, color=ft.Colors.BLUE_700),
            ft.Text(
                "Instrucciones",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
            ),
            ft.Divider(height=16, color=ft.Colors.TRANSPARENT),
            ft.Container(
                content=ft.Column(controls=pasos_controls, spacing=16),
                bgcolor=ft.Colors.BLUE_50,
                border_radius=12,
                padding=ft.Padding.all(20),
                width=500,
            ),
            ft.Divider(height=24, color=ft.Colors.TRANSPARENT),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=16,
                controls=[
                    ft.OutlinedButton(
                        content="Atrás",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda _: ir_a_inicio(),
                    ),
                    ft.Button(
                        content="Iniciar cuestionario",
                        icon=ft.Icons.CHECKLIST,
                        on_click=lambda _: ir_a_cuestionario(),
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_700,
                            color=ft.Colors.WHITE,
                            padding=ft.Padding.symmetric(horizontal=32, vertical=14),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                ],
            ),
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
        ],
    )
