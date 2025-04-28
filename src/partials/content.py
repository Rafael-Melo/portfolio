import flet as ft

def MainContent():
    banner = ft.Container(

    )

    experience = ft.Container(

    )

    projects = ft.Container(

    )

    prices = ft.Container(

    )

    testimoials = ft.Container(

    )

    logos = ft.Container(

    )

    footer = ft.Container(

    )


    return ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                ft.Text(value='Conteúdo sendo feito aqui'),
                banner,
                experience,
                projects,
                prices,
                testimoials,
                logos,
                footer,
            ]
        ),
        bgcolor=ft.Colors.BLACK87,
        padding=ft.padding.all(30),
    )