import flet as ft
from components.skills import SkillRing, SkillProgresseBar, SkillList

def sidebar_header():
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

def sidebar_content():
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

    skills = ft.Column(
        controls=[
            SkillProgresseBar(title='Python', value=0.8),
            SkillProgresseBar(title='HTML', value=0.9),
            SkillProgresseBar(title='CSS', value=0.9),
            SkillProgresseBar(title='SQL', value=0.7),
        ]
    )

    technologies = ft.Column(
        controls=[
            SkillList(title='Flet'),
            SkillList(title='Django, Flask, FastApi'),
            SkillList(title='Versionamento com Git'),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=0,
    )

    cv = ft.TextButton(
        text='DOWNLOAD CV',
        style=ft.ButtonStyle(color=ft.Colors.GREY),
        icon=ft.Icons.DOWNLOAD,
        icon_color=ft.Colors.GREY,
        url='https://drive.google.com/uc?export=download&id=1Ell39yCLqAgfkPl2xQhk7moVMImHyrG9'
        # https://sites.google.com/site/gdocs2direct/?pli=1 - Site para gerar download automático de arquivos do Google Drive
    )

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
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            expand=True,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )

def sidebar_footer():
    return ft.Container(
        padding=ft.padding.symmetric(vertical=10),
        content=ft.Row(
            expand=True,
            controls=[
                ft.IconButton(
                    content=ft.Image(src='icons/001-instagram.png', height=15, color=ft.Colors.WHITE),
                    url='https://www.instagram.com/rafamelo7/',
                ),
                ft.IconButton(
                    content=ft.Image(src='icons/002-linkedin.png', height=15, color=ft.Colors.WHITE),
                    url='https://www.linkedin.com/in/rafaelvbdemelo/',
                ),
                ft.IconButton(
                    content=ft.Image(src='icons/003-github.png', height=15, color=ft.Colors.WHITE),
                    url='https://github.com/Rafael-Melo',
                ),
                ft.IconButton(
                    content=ft.Image(src='icons/004-youtube.png', height=15, color=ft.Colors.WHITE),
                    url='https://www.youtube.com/@ravielburn',
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
    )

def sidebar():
    return ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                sidebar_header(),
                sidebar_content(),
                sidebar_footer(),
            ]
        ),
        bgcolor=ft.Colors.BLACK,
    )