import flet as ft
from partials.sidebar import sidebar
from partials.content import main_content

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.Colors.BLACK
        self.main()

    def main(self):
        self.sidebar = sidebar()

        self.content = main_content()

        layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Column(col={"xs": 0, "md": 5, "lg": 4, "xxl": 3}, controls=[self.sidebar]),
                ft.Column(col={"xs": 12, "md": 7, "lg": 8, "xxl": 9}, controls=[self.content]),
            ],
            expand=True,
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')
