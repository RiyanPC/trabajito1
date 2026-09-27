# views/resultados.py
# Pantalla de resultados y recomendaciones

import flet as ft
from scoring import calcular_resultados, calcular_puntaje_general


# Color por nivel
COLOR_NIVEL = {
    "Inicial":       ft.Colors.RED_400,
    "En proceso":    ft.Colors.ORANGE_400,
    "Satisfactorio": ft.Colors.LIGHT_BLUE_600,
    "Destacado":     ft.Colors.GREEN_600,
    "Sin evaluar":   ft.Colors.GREY_400,
}

ICONO_NIVEL = {
    "Inicial":       ft.Icons.SENTIMENT_VERY_DISSATISFIED,
    "En proceso":    ft.Icons.SENTIMENT_NEUTRAL,
    "Satisfactorio": ft.Icons.SENTIMENT_SATISFIED,
    "Destacado":     ft.Icons.SENTIMENT_VERY_SATISFIED,
    "Sin evaluar":   ft.Icons.HELP_OUTLINE,
}


def _tarjeta_competencia(resultado: dict) -> ft.Container:
    nivel = resultado["nivel"]
    color = COLOR_NIVEL.get(nivel, ft.Colors.GREY_400)
    icono = ICONO_NIVEL.get(nivel, ft.Icons.HELP_OUTLINE)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(icono, color=color, size=24),
                        ft.Text(
                            resultado["competencia"],
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_GREY_900,
                            expand=True,
                        ),
                        ft.Container(
                            content=ft.Text(
                                nivel,
                                size=12,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                            ),
                            bgcolor=color,
                            border_radius=12,
                            padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                        ),
                    ],
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            f"Promedio: {resultado['promedio']:.2f} / 4.00",
                            size=13,
                            color=ft.Colors.BLUE_GREY_600,
                        ),
                    ]
                ),
                ft.ProgressBar(
                    value=resultado["promedio"] / 4.0,
                    color=color,
                    bgcolor=ft.Colors.BLUE_GREY_100,
                    height=8,
                    border_radius=4,
                ),
                ft.Text(
                    resultado["descripcion_nivel"],
                    size=13,
                    color=ft.Colors.BLUE_GREY_700,
                    italic=True,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, size=16, color=ft.Colors.AMBER_700),
                            ft.Text(
                                resultado["recomendacion"],
                                size=13,
                                color=ft.Colors.BROWN_700,
                                expand=True,
                            ),
                        ],
                        spacing=8,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    bgcolor=ft.Colors.AMBER_50,
                    border_radius=8,
                    padding=ft.Padding.all(10),
                ),
            ],
            spacing=8,
        ),
        bgcolor=ft.Colors.WHITE,
        border=ft.Border.all(1, ft.Colors.BLUE_100),
        border_radius=12,
        padding=ft.Padding.all(16),
        width=500,
    )


def vista_resultados(page: ft.Page, respuestas: dict, reiniciar):
    """Construye y retorna el contenido de la pantalla de resultados."""

    resultados = calcular_resultados(respuestas)
    general = calcular_puntaje_general(resultados)

    color_general = COLOR_NIVEL.get(general["nivel_general"], ft.Colors.GREY_400)

    tarjetas = [_tarjeta_competencia(r) for r in resultados]

    resumen_general = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Resultado general",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_GREY_800,
                ),
                ft.Text(
                    f"{general['promedio_general']:.2f} / 4.00",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=color_general,
                ),
                ft.Container(
                    content=ft.Text(
                        general["nivel_general"],
                        size=14,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    bgcolor=color_general,
                    border_radius=16,
                    padding=ft.Padding.symmetric(horizontal=20, vertical=6),
                ),
                ft.Text(
                    general["descripcion_general"],
                    size=13,
                    color=ft.Colors.BLUE_GREY_700,
                    text_align=ft.TextAlign.CENTER,
                    italic=True,
                ),
            ],
            spacing=6,
        ),
        bgcolor=ft.Colors.BLUE_50,
        border_radius=14,
        padding=ft.Padding.all(20),
        width=500,
    )

    return ft.Column(
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            ft.Icon(ft.Icons.ASSESSMENT, size=50, color=ft.Colors.BLUE_700),
            ft.Text(
                "Tus resultados",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
            ),
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            resumen_general,
            ft.Divider(height=16, color=ft.Colors.TRANSPARENT),
            ft.Text(
                "Detalle por competencia",
                size=16,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_GREY_800,
            ),
            ft.Divider(height=8, color=ft.Colors.TRANSPARENT),
            *tarjetas,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Button(
                content="Nueva evaluación",
                icon=ft.Icons.REFRESH,
                on_click=lambda _: reiniciar(),
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.BLUE_700,
                    color=ft.Colors.WHITE,
                    padding=ft.Padding.symmetric(horizontal=36, vertical=14),
                    shape=ft.RoundedRectangleBorder(radius=8),
                ),
            ),
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        ],
    )
