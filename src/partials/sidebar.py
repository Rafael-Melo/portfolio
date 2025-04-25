import flet as ft
from components.skills import SkillRing

def SidebarHeader():
    return ft.Container(
        content=ft.Column(
            controls=[
                    ft.Image(
                        src='img/face-1.png',
                        border_radius=70,
                        width=100,
                        badge=ft.Badge(
                            bgcolor=ft.Colors.PRIMARY,
                            small_size=20,
                            alignment=ft.alignment.top_right,
                        ),
                    ),
                ft.Text(value='Rafael Melo', theme_style=ft.TextThemeStyle.BODY_LARGE),
                ft.Text(value='Desenvolvedor Python', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.symmetric(vertical=20, horizontal=40),
        alignment=ft.alignment.center,
    )

def SidebarContent():
    location = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.Row(
                controls=[
                    ft.Text(value='Cidade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Artur Nogueira', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.Row(
                controls=[
                    ft.Text(value='Idade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='36', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        ]
    )

    languages = ft.Row(
        controls=[
            SkillRing(title='Português', value=1),
            SkillRing(title='Inglês', value=0.70),
            SkillRing(title='Francês', value=0.15),
        ]
    )

    skills = ft.Container()

    technologies = ft.Container()

    cv = ft.Container()

    return ft.Container(
        bgcolor=ft.Colors.BLACK12,
        padding=ft.padding.all(20),
        content=ft.Column(
            controls=[
                location,
                ft.Divider(height=30),
                languages,
                ft.Divider(height=30),
                skills,
                ft.Divider(height=30),
                technologies,
                ft.Divider(height=30),
                cv,
            ]
        ),
    )

def SidebarFooter():
    return ft.Container(
        padding=ft.padding.symmetric(vertical=10),
        content=ft.Row(
            expand=True,
            controls=[
                ft.IconButton(
                    content=ft.Image(src='icons/001-instagram.png', height=15, color=ft.Colors.WHITE),
                    url='',
                ),
                ft.IconButton(
                    content=ft.Image(src='icons/002-linkedin.png', height=15, color=ft.Colors.WHITE),
                    url='',
                ),
                ft.IconButton(
                    content=ft.Image(src='icons/003-github.png', height=15, color=ft.Colors.WHITE),
                    url='',
                ),
                ft.IconButton(
                    content=ft.Image(src='icons/004-youtube.png', height=15, color=ft.Colors.WHITE),
                    url='',
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
    )

def Sidebar():
    return ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                SidebarHeader(),
                SidebarContent(),
                SidebarFooter(),
            ]
        ),
        bgcolor=ft.Colors.BLACK,
    )