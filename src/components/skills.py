import flet as ft

def SkillRing(title, value):
    return ft.Column(
        controls=[
            ft.Stack(
                controls=[
                    ft.PieChart(
                        sections=[
                            ft.PieChartSection(value=value, color=ft.Colors.PRIMARY, radius=5),
                            ft.PieChartSection(value=1-value, color=ft.Colors.BLACK26, radius=5),
                        ],
                        sections_space=0,
                        center_space_color=ft.Colors.BLACK12,
                        height=70,
                    ),
                    ft.Container(
                        content=ft.Text(value=f'{value:.0%}', theme_style=ft.TextThemeStyle.BODY_LARGE),
                        alignment=ft.alignment.center,
                        height=70,
                    )
                ]
            ),
            ft.Text(value=title, theme_style=ft.TextThemeStyle.BODY_LARGE),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

def SkillProgresseBar(title, value):
    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text(value=title, theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value=f'{value:.0%}', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.ProgressBar(value=value, color=ft.Colors.PRIMARY, bgcolor=ft.Colors.BLACK26),
            ft.Divider(height=10, color=ft.Colors.BLACK12),
        ],
    )

def SkillList(title):
    return ft.Column(
        controls=[
            ft.ListTile(
                leading=ft.Icon(name=ft.Icons.CHECK, color=ft.Colors.PRIMARY),
                title=ft.Text(value=title, theme_style=ft.TextThemeStyle.BODY_MEDIUM),
            )
        ]
    )
    

