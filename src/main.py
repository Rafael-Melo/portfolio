import flet as ft
from partials.sidebar import Sidebar

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.Colors.BLACK
        self.main()

    def main(self):
        self.sidebar = Sidebar()

        self.content = ft.Container(
            ft.Column(
                controls=[
                    ft.Text('Seja bem-vindo ao meu portfólio!', size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Apaixonado por tecnologia e resolução de problemas. Tenho experiência com automações em Python e APIs, e adoro transformar desafios em soluções simples e eficientes."),
                    ft.Divider(height=30),
                    ft.Text('Em construção!')
                ]
            )
        )

        layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Column(col={"sm": 12, "md": 4, "lg": 3}, controls=[self.sidebar]),
                ft.Column(col={"sm": 12, "md": 8, "lg": 9}, controls=[self.content]),
            ],
            expand=True,
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')
